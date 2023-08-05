#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random
import psutil
import logging
import pandas as pd
import numpy as np
from io import open
from collections import Counter
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor
from scipy.sparse import csr_matrix, save_npz, load_npz, lil_matrix
from argparse import ArgumentParser, FileType, ArgumentDefaultsHelpFormatter
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

from six import text_type as unicode
from six import iteritems
from six.moves import range

from fastGraph.graph import Graph
from fastGraph import ngram
import pdb

p = psutil.Process(os.getpid())
try:
	p.cpu_affinity(list(range(cpu_count())))
except AttributeError:
	pass


LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s Line %(lineno)s: %(message)s"
logging.basicConfig(format=LOGFORMAT)

logger = logging.getLogger("fastGraph")
logger.setLevel(logging.INFO)

DTYPE = np.float64

def debug(type_, value, tb):
	if hasattr(sys, 'ps1') or not sys.stderr.isatty():
		sys.__excepthook__(type_, value, tb)
	else:
		import traceback
		import pdb
		traceback.print_exception(type_, value, tb)
		print(u"\n")
		pdb.pm()

def load_matrix(args):
	logger.info("Reading from "+str(args.input))
	if "wiki-Vote.csv" in args.input:
		df = pd.read_csv(args.input, sep=',', comment='#')
		max_node = max(max(df['FromNodeId'].unique()), max(df['ToNodeId'].unique()))
		total_len = max_node + 1
		matrix = lil_matrix(np.zeros((total_len, total_len), dtype=DTYPE))
		for row in df.itertuples():
			matrix[row.FromNodeId, row.ToNodeId] = matrix[row.FromNodeId, row.ToNodeId] + 1 # Each edge is binary
		return csr_matrix(matrix)
	elif "weighted_directed.csv" in args.input:
		df = pd.read_csv(args.input, sep=',', comment='#')
		max_node = max(max(df['SOURCE'].unique()), max(df['TARGET'].unique()))
		total_len = max_node + 1
		matrix = lil_matrix(np.zeros((total_len, total_len), dtype=DTYPE))
		for row in df.itertuples():
			matrix[row.SOURCE, row.TARGET] = matrix[row.SOURCE, row.TARGET] + row.RATING # Each edge has different weights
		return csr_matrix(matrix)
	elif ".npz" in args.input or ".npy" in args.input:
		logger.info("Load matrix directly")
		matrix = np.load(args.input)
		return csr_matrix(matrix)
	else:
		# Implement parsing here to transform into matrix form.
		raise NotImplementedError("Implement customized parsing here.")

def fastGraph_flow(args):
	# Read and process different input
	matrix = load_matrix(args)
	logger.info("Matrix loaded.")

	graph = Graph()
	graph.build_graph_from_matrix(matrix, is_directed=True, remove_self_loops=False,
								  normalized_edge=True, outward_prob_check=True)

	# Generate walks, select which walk to use by de-comment
	if args.walk_type == "likely":
		# walks = graph.build_likely_walk_corpus_multiprocess(args.number_paths, args.path_length,
		# rand=random.Random(0), shuffle=True, deduplicate=False)
		walks = graph.build_likely_walk_corpus(args.number_paths, args.path_length, rand=random.Random(0),
											 shuffle=True, deduplicate=False)
	elif args.walk_type == "node2vec":
		graph.preprocess_node2vec_walk(args.p, args.q)
		walks = graph.build_node2vec_walk_corpus(args.number_paths, args.path_length, rand=random.Random(0),
												 shuffle=True, deduplicate=False)
	elif args.walk_type == "deep":
		walks = graph.build_deepwalk_corpus(args.number_paths, args.path_length, rand=random.Random(0),
											shuffle=True, deduplicate=False)
	else:
		raise ValueError("--walk-type must be either 'likely', 'node2vec' or 'deep'.")

	# Save walks to storage, enabling gensim's iterator ability.
	walks_file = ''.join(str(args.input).split('.')[:-1])+'.walks'
	with open(walks_file, 'w') as fout:
		for walk in walks:
			fout.write(' '.join(walk)+'\n')
	logger.info("Walks saved to "+walks_file)
	walks = LineSentence(args.input)

	# Phrases
	if args.ngram > 1:
		logger.info("Building n-gram with n="+str(args.ngram)+"...")
		walks, ngram_phrasers = ngram.build_ngram(walks, args.ngram)

	# Word2Vec
	logger.info("Training ...")
	w2v = Word2Vec(walks, size=args.embed_size, window=args.window_size, min_count=0,
					 sg=1, hs=0, negative=10, workers=args.workers)

	# Save model
	w2v.save(args.output)


def main():
	parser = ArgumentParser("fastGraph", formatter_class=ArgumentDefaultsHelpFormatter, conflict_handler='resolve')

	parser.add_argument("-l", "--log", dest="log", default="INFO",
						help="log verbosity level")

	parser.add_argument('--input', nargs='?', required=True,
						help='Input matrix')

	parser.add_argument('--max-memory-data-size', default=1000000000, type=int,
						help='Size to start dumping walks to disk, instead of keeping them in memory.')

	parser.add_argument('--number-paths', default=5, type=int,
						help='Number of random walks to start at each node')

	parser.add_argument('--output', required=True,
						help='Output representation file')

	parser.add_argument('--embed-size', default=64, type=int,
						help='Dimension of the latent vector as embedding.')

	parser.add_argument('--seed', default=0, type=int,
						help='Seed for random walk generator.')

	parser.add_argument('--directed', default=True, type=bool,
						help='Treat the graph as directed.')

	parser.add_argument('--path-length', default=40, type=int,
						help='Length of the random walk started at each node')

	parser.add_argument('--window-size', default=5, type=int,
						help='Window size of skipgram model.')

	parser.add_argument('--walk-type', default="likely", type=str,
						help='Which walk method to use: likely, random, node2vec.')

	parser.add_argument('--p', default=5, type=int,
						help="p value, refer to original paper: https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf ")

	parser.add_argument('--q', default=3, type=int,
						help="q value, refer to original paper: https://cs.stanford.edu/~jure/pubs/node2vec-kdd16.pdf ")

	parser.add_argument('--workers', default=cpu_count(), type=int,
						help='Number of parallel processes.')

	parser.add_argument('--ngram',  default=1, type=int,
						help='N of n-grams, e.g.: set 2 for bigrams, 3 for trigrams, etc.')

	args = parser.parse_args()
	numeric_level = getattr(logging, args.log.upper(), None)
	logging.basicConfig(format=LOGFORMAT)
	logger.setLevel(numeric_level)

	fastGraph_flow(args)

if __name__ == "__main":
	sys.exit(main())
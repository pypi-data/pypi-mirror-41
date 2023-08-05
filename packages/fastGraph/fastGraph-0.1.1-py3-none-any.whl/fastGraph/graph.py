#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import numpy as np
import pickle
import random

from time import time
from six.moves import range
from six import iterkeys
from collections import defaultdict, Iterable
from scipy.sparse import issparse, csr_matrix
from sklearn.preprocessing import normalize
from multiprocessing import Process, Manager
from pdb import set_trace

logger = logging.getLogger("fastGraph")

DUPLICATION_WARN_THRESHOLD = 0.2

class Graph():
	"""
	Implementation of a light-weight Graph supporting directed, undirected and edge weights.
	Walk sequence options include Random Walk (Deep Walk), Likely Walk or node2vec Walk.
	"""

	def __init__(self, dtype=np.float64):
		'''
		self.nodes              = { Node 1: [Node2, Node3, ...All outward nodes... ], Node 2: [Node 4, ... ] }.
									NOTE: Using the index of matrix, to gain the speed.
		self.edges              = Sparse Matrix of shape (nb_node, nb_node)
		self.normalized         =

		self.idx_name [Optional]    = The mapping from index to name of string, for easier understanding and embedding lookup.
		self.alias_edge [Optional]  = Precalculation matrix for node2vec walk

		:param dtype:
		'''
		self.nodes = defaultdict(list)
		self.edges = csr_matrix(np.zeros(0, dtype=np.float64))
		self.normalized = False

		self.idx_name = None
		self.alias_edge = None

	def save_matrix_of_edges(self, file_):
		np.save(file_, self.edges)
		logger.info("Graph.edges save to "+str(file_))

	def adjacency_iter(self):
		return self.nodes.items()

	def subgraph(self, input_nodes):
		subgraph = Graph()

		for n in input_nodes:
			if n in self.nodes:
				subgraph.nodes[n] = [x for x in self.nodes.get(n, []) if x in input_nodes]

		nodes_list = list(subgraph.nodes.keys())
		subgraph.edges = np.ix_(nodes_list,nodes_list)

		return subgraph

	def make_bidirection(self):
		fix_keys = list(self.nodes.keys())
		for v in fix_keys:
			for other in self.nodes[v]:
				if v != other:
					self.nodes[other].append(v)
					assert(self.edges[v, other] != 0)
					self.edges[other, v] = self.edges[v, other]

		logger.info("make_bidirection: Added reverse node relationships and edge transpose element.")

	def make_consistent(self):
		t0 = time()
		for k in iterkeys(self.nodes):
			self.nodes[k] = list(sorted(set(self.nodes[k])))

		t1 = time()
		logger.info('make_consistent: made consistent in {}s'.format(t1 - t0))

	def normalize_edges(self):
		"""
		Normalize the outward probability of each row in self.edges
		"""
		assert (self.edges.shape[0] == self.edges.shape[1])
		# sklearn has optimized normalization for sparse matrix.
		self.edges = normalize(self.edges, axis=1, norm='l1', copy=False)
		self.normalized = True

	def remove_self_loops(self):
		removed = 0
		for x in self.nodes:
			if x in self.nodes.get(x,[]):
				self.nodes[x].remove(x)
				removed += 1

		logger.info("remove_self_loops: removed "+str(removed)+" loops in")

	def check_valid(self, outward_prob_check=True, precesion_error=1e-4):
		total_nodes = len(self.nodes.keys())
		if total_nodes == 0:
			raise ValueError("0 node is found here in the graph.")
		logger.info("Graph.nodes has total "+str(total_nodes)+" keys(starting nodes).")

		neighbor_count = 0.
		for node, neighbor_nodes in self.nodes.items():
			if len(neighbor_nodes) > total_nodes:
				raise ValueError("Node no."+str(node)+" has "+str(len(neighbor_nodes))+" neighbor nodes.")
			neighbor_count = neighbor_count + len(neighbor_nodes)
		neighbor_count = neighbor_count / total_nodes
		logger.info("Graph.nodes is valid with average "+str(neighbor_count)+" neighbor nodes.")

		if self.edges.shape[0] != self.edges.shape[1]:
			raise ValueError("Graph.edges should be a symmetric matrix.")
		logger.info("Graph.edges is valid with shape= "+str(self.edges.shape))

		if outward_prob_check:
			logger.warning("Enabeling outward_prob_check will check whether each row sum to zero. Might be very slow! "
			               "Disable it by setting build_graph_from_matriz(..., outward_prob_check=False)  ")
			for row_i in range(self.edges.shape[0]):
				npsum = np.sum(self.edges[row_i,:])
				if abs(npsum - 1.0) > precesion_error and npsum != 0.0: # Outward probability might be all zero.
					raise ValueError("Edge Matrix no."+str(row_i)+" row (outward probability) is not normalized. np.sum="+str(np.sum(self.edges[row_i,:])))
		if not self.normalized:
			logger.warning("Edge Matrix's row (outward probability) is not normalized.")
			logger.warning("In this pdb:")
			logger.warning("    1. self.normalize_edges()")
			logger.warning("    2. c")
			set_trace()
			logger.info("Recheck validity of graph.")
			self.check_valid(outward_prob_check=outward_prob_check, precesion_error=precesion_error)
			return
		logger.info("Graph.edges is valid with all outward probabilities(row) normalized!")

	def load_idx_name_dict(self, filename):
		self.idx_name = pickle.load(open(filename, 'rb'))
		logger.info("Read idx_name dictionary with "+str(len(self.idx_name))+" nodes name.")

	def rename_idx_with_name(self, walk_sequences):
		'''Rename the Walk Sequences of index into name of string'''
		if not self.idx_name:
			logger.warning("The mapping dictionary (self.idx_name) is not defined yet.")
			return walk_sequences
		return [self.idx_name[elem] for elem in walk_sequences]

	def check_self_loops(self):
		for x in self.nodes:
			for y in self.nodes.get(x, []):
				if x == y:
					return True
		return False

	def has_edge(self, v1, v2):
		if v2 in self.nodes.get(v1, []) or v1 in self.nodes.get(v2, []):
			return True
		return False

	def degree(self, nodes=None):
		if isinstance(nodes, Iterable):
			return {v: len(self.nodes.get(v, [])) for v in nodes}
		else:
			return len(self.nodes.get(nodes, []))

	def number_of_edges(self):
		'''Returns the number of edges in the graph'''
		if self.edges == np.zeros(1):
			return sum([self.degree(x) for x in self.nodes.keys()]) / 2
		else:
			return np.count_nonzero(self.edges)

	def number_of_nodes(self):
		'''Returns the total number of nodes in the graph'''
		return len(self.nodes)

	def check_walks(self, walks, rand, shuffle, deduplicate):
		logger.info("Complete total "+str(len(walks))+" walk sequences.")
		if shuffle:
			rand.shuffle(walks)
			logger.info("Walk sequences shuffled.")
		if deduplicate:
			walks = self.deduplicate(walks)
		else:
			ori_len = len(walks)
			deduplicated_walks = [list(w) for w in set([tuple(w) for w in walks])]
			deduplicated_len = len(deduplicated_walks)
			duplicate_ratio = 1 - deduplicated_len/ori_len
			if duplicate_ratio > DUPLICATION_WARN_THRESHOLD:
				logger.warning("Duplicate ratio ="+str(duplicate_ratio)+", with original length ="+str(ori_len)+" and deduplicated_len ="+str(deduplicated_len))
				logger.warning("Recommend to deduplicate to avoid overfitting specific sequences.")

		return walks

	def deduplicate(self, walks):
		ori_len = len(walks)
		walks = [list(w) for w in set([tuple(w) for w in walks])]
		deduplicate_len = len(walks)
		logger.info("Original seq count:" + str(ori_len) + ", Deduplicated seq count:" + str(deduplicate_len))
		return walks


	def node2vec_walk(self, path_length, rand=random.Random(), start=None):
		if start:
			path = [start]
		else:
			# Sampling is uniform w.r.t V, and not w.r.t E
			path = [rand.choice(list(self.nodes.keys()))]

		while len(path) < path_length:
			cur = path[-1]
			if len(self.nodes.get(cur,[])) > 0: # Has neighbor
				cur_nbrs = self.nodes.get(cur, [])
				# Given current node=G[cur], do the p, q search walk
				if len(path) == 1:
					path.append(int(self.likely_walk(2, start=cur)[1]))
				else:
					prev = path[-2]
					J, q = self.alias_edge[(prev,cur)]
					next = cur_nbrs[alias_draw(J, q)]
					path.append(next)
			else: # No neighbors, break!
				break
		return [str(node) for node in path]

	def build_node2vec_walk_corpus(self, num_paths, path_length, rand=random.Random(0), shuffle=True, deduplicate=False):
		if not self.alias_edge:
			logger.warning("Must do preprocess_node2vec_walk() before doing node2vec walk")
			logger.warning("In this pdb:")
			logger.warning("    1. self.preprocess_node2vec_walk(p, q)")
			logger.warning("    2. c")
			set_trace()
			return self.build_node2vec_walk_corpus(num_paths, path_length, rand)

		walks = []
		nodes = list(self.nodes.keys()) * num_paths
		total_paths = len(nodes)
		percent_done = 0
		logger.info("Node2vec Walking with "+str(num_paths)+" paths per node and each path length of "+str(path_length))

		for idx, node in enumerate(nodes):
			walks.append(self.node2vec_walk(path_length, rand=rand, start=node))
			if int(idx/(total_paths/100)) > percent_done:
				percent_done += 1
				logger.info(str(percent_done)+"% done")

		return self.check_walks(walks, rand, shuffle, deduplicate)

	def random_walk(self, path_length, rand=random.Random(), start=None):
		''' Returns a truncated random walk.

			path_length: Length of the random walk.
			alpha: probability of restarts.
			start: the start node of the random walk.
		'''
		if start:
			path = [start]
		else:
			# Sampling is uniform w.r.t V, and not w.r.t E
			path = [rand.choice(list(self.nodes.keys()))]

		while len(path) < path_length:
			cur = path[-1]
			neighbor_nodes = self.nodes.get(cur, [])

			if len(neighbor_nodes) > 0:
				path.append(rand.choice(neighbor_nodes))
			else:
				break
		return [str(node) for node in path]

	def build_deepwalk_corpus(self, num_paths, path_length, rand=random.Random(0), shuffle=True, deduplicate=False):
		walks = []
		nodes = list(self.nodes.keys()) * num_paths
		total_paths = len(nodes)
		percent_done = 0
		logger.info("Deep Walking with "+str(num_paths)+" paths per node and each path length of "+str(path_length))

		for idx, node in enumerate(nodes):
			walks.append(self.random_walk(path_length, rand=rand, start=node))
			if int(idx/(total_paths/100)) > percent_done:
				percent_done += 1
				logger.info(str(percent_done)+"% done")

		return self.check_walks(walks, rand, shuffle, deduplicate)

	def build_deepwalk_corpus_iter(self, num_paths, path_length, rand=random.Random(0), shuffle=True):
		# FIXME: yield series
		logger.warning("Not implemented yet, calling Graph.build_deepwalk_corpus() instead.")
		return self.build_deepwalk_corpus(num_paths, path_length, rand=rand, shuffle=shuffle)

	def likely_walk(self, path_length, rand=random.Random(), start=None):
		if start:
			path = [start]
		else:
			# Sampling is uniform w.r.t V, and not w.r.t E
			path = [rand.choice(list(self.nodes.keys()))]

		while len(path) < path_length:
			cur = path[-1]
			neighbor_nodes = self.nodes.get(cur, [])

			if len(neighbor_nodes) > 0:
				neighbor_probs = [self.edges[cur, node] for node in neighbor_nodes]
				next_node = neighbor_nodes[np.random.choice(len(neighbor_probs), 1, p=neighbor_probs)[0]]
				path.append(next_node)
			else:
				break
		return [str(node) for node in path]

	# TODO: Build correct way of multiprocessing
	def likely_walk_multiprocess(self, shared_list, path_length, rand=random.Random(), start=None):
		if start:
			path = [start]
		else:
			# Sampling is uniform w.r.t V, and not w.r.t E
			path = [rand.choice(list(self.nodes.keys()))]

		while len(path) < path_length:
			cur = path[-1]
			neighbor_nodes = self.nodes.get(cur, [])

			if len(neighbor_nodes) > 0:
				neighbor_probs = [self.edges[cur, node] for node in neighbor_nodes]
				next_node = neighbor_nodes[np.random.choice(len(neighbor_probs), 1, p=neighbor_probs)[0]]
				path.append(next_node)
			else:
				break
		shared_list.append([str(node) for node in path])

	def build_likely_walk_corpus(self, num_paths, path_length, rand=random.Random(0), shuffle=True, deduplicate=False):
		logger.info("Likely Walking without multiprocessing (multiprocess is available through seperate function: build_likely_walk_corpus_multiprocess)... ")
		walks = []

		nodes = list(self.nodes.keys())
		nodes_len = len(nodes)

		percent_done = 0
		for idx, node in enumerate(nodes):
			for cnt in range(num_paths):
				walks.append(self.likely_walk(path_length, rand=rand, start=node))
			if int(idx / (nodes_len / 100)) > percent_done:
				percent_done += 1
				logger.info(str(percent_done) + "% done")

		return self.check_walks(walks, rand, shuffle, deduplicate)

	def build_likely_walk_corpus_multiprocess(self, num_paths, path_length, rand=random.Random(0), shuffle=True, deduplicate=False):
		'''
		To avoid "Connection Refused Error", num_paths should be set below the number of available threads.
		'''
		logger.info("Likely Walking with multiprocessing ...")
		if num_paths > 7: # TODO: Build correct way of multiprocessing
			logger.warning("Setting num_paths higher than the thread count might cause Connection Lost Error.")

		walks = []

		nodes = list(self.nodes.keys())
		nodes_len = len(nodes)

		percent_done = 0
		for idx, node in enumerate(nodes):
			with Manager() as manager:
				L = manager.list()
				processes = []
				for cnt in range(num_paths):
					p = Process(target=self.likely_walk_multiprocess, args=(L, path_length, rand, node))
					p.start()
					processes.append(p)
				for p in processes:
					p.join()
				walks.extend(L)
			if int(idx/(nodes_len/100)) > percent_done:
				percent_done += 1
				logger.info(str(percent_done)+"% done, with "+str(len(walks))+" paths walked.")

		return self.check_walks(walks, rand, shuffle, deduplicate)

	def build_graph_from_matrix(self, x, is_directed=True, remove_self_loops=False, normalized_edge=True, outward_prob_check=False):
		# The x matrix is exactly the relationship map between them.
		logger.info("Building graph.")
		self.edges = x #For memmap compatibility
		if not issparse(self.edges):
			logger.info("Transforming into scipy sparse matrix")
			self.edges = csr_matrix(self.edges)

		# Iterate through matrix to get directed node -> node relationship
		logger.info("Build relation matrix (self.edges)")
		row_idxs, col_idxs = csr_matrix.nonzero(self.edges)
		assert len(row_idxs)==len(col_idxs)
		for i in range(len(row_idxs)):
			self.nodes[row_idxs[i]].append(col_idxs[i])

		self.make_consistent()

		if remove_self_loops:
			self.remove_self_loops()

		if not is_directed:
			self.make_bidirection()

		if normalized_edge:
			self.normalize_edges()

		self.check_valid(outward_prob_check=outward_prob_check)

	def get_alias_edge(self, prev, cur, p, q):
		"""
		Calculate pq_sample.

		:param prev: previous node
		:param cur: current node
		:param p: p value for
		:param q: q value for

		:return: next node sampled by probabilities
		"""
		#start = time()
		neighbor_nodes = self.nodes.get(cur, [])
		neighbor_probs = [self.edges[cur,node]*(1/p) if node==prev else self.edges[cur,node] if self.has_edge(prev,node)
			else self.edges[cur,node]*(1/q) for node in neighbor_nodes]

		assert (len(neighbor_probs) == len(neighbor_nodes))
		assert (all([p > 0 for p in neighbor_probs]))

		# Normalization for neighbor probabilities
		sum_prob = sum(neighbor_probs)
		neighbor_probs = np.asfarray([p/sum_prob for p in neighbor_probs], dtype='float32')

		J, q = alias_setup(neighbor_probs)
		return J, q

	def preprocess_node2vec_walk(self, p, q):
		logger.info("Preprocessing p, q sampled probabilities for node2vec walk...")
		self.alias_edge = dict()

		total_nodes = len(self.nodes.keys())
		percent_done = 0
		for i, prev in enumerate(self.nodes.keys()):
			cur_nodes = self.nodes.get(prev, [])
			for cur in cur_nodes:
				self.alias_edge[(prev,cur)] = self.get_alias_edge(prev, cur, p, q)
			if i/(total_nodes/100) > percent_done:
				percent_done += 1
				logger.info(str(percent_done)+"% done")
		logger.info("Done.")


def alias_setup(probs):
	"""
	Compute utility lists for non-uniform sampling from discrete distributions.
	Refer to https://hips.seas.harvard.edu/blog/2013/03/03/the-alias-method-efficient-sampling-with-many-discrete-outcomes/
	for details
	"""
	K = len(probs)
	q = np.zeros(K)
	J = np.zeros(K, dtype=np.int32)

	smaller = []
	larger = []
	for kk, prob in enumerate(probs):
		q[kk] = K * prob
		if q[kk] < 1.0:
			smaller.append(kk)
		else:
			larger.append(kk)

	while len(smaller) > 0 and len(larger) > 0:
		small = smaller.pop()
		large = larger.pop()

		J[small] = large
		q[large] = q[large] + q[small] - 1.0
		if q[large] < 1.0:
			smaller.append(large)
		else:
			larger.append(large)

	return J, q

def alias_draw(J, q):
	"""
	Draw sample from a non-uniform discrete distribution using alias sampling.
	"""
	K = len(J)

	kk = int(np.floor(np.random.rand() * K))
	if np.random.rand() < q[kk]:
		return kk
	else:
		return J[kk]

"""
Manage process relations
"""
import traceback
from collections import OrderedDict
from .exception import ProcTreeProcExists, ProcTreeParseError

class ProcNode(object):
	"""
	The node for processes to manage relations between each other
	"""

	def __init__(self, proc):
		"""
		Constructor
		@params:
			`proc`: The `Proc` instance
		"""
		self.proc    = proc
		self.prev    = [] # prev nodes
		self.next    = [] # next nodes
		self.ran     = False
		self.start   = False
		self.defs    = traceback.format_stack()[:-4]

	def sameIdTag(self, proc):
		"""
		Check if the process has the same id and tag with me.
		@params:
			`proc`: The `Proc` instance
		@returns:
			`True` if it is.
			`False` if not.
		"""
		return proc.id == self.proc.id and proc.tag  == self.proc.tag

	def __repr__(self):
		return '<ProcNode(<Proc(id=%s,tag=%s) @ %s>) @ %s>' % (self.proc.id, self.proc.tag, hex(id(self.proc)), hex(id(self)))


class ProcTree(object):
	"""
	A tree of processes.
	"""
	# all processes, key is the object id
	# use static, because we want different pipelines in the same session
	# have unique (id and tag)
	NODES    = OrderedDict()

	@staticmethod
	def register(proc):
		"""
		Register the process
		@params:
			`proc`: The `Proc` instance
		"""
		ProcTree.NODES[proc] = ProcNode(proc)

	@staticmethod
	def check(proc):
		"""
		Check whether a process with the same id and tag exists
		@params:
			`proc`: The `Proc` instance
		"""
		for p in ProcTree.NODES.keys():
			if p is proc: continue
			if ProcTree.NODES[p].sameIdTag(proc):
				raise ProcTreeProcExists(ProcTree.NODES[p], ProcTree.NODES[proc])

	@staticmethod
	def getPrevStr(proc):
		"""
		Get the names of processes a process depends on
		@params:
			`proc`: The `Proc` instance
		@returns:
			The names
		"""
		node = ProcTree.NODES[proc]
		prev = [np.proc.name() for np in node.prev]
		return 'START' if not prev else '[%s]' % ', '.join(prev)
	
	@staticmethod
	def getNextStr(proc):
		"""
		Get the names of processes depend on a process
		@params:
			`proc`: The `Proc` instance
		@returns:
			The names
		"""
		node = ProcTree.NODES[proc]
		nexs = [nn.proc.name() for nn in node.next]
		return 'END' if not nexs else '[%s]' % ', '.join(nexs)

	@staticmethod
	def getNext(proc):
		"""
		Get next processes of process
		@params:
			`proc`: The `Proc` instance
		@returns:
			The processes depend on this process
		"""
		node = ProcTree.NODES[proc]
		return [nn.proc for nn in node.next]

	@staticmethod
	def reset():
		"""
		Reset the status of all `ProcNode`s
		"""
		for node in ProcTree.NODES.values():
			node.prev   = []
			node.next   = []
			node.ran    = False
			node.start  = False
	
	def __init__(self):
		"""
		Constructor, set the status of all `ProcNode`s
		"""
		ProcTree.reset()
		self.starts  = [] # start procs
		self.ends    = [] # end procs
		# build prevs and nexts
		for node in ProcTree.NODES.values():
			depends = node.proc.depends
			if not depends: continue
			for dep in depends:
				dnode = ProcTree.NODES[dep]
				if node not in dnode.next:
					dnode.next.append(node)
				if dnode not in node.prev:
					node.prev.append(dnode)

	@classmethod
	def setStarts(cls, starts):
		"""
		Set the start processes
		@params:
			`starts`: The start processes
		"""
		for n in ProcTree.NODES.values():
			n.start = False
		for s in starts:
			ProcTree.NODES[s].start = True

	def getStarts(self):
		"""
		Get the start processes
		@returns:
			The start processes
		"""
		if not self.starts: 
			self.starts = [n.proc for n in ProcTree.NODES.values() if n.start]
		return self.starts

	def getPaths(self, proc, proc0 = None):
		"""
		Infer the path to a process
		@params:
			`proc`: The process
			`proc0`: The original process, because this function runs recursively.
		@returns:
			```
			p1 -> p2 -> p3
			      p4  _/
			Paths for p3: [[p4], [p2, p1]]
			```
		"""
		node  = proc if isinstance(proc, ProcNode) else ProcTree.NODES[proc]
		proc0 = proc0 or [node]
		paths = []
		for np in node.prev:
			if np in proc0:
				raise ProcTreeParseError(np.proc, 'Loop dependency through')
			if not np.prev:
				ps = [[np.proc]]
			else:
				ps = self.getPaths(np, proc0 + [np])
				for p in ps: p.insert(0, np.proc)
			paths.extend(ps)
		return paths

	def getPathsToStarts(self, proc):
		"""
		Filter the paths with start processes
		@params:
			`proc`: The process
		@returns:
			The filtered path
		"""
		paths  = self.getPaths(proc)
		ret    = []
		starts = self.getStarts()
		for path in paths:
			overlap = [p for p in path if p in starts]
			if not overlap: continue
			index   = max([path.index(p) for p in overlap])
			path    = path[:(index+1)]
			if path:
				ret.append(path[:(index+1)])
		return ret

	def checkPath(self, proc):
		"""
		Check whether paths of a process can start from a start process
		@params:
			`proc`: The process
		@returns:
			`True` if all paths can pass
			The failed path otherwise
		"""
		paths  = self.getPaths(proc)
		starts = set(self.getStarts())
		passed = True
		for path in paths:
			if not starts & set(path):
				passed = path
				break
		return passed

	def getEnds(self):
		"""
		Get the end processes
		@returns:
			The end processes
		"""
		if self.ends:
			return self.ends
			
		failedPaths = []
		nodes = [ProcTree.NODES[s] for s in self.getStarts()]
		while nodes:
			# check loops
			for n in nodes: self.getPaths(n)

			nodes2 = []
			for node in nodes:
				if not node.next:
					passed = self.checkPath(node)
					if passed is True:
						if node.proc not in self.ends: 
							self.ends.append(node.proc)
					else:
						passed.insert(0, node.proc)
						failedPaths.append(passed)
				else:
					nodes2.extend(node.next)
			nodes = set(nodes2)

		# didn't find any ends
		if not self.ends:
			if failedPaths:
				raise ProcTreeParseError(' <- '.join([fn.name() for fn in failedPaths[0]]), 'Failed to determine end processes, one of the paths cannot go through')
			else:
				raise ProcTreeParseError(', '.join(s.name() for s in self.getStarts()), 'Failed to determine end processes by start processes')
		return self.ends

	def getAllPaths(self):
		"""
		Get all paths of the pipeline
		"""
		ret = set()
		ends = self.getEnds()
		for end in ends:
			paths = self.getPathsToStarts(end)
			if not paths:
				p = [end]
				pstr = str(p)
				if pstr not in ret:
					yield [end]
					ret.add(pstr)
			else:
				for p in paths:
					p = [end] + p
					pstr = str(p)
					if pstr not in ret:
						yield p
						ret.add(pstr)

	@classmethod
	def getNextToRun(cls):
		"""
		Get the process to run next
		@returns:
			The process next to run
		"""
		#ret = []
		for node in ProcTree.NODES.values():
			# already ran
			if node.ran: continue
			# not a start and not depends on any procs
			if not node.start and not node.prev: continue
			# start
			if node.start or all([p.ran for p in node.prev]):
				node.ran = True
				return node.proc
				#ret.append(node.proc)
		return None

	def unranProcs(self):
		"""
		Get the unran processes.
		@returns:
			The processes haven't run.
		"""
		ret = {}
		starts = set(self.getStarts())
		for node in ProcTree.NODES.values():
			# just for possible end process
			if node.next: continue
			# don't report obsolete process
			if not self.getPathsToStarts(node): continue
			# check paths can't reach
			paths = self.getPaths(node)
			for ps in paths:
				# the path can be reached
				if set(ps) & set(starts): continue
				ret[node.proc.name()] = [p.name() for p in ps]
				break
		return ret

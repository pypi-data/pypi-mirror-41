"""
SGE runner for PyPPL
"""

import re
import copy
from subprocess import CalledProcessError, list2cmdline
from .runner import Runner
from ..utils import cmd, box

class RunnerSge (Runner):
	"""
	The sge runner
	"""
	
	INTERVAL = 5

	def __init__ (self, job):
		"""
		Constructor
		@params:
			`job`:    The job object
			`config`: The properties of the process
		"""
		super(RunnerSge, self).__init__(job)

		# construct an sge script
		self.script = self.job.script + '.sge'
		sgesrc  = ['#!/usr/bin/env bash']

		conf = self.job.config.get('runnerOpts', {})
		conf = copy.copy(conf.get('sgeRunner', {}))
		
		self.commands = {'qsub': 'qsub', 'qstat': 'qstat', 'qdel': 'qdel'}
		if 'qsub' in conf:
			self.commands['qsub'] = conf['qsub']
		if 'qstat' in conf:
			self.commands['qstat'] = conf['qstat']
		if 'qdel' in conf:
			self.commands['qdel'] = conf['qdel']
			
		if not 'sge.N' in conf:
			jobname = '.'.join([
				self.job.config['proc'],
				self.job.config['tag'],
				self.job.config['suffix'],
				str(self.job.index + 1)
			])
			sgesrc.append('#$ -N %s' % jobname)
		else:
			jobname = conf['sge.N']
			sgesrc.append('#$ -N %s' % jobname)
			del conf['sge.N']
		
		if 'sge.q' in conf:
			sgesrc.append('#$ -q %s' % conf['sge.q'])
			del conf['sge.q']
			
		if 'sge.j' in conf:
			sgesrc.append('#$ -j %s' % conf['sge.j'])
			del conf['sge.j']
		
		if 'sge.o' in conf:
			sgesrc.append('#$ -o %s' % conf['sge.o'])
			del conf['sge.o']
		else:
			sgesrc.append('#$ -o %s' % self.job.outfile)
			
		if 'sge.e' in conf:
			sgesrc.append('#$ -e %s' % conf['sge.e'])
			del conf['sge.e']
		else:
			sgesrc.append('#$ -e %s' % self.job.errfile)
			
		sgesrc.append('#$ -cwd')
		
		if 'sge.M' in conf:
			sgesrc.append('#$ -M %s' % conf['sge.M'])
			del conf['sge.M']
		
		if 'sge.m' in conf:
			sgesrc.append('#$ -m %s' % conf['sge.m'])
			del conf['sge.m']
		
		for k in sorted(conf.keys()):
			if not k.startswith ('sge.'): continue
			v = conf[k]
			k = k[4:].strip()
			src = '#$ -' + k
			if v != True: # {'notify': True} ==> -notify
				src += ' ' + str(v)
			sgesrc.append(src)

		sgesrc.append ('')
		sgesrc.append ('trap "status=\\$?; echo \\$status >\'%s\'; exit \\$status" 1 2 3 6 7 8 9 10 11 12 15 16 17 EXIT' % self.job.rcfile)
		
		if 'preScript' in conf:
			sgesrc.append (conf['preScript'])

		sgesrc.append ('')
		sgesrc.append (self.cmd2run)

		if 'postScript' in conf:
			sgesrc.append (conf['postScript'])
		
		with open (self.script, 'w') as f:
			f.write ('\n'.join(sgesrc) + '\n')
		
	def submit(self):
		"""
		Submit the job
		@returns:
			The `utils.cmd.Cmd` instance if succeed 
			else a `Box` object with stderr as the exception and rc as 1
		"""
		cmdlist = [self.commands['qsub'], self.script]
		try:
			r = cmd.run(cmdlist)
			# Your job 6556149 ("pSort.notag.3omQ6NdZ.0") has been submitted
			m = re.search(r'\s(\d+)\s', r.stdout)
			if not m:
				r.rc = 1
			else:
				self.job.pid = m.group(1)
			return r

		except (OSError, CalledProcessError) as ex:
			r        = box.Box()
			r.stderr = str(ex)
			r.rc     = 1
			r.cmd    = list2cmdline(cmdlist)
			return r

	def kill(self):
		"""
		Kill the job
		"""
		cmdlist = [self.commands['qdel'], '--force', str(self.job.pid)]
		try:
			cmd.run(cmdlist)
		except (OSError, CalledProcessError): # pragma: no cover
			pass

	def isRunning(self):
		"""
		Tell if the job is alive
		@returns:
			`True` if it is else `False`
		"""
		if not self.job.pid:
			return False
		cmdlist = [self.commands['qstat'], '-j', str(self.job.pid)]
		try:
			r = cmd.run(cmdlist)
			return r.rc == 0
		except (OSError, CalledProcessError):
			return False

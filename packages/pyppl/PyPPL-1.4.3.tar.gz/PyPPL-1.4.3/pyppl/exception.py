"""
A set of exceptions used by PyPPL
"""

class LoggerThemeError(Exception):
	"""Theme errors for logger"""
	def __init__(self, name, msg = None):
		msg = msg or "Logger theme error"
		super(LoggerThemeError, self).__init__(str(msg) + ': ' + repr(name))

class ParameterNameError(Exception):
	"""Malformed name not allowed"""
	def __init__(self, name, msg = None):
		msg = msg or "Parameter name error"
		super(ParameterNameError, self).__init__(str(msg) + ': ' + repr(name))

class ParameterTypeError(TypeError):
	"""Unable to set type"""
	def __init__(self, name, msg = None):
		msg = msg or "Parameter type error"
		super(ParameterTypeError, self).__init__(str(msg) + ': ' + repr(name))

class ParametersParseError(Exception):
	"""Error when parsing the parameters"""
	def __init__(self, name, msg = None):
		msg = msg or 'Error when parsing command line arguments'
		super(ParametersParseError, self).__init__(str(msg) + ': ' + repr(name))

class ParametersLoadError(Exception):
	"""Error loading dict to Parameters"""
	def __init__(self, name, msg = None):
		msg = msg or 'Error loading dict to Parameters'
		super(ParametersLoadError, self).__init__(str(msg) + ': ' + repr(name))

class ProcTreeProcExists(Exception):
	"""Raise when two Procs with same id and tag defined"""
	def __init__(self, pn1, pn2):
		msg = [
			"There are two processes with id(%s) and tag(%s)" % (pn1.proc.id, pn1.proc.tag),
			"",
			">>> One is defined here:",
			''.join(pn1.defs),
			">>> The other is defined here:",
			''.join(pn2.defs)
		]
		super(ProcTreeProcExists, self).__init__("\n".join(msg))

class ProcTreeParseError(Exception):
	"""Raise when failed to parse the tree"""
	def __init__(self, name, msg = None):
		msg = msg or 'Failed to parse the process tree'
		super(ProcTreeParseError, self).__init__(str(msg) + ': ' + repr(name))

class JobInputParseError(Exception):
	"""Raise when failed to parse the input data for jobs"""
	def __init__(self, name, msg = None):
		msg = msg or 'Failed to parse the input data'
		super(JobInputParseError, self).__init__(str(msg) + ': ' + str(name))

class JobOutputParseError(Exception):
	"""Raise when failed to parse the output data for jobs"""
	def __init__(self, name, msg = None):
		msg = msg or 'Failed to parse the output data'
		super(JobOutputParseError, self).__init__(str(msg) + ': ' + repr(name))

class RunnerSshError(Exception):
	"""Raise when failed to initiate RunnerSsh"""
	def __init__(self, msg = 'Failed to initiate RunnerSsh'):
		super(RunnerSshError, self).__init__(str(msg))

class ProcTagError(Exception):
	"""Raise when malformed tag is assigned to a process"""
	def __init__(self, msg = 'Failed to specify tag for process.'):
		super(ProcTagError, self).__init__(str(msg))

class ProcAttributeError(AttributeError):
	"""Raise when set/get process' attributes"""
	def __init__(self, name, msg = 'No such attribute'):
		super(ProcAttributeError, self).__init__(str(msg) + ': ' + repr(name))

class ProcInputError(Exception):
	"""Raise when failed to parse process input"""
	def __init__(self, name, msg = 'Failed to parse input'):
		super(ProcInputError, self).__init__(str(msg) + ': ' + repr(name))

class ProcOutputError(Exception):
	"""Raise when failed to parse process output"""
	def __init__(self, name, msg = 'Failed to parse output'):
		super(ProcOutputError, self).__init__(str(msg) + ': ' + repr(name))

class ProcScriptError(Exception):
	"""Raise when failed to parse process script"""
	def __init__(self, name, msg = 'Failed to parse process script'):
		super(ProcScriptError, self).__init__(str(msg) + ': ' + repr(name))

class ProcRunCmdError(Exception):
	"""Raise when failed to run before/after cmds for process"""
	def __init__(self, cmd, key, ex = ''):
		msg = 'Failed to run <%s>: %s\n\n' % (key, str(ex))
		msg += cmd
		super(ProcRunCmdError, self).__init__(msg)

class PyPPLProcFindError(Exception):
	"""Raise when failed to find a proc"""
	def __init__(self, p, msg = 'Failed to find process'):
		super(PyPPLProcFindError, self).__init__(str(msg) + ': ' + repr(p))

class PyPPLProcRelationError(Exception):
	"""Raise when failed to parse the relation of processes"""
	def __init__(self, p, msg):
		super(PyPPLProcRelationError, self).__init__(str(msg) + ': ' + repr(p))

class PyPPLConfigError(Exception):
	"""Raise when failed to parse the configuration of pyppl"""
	def __init__(self, key, msg):
		super(PyPPLConfigError, self).__init__(str(msg) + ': ' + repr(key))

class AggrAttributeError(AttributeError):
	"""Raise when there is an error to set/get Aggr attributes"""
	def __init__(self, key, msg):
		super(AggrAttributeError, self).__init__(str(msg) + ': ' + repr(key))

class AggrCopyError(Exception):
	"""Raise when there is an error to set/get Aggr attributes"""
	def __init__(self, key, msg = 'Failed to copy aggregation'):
		super(AggrCopyError, self).__init__(str(msg) + ': ' + repr(key))

class AggrKeyError(KeyError):
	"""Raise when error occurred doing aggr[...]"""
	def __init__(self, key, msg = 'Key error'):
		super(AggrKeyError, self).__init__(str(msg) + ': ' + repr(key))

class JobFailException(Exception):
	"""Raise when a job failed to run"""
	pass

class JobSubmissionException(Exception):
	"""Raise when a job failed to submit"""
	pass

class JobBuildingException(Exception):
	"""Raise when a job failed to build"""
	pass

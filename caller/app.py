import caller

class App:

	#
	# initiailses the app and secret of the app
	#
	@classmethod
	def init(cls):
		cls.base    = None

	#
	# sets the base url of the app
	#
	@classmethod
	def set_base(cls, base = None):
		cls.base = base

	#
	# returns the base url of the app
	#
	@classmethod
	def get_base(cls):
		return cls.base

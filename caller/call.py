import caller
from caller.http import request

class Call:

	def __init__(self):
		self.request = request.Request()


	#
	# Returns a Call
	#
	def call(self, endpoint = None):
		return self.request.request(
			'get', endpoint)

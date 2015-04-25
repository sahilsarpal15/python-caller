import json
import caller
from caller.http import client
from caller.http.response import Response

class Request(object):
	def __init__(self):
		self.client  = client.Client()
		self.base    = caller.App().get_base()

	#
	# Manages all the processing of the request
	#
	def request(self, method, endpoint, params=None):

		# creating an request
		result = self.request_raw(
			method, endpoint, params)

		return Response(result)

	#
	# Handles the requset to be send
	#
	def request_raw(self, method, endpoint, params):
		if endpoint == None:
		    url = self.base
		else:
		    url = self.base + endpoint

		auth = None

		headers = {
			'Content-Type' : 'application/json'
		}


		# encoding the parameters
		params = json.dumps(params)

		return self.client.request(
			method, url, headers, auth, params)

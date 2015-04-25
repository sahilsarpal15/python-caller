import caller

print "Attempting horn..."

try:
	caller.App().set_base('http://naukri.com')
	resp = caller.Call().call()
	orignal = resp.get_original()
	print 'Success: %r' % (orignal.content)
	# print 'Success: %r' % (resp)
except Exception, e:
	print e

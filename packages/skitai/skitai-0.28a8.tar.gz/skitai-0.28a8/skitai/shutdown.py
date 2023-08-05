def shutdown (root):
	import md5
	import os
	from rs4  import confparse	
	from rs4  import timeoutsocket
	import urllib.request, urllib.parse, urllib.error
	
	cf = confparse.ConfParse (os.path.join (root, "etc/server.conf"))	
	port = cf.getint ("server", "port")
	timeoutsocket.setDefaultSocketTimeout (3)
	try:
		urllib.request.urlopen ("http://127.0.0.1:%d/admin/maintern/shutdown" % port)
	except AttributeError:
		pass	
	
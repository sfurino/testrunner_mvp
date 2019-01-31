#!/usr/bin/python

# A crude demo testrunner server.
# Generates test indexes and serves them up locally

# A real implementation would likely serve with a better httpd
# and support distributed publishing from multiple team
# repositories, pull requests, locked team directories, and all
# sorts of goodness.


import os
import SimpleHTTPServer
import SocketServer


PORT=8400
tr='demo-testroot'

idxn='.tr.idx'

idxf='{}|{}|{}\n'

# Create tr.idx files for each test
## First, find tests
tests=[]
for dp,dn,fn in os.walk(tr):
	dps=dp.split(os.path.sep)
	if len(dps) == 4:
		if dps[2] == 'tests':
			tests.append(dp)

## Second, index tests
for t in tests:
	idxfn=os.path.join(t,idxn)
	with open(idxfn, 'w') as out:
		print 'Generating', idxfn
		for dp,dn,fn in os.walk(t):
			ldn=dp.replace(t,'').strip(os.path.sep)
			for name in dn:
				rfn=os.path.join(dp,name)
				mode=str(oct(os.stat(rfn).st_mode & 0o777))
				out.write(idxf.format("DIR",os.path.join(ldn,name), mode))
			for name in fn:
				if name == idxf:
					continue
				rfn=os.path.join(dp,name)
				mode=str(oct(os.stat(rfn).st_mode & 0o777))
				out.write(idxf.format("FILE",os.path.join(ldn,name), mode))



## Serve
os.chdir(tr)
H=SimpleHTTPServer.SimpleHTTPRequestHandler
httpd=SocketServer.TCPServer(('',PORT), H)
print "Starting webserver"
httpd.serve_forever()

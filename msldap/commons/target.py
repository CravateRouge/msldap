
#!/usr/bin/env python3
#
# Author:
#  Tamas Jos (@skelsec)
#

import enum
from urllib.parse import urlparse, parse_qs


class LDAPProtocol(enum.Enum):
	TCP = 'TCP'
	UDP = 'UDP'
	SSL = 'SSL'


class MSLDAPTarget:
	def __init__(self, host, port = 389, proto = LDAPProtocol.TCP, tree = None, proxy = None, timeout = 10):
		self.proto = proto
		self.host = host
		self.tree = tree
		self.port = port
		self.proxy = proxy
		self.timeout = timeout
		self.dc_ip = None
		self.domain = None

	def to_target_string(self):
		return 'ldap/%s@%s' % (self.host,self.domain)  #ldap/WIN2019AD.test.corp @ TEST.CORP

	def get_host(self):
		return '%s://%s:%s' % (self.proto, self.host, self.port)

	def is_ssl(self):
		return self.proto == LDAPProtocol.SSL
	
	def __str__(self):
		t = '==== MSLDAPTarget ====\r\n'
		for k in self.__dict__:
			t += '%s: %s\r\n' % (k, self.__dict__[k])
			
		return t
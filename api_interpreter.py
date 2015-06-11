Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> import os
>>> os.environ['OS_USERNAME']
'demo'
>>> os.environ['OS_PASSWD']

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    os.environ['OS_PASSWD']
  File "/usr/lib/python2.7/UserDict.py", line 23, in __getitem__
    raise KeyError(key)
KeyError: 'OS_PASSWD'
>>> os.environ['OS_PASSWORD']
'nomoresecrete'
>>> os.environ['OS_AUTH_URL']
'http://192.168.80.130:5000/v2.0'
>>> def get_keystone_creds():
	d = {}
	d['username'] = os.environ['OS_USERNAME']
	d['password'] = os.environ['OS_PASSWORD']
	d['auth_url'] = os.environ['OS_AUTH_URL']
	d['tenant_name'] = os.environ['OS_TENANT_NAME']
	return d

>>> 
>>> def get_keystone_admin_creds():
	d = {}
	d['username'] = 'admin'
	d['password'] = 'nomoresecrete'
	d['auth_url'] = 'http://192.168.80.130:5000/v2.0'
	d['tenant_name'] = 'admin'
	return d

>>> import keystoneclient.v2_0.client as ksclient
>>> creds = get_keystone_admin_creds()
>>> creds
{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> keystone = ksclient.Client(**creds)
>>> keystone.auth_token
u'9eceeb2176e440128d0459864752e733'
>>> keystone.tenants.list()
[<Tenant {u'enabled': True, u'description': None, u'name': u'service', u'id': u'42a758197838431ea8d23aa3792ea9f6'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'invisible_to_admin', u'id': u'9de40b4a9e4d4fae9a2010879e4c4e24'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'demo', u'id': u'd8f42a85e023411080a86768fa0e4692'}>]
>>> dir(keystone)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_adapter', '_auth_token', '_build_keyring_key', '_cs_request', '_endpoint', '_management_url', '_process_management_url', 'auth_domain_id', 'auth_ref', 'auth_tenant_id', 'auth_token', 'auth_token_from_user', 'auth_url', 'auth_user_id', 'authenticate', 'certificates', 'debug_log', 'delete', 'deprecated_adapter_variables', 'deprecated_session_variables', 'domain', 'domain_id', 'domain_name', 'ec2', 'endpoints', 'extensions', 'force_new_token', 'get', 'get_auth_ref_from_keyring', 'get_endpoint', 'get_headers', 'get_options', 'get_project_id', 'get_raw_token_from_identity_service', 'get_token', 'get_user_id', 'has_service_catalog', 'head', 'invalidate', 'load_from_argparse_arguments', 'load_from_conf_options', 'load_from_options', 'load_from_options_getter', 'management_url', 'password', 'patch', 'post', 'process_token', 'project_domain_id', 'project_domain_name', 'project_id', 'project_name', 'put', 'register_argparse_arguments', 'register_conf_options', 'request', 'roles', 'serialize', 'service_catalog', 'services', 'session', 'stale_duration', 'store_auth_ref_into_keyring', 'tenant_id', 'tenant_name', 'tenants', 'tokens', 'trust_id', 'use_keyring', 'user_domain_id', 'user_domain_name', 'user_id', 'username', 'users', 'version']
>>> keystone.services.list()
[<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}>, <Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>, <Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}>, <Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}>, <Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}>, <Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}>, <Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}>, <Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}>, <Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}>, <Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}>]
>>> keystone.users.list()
[<User {u'username': u'heat', u'id': u'126452eda45e47549d8c7e75f355c76e', u'enabled': True, u'name': u'heat', u'email': None}>, <User {u'username': u'admin', u'id': u'5651e750923546e695e06ca9a810c759', u'enabled': True, u'name': u'admin', u'email': None}>, <User {u'username': u'neutron', u'id': u'81758bbaec0c420fbe97e5fbdbb52152', u'enabled': True, u'name': u'neutron', u'email': None}>, <User {u'username': u'cinder', u'id': u'934ff7c1dc1845a48244a3232d67c86a', u'enabled': True, u'name': u'cinder', u'email': None}>, <User {u'username': u'nova', u'id': u'c457ef7813c149eca1c6b1b02da394ca', u'enabled': True, u'name': u'nova', u'email': None}>, <User {u'username': u'glance', u'id': u'ccfa207f5b33407699ed3d39b96319d8', u'enabled': True, u'name': u'glance', u'email': None}>, <User {u'username': u'demo', u'id': u'f2e0e944388943e389e5f50f0de1ade3', u'enabled': True, u'name': u'demo', u'email': u'demo@example.com'}>]
>>> len(keystone.users.list())
7
>>> users = keystone.users.list()
>>> for u in users:
	print u
	print "\n"

	
<User {u'username': u'heat', u'id': u'126452eda45e47549d8c7e75f355c76e', u'enabled': True, u'name': u'heat', u'email': None}>


<User {u'username': u'admin', u'id': u'5651e750923546e695e06ca9a810c759', u'enabled': True, u'name': u'admin', u'email': None}>


<User {u'username': u'neutron', u'id': u'81758bbaec0c420fbe97e5fbdbb52152', u'enabled': True, u'name': u'neutron', u'email': None}>


<User {u'username': u'cinder', u'id': u'934ff7c1dc1845a48244a3232d67c86a', u'enabled': True, u'name': u'cinder', u'email': None}>


<User {u'username': u'nova', u'id': u'c457ef7813c149eca1c6b1b02da394ca', u'enabled': True, u'name': u'nova', u'email': None}>


<User {u'username': u'glance', u'id': u'ccfa207f5b33407699ed3d39b96319d8', u'enabled': True, u'name': u'glance', u'email': None}>


<User {u'username': u'demo', u'id': u'f2e0e944388943e389e5f50f0de1ade3', u'enabled': True, u'name': u'demo', u'email': u'demo@example.com'}>


>>> services = keystone.services.list()
>>> for s in services:
	print s

	
<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}>
<Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>
<Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}>
<Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}>
<Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}>
<Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}>
<Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}>
<Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}>
<Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}>
<Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}>
>>> for s in services:
	print s + "\n"

	

Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    print s + "\n"
TypeError: unsupported operand type(s) for +: 'Service' and 'str'
>>> for s in services:
	print s
	print "\n"

	
<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}>


<Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>


<Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}>


<Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}>


<Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}>


<Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}>


<Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}>


<Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}>


<Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}>


<Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}>


>>> s1 = services[1]
>>> s1
<Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>
>>> dir(s1)
['HUMAN_ID', 'NAME_ATTR', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_details', '_info', '_loaded', 'delete', 'description', 'enabled', 'get', 'human_id', 'id', 'is_loaded', 'manager', 'name', 'set_loaded', 'to_dict', 'type']
>>> s1.name
u'cinderv2'
>>> s1.description
u'Cinder Volume Service V2'
>>> keystone.session
<keystoneclient.session.Session object at 0x7f141db26c50>
>>> 
>>> ksclient.endpoints.list()

Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ksclient.endpoints.list()
AttributeError: 'module' object has no attribute 'list'
>>> 
>>> dir(ksclient.endpoints)
['Endpoint', 'EndpointManager', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'base']
>>> 
>>> ksclient.users.list()

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    ksclient.users.list()
AttributeError: 'module' object has no attribute 'list'
>>> 
>>> keystone.endpoints.list()
[<Endpoint {u'adminurl': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'enabled': True, u'id': u'9a1764a2ecfd4890a5d80edb03365d99', u'service_id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'internalurl': u'http://192.168.80.130:9696/', u'publicurl': u'http://192.168.80.130:9696/'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'71c0c32a001848e98d62ef44df238633', u'service_id': u'a5717708347648c19306ddb197cc7b9f', u'internalurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'enabled': True, u'id': u'e48968c44dfc4724a3cd96365531b585', u'service_id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'internalurl': u'http://192.168.80.130:8773/', u'publicurl': u'http://192.168.80.130:8773/'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'enabled': True, u'id': u'a53a05b0c1ee49dfae3f03f7aaf97721', u'service_id': u'f0ae91766045456a9e19fa36f52fdd9d', u'internalurl': u'http://192.168.80.130:9292', u'publicurl': u'http://192.168.80.130:9292'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:5000/v2.0', u'service_id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'id': u'a61044ddcefa4df283e79184ebea3cd4', u'publicurl': u'http://192.168.80.130:5000/v2.0'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'enabled': True, u'id': u'94d0e7eafa244ed49485ac0b82361ffe', u'service_id': u'1601c35405454cdd8a935c492c2dfe66', u'internalurl': u'http://192.168.80.130:8000/v1', u'publicurl': u'http://192.168.80.130:8000/v1'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8755e2c0681b44e28a98097ba8935f8b', u'service_id': u'74152f778c794c3582c2d418f4fe62f4', u'internalurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'25e18edad644455d828020d89a937976', u'service_id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'internalurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8b64ac979eef4064988315e1596ecac0', u'service_id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'internalurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s'}>]
>>> for x in keystone.endpoints.list():
	print x
	print "\n"

	
<Endpoint {u'adminurl': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'enabled': True, u'id': u'9a1764a2ecfd4890a5d80edb03365d99', u'service_id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'internalurl': u'http://192.168.80.130:9696/', u'publicurl': u'http://192.168.80.130:9696/'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'71c0c32a001848e98d62ef44df238633', u'service_id': u'a5717708347648c19306ddb197cc7b9f', u'internalurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'enabled': True, u'id': u'e48968c44dfc4724a3cd96365531b585', u'service_id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'internalurl': u'http://192.168.80.130:8773/', u'publicurl': u'http://192.168.80.130:8773/'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'enabled': True, u'id': u'a53a05b0c1ee49dfae3f03f7aaf97721', u'service_id': u'f0ae91766045456a9e19fa36f52fdd9d', u'internalurl': u'http://192.168.80.130:9292', u'publicurl': u'http://192.168.80.130:9292'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:5000/v2.0', u'service_id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'id': u'a61044ddcefa4df283e79184ebea3cd4', u'publicurl': u'http://192.168.80.130:5000/v2.0'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'enabled': True, u'id': u'94d0e7eafa244ed49485ac0b82361ffe', u'service_id': u'1601c35405454cdd8a935c492c2dfe66', u'internalurl': u'http://192.168.80.130:8000/v1', u'publicurl': u'http://192.168.80.130:8000/v1'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8755e2c0681b44e28a98097ba8935f8b', u'service_id': u'74152f778c794c3582c2d418f4fe62f4', u'internalurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'25e18edad644455d828020d89a937976', u'service_id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'internalurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8b64ac979eef4064988315e1596ecac0', u'service_id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'internalurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s'}>


>>> x1 = keystone.endpoints.list()[1]
>>> x1
<Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}>
>>> 
>>> dir(x1)
['HUMAN_ID', 'NAME_ATTR', '__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_add_details', '_info', '_loaded', 'adminurl', 'delete', 'enabled', 'get', 'human_id', 'id', 'internalurl', 'is_loaded', 'manager', 'publicurl', 'region', 'service_id', 'set_loaded', 'to_dict']
>>> x1.HUMAN_ID
False
>>> x1.NAME_ATTR
'name'
>>> x1.adminurl
u'http://192.168.80.130:8004/v1/$(tenant_id)s'
>>> x1.manager
<keystoneclient.v2_0.endpoints.EndpointManager object at 0x7f141db26c10>
>>> 
>>> import retrying
>>> dir(retrying)
['Attempt', 'MAX_WAIT', 'RetryError', 'Retrying', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'random', 'retry', 'six', 'sys', 'time', 'traceback']
>>> 
>>> 
>>> from heatclient.v1 import client as heatclient
>>> 
>>> 
>>> demo_creds = get_keystone_creds()
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> 
>>> hc = heatclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    hc = heatclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/client.py", line 40, in __init__
    self.http_client = http._construct_http_client(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 389, in _construct_http_client
    return HTTPClient(*args, **kwargs)
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> import novaclient.v1_1.client as nvclient

Warning (from warnings module):
  File "/usr/local/lib/python2.7/dist-packages/novaclient/v1_1/__init__.py", line 30
    warnings.warn("Module novaclient.v1_1 is deprecated (taken as a basis for "
UserWarning: Module novaclient.v1_1 is deprecated (taken as a basis for novaclient.v2). The preferable way to get client class or object you can find in novaclient.client module.
>>> import novaclient.v2.client as nvclient
>>> 
>>> nova = nvclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    nova = nvclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/novaclient/v2/client.py", line 227, in __init__
    **kwargs)
TypeError: _construct_http_client() got multiple values for keyword argument 'password'
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> hc = heatclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    hc = heatclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/client.py", line 40, in __init__
    self.http_client = http._construct_http_client(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 389, in _construct_http_client
    return HTTPClient(*args, **kwargs)
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> hc = heatclient.Client(demo_creds)

Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    hc = heatclient.Client(demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/client.py", line 40, in __init__
    self.http_client = http._construct_http_client(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 389, in _construct_http_client
    return HTTPClient(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 83, in __init__
    if parse.urlparse(endpoint).scheme == "https":
  File "/usr/lib/python2.7/urlparse.py", line 143, in urlparse
    tuple = urlsplit(url, scheme, allow_fragments)
  File "/usr/lib/python2.7/urlparse.py", line 176, in urlsplit
    cached = _parse_cache.get(key, None)
TypeError: unhashable type: 'dict'
>>> 
>>> hc = heatclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    hc = heatclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/client.py", line 40, in __init__
    self.http_client = http._construct_http_client(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 389, in _construct_http_client
    return HTTPClient(*args, **kwargs)
TypeError: __init__() takes exactly 2 arguments (1 given)
>>> 
>>> os.environ['HEAT_URL']

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    os.environ['HEAT_URL']
  File "/usr/lib/python2.7/UserDict.py", line 23, in __getitem__
    raise KeyError(key)
KeyError: 'HEAT_URL'
>>> ksclient.tenants.list()

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    ksclient.tenants.list()
AttributeError: 'module' object has no attribute 'list'
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'creds', 'demo_creds', 'get_keystone_admin_creds', 'get_keystone_creds', 'heatclient', 'keystone', 'ksclient', 'nvclient', 'os', 'retrying', 's', 's1', 'services', 'u', 'users', 'x', 'x1']
>>> keystone.tenants.list()
[<Tenant {u'enabled': True, u'description': None, u'name': u'service', u'id': u'42a758197838431ea8d23aa3792ea9f6'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'invisible_to_admin', u'id': u'9de40b4a9e4d4fae9a2010879e4c4e24'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'demo', u'id': u'd8f42a85e023411080a86768fa0e4692'}>]
>>> 
>>> for t in keystone.tenants.list():
	print t
	print "\n"

	
<Tenant {u'enabled': True, u'description': None, u'name': u'service', u'id': u'42a758197838431ea8d23aa3792ea9f6'}>


<Tenant {u'enabled': True, u'description': None, u'name': u'invisible_to_admin', u'id': u'9de40b4a9e4d4fae9a2010879e4c4e24'}>


<Tenant {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}>


<Tenant {u'enabled': True, u'description': None, u'name': u'demo', u'id': u'd8f42a85e023411080a86768fa0e4692'}>


>>> for e in keystone.endpoints.list():
	print e
	print "\n"

	
<Endpoint {u'adminurl': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'enabled': True, u'id': u'9a1764a2ecfd4890a5d80edb03365d99', u'service_id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'internalurl': u'http://192.168.80.130:9696/', u'publicurl': u'http://192.168.80.130:9696/'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'71c0c32a001848e98d62ef44df238633', u'service_id': u'a5717708347648c19306ddb197cc7b9f', u'internalurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'enabled': True, u'id': u'e48968c44dfc4724a3cd96365531b585', u'service_id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'internalurl': u'http://192.168.80.130:8773/', u'publicurl': u'http://192.168.80.130:8773/'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'enabled': True, u'id': u'a53a05b0c1ee49dfae3f03f7aaf97721', u'service_id': u'f0ae91766045456a9e19fa36f52fdd9d', u'internalurl': u'http://192.168.80.130:9292', u'publicurl': u'http://192.168.80.130:9292'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:5000/v2.0', u'service_id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'id': u'a61044ddcefa4df283e79184ebea3cd4', u'publicurl': u'http://192.168.80.130:5000/v2.0'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'enabled': True, u'id': u'94d0e7eafa244ed49485ac0b82361ffe', u'service_id': u'1601c35405454cdd8a935c492c2dfe66', u'internalurl': u'http://192.168.80.130:8000/v1', u'publicurl': u'http://192.168.80.130:8000/v1'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8755e2c0681b44e28a98097ba8935f8b', u'service_id': u'74152f778c794c3582c2d418f4fe62f4', u'internalurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'25e18edad644455d828020d89a937976', u'service_id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'internalurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s'}>


<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8b64ac979eef4064988315e1596ecac0', u'service_id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'internalurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s'}>


>>> 
>>> [<Tenant {u'enabled': True, u'description': None, u'name': u'service', u'id': u'42a758197838431ea8d23aa3792ea9f6'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'invisible_to_admin', u'id': u'9de40b4a9e4d4fae9a2010879e4c4e24'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}>, <Tenant {u'enabled': True, u'description': None, u'name': u'demo', u'id': u'd8f42a85e023411080a86768fa0e4692'}>]
SyntaxError: invalid syntax
>>> 
>>> heat_endpoint = "http://192.168.80.130:8004/v1/"
>>> heat_endpoint += "d8f42a85e023411080a86768fa0e4692"
>>> heat_endpoint
'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> demo_creds['endpoint'] = heat_endpoint
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'endpoint': 'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'}
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'creds', 'demo_creds', 'e', 'get_keystone_admin_creds', 'get_keystone_creds', 'heat_endpoint', 'heatclient', 'keystone', 'ksclient', 'nvclient', 'os', 'retrying', 's', 's1', 'services', 't', 'u', 'users', 'x', 'x1']
>>> heat = heatclient.Client(**demo_creds)
>>> 
>>> heat.stacks.list()
<generator object paginate at 0x7f141d6b9e60>
>>> for s in heat.stacks.list():
	print s

	

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> 
>>> heat.http_client
<heatclient.common.http.HTTPClient object at 0x7f141d6ae610>
>>> heat.http_client.auth_token
>>> 
>>> print heat.http_client.auth_token
None
>>> dir(heat.stacks)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_delete', '_get', '_head', '_hooks_map', '_list', '_patch', '_post', '_put', 'abandon', 'add_hook', 'client', 'create', 'delete', 'get', 'list', 'preview', 'resource_class', 'restore', 'run_hooks', 'snapshot', 'snapshot_delete', 'snapshot_list', 'snapshot_show', 'template', 'update', 'validate']
>>> 
>>> dir(heat)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'actions', 'build_info', 'events', 'http_client', 'resource_types', 'resources', 'services', 'software_configs', 'software_deployments', 'stacks']
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'endpoint': 'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'}
>>> heat = heatclient.Cl

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    heat = heatclient.Cl
AttributeError: 'module' object has no attribute 'Cl'
>>> 
>>> dir(heatclient)
['Client', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'actions', 'build_info', 'events', 'http', 'resource_types', 'resources', 'services', 'software_configs', 'software_deployments', 'stacks']
>>> type(heatclient)
<type 'module'>
>>> 
>>> keystone.auth_token
u'cb7d4d2ab474410fbb03f98a8059da58'
>>> keystone.services.list()
[<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}>, <Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>, <Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}>, <Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}>, <Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}>, <Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}>, <Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}>, <Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}>, <Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}>, <Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}>]
>>> 
>>> keystone.auth_token
u'cb7d4d2ab474410fbb03f98a8059da58'
>>> 
>>> 
>>> del demo_creds['endpoint']
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> 
>>> heat = heatclient.Client(heat_endpoint, **demo_creds)
>>> heat.stacks.list()
<generator object paginate at 0x7f141d6b9e60>
>>> heat.s

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    heat.s
AttributeError: 'Client' object has no attribute 's'
>>> for x in heat.stacks.list():
	print x

	

Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    for x in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> heat.stacks.get('s')

Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    heat.stacks.get('s')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 202, in get
    resp, body = self.client.json_request('GET', '/stacks/%s' % stack_id)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> heat = heatclient.Client(heat_endpoint, **demo_creds)
>>> token = keystone.auth_token
>>> token
u'cb7d4d2ab474410fbb03f98a8059da58'
>>> heat = heatclient.Client(heat_endpoint, token=token, **demo_creds)
>>> heat.stacks.get('s')

Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    heat.stacks.get('s')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 202, in get
    resp, body = self.client.json_request('GET', '/stacks/%s' % stack_id)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> 
>>> 
>>> 
>>> keystone = ksclient.Client(**demo_creds)
>>> keystone.services.list()

Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    keystone.services.list()
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/services.py", line 32, in list
    return self._list("/OS-KSADM/services", "OS-KSADM:services")
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/base.py", line 113, in _list
    resp, body = self.client.get(url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 170, in get
    return self.request(url, 'GET', **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 206, in request
    resp = super(LegacyJsonAdapter, self).request(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 95, in request
    return self.session.request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/utils.py", line 336, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/session.py", line 397, in request
    raise exceptions.from_response(resp, method, url)
Forbidden: You are not authorized to perform the requested action: admin_required (Disable debug mode to suppress these details.) (HTTP 403) (Request-ID: req-becd4247-358c-410d-b0ca-1df3004c40b5)
>>> 
>>> keystone.auth_token
u'81a536e331644a6bb80d5de04579478b'
>>> 
>>> heat = heatclient.Client(heat_endpoint, token=token, **demo_creds)
>>> token = keystone.auth_token
>>> token
u'81a536e331644a6bb80d5de04579478b'
>>> heat = heatclient.Client(heat_endpoint, token=token, **demo_creds)
>>> heat.stacks.get('s')
<Stack {u'disable_rollback': True, u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'capabilities': [], u'notification_topics': [], u'parameters': {u'OS::project_id': u'd8f42a85e023411080a86768fa0e4692', u'OS::stack_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'OS::stack_name': u's', u'instance_type': u'm1.tiny', u'key_name': u'heat_key', u'image_id': u'cirros-0.3.4-x86_64-uec'}, u'timeout_mins': None, u'stack_status': u'CREATE_COMPLETE', u'stack_owner': u'demo', u'updated_time': None, u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'outputs': [], u'template_description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n'}>
>>> for s in heat.stacks.list():
	print s

	
<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}>
>>> 
>>> s = heat.stacks.get('s')
>>> s.outputs
[]
>>> 
>>> heat.resources.list('s)
		    
SyntaxError: EOL while scanning string literal
>>> heat.resources.list('s')
[<Resource {u'resource_name': u'myserver1', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver1', u'creation_time': u'2015-06-08T10:24:48', u'resource_status': u'CREATE_COMPLETE', u'updated_time': u'2015-06-08T10:24:48', u'required_by': [], u'resource_status_reason': u'state changed', u'physical_resource_id': u'd92e0280-f1e9-46c9-9397-565c0ca003a0', u'resource_type': u'OS::Nova::Server'}>, <Resource {u'resource_name': u'myserver', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver', u'creation_time': u'2015-06-08T10:24:48', u'resource_status': u'CREATE_COMPLETE', u'updated_time': u'2015-06-08T10:24:48', u'required_by': [u'myserver1'], u'resource_status_reason': u'state changed', u'physical_resource_id': u'a59ec336-1e3b-43e6-9cb4-2ef839a76fa4', u'resource_type': u'OS::Nova::Server'}>]
>>> r = heat.resources.list('s')
>>> len(r)
2
>>> for x in r:
	print x.name

	

Traceback (most recent call last):
  File "<pyshell#180>", line 2, in <module>
    print x.name
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 494, in __getattr__
    raise AttributeError(k)
AttributeError: name
>>> for x in r:
	print x.resource_name

	
myserver1
myserver
>>> 
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'creds', 'demo_creds', 'e', 'get_keystone_admin_creds', 'get_keystone_creds', 'heat', 'heat_endpoint', 'heatclient', 'keystone', 'ksclient', 'nvclient', 'os', 'r', 'retrying', 's', 's1', 'services', 't', 'token', 'u', 'users', 'x', 'x1']
>>> type(heat)
<class 'heatclient.v1.client.Client'>
>>> heat.events.list('s')
[<Event {u'resource_name': u's', u'event_time': u'2015-06-08T10:25:44', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s/events/82e42593-ce39-4129-b2fc-85d9e7730de2', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u's', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'Stack CREATE completed successfully', u'physical_resource_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'id': u'82e42593-ce39-4129-b2fc-85d9e7730de2'}>, <Event {u'resource_name': u'myserver1', u'event_time': u'2015-06-08T10:25:44', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1/events/cea7a505-63f6-4534-873f-1b23b773de58', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver1', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'state changed', u'physical_resource_id': u'd92e0280-f1e9-46c9-9397-565c0ca003a0', u'id': u'cea7a505-63f6-4534-873f-1b23b773de58'}>, <Event {u'resource_name': u'myserver1', u'event_time': u'2015-06-08T10:25:34', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1/events/a812b9fd-8c66-4ee3-ad88-b93d19e6983f', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver1', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'state changed', u'physical_resource_id': None, u'id': u'a812b9fd-8c66-4ee3-ad88-b93d19e6983f'}>, <Event {u'resource_name': u'myserver', u'event_time': u'2015-06-08T10:24:57', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver/events/db86280d-818f-4f2b-8b9d-a56341ab3cc6', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'state changed', u'physical_resource_id': u'a59ec336-1e3b-43e6-9cb4-2ef839a76fa4', u'id': u'db86280d-818f-4f2b-8b9d-a56341ab3cc6'}>, <Event {u'resource_name': u'myserver', u'event_time': u'2015-06-08T10:24:48', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver/events/b09bc00d-09b1-4763-b29f-5f459b0b53a4', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'state changed', u'physical_resource_id': None, u'id': u'b09bc00d-09b1-4763-b29f-5f459b0b53a4'}>, <Event {u'resource_name': u's', u'event_time': u'2015-06-08T10:24:48', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s/events/ad3ebf05-eb1e-46c9-82d7-030ec9532748', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u's', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'Stack CREATE started', u'physical_resource_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'id': u'ad3ebf05-eb1e-46c9-82d7-030ec9532748'}>]
>>> len(heat.events.list('s'))
6
>>> for e in heat.events.list('s'):
	print e
	print "\n"

	
<Event {u'resource_name': u's', u'event_time': u'2015-06-08T10:25:44', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s/events/82e42593-ce39-4129-b2fc-85d9e7730de2', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u's', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'Stack CREATE completed successfully', u'physical_resource_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'id': u'82e42593-ce39-4129-b2fc-85d9e7730de2'}>


<Event {u'resource_name': u'myserver1', u'event_time': u'2015-06-08T10:25:44', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1/events/cea7a505-63f6-4534-873f-1b23b773de58', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver1', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'state changed', u'physical_resource_id': u'd92e0280-f1e9-46c9-9397-565c0ca003a0', u'id': u'cea7a505-63f6-4534-873f-1b23b773de58'}>


<Event {u'resource_name': u'myserver1', u'event_time': u'2015-06-08T10:25:34', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1/events/a812b9fd-8c66-4ee3-ad88-b93d19e6983f', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver1', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver1', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'state changed', u'physical_resource_id': None, u'id': u'a812b9fd-8c66-4ee3-ad88-b93d19e6983f'}>


<Event {u'resource_name': u'myserver', u'event_time': u'2015-06-08T10:24:57', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver/events/db86280d-818f-4f2b-8b9d-a56341ab3cc6', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver', u'resource_status': u'CREATE_COMPLETE', u'resource_status_reason': u'state changed', u'physical_resource_id': u'a59ec336-1e3b-43e6-9cb4-2ef839a76fa4', u'id': u'db86280d-818f-4f2b-8b9d-a56341ab3cc6'}>


<Event {u'resource_name': u'myserver', u'event_time': u'2015-06-08T10:24:48', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver/events/b09bc00d-09b1-4763-b29f-5f459b0b53a4', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/myserver', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u'myserver', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'state changed', u'physical_resource_id': None, u'id': u'b09bc00d-09b1-4763-b29f-5f459b0b53a4'}>


<Event {u'resource_name': u's', u'event_time': u'2015-06-08T10:24:48', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s/events/ad3ebf05-eb1e-46c9-82d7-030ec9532748', u'rel': u'self'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431/resources/s', u'rel': u'resource'}, {u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'stack'}], u'logical_resource_id': u's', u'resource_status': u'CREATE_IN_PROGRESS', u'resource_status_reason': u'Stack CREATE started', u'physical_resource_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'id': u'ad3ebf05-eb1e-46c9-82d7-030ec9532748'}>


>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> keystone.users.list()

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    keystone.users.list()
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/users.py", line 125, in list
    return self._list("/users%s" % query, "users")
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/base.py", line 113, in _list
    resp, body = self.client.get(url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 170, in get
    return self.request(url, 'GET', **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 206, in request
    resp = super(LegacyJsonAdapter, self).request(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 95, in request
    return self.session.request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/utils.py", line 336, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/session.py", line 397, in request
    raise exceptions.from_response(resp, method, url)
Forbidden: You are not authorized to perform the requested action: admin_required (Disable debug mode to suppress these details.) (HTTP 403) (Request-ID: req-56626733-9701-4503-b4da-58e4ac814f49)
>>> creds
{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> keystone = ksclient.Client(**creds)
>>> for u in keystone.users.list():
	print u
	print "\N
	
SyntaxError: EOL while scanning string literal
>>> for u in keystone.users.list():
	print u
	print "\n"

	
<User {u'username': u'heat', u'id': u'126452eda45e47549d8c7e75f355c76e', u'enabled': True, u'name': u'heat', u'email': None}>


<User {u'username': u'admin', u'id': u'5651e750923546e695e06ca9a810c759', u'enabled': True, u'name': u'admin', u'email': None}>


<User {u'username': u'neutron', u'id': u'81758bbaec0c420fbe97e5fbdbb52152', u'enabled': True, u'name': u'neutron', u'email': None}>


<User {u'username': u'cinder', u'id': u'934ff7c1dc1845a48244a3232d67c86a', u'enabled': True, u'name': u'cinder', u'email': None}>


<User {u'username': u'nova', u'id': u'c457ef7813c149eca1c6b1b02da394ca', u'enabled': True, u'name': u'nova', u'email': None}>


<User {u'username': u'glance', u'id': u'ccfa207f5b33407699ed3d39b96319d8', u'enabled': True, u'name': u'glance', u'email': None}>


<User {u'username': u'demo', u'id': u'f2e0e944388943e389e5f50f0de1ade3', u'enabled': True, u'name': u'demo', u'email': u'demo@example.com'}>


>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> del demo_creds['username']
>>> demo_creds
{'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> demo_creds['user_id']='f2e0e944388943e389e5f50f0de1ade3'
>>> help(ksclient.Client)
Help on class Client in module keystoneclient.v2_0.client:

class Client(keystoneclient.httpclient.HTTPClient)
 |  Client for the OpenStack Keystone v2.0 API.
 |  
 |  :param string username: Username for authentication. (optional)
 |  :param string password: Password for authentication. (optional)
 |  :param string token: Token for authentication. (optional)
 |  :param string tenant_id: Tenant id. (optional)
 |  :param string tenant_name: Tenant name. (optional)
 |  :param string auth_url: Keystone service endpoint for authorization.
 |  :param string region_name: Name of a region to select when choosing an
 |                             endpoint from the service catalog.
 |  :param string endpoint: A user-supplied endpoint URL for the keystone
 |                          service.  Lazy-authentication is possible for API
 |                          service calls if endpoint is set at
 |                          instantiation.(optional)
 |  :param integer timeout: Allows customization of the timeout for client
 |                          http requests. (optional)
 |  :param string original_ip: The original IP of the requesting user
 |                             which will be sent to Keystone in a
 |                             'Forwarded' header. (optional)
 |  :param string cert: Path to the Privacy Enhanced Mail (PEM) file which
 |                      contains the corresponding X.509 client certificate
 |                      needed to established two-way SSL connection with
 |                      the identity service. (optional)
 |  :param string key: Path to the Privacy Enhanced Mail (PEM) file which
 |                     contains the unencrypted client private key needed
 |                     to established two-way SSL connection with the
 |                     identity service. (optional)
 |  :param string cacert: Path to the Privacy Enhanced Mail (PEM) file which
 |                        contains the trusted authority X.509 certificates
 |                        needed to established SSL connection with the
 |                        identity service. (optional)
 |  :param boolean insecure: Does not perform X.509 certificate validation
 |                           when establishing SSL connection with identity
 |                           service. default: False (optional)
 |  :param dict auth_ref: To allow for consumers of the client to manage their
 |                        own caching strategy, you may initialize a client
 |                        with a previously captured auth_reference (token)
 |  :param boolean debug: Enables debug logging of all request and responses
 |                        to keystone. default False (option)
 |  
 |  .. warning::
 |  
 |      If debug is enabled, it may show passwords in plain text as a part of
 |      its output.
 |  
 |  
 |  The client can be created and used like a user or in a strictly
 |  bootstrap mode. Normal operation expects a username, password, auth_url,
 |  and tenant_name or id to be provided. Other values will be lazily loaded
 |  as needed from the service catalog.
 |  
 |  Example::
 |  
 |      >>> from keystoneclient.v2_0 import client
 |      >>> keystone = client.Client(username=USER,
 |      ...                          password=PASS,
 |      ...                          tenant_name=TENANT_NAME,
 |      ...                          auth_url=KEYSTONE_URL)
 |      >>> keystone.tenants.list()
 |      ...
 |      >>> user = keystone.users.get(USER_ID)
 |      >>> user.delete()
 |  
 |  Once authenticated, you can store and attempt to re-use the
 |  authenticated token. the auth_ref property on the client
 |  returns as a dictionary-like-object so that you can export and
 |  cache it, re-using it when initiating another client::
 |  
 |      >>> from keystoneclient.v2_0 import client
 |      >>> keystone = client.Client(username=USER,
 |      ...                          password=PASS,
 |      ...                          tenant_name=TENANT_NAME,
 |      ...                          auth_url=KEYSTONE_URL)
 |      >>> auth_ref = keystone.auth_ref
 |      >>> # pickle or whatever you like here
 |      >>> new_client = client.Client(auth_ref=auth_ref)
 |  
 |  Alternatively, you can provide the administrative token configured in
 |  keystone and an endpoint to communicate with directly. See
 |  (``admin_token`` in ``keystone.conf``) In this case, authenticate()
 |  is not needed, and no service catalog will be loaded.
 |  
 |  Example::
 |  
 |      >>> from keystoneclient.v2_0 import client
 |      >>> admin_client = client.Client(
 |      ...     token='12345secret7890',
 |      ...     endpoint='http://localhost:35357/v2.0')
 |      >>> admin_client.tenants.list()
 |  
 |  Method resolution order:
 |      Client
 |      keystoneclient.httpclient.HTTPClient
 |      keystoneclient.baseclient.Client
 |      keystoneclient.auth.base.BaseAuthPlugin
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  __init__(self, **kwargs)
 |      Initialize a new client for the Keystone v2.0 API.
 |  
 |  get_raw_token_from_identity_service(self, auth_url, username=None, password=None, tenant_name=None, tenant_id=None, token=None, project_name=None, project_id=None, trust_id=None, **kwargs)
 |      Authenticate against the v2 Identity API.
 |      
 |      If a token is provided it will be used in preference over username and
 |      password.
 |      
 |      :returns: access.AccessInfo if authentication was successful.
 |      :raises keystoneclient.exceptions.AuthorizationFailure: if unable to
 |          authenticate or validate the existing authorization token
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  version = 'v2.0'
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from keystoneclient.httpclient.HTTPClient:
 |  
 |  __getattr__(self, name)
 |  
 |  __setattr__(self, name, val)
 |  
 |  authenticate(*args, **kwargs)
 |      Authenticate user.
 |      
 |      Uses the data provided at instantiation to authenticate against
 |      the Identity server. This may use either a username and password
 |      or token for authentication. If a tenant name or id was provided
 |      then the resulting authenticated client will be scoped to that
 |      tenant and contain a service catalog of available endpoints.
 |      
 |      With the v2.0 API, if a tenant name or ID is not provided, the
 |      authentication token returned will be 'unscoped' and limited in
 |      capabilities until a fully-scoped token is acquired.
 |      
 |      With the v3 API, if a domain name or id was provided then the resulting
 |      authenticated client will be scoped to that domain. If a project name
 |      or ID is not provided, and the authenticating user has a default
 |      project configured, the authentication token returned will be 'scoped'
 |      to the default project. Otherwise, the authentication token returned
 |      will be 'unscoped' and limited in capabilities until a fully-scoped
 |      token is acquired.
 |      
 |      With the v3 API, with the OS-TRUST extension enabled, the trust_id can
 |      be provided to allow project-specific role delegation between users
 |      
 |      If successful, sets the self.auth_ref and self.auth_token with
 |      the returned token. If not already set, will also set
 |      self.management_url from the details provided in the token.
 |      
 |      :returns: ``True`` if authentication was successful.
 |      :raises keystoneclient.exceptions.AuthorizationFailure: if unable to
 |          authenticate or validate the existing authorization token
 |      :raises keystoneclient.exceptions.ValueError: if insufficient
 |                                                    parameters are used.
 |      
 |      If keyring is used, token is retrieved from keyring instead.
 |      Authentication will only be necessary if any of the following
 |      conditions are met:
 |      
 |      * keyring is not used
 |      * if token is not found in keyring
 |      * if token retrieved from keyring is expired or about to
 |        expired (as determined by stale_duration)
 |      * if force_new_token is true
 |  
 |  delete(self, url, **kwargs)
 |      Perform an authenticate DELETE request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``DELETE`` and
 |      an authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  get(self, url, **kwargs)
 |      Perform an authenticated GET request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``GET`` and an
 |      authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  get_auth_ref_from_keyring(self, **kwargs)
 |      Retrieve auth_ref from keyring.
 |      
 |      If auth_ref is found in keyring, (keyring_key, auth_ref) is returned.
 |      Otherwise, (keyring_key, None) is returned.
 |      
 |      :returns: (keyring_key, auth_ref) or (keyring_key, None)
 |      :returns: or (None, None) if use_keyring is not set in the object
 |  
 |  get_endpoint(self, session, interface=None, **kwargs)
 |  
 |  get_project_id(self, session, **kwargs)
 |  
 |  get_token(self, session, **kwargs)
 |  
 |  get_user_id(self, session, **kwargs)
 |  
 |  has_service_catalog(self)
 |      Returns True if this client provides a service catalog.
 |  
 |  head(self, url, **kwargs)
 |      Perform an authenticated HEAD request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``HEAD`` and an
 |      authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  patch(self, url, **kwargs)
 |      Perform an authenticate PATCH request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``PATCH`` and
 |      an authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  post(self, url, **kwargs)
 |      Perform an authenticate POST request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``POST`` and an
 |      authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  process_token(self, region_name=None)
 |      Extract and process information from the new auth_ref.
 |      
 |      And set the relevant authentication information.
 |  
 |  put(self, url, **kwargs)
 |      Perform an authenticate PUT request.
 |      
 |      This calls :py:meth:`.request()` with ``method`` set to ``PUT`` and an
 |      authentication token if one is available.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used by the managers and the managers now receive an adapter so
 |          this function is no longer on the standard request path.
 |  
 |  request(self, *args, **kwargs)
 |      Send an http request with the specified characteristics.
 |      
 |      Wrapper around requests.request to handle tasks such as
 |      setting headers, JSON encoding/decoding, and error handling.
 |      
 |      .. warning::
 |          *DEPRECATED*: This function is no longer used. It was designed to
 |          be used only by the managers and the managers now receive an
 |          adapter so this function is no longer on the standard request path.
 |  
 |  serialize(self, entity)
 |  
 |  store_auth_ref_into_keyring(self, keyring_key)
 |      Store auth_ref into keyring.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from keystoneclient.httpclient.HTTPClient:
 |  
 |  auth_token
 |  
 |  management_url
 |  
 |  service_catalog
 |      Returns this client's service catalog.
 |  
 |  tenant_id
 |      Provide read-only backwards compatibility for tenant_id.
 |      This is deprecated, use project_id instead.
 |  
 |  tenant_name
 |      Provide read-only backwards compatibility for tenant_name.
 |      This is deprecated, use project_name instead.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from keystoneclient.httpclient.HTTPClient:
 |  
 |  deprecated_adapter_variables = {'region_name': None}
 |  
 |  deprecated_session_variables = {'cert': None, 'original_ip': None, 'ti...
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from keystoneclient.baseclient.Client:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from keystoneclient.auth.base.BaseAuthPlugin:
 |  
 |  get_headers(self, session, **kwargs)
 |      Fetch authentication headers for message.
 |      
 |      This is a more generalized replacement of the older get_token to allow
 |      plugins to specify different or additional authentication headers to
 |      the OpenStack standard 'X-Auth-Token' header.
 |      
 |      How the authentication headers are obtained is up to the plugin. If the
 |      headers are still valid they may be re-used, retrieved from cache or
 |      the plugin may invoke an authentication request against a server.
 |      
 |      The default implementation of get_headers calls the `get_token` method
 |      to enable older style plugins to continue functioning unchanged.
 |      Subclasses should feel free to completely override this function to
 |      provide the headers that they want.
 |      
 |      There are no required kwargs. They are passed directly to the auth
 |      plugin and they are implementation specific.
 |      
 |      Returning None will indicate that no token was able to be retrieved and
 |      that authorization was a failure. Adding no authentication data can be
 |      achieved by returning an empty dictionary.
 |      
 |      :param session: The session object that the auth_plugin belongs to.
 |      :type session: keystoneclient.session.Session
 |      
 |      :returns: Headers that are set to authenticate a message or None for
 |                failure. Note that when checking this value that the empty
 |                dict is a valid, non-failure response.
 |      :rtype: dict
 |  
 |  invalidate(self)
 |      Invalidate the current authentication data.
 |      
 |      This should result in fetching a new token on next call.
 |      
 |      A plugin may be invalidated if an Unauthorized HTTP response is
 |      returned to indicate that the token may have been revoked or is
 |      otherwise now invalid.
 |      
 |      :returns: True if there was something that the plugin did to
 |                invalidate. This means that it makes sense to try again. If
 |                nothing happens returns False to indicate give up.
 |      :rtype: bool
 |  
 |  ----------------------------------------------------------------------
 |  Class methods inherited from keystoneclient.auth.base.BaseAuthPlugin:
 |  
 |  get_options(cls) from __builtin__.type
 |      Return the list of parameters associated with the auth plugin.
 |      
 |      This list may be used to generate CLI or config arguments.
 |      
 |      :returns: A list of Param objects describing available plugin
 |                parameters.
 |      :rtype: list
 |  
 |  load_from_argparse_arguments(cls, namespace, **kwargs) from __builtin__.type
 |      Load a specific plugin object from an argparse result.
 |      
 |      Convert the results of a parse into the specified plugin.
 |      
 |      :param namespace: The result from CLI parsing.
 |      :type namespace: argparse.Namespace
 |      
 |      :returns: An auth plugin, or None if a name is not provided.
 |      :rtype: :py:class:`keystoneclient.auth.BaseAuthPlugin`
 |  
 |  load_from_conf_options(cls, conf, group, **kwargs) from __builtin__.type
 |      Load the plugin from a CONF object.
 |      
 |      Convert the options already registered into a real plugin.
 |      
 |      :param conf: A config object.
 |      :type conf: oslo_config.cfg.ConfigOpts
 |      :param string group: The group name that options should be read from.
 |      
 |      :returns: An authentication Plugin.
 |      :rtype: :py:class:`keystoneclient.auth.BaseAuthPlugin`
 |  
 |  load_from_options(cls, **kwargs) from __builtin__.type
 |      Create a plugin from the arguments retrieved from get_options.
 |      
 |      A client can override this function to do argument validation or to
 |      handle differences between the registered options and what is required
 |      to create the plugin.
 |  
 |  load_from_options_getter(cls, getter, **kwargs) from __builtin__.type
 |      Load a plugin from a getter function that returns appropriate values
 |      
 |      To handle cases other than the provided CONF and CLI loading you can
 |      specify a custom loader function that will be queried for the option
 |      value.
 |      
 |      The getter is a function that takes one value, an
 |      :py:class:`oslo_config.cfg.Opt` and returns a value to load with.
 |      
 |      :param getter: A function that returns a value for the given opt.
 |      :type getter: callable
 |      
 |      :returns: An authentication Plugin.
 |      :rtype: :py:class:`keystoneclient.auth.BaseAuthPlugin`
 |  
 |  register_argparse_arguments(cls, parser) from __builtin__.type
 |      Register the CLI options provided by a specific plugin.
 |      
 |      Given a plugin class convert it's options into argparse arguments and
 |      add them to a parser.
 |      
 |      :param parser: the parser to attach argparse options.
 |      :type parser: argparse.ArgumentParser
 |  
 |  register_conf_options(cls, conf, group) from __builtin__.type
 |      Register the oslo_config options that are needed for a plugin.
 |      
 |      :param conf: A config object.
 |      :type conf: oslo_config.cfg.ConfigOpts
 |      :param string group: The group name that options should be read from.

>>> demo_creds
{'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'user_id': 'f2e0e944388943e389e5f50f0de1ade3'}
>>> 
>>> keystone = ksclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    keystone = ksclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/client.py", line 152, in __init__
    self.authenticate()
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/utils.py", line 336, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/httpclient.py", line 507, in authenticate
    resp = self.get_raw_token_from_identity_service(**kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/client.py", line 184, in get_raw_token_from_identity_service
    raise exceptions.AuthorizationFailure(msg)
AuthorizationFailure: A username and password or token is required.
>>> demo_creds['id'] = 'f2e0e944388943e389e5f50f0de1ade3'
>>> 
>>> keystone = ksclient.Client(**demo_creds)

Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    keystone = ksclient.Client(**demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/client.py", line 152, in __init__
    self.authenticate()
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/utils.py", line 336, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/httpclient.py", line 507, in authenticate
    resp = self.get_raw_token_from_identity_service(**kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/client.py", line 184, in get_raw_token_from_identity_service
    raise exceptions.AuthorizationFailure(msg)
AuthorizationFailure: A username and password or token is required.
>>> demo_creds
{'user_id': 'f2e0e944388943e389e5f50f0de1ade3', 'tenant_name': 'demo', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'password': 'nomoresecrete', 'id': 'f2e0e944388943e389e5f50f0de1ade3'}
>>> del demo_creds['user_id']
>>> del demo_creds['id']
>>> del demo_creds['username'] = 'demo'
SyntaxError: invalid syntax
>>> demo_creds['username'] = 'demo'
>>> 
>>> keystone = ksclient.Client(**demo_creds)
>>> keystone.auth_token
u'75d87a4e01f14868a41d9397147c7c79'
>>> heat.services.list()

Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    heat.services.list()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/services.py", line 32, in list
    return self._list(url, "services")
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 217, in _http_request
    'content': resp.content
HTTPUnauthorized: ERROR: Authentication failed. Please try again with option --include-password or export HEAT_INCLUDE_PASSWORD=1
Authentication required
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'password': 'nomoresecrete'}
>>> heat = heatclient.Client(keystone.auth_token, heat_endpoint, **demo_creds)

Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    heat = heatclient.Client(keystone.auth_token, heat_endpoint, **demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/client.py", line 40, in __init__
    self.http_client = http._construct_http_client(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 389, in _construct_http_client
    return HTTPClient(*args, **kwargs)
TypeError: __init__() takes exactly 2 arguments (7 given)
>>> 
>>> 
>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'password': 'nomoresecrete'}
>>> 
>>> demo_creds['endpoint'] = heat_endpoint
>>> heat_endpoint
'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'
>>> 
>>> 
>>> heat = heatclient.Client(**demo_creds)
>>> heat.services.list()

Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    heat.services.list()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/services.py", line 32, in list
    return self._list(url, "services")
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> demo_creds
{'username': 'demo', 'endpoint': 'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692', 'tenant_name': 'demo', 'auth_url': 'http://192.168.80.130:5000/v2.0', 'password': 'nomoresecrete'}
>>> 
>>> heat.stacks.list()
<generator object paginate at 0x7f141d64f690>
>>> x = heat.stacks.list()
>>> x.next()

Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    x.next()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> 
>>> s = heat.stacks.get('s')

Traceback (most recent call last):
  File "<pyshell#242>", line 1, in <module>
    s = heat.stacks.get('s')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 202, in get
    resp, body = self.client.json_request('GET', '/stacks/%s' % stack_id)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> ================================ RESTART ================================
>>> ================================ RESTART ================================
>>> 
{'username': 'demo'}
>>> 
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> 
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 28, in <module>
    keystone.services.list()
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/v2_0/services.py", line 32, in list
    return self._list("/OS-KSADM/services", "OS-KSADM:services")
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/base.py", line 113, in _list
    resp, body = self.client.get(url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 170, in get
    return self.request(url, 'GET', **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 206, in request
    resp = super(LegacyJsonAdapter, self).request(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/adapter.py", line 95, in request
    return self.session.request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/utils.py", line 336, in inner
    return func(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/keystoneclient/session.py", line 397, in request
    raise exceptions.from_response(resp, method, url)
Forbidden: You are not authorized to perform the requested action: admin_required (Disable debug mode to suppress these details.) (HTTP 403) (Request-ID: req-6a604880-15f7-41fd-aa4c-0fc8fbcf17d6)
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

[<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}>, <Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}>, <Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}>, <Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}>, <Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}>, <Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}>, <Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}>, <Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}>, <Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}>, <Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}>] 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}> 

<Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}> 

<Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}> 

<Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}> 

<Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}> 

<Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}> 

<Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}> 

<Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}> 

<Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}> 

<Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}> 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

<Service {u'type': u'cloudformation', u'description': u'Heat CloudFormation Service', u'enabled': True, u'id': u'1601c35405454cdd8a935c492c2dfe66', u'name': u'heat-cfn'}> 

<Service {u'type': u'volumev2', u'description': u'Cinder Volume Service V2', u'enabled': True, u'id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'name': u'cinderv2'}> 

<Service {u'type': u'network', u'description': u'Neutron Service', u'enabled': True, u'id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'name': u'neutron'}> 

<Service {u'type': u'volume', u'description': u'Cinder Volume Service', u'enabled': True, u'id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'name': u'cinder'}> 

<Service {u'type': u'identity', u'description': u'Keystone Identity Service', u'enabled': True, u'id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'name': u'keystone'}> 

<Service {u'type': u'computev21', u'description': u'Nova Compute Service V2.1', u'enabled': True, u'id': u'74152f778c794c3582c2d418f4fe62f4', u'name': u'novav21'}> 

<Service {u'type': u'orchestration', u'description': u'Heat Orchestration Service', u'enabled': True, u'id': u'76e54b792a6d4287817de2f982add4fd', u'name': u'heat'}> 

<Service {u'type': u'compute', u'description': u'Nova Compute Service', u'enabled': True, u'id': u'a5717708347648c19306ddb197cc7b9f', u'name': u'nova'}> 

<Service {u'type': u'image', u'description': u'Glance Image Service', u'enabled': True, u'id': u'f0ae91766045456a9e19fa36f52fdd9d', u'name': u'glance'}> 

<Service {u'type': u'ec2', u'description': u'EC2 Compatibility Layer', u'enabled': True, u'id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'name': u'ec2'}> 

9f8aa9c4b352418e9a65367bad7fc450 

>>> 
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  74443aa764b1425894125ef10005440a 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  a981548b5cbd4b02a39da201598414ee 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  0b73408bd2aa4bd1969d61cb1c45bab4 

>>> 
>>> help(admin_keystone.endpoints)
Help on EndpointManager in module keystoneclient.v2_0.endpoints object:

class EndpointManager(keystoneclient.base.ManagerWithFind)
 |  Manager class for manipulating Keystone endpoints.
 |  
 |  Method resolution order:
 |      EndpointManager
 |      keystoneclient.base.ManagerWithFind
 |      keystoneclient.base.Manager
 |      __builtin__.object
 |  
 |  Methods defined here:
 |  
 |  create(self, region, service_id, publicurl, adminurl=None, internalurl=None)
 |      Create a new endpoint.
 |  
 |  delete(self, id)
 |      Delete an endpoint.
 |  
 |  list(self)
 |      List all available endpoints.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __abstractmethods__ = frozenset([])
 |  
 |  resource_class = <class 'keystoneclient.v2_0.endpoints.Endpoint'>
 |      Represents a Keystone endpoint.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from keystoneclient.base.ManagerWithFind:
 |  
 |  find(self, **kwargs)
 |      Find a single item with attributes matching ``**kwargs``.
 |      
 |      This isn't very efficient: it loads the entire list then filters on
 |      the Python side.
 |  
 |  findall(self, **kwargs)
 |      Find all items with attributes matching ``**kwargs``.
 |      
 |      This isn't very efficient: it loads the entire list then filters on
 |      the Python side.
 |  
 |  ----------------------------------------------------------------------
 |  Methods inherited from keystoneclient.base.Manager:
 |  
 |  __init__(self, client)
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from keystoneclient.base.Manager:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)
 |  
 |  api
 |      Deprecated. Use `client` instead.

>>> 
>>> c = admin_keystone.service_catalog.catalog
>>> print c
{u'token': {u'issued_at': u'2015-06-10T12:07:50.960149', u'expires': u'2015-06-10T13:07:50Z', u'id': u'edc93a27a6b242058eb759a11094b99a', u'tenant': {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}, u'audit_ids': [u'687ySkIfR8q02yzuvwxACw']}, 'version': 'v2.0', u'serviceCatalog': [{u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8774/v2.1/d60b5c7ed1a449efb4dab22162da0cb8', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8774/v2.1/d60b5c7ed1a449efb4dab22162da0cb8', u'internalURL': u'http://192.168.80.130:8774/v2.1/d60b5c7ed1a449efb4dab22162da0cb8', u'id': u'3af1db04807e449c8c3f425662a11b4f'}], u'type': u'computev21', u'name': u'novav21'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8774/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8774/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'internalURL': u'http://192.168.80.130:8774/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'id': u'60c199e3da3141eaa6a2d36df9e88349'}], u'type': u'compute', u'name': u'nova'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:9696/', u'internalURL': u'http://192.168.80.130:9696/', u'id': u'5c40e8080b3542df9a347891ac9192a4'}], u'type': u'network', u'name': u'neutron'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8776/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8776/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'internalURL': u'http://192.168.80.130:8776/v2/d60b5c7ed1a449efb4dab22162da0cb8', u'id': u'44ef469155ce4965a9040bbe0fabb443'}], u'type': u'volumev2', u'name': u'cinderv2'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:9292', u'internalURL': u'http://192.168.80.130:9292', u'id': u'631a14128a1f45698018a14d2e792a06'}], u'type': u'image', u'name': u'glance'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8000/v1', u'internalURL': u'http://192.168.80.130:8000/v1', u'id': u'0a289fc17f6340d7894f471fad718d04'}], u'type': u'cloudformation', u'name': u'heat-cfn'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8776/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8776/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'internalURL': u'http://192.168.80.130:8776/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'id': u'1befc5b6596047f0be6497e208cbb048'}], u'type': u'volume', u'name': u'cinder'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8773/', u'internalURL': u'http://192.168.80.130:8773/', u'id': u'44fde810be834cecabb9a09ef85bed2f'}], u'type': u'ec2', u'name': u'ec2'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'internalURL': u'http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8', u'id': u'904dcfc60468482895b30139d1c8ed0a'}], u'type': u'orchestration', u'name': u'heat'}, {u'endpoints_links': [], u'endpoints': [{u'adminURL': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'publicURL': u'http://192.168.80.130:5000/v2.0', u'internalURL': u'http://192.168.80.130:5000/v2.0', u'id': u'30630b6b63c34b59b4c6acf45cbf86f1'}], u'type': u'identity', u'name': u'keystone'}], u'user': {u'username': u'admin', u'roles_links': [], u'id': u'5651e750923546e695e06ca9a810c759', u'roles': [{u'name': u'admin'}], u'name': u'admin'}, u'metadata': {u'is_admin': 0, u'roles': [u'6e6d9a50da254925be8f38be460642ac']}}
>>> len(c)
5
>>> for x in c:
	print x, '\n'

	
token 

version 

serviceCatalog 

user 

metadata 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  9233e1263f65442d952bd49a996ea0d8 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 

auth_token:  3c228f403cf046438feecf1e130fd305 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

{'username': 'admin', 'tenant_name': 'admin', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  e668834fad6a41ec846e5081e11e0297 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 

>>> demo_creds
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'}
>>> hc.Client(endpoint=heat_endpoint, **demo_creds)

Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    hc.Client(endpoint=heat_endpoint, **demo_creds)
TypeError: Client() takes at least 1 argument (0 given)
>>> hc.Client(1, endpoint=heat_endpoint, **demo_creds)
<heatclient.v1.client.Client object at 0x7f5a996fdfd0>
>>> 
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/opt/stack/exp.py", line 47, in <module>
    heat = hc.Client(HEAT_VERSION, endpoint=heat_endpoint, **demo_args)
NameError: name 'demo_args' is not defined
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/opt/stack/exp.py", line 48, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/opt/stack/exp.py", line 51, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPUnauthorized: ERROR: Authentication required
>>> ================================ RESTART ================================
>>> 

Traceback (most recent call last):
  File "/opt/stack/exp.py", line 51, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> ================================ RESTART ================================
>>> 
http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 51, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  f07cbd070c2149de958869ba1821ba41 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 51, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  f2a2edd1bb2e457ea1f68a5c37b237f6 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 49, in <module>
    **demo_creds)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/client.py", line 17, in Client
    module = utils.import_versioned_module(version, 'client')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/utils.py", line 113, in import_versioned_module
    return importutils.import_module(module)
  File "/usr/local/lib/python2.7/dist-packages/oslo_utils/importutils.py", line 57, in import_module
    __import__(import_str)
ImportError: Import by filename is not supported.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  e98d1758893a461e976d6d148b93fd4e 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 47, in <module>
    heat = heatclient.client.Client(heat_endpoint,
NameError: name 'heatclient' is not defined
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  dfa86afdff5d4a7082533a9ac1697003 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 48, in <module>
    heat = heatclient.client.Client(heat_endpoint,
AttributeError: 'module' object has no attribute 'client'
>>> import heatclient
>>> dir(heatclient)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', '__version__', 'pbr']
>>> 
>>> import heatclient.client
>>> dir(heatclient.client)
['Client', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'utils']
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  88662c18b790410d94140fdd3018faa1 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 52, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> heat
<heatclient.v1.client.Client object at 0x7ff283584dd0>
>>> heat.stacks.list()
<generator object paginate at 0x7ff289d6a820>
>>> s = heat.stacks.list()
>>> s.next()

Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    s.next()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> heat.build_info
<heatclient.v1.build_info.BuildInfoManager object at 0x7ff2830f3a50>
>>> heat.stacks
<heatclient.v1.stacks.StackManager object at 0x7ff2830c5190>
>>> 
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  190aefa6cf0541f496e855bc1c6cca0f 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 57, in <module>
    heat = heatclient.client.Client(heat_endpoint,
AttributeError: 'module' object has no attribute 'client'
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  9bff2f9900144c1d9fe403ac3b88cb55 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 60, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  ea02733fc3ea4c56a6f468a1ff339f9f 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 60, in <module>
    for s in heat.stacks.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 100, in paginate
    stacks = self._list(url, 'stacks')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: Access was denied to this resource.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  1dd47eaf85a4429a90ed25deedec490e 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 

>>> dir(heatclient)
['Client', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'actions', 'build_info', 'events', 'http', 'resource_types', 'resources', 'services', 'software_configs', 'software_deployments', 'stacks']
>>> heat_endpoint
u'http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8'
>>> admin_keystone.endpoints.list()
[<Endpoint {u'adminurl': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'enabled': True, u'id': u'9a1764a2ecfd4890a5d80edb03365d99', u'service_id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'internalurl': u'http://192.168.80.130:9696/', u'publicurl': u'http://192.168.80.130:9696/'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'71c0c32a001848e98d62ef44df238633', u'service_id': u'a5717708347648c19306ddb197cc7b9f', u'internalurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'enabled': True, u'id': u'e48968c44dfc4724a3cd96365531b585', u'service_id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'internalurl': u'http://192.168.80.130:8773/', u'publicurl': u'http://192.168.80.130:8773/'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'enabled': True, u'id': u'a53a05b0c1ee49dfae3f03f7aaf97721', u'service_id': u'f0ae91766045456a9e19fa36f52fdd9d', u'internalurl': u'http://192.168.80.130:9292', u'publicurl': u'http://192.168.80.130:9292'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:5000/v2.0', u'service_id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'id': u'a61044ddcefa4df283e79184ebea3cd4', u'publicurl': u'http://192.168.80.130:5000/v2.0'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'enabled': True, u'id': u'94d0e7eafa244ed49485ac0b82361ffe', u'service_id': u'1601c35405454cdd8a935c492c2dfe66', u'internalurl': u'http://192.168.80.130:8000/v1', u'publicurl': u'http://192.168.80.130:8000/v1'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8755e2c0681b44e28a98097ba8935f8b', u'service_id': u'74152f778c794c3582c2d418f4fe62f4', u'internalurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'25e18edad644455d828020d89a937976', u'service_id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'internalurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s'}>, <Endpoint {u'adminurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8b64ac979eef4064988315e1596ecac0', u'service_id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'internalurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s'}>]
>>> for e in admin_keystone.endpoints.list():
	print e, '\n'

	
<Endpoint {u'adminurl': u'http://192.168.80.130:9696/', u'region': u'RegionOne', u'enabled': True, u'id': u'9a1764a2ecfd4890a5d80edb03365d99', u'service_id': u'28f5d5bbbc7f4b11b54cf7ddb81ea637', u'internalurl': u'http://192.168.80.130:9696/', u'publicurl': u'http://192.168.80.130:9696/'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s', u'service_id': u'76e54b792a6d4287817de2f982add4fd', u'id': u'4654524b478c4eac923fb3570f4b7e5e', u'publicurl': u'http://192.168.80.130:8004/v1/$(tenant_id)s'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'71c0c32a001848e98d62ef44df238633', u'service_id': u'a5717708347648c19306ddb197cc7b9f', u'internalurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2/$(tenant_id)s'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8773/', u'region': u'RegionOne', u'enabled': True, u'id': u'e48968c44dfc4724a3cd96365531b585', u'service_id': u'f9f040f16b3f42e780e29ee4f506a1bd', u'internalurl': u'http://192.168.80.130:8773/', u'publicurl': u'http://192.168.80.130:8773/'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:9292', u'region': u'RegionOne', u'enabled': True, u'id': u'a53a05b0c1ee49dfae3f03f7aaf97721', u'service_id': u'f0ae91766045456a9e19fa36f52fdd9d', u'internalurl': u'http://192.168.80.130:9292', u'publicurl': u'http://192.168.80.130:9292'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:35357/v2.0', u'region': u'RegionOne', u'enabled': True, u'internalurl': u'http://192.168.80.130:5000/v2.0', u'service_id': u'5c97d29cffb24f4aa5f1d3bf439a71eb', u'id': u'a61044ddcefa4df283e79184ebea3cd4', u'publicurl': u'http://192.168.80.130:5000/v2.0'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8000/v1', u'region': u'RegionOne', u'enabled': True, u'id': u'94d0e7eafa244ed49485ac0b82361ffe', u'service_id': u'1601c35405454cdd8a935c492c2dfe66', u'internalurl': u'http://192.168.80.130:8000/v1', u'publicurl': u'http://192.168.80.130:8000/v1'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8755e2c0681b44e28a98097ba8935f8b', u'service_id': u'74152f778c794c3582c2d418f4fe62f4', u'internalurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8774/v2.1/$(tenant_id)s'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'25e18edad644455d828020d89a937976', u'service_id': u'4c9ac854ec094f12b6b3a88275c5ca14', u'internalurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v1/$(tenant_id)s'}> 

<Endpoint {u'adminurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'region': u'RegionOne', u'enabled': True, u'id': u'8b64ac979eef4064988315e1596ecac0', u'service_id': u'1daebc2a4ea74ae5bb0878bc04e63fed', u'internalurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s', u'publicurl': u'http://192.168.80.130:8776/v2/$(tenant_id)s'}> 

>>> 
>>> for t in admin_keystone.tenants.list():
	print t, '\n'

	
<Tenant {u'enabled': True, u'description': None, u'name': u'service', u'id': u'42a758197838431ea8d23aa3792ea9f6'}> 

<Tenant {u'enabled': True, u'description': None, u'name': u'invisible_to_admin', u'id': u'9de40b4a9e4d4fae9a2010879e4c4e24'}> 

<Tenant {u'enabled': True, u'description': None, u'name': u'admin', u'id': u'd60b5c7ed1a449efb4dab22162da0cb8'}> 

<Tenant {u'enabled': True, u'description': None, u'name': u'demo', u'id': u'd8f42a85e023411080a86768fa0e4692'}> 

>>> heat_endpoint
u'http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8'
>>> 
>>> heat_endpoint = u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'
>>> heat_endpoint
u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692'
>>> 
>>> hc = heatclient.Client(heat_endpoint, token=keystone.auth_token,
		           **demo_creds)
>>> hc.stacks.get('s')

Traceback (most recent call last):
  File "<pyshell#289>", line 1, in <module>
    hc.stacks.get('s')
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/stacks.py", line 202, in get
    resp, body = self.client.json_request('GET', '/stacks/%s' % stack_id)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPInternalServerError: ERROR: Timed out waiting for a reply to message ID 914a0c77c77a4b2b86517247ba92d64c

>>> hc.stacks.get('s')
<Stack {u'disable_rollback': True, u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'capabilities': [], u'notification_topics': [], u'parameters': {u'OS::project_id': u'd8f42a85e023411080a86768fa0e4692', u'OS::stack_id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'OS::stack_name': u's', u'instance_type': u'm1.tiny', u'key_name': u'heat_key', u'image_id': u'cirros-0.3.4-x86_64-uec'}, u'timeout_mins': None, u'stack_status': u'CREATE_COMPLETE', u'stack_owner': u'demo', u'updated_time': None, u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'outputs': [], u'template_description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n'}>
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  f9b7cb6c75ef40649bc6ebe7899a3998 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  f430f41820c74a61899c8cf6f1b61afb 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1097466543', u'stack_user_project_id': u'bdacda6174b842b196708a09e8d509ea', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1097466543/5d0bb2e4-d7e9-484e-a5c6-a0549c4de136', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'5d0bb2e4-d7e9-484e-a5c6-a0549c4de136'}> 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1777063136', u'stack_user_project_id': u'430afe5d86b44800841c5452b8aae057', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1777063136/478089b2-f548-4aa7-acc9-d96493e2c600', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'478089b2-f548-4aa7-acc9-d96493e2c600'}> 

<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}> 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  d5d1998b953c4953a1f4be86db90e477 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 


Traceback (most recent call last):
  File "/opt/stack/exp.py", line 48, in <module>
    heat = heatclient.client.Client(HEAT_VERSION,
AttributeError: 'module' object has no attribute 'client'
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  0fac228dc5b0464580de1ef17679c09d 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1097466543', u'stack_user_project_id': u'bdacda6174b842b196708a09e8d509ea', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1097466543/5d0bb2e4-d7e9-484e-a5c6-a0549c4de136', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'5d0bb2e4-d7e9-484e-a5c6-a0549c4de136'}> 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1777063136', u'stack_user_project_id': u'430afe5d86b44800841c5452b8aae057', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1777063136/478089b2-f548-4aa7-acc9-d96493e2c600', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'478089b2-f548-4aa7-acc9-d96493e2c600'}> 

<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}> 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  48da2a8705ba4f5ca5c42178bffa6bf5 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1097466543', u'stack_user_project_id': u'bdacda6174b842b196708a09e8d509ea', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1097466543/5d0bb2e4-d7e9-484e-a5c6-a0549c4de136', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'5d0bb2e4-d7e9-484e-a5c6-a0549c4de136'}> 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1777063136', u'stack_user_project_id': u'430afe5d86b44800841c5452b8aae057', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1777063136/478089b2-f548-4aa7-acc9-d96493e2c600', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'478089b2-f548-4aa7-acc9-d96493e2c600'}> 

<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}> 

>>> for s in heat.services.list():
	print s

	

Traceback (most recent call last):
  File "<pyshell#293>", line 1, in <module>
    for s in heat.services.list():
  File "/usr/local/lib/python2.7/dist-packages/heatclient/v1/services.py", line 32, in list
    return self._list(url, "services")
  File "/usr/local/lib/python2.7/dist-packages/heatclient/openstack/common/apiclient/base.py", line 131, in _list
    body = self.client.get(url).json()
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 291, in get
    return self.client_request("GET", url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 284, in client_request
    resp, body = self.json_request(method, url, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 265, in json_request
    resp = self._http_request(url, method, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/heatclient/common/http.py", line 220, in _http_request
    raise exc.from_response(resp)
HTTPForbidden: ERROR: You are not authorized to complete this action.
>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  46c8b068564b4fada4413d8f2b92cac2 

http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1097466543', u'stack_user_project_id': u'bdacda6174b842b196708a09e8d509ea', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1097466543/5d0bb2e4-d7e9-484e-a5c6-a0549c4de136', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'5d0bb2e4-d7e9-484e-a5c6-a0549c4de136'}> 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1777063136', u'stack_user_project_id': u'430afe5d86b44800841c5452b8aae057', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1777063136/478089b2-f548-4aa7-acc9-d96493e2c600', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'478089b2-f548-4aa7-acc9-d96493e2c600'}> 

<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}> 

http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'97a21520-55a5-4c35-a0b8-dffd92b17419', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:20:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'1427ac5e-e806-4d67-9b14-c365bf0aac3c'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'a48ac46f-6c9c-4057-9317-84555c517ca3', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:20:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'459be296-2adb-4f7f-a7fb-d4b2fb4dd759'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'eb2f00e4-f279-419f-a581-bfa972ae14c7', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:20:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'c1d9d741-c3c2-4e89-aeed-ff4fd06ad27c'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'3d26326c-c5bb-43d1-afbd-bc3f01872efb', u'created_at': u'2015-06-11T04:14:24.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:20:17.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'd999aa4e-488a-4322-aede-35f096326ece'}> 

>>> ================================ RESTART ================================
>>> 
{'username': 'demo', 'tenant_name': 'demo', 'password': 'nomoresecrete', 'auth_url': 'http://192.168.80.130:5000/v2.0'} 

auth_token:  a8b27984caf349d693826acaca6211db 

demo_heat_endpoint:  http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1097466543', u'stack_user_project_id': u'bdacda6174b842b196708a09e8d509ea', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1097466543/5d0bb2e4-d7e9-484e-a5c6-a0549c4de136', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'5d0bb2e4-d7e9-484e-a5c6-a0549c4de136'}> 

<Stack {u'description': u'No description', u'parent': None, u'tags': None, u'stack_name': u'DefaultParametersTest-1777063136', u'stack_user_project_id': u'430afe5d86b44800841c5452b8aae057', u'stack_status_reason': u'Engine went down during stack CREATE', u'creation_time': u'2015-06-10T10:17:12', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/DefaultParametersTest-1777063136/478089b2-f548-4aa7-acc9-d96493e2c600', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_FAILED', u'id': u'478089b2-f548-4aa7-acc9-d96493e2c600'}> 

<Stack {u'description': u'Heat WordPress template to support F18, using only Heat OpenStack-native resource types, and without the requirement for heat-cfntools in the image. WordPress is web software you can use to create a beautiful website or blog. This template installs a single-instance WordPress deployment using a local MySQL database to store the data.\n', u'parent': None, u'tags': None, u'stack_name': u's', u'stack_user_project_id': u'27d984f4753b4f76b195e52060ac7af9', u'stack_status_reason': u'Stack CREATE completed successfully', u'creation_time': u'2015-06-08T10:24:47', u'links': [{u'href': u'http://192.168.80.130:8004/v1/d8f42a85e023411080a86768fa0e4692/stacks/s/8f2d5f57-d5c5-4eed-b09b-feaf04779431', u'rel': u'self'}], u'updated_time': None, u'stack_owner': u'demo', u'stack_status': u'CREATE_COMPLETE', u'id': u'8f2d5f57-d5c5-4eed-b09b-feaf04779431'}> 

admin_heat_endpoint:  http://192.168.80.130:8004/v1/d60b5c7ed1a449efb4dab22162da0cb8 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'97a21520-55a5-4c35-a0b8-dffd92b17419', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:21:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'1427ac5e-e806-4d67-9b14-c365bf0aac3c'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'a48ac46f-6c9c-4057-9317-84555c517ca3', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:21:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'459be296-2adb-4f7f-a7fb-d4b2fb4dd759'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'eb2f00e4-f279-419f-a581-bfa972ae14c7', u'created_at': u'2015-06-11T04:14:15.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:21:15.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'c1d9d741-c3c2-4e89-aeed-ff4fd06ad27c'}> 

<Service {u'status': u'up', u'binary': u'heat-engine', u'report_interval': 60, u'engine_id': u'3d26326c-c5bb-43d1-afbd-bc3f01872efb', u'created_at': u'2015-06-11T04:14:24.000000', u'hostname': u'kartoos', u'updated_at': u'2015-06-11T04:21:17.000000', u'topic': u'engine', u'host': u'kartoos', u'deleted_at': None, u'id': u'd999aa4e-488a-4322-aede-35f096326ece'}> 

>>> 

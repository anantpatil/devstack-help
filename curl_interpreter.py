Python 2.7.6 (default, Jun 22 2015, 17:58:13) 
[GCC 4.8.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> cmd = ['curl']
>>> 
>>> cmd.append('--insecure')
>>> cmd
['curl', '--insecure']
>>> cmd.append('-X', 'PUT')

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cmd.append('-X', 'PUT')
TypeError: append() takes exactly one argument (2 given)
>>> cmd.extend(['-X', 'PUT'])
>>> cmd
['curl', '--insecure', '-X', 'PUT']
>>> 
>>> cmd= ['curl']
>>> cmd.extend([
	'-i',
	'-H',
	"Content-Type: application/json",
	'-d'
	})
SyntaxError: invalid syntax
>>> cmd.extend([
	'-i',
	'-H',
	"Content-Type: application/json",
	'-d'
	])
>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d']
>>> data = '{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "nomoresecrete"
        }
      }
    }
  }
}'
SyntaxError: EOL while scanning string literal
>>> data = """
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "admin",
          "domain": { "id": "default" },
          "password": "nomoresecrete"
        }
      }
    }
  }
}
"""
>>> data
'\n{ "auth": {\n    "identity": {\n      "methods": ["password"],\n      "password": {\n        "user": {\n          "name": "admin",\n          "domain": { "id": "default" },\n          "password": "nomoresecrete"\n        }\n      }\n    }\n  }\n}\n'
>>> 
>>> 
>>> data = { "auth": {"identity": {"methods": "["password"],
			       
SyntaxError: invalid syntax
>>> data = { "auth": {"identity": {"methods": ["password"],
			       "password": {
				       "user": {
					       "name": "admin",
					       "domain": {"id": "default"},
					       "password": "nomoresecrete"
					       }
				       }
			       }
		  }
	 }
>>> data
{'auth': {'identity': {'password': {'user': {'domain': {'id': 'default'}, 'password': 'nomoresecrete', 'name': 'admin'}}, 'methods': ['password']}}}
>>> 
>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d']
>>> import json
>>> s=json.dumps(data)
>>> s
'{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}'
>>> 
>>> cmd.append(s)
>>> cms

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    cms
NameError: name 'cms' is not defined
>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}']
>>> 
>>> url='http://localhost:5000/v3/auth/tokens'
>>> cmd.append(url)
>>> 
>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> 
>>> import subprocess
>>> sub = subprocess.Po

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sub = subprocess.Po
AttributeError: 'module' object has no attribute 'Po'
>>> sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stder=subprocess.PIPE)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stder=subprocess.PIPE)
TypeError: __init__() got an unexpected keyword argument 'stder'
>>> sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> output = sub.communicate()
>>> print output[0]
HTTP/1.1 201 Created
Date: Fri, 04 Sep 2015 03:24:25 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: aa6acadf262944dcb0314b951344fc43
Vary: X-Auth-Token
x-openstack-request-id: req-f86c8c4e-5aa8-4eb6-b500-8873022c68b6
Content-Length: 297
Content-Type: application/json

{"token": {"methods": ["password"], "expires_at": "2015-09-04T04:24:25.347509Z", "extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id": "36be4c8e3bc844d785820467aa1ca744", "name": "admin"}, "audit_ids": ["UxjXbn9WRISahQF5n_qo6Q"], "issued_at": "2015-09-04T03:24:25.347557Z"}}
>>> print output[1]
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0100   445  100   297  100   148   2610   1300 --:--:-- --:--:-- --:--:--  2628

>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> cmd1=['curl']
>>> cmd1.append('--insecure')
>>> cmd1.extend([
	'-i',
	'-H',
	'Content-Type:',
	'-d',
	s,
	url
	])
>>> cmd
['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> cmd1
['curl', '--insecure', '-i', '-H', 'Content-Type:', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> cm1 == cmd

Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    cm1 == cmd
NameError: name 'cm1' is not defined
>>> cmd1 == cmd
False
>>> sub = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> output = sub.communicate()
>>> print output[0]
HTTP/1.1 201 Created
Date: Fri, 04 Sep 2015 03:29:40 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: 3b44be9d231e47439f56c3c2bace2760
Vary: X-Auth-Token
x-openstack-request-id: req-6f1676b3-0efe-4414-b3a7-e1f0fa28f2fb
Content-Length: 297
Content-Type: application/json

{"token": {"methods": ["password"], "expires_at": "2015-09-04T04:29:40.206107Z", "extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id": "36be4c8e3bc844d785820467aa1ca744", "name": "admin"}, "audit_ids": ["2YwwL3FsS3mJ-tulBm6uDw"], "issued_at": "2015-09-04T03:29:40.206176Z"}}
>>> 
>>> 
>>> print "%s" % cmd1
['curl', '--insecure', '-i', '-H', 'Content-Type:', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> 
>>> cmd1=['curl']
>>> cmd1.append('--insecure')
>>> cmd1.extend([
	'-i',
	'-H',
	'-d',
	s,
	url
	])
>>> 
>>> sub = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> output = sub.communicate()
>>> print output[0]
HTTP/1.1 401 Unauthorized
Date: Fri, 04 Sep 2015 03:33:14 GMT
Server: Apache/2.4.7 (Ubuntu)
Vary: X-Auth-Token
x-openstack-request-id: req-69b7a3ea-7585-4a79-83a0-770803608ddc
WWW-Authenticate: Keystone uri="http://localhost:5000"
Content-Length: 162
Content-Type: application/json

{"error": {"message": "The request you have made requires authentication. (Disable debug mode to suppress these details.)", "code": 401, "title": "Unauthorized"}}
>>> cmd1
['curl', '--insecure', '-i', '-H', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> cmd1=['curl']
>>> cmd1.extend([
	'-i',
	'-H',
	'Content-Type',
	'-d',
	s,
	url
	])
>>> sub = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> output = sub.communicate()
>>> print output[0]
HTTP/1.1 400 Bad Request
Date: Fri, 04 Sep 2015 03:35:14 GMT
Server: Apache/2.4.7 (Ubuntu)
Vary: X-Auth-Token
x-openstack-request-id: req-9a19436e-07e7-414f-af2b-51de195904f9
Content-Length: 258
Connection: close
Content-Type: application/json

{"error": {"message": "Expecting to find application/json in Content-Type header - the server could not comply with the request since it is either malformed or otherwise incorrect. The client is assumed to be in error.", "code": 400, "title": "Bad Request"}}
>>> cmd1
['curl', '-i', '-H', 'Content-Type', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> ['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
['curl', '-i', '-H', 'Content-Type: application/json', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> 
>>> cmd1=['curl']
>>> cmd1.extend([
	'-i',
	'-H',
	'Content-Type:',
	'-d',
	s,
	url
	])
>>> s
'{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}'
>>> url
'http://localhost:5000/v3/auth/tokens'
>>> sub = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> o = sub.communicate()
>>> print o[0]
HTTP/1.1 201 Created
Date: Fri, 04 Sep 2015 03:37:26 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: 9abcbb7fcef8400d9177daed2ae52c55
Vary: X-Auth-Token
x-openstack-request-id: req-b9c18dff-9c00-40fd-904a-d98a287c9b19
Content-Length: 297
Content-Type: application/json

{"token": {"methods": ["password"], "expires_at": "2015-09-04T04:37:26.222261Z", "extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id": "36be4c8e3bc844d785820467aa1ca744", "name": "admin"}, "audit_ids": ["nOlC3ZgkTfuyPkcNACPnXg"], "issued_at": "2015-09-04T03:37:26.222297Z"}}
>>> cmd1
['curl', '-i', '-H', 'Content-Type:', '-d', '{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> cmd = 'curl -i -H Content-Type: -d %s %s' % s, url

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    cmd = 'curl -i -H Content-Type: -d %s %s' % s, url
TypeError: not enough arguments for format string
>>> cmd = 'curl -i -H Content-Type: -d %s %s' % (s, url)
>>> cmd
'curl -i -H Content-Type: -d {"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}} http://localhost:5000/v3/auth/tokens'
>>> sub = subprocess.Popen(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> o = sub.communicate()
>>> o[0]
'HTTP/1.1 201 Created\r\nDate: Fri, 04 Sep 2015 03:48:01 GMT\r\nServer: Apache/2.4.7 (Ubuntu)\r\nX-Subject-Token: 90686608d2954e158e73847f192c1550\r\nVary: X-Auth-Token\r\nx-openstack-request-id: req-daa69744-41d3-44ef-8a07-1099bcce3398\r\nContent-Length: 297\r\nContent-Type: application/json\r\n\r\n{"token": {"methods": ["password"], "expires_at": "2015-09-04T04:48:01.779563Z", "extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id": "36be4c8e3bc844d785820467aa1ca744", "name": "admin"}, "audit_ids": ["vsjfLfH7TuSLxBED2VlJwg"], "issued_at": "2015-09-04T03:48:01.779616Z"}}'
>>> print o[0]
HTTP/1.1 201 Created
Date: Fri, 04 Sep 2015 03:48:01 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Subject-Token: 90686608d2954e158e73847f192c1550
Vary: X-Auth-Token
x-openstack-request-id: req-daa69744-41d3-44ef-8a07-1099bcce3398
Content-Length: 297
Content-Type: application/json

{"token": {"methods": ["password"], "expires_at": "2015-09-04T04:48:01.779563Z", "extras": {}, "user": {"domain": {"id": "default", "name": "Default"}, "id": "36be4c8e3bc844d785820467aa1ca744", "name": "admin"}, "audit_ids": ["vsjfLfH7TuSLxBED2VlJwg"], "issued_at": "2015-09-04T03:48:01.779616Z"}}
>>> cmd_str = ("curl -i -H \'Content-Type:\' -d \'%s\' \"%s\"" % (s, url))
>>> cmd_str
'curl -i -H \'Content-Type:\' -d \'{"auth": {"identity": {"password": {"user": {"domain": {"id": "default"}, "password": "nomoresecrete", "name": "admin"}}, "methods": ["password"]}}}\' "http://localhost:5000/v3/auth/tokens"'
>>> 
>>> cmd = cmd_str.split()
>>> cmd
['curl', '-i', '-H', "'Content-Type:'", '-d', '\'{"auth":', '{"identity":', '{"password":', '{"user":', '{"domain":', '{"id":', '"default"},', '"password":', '"nomoresecrete",', '"name":', '"admin"}},', '"methods":', '["password"]}}}\'', '"http://localhost:5000/v3/auth/tokens"']
>>> 
>>> sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> o = sub.communicate()

Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    o = sub.communicate()
  File "/usr/lib/python2.7/subprocess.py", line 799, in communicate
    return self._communicate(input)
  File "/usr/lib/python2.7/subprocess.py", line 1401, in _communicate
    stdout, stderr = self._communicate_with_poll(input)
  File "/usr/lib/python2.7/subprocess.py", line 1455, in _communicate_with_poll
    ready = poller.poll()
TypeError: 'int' object is not callable
>>> 
>>> cmd_str = ("curl -i -H Content-Type: -d %s %s" % (s, url))
>>> cmd = cmd_str.split()
>>> sub = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
>>> o = sub.communicate()

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    o = sub.communicate()
  File "/usr/lib/python2.7/subprocess.py", line 799, in communicate
    return self._communicate(input)
  File "/usr/lib/python2.7/subprocess.py", line 1401, in _communicate
    stdout, stderr = self._communicate_with_poll(input)
  File "/usr/lib/python2.7/subprocess.py", line 1455, in _communicate_with_poll
    ready = poller.poll()
TypeError: 'int' object is not callable
>>> 
>>> cmd
['curl', '-i', '-H', 'Content-Type:', '-d', '{"auth":', '{"identity":', '{"password":', '{"user":', '{"domain":', '{"id":', '"default"},', '"password":', '"nomoresecrete",', '"name":', '"admin"}},', '"methods":', '["password"]}}}', 'http://localhost:5000/v3/auth/tokens']
>>> 
>>> 

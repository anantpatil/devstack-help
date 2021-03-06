import os

from keystoneclient.v2_0 import client as ksclient

''' ================== STUFF AS ADMIN USER ========================= '''

'''
def get_admin_creds():
    d = {}
    d['username'] = 'admin'
    d['password'] = 'nomoresecrete'
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = 'admin'
    return d

admin_creds = get_admin_creds()
# print admin_creds, "\n"

admin_keystone = ksclient.Client(**admin_creds)
services = admin_keystone.services.list()

for s in services:
    print s, "\n"

# admin heat client (instance as admin user)
# get the heat endpoint URL from service_catalog
admin_heat_endpoint = admin_keystone.service_catalog.url_for(service_type='orchestration',
                                                             endpoint_type='publicURL')
print "admin_heat_endpoint: ", admin_heat_endpoint, '\n'

admin_heat = hc.Client(HEAT_VERSION,
                       admin_heat_endpoint,
                       token=admin_keystone.auth_token,
                       **demo_creds)
for s in admin_heat.services.list():
    print s, '\n'

'''
    
''' =================== END STUFF AS ADMIN USER =================='''





''' ================== STUFF AS DEMO USER YOU SHOULD CARE ========================= '''

def get_demo_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

demo_creds = get_demo_creds()
print demo_creds, "\n"

# get auth_token to connect to heat API
# you need an auth token to connect to Heat API always.
me = ksclient.Client(**demo_creds)
print "auth_token: ", me.auth_token, "\n"


# get the heat endpoint URL from service_catalog
heat_endpoint = me.service_catalog.url_for(service_type='orchestration',
                                           endpoint_type='publicURL')
print "demo_heat_endpoint: ", heat_endpoint, '\n'

# create heat client for demo/demo
# heat client asks for auth_token, not all clients ask for this, you may
# want to check the openstack documents once.
# from heatclient import client as hc
import heatclient.client as hc
HEAT_VERSION = 1
heat = hc.Client(HEAT_VERSION,
                 heat_endpoint,
                 token=me.auth_token,
                 **demo_creds)
for s in heat.stacks.list():
    print s, '\n'


''' =================== END STUFF AS DEMO USER =================='''

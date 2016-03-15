# Connecting to heat db using interpreter and run commands

from heat.common import import context
from oslo_config import cfg

cfg.CONF.set_override('connection','mysql+pymysql://root:stackdb@127.0.0.1/heat?charset=utf8',
                      group='database')

# this api is api.py in devstack-help. Add this to PYTHONPATH
# IMPORTANT: Make sure you have correct admin url in api.py
from api import keystone as me

ctx=context.RequestContext(auth_token=me.auth_token, user=me.username,
        tenant_id=me.tenant_id,
        request_id=me.request,user_domain_id=me.user_domain_id,project_domain_id=me.project_domain_id,
        is_admin=False)

from heat.db.sqlalchemy import import api as db_api

db_api.resource_get_all(ctx)

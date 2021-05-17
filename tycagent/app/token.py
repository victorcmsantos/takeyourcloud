from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystoneC
from oslo_config import cfg
import json

CONF = cfg.CONF
keystone_authtoken = cfg.OptGroup(name = "keystone_authtoken")
keystone_authtoken_opts=[
  cfg.StrOpt('project_domain_name', default = '', help = ''),
  cfg.StrOpt('project_name', default = '', help = ''),
  cfg.StrOpt('user_domain_name', default = '', help = ''),
  cfg.StrOpt('password', default = '', help = ''),
  cfg.StrOpt('username', default = '', help = ''),
  cfg.StrOpt('auth_url', default = '', help = ''),
  cfg.StrOpt('region', default = '', help = ''),
  cfg.StrOpt('interface', default = '', help = ''),
]
CONF.register_group(keystone_authtoken)
CONF.register_opts(keystone_authtoken_opts, keystone_authtoken)
CONF(default_config_files=['tyc.conf',])

def token_validator():
  try:
    auth_origin = v3.Password(
      auth_url=CONF.keystone_authtoken.auth_url,
      username=CONF.keystone_authtoken.username,
      password=CONF.keystone_authtoken.password,
      project_name=CONF.keystone_authtoken.project_name,
      user_domain_name=CONF.keystone_authtoken.user_domain_name,
      project_domain_name=CONF.keystone_authtoken.project_domain_name
    )
    sess = session.Session(auth=auth_origin)
    token = sess.get_token()
    keystone = keystoneC.Client(session=sess, interface=CONF.keystone_authtoken.interface)
    service_id = keystone.services.list(type='cloudaas')[0].id
    cloudaas_public_url = keystone.endpoints.list(service=service_id, interface='internal', region=CONF.keystone_authtoken.region)[0].url
    return True, json.dumps({"token": token,"cloudaas": cloudaas_public_url})
  except Exception as e:
    return False, json.dumps({"ERROR": "%s" % e})

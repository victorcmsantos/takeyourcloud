from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client as keystoneC
from oslo_config import cfg
from flask import jsonify
from app.api.v1.headers import check_token

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
]
CONF.register_group(keystone_authtoken)
CONF.register_opts(keystone_authtoken_opts, keystone_authtoken)
CONF(default_config_files=['tyc.conf',])

def token_validator(request):
  result, json, http_code = check_token(request)
  if result:
    token = request.headers['X-Auth-Token']
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
      keystone = keystoneC.Client(session=sess)
      keystone.tokens.validate(token)
      return True, jsonify({"status": "everything is ok - nice if have some way to add all options here like a help -"}), 200
    except Exception as e:
      return False, jsonify({"ERROR": "%s" % e}), 400
  else:
    return result, json, http_code

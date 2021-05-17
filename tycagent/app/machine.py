from app.token import token_validator
import json
import requests
import socket
#import subprocess
import os


def shell(commands):
  commands = json.loads(commands)
  for i in commands.get('shell'):
    os.system(i)
    #subprocess.run(i)
    print(i)
  

def newDay(json_server):
  server_uuid = list(json.loads(json_server).keys())[0] 
  t_result, t_json = token_validator()
  t_json = json.loads(t_json)
  nodes_post = requests.post(
                 "%s/v1/nodes/%s" % (t_json.get('cloudaas'), server_uuid),
                 headers = {'X-Auth-Token': t_json.get('token')}
               )
  shell(nodes_post.content)
  return "executa!!!"


def m_execute():
  t_result, t_json = token_validator()
  t_json = json.loads(t_json)
  if t_result:
    nodes_post = requests.post(
                   "%s/v1/nodes" % t_json.get('cloudaas'), 
                   headers = {'X-Auth-Token': t_json.get('token')}, 
                   json={"name": "akaasdsadasdasdsadsadsadasdasd"}
                   #json={"name": socket.getfqdn()}
                )
    if nodes_post.status_code == 308:
      print("update and load config")
      return newDay(nodes_post.content)
    else:
      print("maquina adicionada")
      return nodes_post.content
  else:
    return 'some error on the token_validator'

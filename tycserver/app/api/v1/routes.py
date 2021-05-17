from app import app
from flask import Flask
from flask import request, jsonify
from app.api.v1.token import token_validator
from app.api.v1.headers import json_headers
from app.dbmods.mgmt_nodes import CreateNode, ListNodes, UpdateNode

@app.route('/v1', methods=['GET'])
def v1():
  result, json, http_code = token_validator(request)
  return json, http_code

@app.route('/v1/nodes', methods=['POST', 'GET'])
def v1nodes():
  result, json, http_code = token_validator(request)
  if result:
    if request.method == 'GET':
      return ListNodes()
    if request.method == 'POST':
      required_json = ['name']
      result_1, json_1, http_code_1 = json_headers(request, required_json)
      if not result_1:
        return json_1, http_code_1
      return CreateNode(  
                name = request.json.get('name'), 
             )
  else:
    return json, http_code

@app.route('/v1/nodes/<path:node_uuid>', methods=['GET', 'POST'])
def v1nodes_uuid(node_uuid):
  result, json, http_code = token_validator(request)
  if result:
    if request.method == 'POST':
      return UpdateNode(node_uuid)
  else:
    return json, http_code


@app.errorhandler(404)
def page_not_found(e):
  return "as"


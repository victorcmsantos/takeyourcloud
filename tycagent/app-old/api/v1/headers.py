
from flask import jsonify


def check_token(request):
  if not request.headers.get('X-Auth-Token'):
    return False, jsonify({"msg": "X-Auth-Token is missing"}), 400
  return True, jsonify({"try...": "%s/v1/" % request.headers['host']}), 200

def json_headers(request, f_json_as_array):
  if not request.is_json:
    return False, jsonify({"msg": "Missing JSON in request"}), 400
  for i in f_json_as_array:
    if not request.json.get(i):
      return False, jsonify({"msg": "%s is missing" % i}), 400
  return True, jsonify({"try...": "%s/v1/" % request.headers['host']}), 200

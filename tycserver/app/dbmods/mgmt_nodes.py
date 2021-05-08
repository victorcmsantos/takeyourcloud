from app import db
from app.dbmods.model import Nodes
from flask import jsonify
from datetime import datetime, timezone

def UpdateNode(node_uuid):
  machine = Nodes.query.filter_by(uuid=node_uuid).first()
  if machine:
    machine.updated_at = datetime.now(timezone.utc).isoformat()
    db.session.commit()


    #a_file = open("shell_script", "r")
    #list_of_lists = [(line.strip()).split() for line in a_file]
    #a_file.close()
    f = open('shell_script','r', encoding="utf-8")
    the_file = f.read().split('\n')
    f.close()
    

    return jsonify( { "shell": the_file }), 200
  else:
    return jsonify( { "ERROR": "uuid not found" }), 400

def CreateNode(name=""):
  machine = Nodes.query.filter_by(name=name).first()
  if machine:
    return jsonify( { machine.uuid: {"name": machine.name } }), 308
  else:
    db_insert = Nodes(name=name)
    db.session.add(db_insert)
    db.session.commit()
    db.session.refresh(db_insert)
    return jsonify({ 
                db_insert.uuid: {
                    "name": name, 
                }
            }), 200
    
def ListNodes():
  return jsonify({"nodes": "list of nodes"}), 200


from app import db
from app.dbmods.model import Nodes
from flask import jsonify

def CreateNode(name="", ipaddress="", password="", user=""):
  db_insert = Nodes(name=name, ipaddress=ipaddress, password=password, user=user)
  db.session.add(db_insert)
  try:
    db.session.commit()
    db.session.refresh(db_insert)
    return jsonify({ 
                db_insert.uuid: {
                    "name": name, 
                    "ipaddress": ipaddress, 
                    "password":"*********", 
                    "user": user,"created_at": db_insert.created_at 
                }
            }), 200
  except Exception as e:
    return jsonify({"ERROR": str(e.orig)}), 400

def ListNodes():
  return jsonify({"nodes": "list of nodes"}), 200

from app import db
from datetime import datetime
import uuid

def uuid_gen():
  return str(uuid.uuid4())

class Nodes(db.Model):
  __tablename__ = 'nodes'
  uuid = db.Column(db.String(50), unique=True, index=True, nullable=False, default=uuid_gen, primary_key=True )
  name = db.Column(db.String(50), unique=True, nullable=False)
  ipaddress = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(50), nullable=False)
  user = db.Column(db.String(50), nullable=False)
  #created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().isoformat()[:-3]+'Z')
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

db.create_all()


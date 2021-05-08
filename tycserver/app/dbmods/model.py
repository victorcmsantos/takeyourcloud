from app import db
from datetime import datetime, timezone
import uuid

def uuid_gen():
  return str(uuid.uuid4())

class Nodes(db.Model):
  __tablename__ = 'nodes'
  uuid = db.Column(db.String(50), unique=True, index=True, nullable=False, default=uuid_gen, primary_key=True )
  name = db.Column(db.String(50), unique=True, nullable=False)
  created_at = db.Column(db.String(50), nullable=False, default=datetime.now(timezone.utc).isoformat())
  updated_at = db.Column(db.String(50), nullable=True)
  def __repr__(self):
    return '<Nodes {}>'.format(self.uuid, self.name)

db.create_all()


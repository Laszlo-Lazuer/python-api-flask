from db import db

class ItemModel(db.Model): # Mapping between a row in a table to Python Class & Objects
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True) # id will auto increment
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id") , unique=False, nullable=False) # Ensures proper linking, some DBs will enforce the constraint
    store = db.relationship("StoreModel", back_populates="items")
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")
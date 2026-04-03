from app import db

class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    bedrooms = db.Column(db.Integer, nullable=False)
    bathrooms = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(50), nullable=False)
    property_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Property {self.title}>"
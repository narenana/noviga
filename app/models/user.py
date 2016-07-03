from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    
    username = db.Column(db.String)
    
    password = db.Column(db.String)
    

    def to_dict(self):
        return dict(
            username = self.username,
            password = self.password,
            id = self.id
        )

    def __repr__(self):
        return '<User %r>' % (self.id)

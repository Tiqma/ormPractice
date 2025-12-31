from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    color_name = db.Column(
        db.String(50),
        db.ForeignKey("color.name"),
        unique=True,
        nullable=True
    )

    color = db.relationship("Color", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}"

class Color(db.Model):
    name = db.Column(db.String(50), unique=True, primary_key=True)

    user = db.relationship("User", back_populates="color", uselist=False)

    def __repr__(self):
        return f"<Color {self.name}>"

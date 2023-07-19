from .database import db


class Admin(db.Model):
    __tablename__ = 'Admin'
    admin_id=db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False,unique=True)
    admin_name=db.Column(db.String,nullable=False,unique=True)
    admin_password=db.Column(db.String,nullable=False,unique=True)

class Venue(db.Model):
    __tablename__ = 'Venue'
    venue_id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False, unique=True)
    venue_name = db.Column(db.String,nullable=False)
    venue_place=db.Column(db.String)
    venue_capacity=db.Column(db.Integer)
    Show = db.relationship("Show")


class Show(db.Model):
    __tablename__ = 'Show'
    show_id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False, unique=True)
    show_name = db.Column(db.String,nullable=False)
    show_rating=db.Column(db.Integer)
    show_tags=db.Column(db.String)
    show_time=db.Column(db.Integer)
    show_total_seat=db.Column(db.Integer)
    show_available_seat=db.Column(db.Integer)
    show_ticketprice=db.Column(db.Integer)
    Booking = db.relationship("Booking")
    show_venue_id= db.Column(db.Integer,db.ForeignKey("Venue.venue_id"), nullable=False)
    show_date=db.Column(db.String)

class Booking(db.Model):
    __tablename__ = 'Booking'
    book_id = db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False, unique=True)
    booking_user_id= db.Column(db.Integer,db.ForeignKey("User.user_id"), nullable=False)
    booking_show_id= db.Column(db.Integer,db.ForeignKey("Show.show_id"), nullable=False)
    booking_number=db.Column(db.Integer)



class User(db.Model):
    __tablename__ = 'User'
    user_id= db.Column(db.Integer, autoincrement=True, primary_key=True,nullable=False)
    user_name = db.Column(db.String,nullable=False,unique=True) 
    user_password= db.Column(db.String,nullable=False, unique=True )
    Booking = db.relationship("Booking")
   
 
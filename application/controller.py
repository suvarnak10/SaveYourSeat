from flask import Flask, url_for,request,redirect,session
from flask import render_template
from flask import current_app as app
from application.models import *
import json 

@app.route("/")
def main():
     return redirect(url_for('login'))
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password) 
        all_users=db.session.query(User).filter(User.user_name == username).all()
        if len(all_users)!=0 and all_users[0].user_password==password:
            uid=all_users[0].user_id
            return redirect(url_for('.user_dashboard',uid=uid))
        else:
            return render_template('user_login.html',msg='Wrong credentials,try again')
    return render_template('user_login.html',msg='')

@app.route('/register', methods =['GET', 'POST'])
def register():
   if request.method=='POST':
      if request.method=='POST':
            username = request.form['username']
            password = request.form['password']
            
            all_users=db.session.query(User).filter(User.user_name == username).all()
            if len(all_users)!=0:
                 return render_template('user_register.html',msg='user already exists')
            new_user=User(user_name=username,user_password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('login'))
   return render_template('user_register.html',msg='')

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=='POST':
        adminname = request.form['adminname']
        password = request.form['password']
        print(adminname,password) 
        all_admin=db.session.query(Admin).filter(Admin.admin_name == adminname).all()
        if len(all_admin)!=0 and all_admin[0].admin_password==password:
            aid=all_admin[0].admin_id
            return redirect(url_for('.add_venue',aid=aid))
        else:
            return render_template('admin_login.html',msg='Wrong Admin user')

    return render_template('admin_login.html',msg='')

@app.route("/add_venue")
def add_venue():
        msg=""
        all_venue=db.session.query(Venue).all()
        if len(all_venue)==0:
             return render_template('ad_venue.html',msg='No Venue added')
        all_show=db.session.query(Show).all()
        return render_template('ad_venue.html',all_venue=all_venue,all_show=all_show)

        
@app.route("/create_venue", methods=['GET','POST'])
def create_venue():
    if request.method=='POST':
        venuename = request.form['venuename']
        place=request.form['place']
        capacity=request.form['capacity']
    
        all_venue=db.session.query(Venue).filter(Venue.venue_name == venuename).all()
        if len(all_venue)!=0:
            return render_template('create_venue.html',msg='Venue already exists')
        new_venue=Venue(venue_name=venuename,venue_place=place,venue_capacity=capacity)
        db.session.add(new_venue)
        db.session.commit() 
        return redirect(url_for('.add_venue'))
    return render_template("create_venue.html",msg="")

@app.route("/create_show/<vid>", methods=['GET','POST'])
def create_show(vid):
     if request.method=='POST':
          showname=request.form['showname']
          rating=request.form['rating']
          totalseat=request.form['total seat']
          date=request.form['date']
          timing=request.form['timing']
          tag=request.form['tag']
          price=request.form['price']
          all_venue=db.session.query(Venue).filter(Venue.venue_id == vid).first()
          #capacity=all_venue.venue_capacity
          all_show=db.session.query(Show).filter(Show.show_name == showname).all()
          if len(all_show)!=0:
            return redirect(url_for('.add_venue',msg='show already exists'))
          new_show=Show(show_name=showname,show_rating=rating,show_date=date,show_time=timing,show_tags=tag,show_ticketprice=price,show_available_seat=totalseat,show_total_seat= totalseat,show_venue_id=vid)
          db.session.add(new_show)
          db.session.commit() 
          return redirect(url_for('add_venue')) 
     return render_template('create_show.html',msg='')

@app.route("/editvenue/<vid>", methods=['GET','POST'])
def editvenue(vid):
     venue=db.session.query(Venue).filter(Venue.venue_id== vid).first()
     print(venue)
     if request.method == 'POST':
        
        if request.form.get('save')=='Save':
        
            venue=db.session.query(Venue).filter(Venue.venue_id == vid).first()
            venue.venue_name = request.form['venuename']
            venue.venue_place=request.form['place']
            venue.venue_capacity=request.form['capacity'] 
            db.session.commit()
            return redirect(url_for('.add_venue',msg="edits added to db",vid=vid)) 
        
        if request.form.get('delete')=='Delete':
            
            venue=db.session.query(Venue).filter(Venue.venue_id == vid).first()
            print(venue)
            db.session.delete(venue)
            print(venue)
            show1=db.session.query(Show).filter(Show.show_venue_id== vid).all()
            for i in show1:
                db.session.delete(i)
            db.session.commit()
            return redirect(url_for('.add_venue',vid=vid))
     return render_template('editvenue.html',venue=venue) 

@app.route("/editshow/<sid>", methods=['GET','POST'])
def editshow(sid):
     show=db.session.query(Show).filter(Show.show_id== sid).first()
     venue=db.session.query(Venue).filter(Venue.venue_id == show.show_venue_id).first()
     print(show)
     if request.method == 'POST':
        
        if request.form.get('save')=='Save':
        
            show=db.session.query(Show).filter(Show.show_id == sid).first()
            show.show_rating=request.form['rating']
            show.show_date=request.form['date']
            show.show_total_seat=int(request.form['total seat'])
            show.show_time=request.form['timing'] 
            show.show_tags=request.form['tag'] 
            show.show_ticketprice=request.form['price'] 
            db.session.commit()
            return redirect(url_for('.add_venue',msg="edits added to db",sid=sid)) 
        
        if request.form.get('delete')=='Delete':
            print('inside delete')
            show=db.session.query(Show).filter(Show.show_id == sid).first()
            print(show.show_id)
            db.session.delete(show)
            db.session.commit()
            return redirect(url_for('.add_venue',sid=sid))
     return render_template('editshow.html',show=show,venue=venue) 
 
@app.route("/user_dashboard/<uid>")   
def user_dashboard(uid):
    venues=db.session.query(Venue).all()
    all_venue=[]
    search=[]
    all_show=db.session.query(Show).all()
    for show in all_show:
         for venue in venues:
            if show.show_venue_id==venue.venue_id:
                st=show.show_name+'-'+show.show_tags+'-'+venue.venue_name
                search.append(st.lower())
            if show.show_venue_id==venue.venue_id and venue not in all_venue:
                all_venue.append(venue)
    
    return render_template('user_dashboard.html',all_venue=all_venue,all_show=all_show,uid=uid,search=json.dumps(search))

@app.route("/booking_user/<uid>/<sid>", methods=['GET','POST'])
def booking_user(uid,sid):
     show=db.session.query(Show).filter(Show.show_id == sid).first() 
     if request.method=='POST':
            number =int( request.form['number'])
            print(number)
            show.show_available_seat=show.show_available_seat-number
            new_booking=Booking(booking_user_id=uid,booking_show_id=sid,booking_number=number)
            db.session.add(new_booking)
            db.session.commit()
            return redirect(url_for('user_dashboard',uid=uid))
     return render_template('booking_user.html',show=show,uid=uid)

@app.route("/delete/<uid>/<sid>")   
def delete(uid,sid):
    bookings=db.session.query(Booking).filter(Booking.booking_show_id==sid).first()
    db.session.delete(bookings)
    db.session.commit()
    show=db.session.query(Show).filter(Show.show_id == sid).first()
    show.show_available_seat=show.show_available_seat+bookings.booking_number
    db.session.add(show)
    db.session.commit()
    return redirect(url_for('user_bookings',bookings=bookings,uid=uid,sid=sid))

@app.route("/user_bookings/<uid>", methods=['GET','POST'])
def user_bookings(uid):
    bookings=db.session.query(Booking).filter(Booking.booking_user_id==uid).all()
    all_show=db.session.query(Show).all() 
    all_venue=db.session.query(Venue).all()
    shows=[]
    for i in bookings:
        for j in all_show:
            for k in all_venue:
                if i.booking_show_id==j.show_id and j.show_venue_id==k.venue_id:
                    shows.append([k.venue_name,j.show_name,j.show_date,j.show_time,i.booking_number,uid,j.show_id])
    
    return render_template('user_bookings.html',shows=shows,uid=uid)

@app.route("/summary")   
def summary():
    all_show=db.session.query(Show).all() 
    all_venue=db.session.query(Venue).all()
    li=[]
    for i in all_venue:
        flag=True
        for j in all_show:
          if i.venue_id == j.show_venue_id :
            flag=False
            li.append([i.venue_name, j.show_name, j.show_total_seat, j.show_total_seat-j.show_available_seat, j.show_ticketprice*(j.show_total_seat-j.show_available_seat)])
            print(li)
        if flag:
            li.append([i.venue_name,'none','none','none','none'])
            print(li)
    return render_template('summary.html',all_venue=all_venue,all_show=all_show,li=li)

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

@app.route('/logout_admin')
def logout_admin():
    return redirect(url_for('admin'))
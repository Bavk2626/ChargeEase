from pyrebase import * 
from flask import * 

config = {

  "apiKey": "AIzaSyDZmiSBPCUpRfCkegjATrEe1057S4j_r1Q",
  "authDomain": "chargeease-21f68.firebaseapp.com",
  "databaseURL": "https://chargeease-21f68-default-rtdb.firebaseio.com",
  "projectId": "chargeease-21f68",
  "storageBucket": "chargeease-21f68.appspot.com",
  "messagingSenderId": "255861292061",
  "appId": "1:255861292061:web:2ae5ca02d54a45419a5af4",
  "measurementId": "G-R1Y1JTCJ42"

}

firebase = initialize_app(config)

db = firebase.database()

app = Flask(__name__) 
#name = "akhil"
#print(name)
#db.child("ChargeEase").child("EVUser").push({"name":name,"age":21,"email":"bandianand900@gmail.com","status":0,"Vechile":"C-name-type","mobile":"6302174710","address":"plot 126"})

@app.route('/',methods=['GET'])
def choose():
  #db.child("ChargeEase").child("Bike").push({"bikeModel":"","bikeType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  #db.child("ChargeEase").child("Car").push({"carModel":"","carType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  return render_template('index.htm')
@app.route('/edit',methods=['GET','POST'])
def edit():
   if request.method == 'POST':
    Name = request.form['name']
    Address= request.form['address']
    Latitude = request.form['lat']
    Longitude = request.form['lng']
    idd = request.form['id']
    print(request.form)
    if 'rapid' in request.form:
      Rapid = 1
    else:
      Rapid = 0
    if 'Battery' in request.form:
      BatteryExchange = 1
    else:
      BatteryExchange = 0
    if 'solar' in request.form:
      Solar = 1
    else:
      Solar = 0
    #print (request.form)
    #print(idd)
    ref = db.child("ChargeEase").child("EVStation").child(idd)
    station = ref.get().val()
    station['name'] = Name
    station['address'] = Address
    station['lat'] = Latitude
    station['lng'] = Longitude
    station['rapid'] = Rapid
    station['batteryexchange'] = BatteryExchange
    station['solar'] = Solar
    ref = db.child("ChargeEase").child("EVStation").child(idd)
    ref.update(station)
    return redirect(url_for('Evdata'))
@app.route('/delete//<string:user_id>',methods=['GET','POST'])
def delete():

  return "mama"
@app.route('/cars',methods=['GET','POST'])
def cars():
  if request.method == 'POST':
    carModel = request.form['carModel']
    carType = request.form['carType']
    power = request.form['power']
    range1 = request.form['range']
    batteryCap = request.form['batteryCap']
    chargingTime = request.form['chargingTime']
    db.child("ChargeEase").child("Car").push({"carModel":carModel,"carType":carType,"power":power,"range":range1,"batteryCap":batteryCap,"chargingTime":chargingTime})
  data = db.child("ChargeEase").child("Car").get()
  l = data.val()
  return render_template('CarsForm.html',data=l)

@app.route('/bike',methods=['GET','POST'])
def bike():
  if request.method == 'POST':
    carModel = request.form['bikeModel']
    carType = request.form['bikeType']
    power = request.form['power']
    range1 = request.form['range']
    batteryCap = request.form['batteryCap']
    chargingTime = request.form['chargingTime']
    db.child("ChargeEase").child("Bike").push({"bikeModel":carModel,"bikeType":carType,"power":power,"range":range1,"batteryCap":batteryCap,"chargingTime":chargingTime})
  data = db.child("ChargeEase").child("Bike").get()
  l = data.val()
  return render_template('BikeForm.html',data=l)

@app.route('/EVdata',methods=['GET','POST'])
def Evdata():
  #db.child("ChargeEase").child("Bik").push({"bikeModel":carModel,"bikeType":carType,"power":power,"range":range1,"batteryCap":batteryCap,"chargingTime":chargingTime})
  data = db.child("ChargeEase").child("EVStation").get()
  l = data.val()
  return render_template('EVdata.html',data=l)


@app.route("/update//<string:user_id>")
def approval(user_id):
  try :
    ref = db.child("ChargeEase").child("EVStation").child(user_id)
    station = ref.get().val() 
    if station['adminstatus']==0 :
      station['adminstatus'] = 1
      ref = db.child("ChargeEase").child("EVStation").child(user_id) 
      ref.update(station)
      return redirect(url_for('Evdata'))
    else :
      #newdata = {'adminstatus':0}
      station['adminstatus'] = 0
      ref = db.child("ChargeEase").child("EVStation").child(user_id) 
      ref.update(station)
      return redirect(url_for('Evdata'))
  except Exception as e:
        print(f"Error: {e}") 
  return "okay" 


if __name__ == '__main__':
  app.run(debug=True)

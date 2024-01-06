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
#db.child("ChargeEase").child("EVUser").push({"id":"EV01","name":name,"age":21,"email":"bandianand900@gmail.com","password":"Bavk@gmail.com","Vechile":"C-name-type","Battery":0,"Range":0,"mobile":"6302174710"})

@app.route('/',methods=['GET'])
def choose():
  #db.child("ChargeEase").child("Bike").push({"bikeModel":"","bikeType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  #db.child("ChargeEase").child("Car").push({"carModel":"","carType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  return render_template('index.htm')
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

if __name__ == '__main__':
  app.run(debug=True)

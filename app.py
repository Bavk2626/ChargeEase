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
auth = firebase.auth()
person = {"present": False}

app = Flask(__name__) 
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
#name = "akhil"
#print(name)
#db.child("ChargeEase").child("EVUser").push({"name":name,"age":21,"email":"bandianand900@gmail.com","status":0,"Vechile":"C-name-type","mobile":"6302174710","address":"plot 126"})

@app.route('/',methods=['GET'])
def home():
  #db.child("ChargeEase").child("Bike").push({"bikeModel":"","bikeType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  #db.child("ChargeEase").child("Car").push({"carModel":"","carType":"","power":"","range":"","batteryCap":"","chargingTime":""})
  return render_template('home.html',person=person)
@app.route('/login',methods=['POST','GET'])
def login():
  return render_template("Login.html", person=person)

@app.route("/result",methods=["POST","GET"])
def result():
  if request.method ==  'POST':
    #print(request.form)
    email = request.form['email']
    password = request.form['password']
    try :
      user = auth.sign_in_with_email_and_password(email,password)
      #verify = auth.get_account_info(user['idToken'])['users'][0]['emailVerified']
      
      f = 0
      if not ("xPK2YsHozMN9vkBp4lcax83jlAr2" == user['localId']):
        f = 1
        raise Exception("Only admin can login")
      person["id"] = user['localId']
      person['present'] = True
      #print(person)
    except Exception as e:
      #s = e.args[1]
      if f == 1 :
        flash("Only admin can login",'danger')
      else :  
        flash("Invalid Email or Password",'danger')
      return redirect(url_for('login'))

    return  redirect(url_for('Evdata'))

@app.route('/edit',methods=['GET','POST'])
def edit():
   if request.method == 'POST':
    Name = request.form['name']
    Address= request.form['address']
    Latitude = request.form['lat']
    Longitude = request.form['lng']
    idd = request.form['id']
    avl = request.form['avl']
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
    station['availability'] = avl
    station['rapid'] = Rapid
    station['batteryexchange'] = BatteryExchange
    station['solar'] = Solar
    ref = db.child("ChargeEase").child("EVStation").child(idd)
    ref.update(station)
    return redirect(url_for('Evdata'))

@app.route('/delete//<string:user_id>//<string:name>',methods=['GET','POST'])
def delete(user_id,name):
  ref = db.child("ChargeEase").child("EVStation").child(user_id)
  ref.remove()
  return name + " Station is Deleted"


@app.route('/cars',methods=['GET','POST'])
def cars():
  if not person['present']:
    return redirect(url_for('login'))

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
  return render_template('CarsForm.html',data=l,person=person)

@app.route('/bike',methods=['GET','POST'])
def bike():
  if not person['present']:
    return redirect(url_for('login'))
  try :
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
    return render_template('BikeForm.html',data=l,person=person)
  except Exception as e :
    return "Connection error"

@app.route('/EVdata',methods=['GET','POST'])
def Evdata():
  if not person['present']:
    return redirect(url_for('login'))
  try :
    #db.child("ChargeEase").child("Bik").push({"bikeModel":carModel,"bikeType":carType,"power":power,"range":range1,"batteryCap":batteryCap,"chargingTime":chargingTime})
    data = db.child("ChargeEase").child("EVStation").get()
    l = data.val()
    return render_template('EVdata.html',data=l,person=person)
  except Exception as e :
    return "Connection Error"


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




@app.route("/logout")
def logout():
  global person 
  #print("logout :", person)
  person = {"present": False}
  return redirect(url_for("home"))



if __name__ == '__main__':
  app.run(debug=True)

import pyrebase

global firebaseConfig

firebaseConfig = {
	  "apiKey": "AIzaSyCsy5bZ0DT6asJa944FLyAuCbVaJFqUGE8",
	  "authDomain": "newogs-e8f1d.firebaseapp.com",
	  "databaseURL": "https://newogs-e8f1d.firebaseio.com",
	  "projectId": "newogs-e8f1d",
	  "storageBucket": "newogs-e8f1d.appspot.com",
	  "messagingSenderId": "560352147437",
	  "appId": "1:560352147437:web:63ce877e60772ae2bdd9e4",
	  "measurementId": "G-3FTM661KJQ"
	}

def Login(email,password):
	

	firebase = pyrebase.initialize_app(firebaseConfig)
	auth = firebase.auth()
	
	login = auth.sign_in_with_email_and_password(email,password)
	'''db = firebase.database()
	print(db)'''
	
	print("login successful")
	
#Login('admin@ogs.com','admin@ogs')

		#return "successful"


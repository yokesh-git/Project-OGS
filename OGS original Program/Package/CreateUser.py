import pyrebase
import requests


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

def CreateUser_Student(year_of_joining,student_dept,student_count,student_domain):

  firebase = pyrebase.initialize_app(firebaseConfig)
  auth = firebase.auth()

  yoj = int(year_of_joining) % 100
  year_of_joining = str(yoj)
  count = int(student_count)
  #Spliting Password from ID
  v = student_domain.split('@',1)
  ori = v[1].split('.',1)

  for i in range(1,count+1):
    try:
      if i in range(1,10):
        print(i)
        user = auth.create_user_with_email_and_password(
          email = year_of_joining+student_dept+'0'+str(i)+student_domain,
          password = year_of_joining+student_dept+'0'+str(i)+'@'+ori[0])
      else:
        user = auth.create_user_with_email_and_password(
          email = year_of_joining+student_dept+str(i)+student_domain,
          password = year_of_joining+student_dept+str(i)+'@'+ori[0])
    except requests.exceptions.HTTPError:
      continue
  print("Created")
  #login = auth.sign_in_with_email_and_password(email,password)
  #print("Logged in")
  #print(login)


def CreateUser_Teacher(teacher_dept,teacher_domain,teacher_count):


  firebase = pyrebase.initialize_app(firebaseConfig)
  auth = firebase.auth()

  count = int(teacher_count)
  v = teacher_domain.split('@',1)
  ori = v[1].split('.',1)

  for i in range(1,count+1):
    try:
      if i in range(1,10):
        print(i)
        user = auth.create_user_with_email_and_password(
          email = 'ap'+teacher_dept+'0'+str(i)+teacher_domain, 
          password = 'ap'+teacher_dept+'0'+str(i)+'@'+ori[0])
        #print(user)
        #print(email)
      else:
        user = auth.create_user_with_email_and_password(
          email = 'ap'+teacher_dept+str(i)+teacher_domain,
          password = 'ap'+teacher_dept+str(i)+'@'+ori[0])
    except requests.exceptions.HTTPError:
      continue

  print("Teacher Created")

def StudentContent(year_of_joining,student_dept,student_count,student_domain,College_Code):


  firebase = pyrebase.initialize_app(firebaseConfig)

  db = firebase.database()

  yoj = int(year_of_joining) % 100
  year_of_joining = str(yoj)
  count = int(student_count)

  v = student_domain.split('@',1)
  ori = v[1].split('.',1)


  for i in range(1,count+1):
    try:
      if i in range(1,10):
        print(i)
        path = db.child("College"+College_Code+"/Student/"+year_of_joining+student_dept+'0'+str(i)+'@'+ori[0])
        Student_Data = {College_Code:"Student"}
        db.push(Student_Data)
      else:
        path = db.child("College"+College_Code+"/Student/"+year_of_joining+student_dept+str(i)+'@'+ori[0])
        Student_Data = {College_Code:"Student"}
        db.push(Student_Data)
    except requests.exceptions.HTTPError:
      continue

  #db.push(Student_Dict)
  #print(Student_Dict)
  print("Done")

def TeacherContent(teacher_dept,teacher_domain,teacher_count,College_Code):

  firebase = pyrebase.initialize_app(firebaseConfig)
  db = firebase.database()

  count = int(teacher_count)
  v = teacher_domain.split('@',1)
  ori = v[1].split('.',1)

  for i in range(1,count+1):
    try:
      if i in range(1,10):
        print(i)

        path = db.child("College"+College_Code+"/Teacher/"+'ap'+teacher_dept+'0'+str(i)+'@'+ori[0])
        Teacher_Data = {College_Code:"Teacher"}
        db.push(Teacher_Data)
        #print(user)
        #print(email)
      else:
        path = db.child("College"+College_Code+"/Teacher/"+'ap'+teacher_dept+str(i)+'@'+ori[0])
        Teacher_Data = {College_Code:"Teacher"}
        db.push(Teacher_Data)
    except requests.exceptions.HTTPError:
      continue

  

  #data = {'9515':'Teacher'}

  #db.push(data)


#StudentContent("17","cs","10","@ogs.com","9515")
#TeacherContent("cs","@ogs.com","10","9515")
#CreateUser_Teacher("ec","@ogs.com","10")
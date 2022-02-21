import re

def register():
    db = open("database.txt","r")
    username = input("Create Username:")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,username)):
      #print("Valid Email")
      #register()
      print("Create Password")
    else:
      print("Invalid Email")
      register()
    password = input("Create Password:")
    password1 =input("Confirm Password:")

    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))


    if password != password1:
       print("Password don't match, restart")
       register()
    else:
      flag = 0
      while True:
        if (len(password)<8):
          flag = -1
          break
        elif (len(password)>16):
          flag = -1
          break
        elif not re.search("[a-z]", password):
          flag = -1
          break
        elif not re.search("[A-Z]", password):
          flag = -1
          break
        elif not re.search("[0-9]", password):
          flag = -1
          break
        elif not re.search("[_@$]", password):
          flag = -1
          break
        elif re.search("\s", password):
          flag = -1
          break
        else:
          flag = 0
          #register()
          break
      if flag ==-1:
        print("Not a Valid Password")
        register()
      elif username in d:
        print("username exists")
        register()
      else:
        db = open("database.txt", "a")
        db.write(username+","+password+"\n")
        print("Success!")

def access():
  db = open("database.txt","r")
  username = input("Enter Your Username:")
  password = input("Enter Your Password:" )

  if not len(username or password)<1:
    d = []
    f = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)
        f.append(b)
    data = dict(zip(d, f))

    try:
      if data [username]:
        try:
          if password == data[username]:
            print("login Success")
            print("Hi,",username)
          else:
            print("Password or Username incorrect")
        except:
          print("Incorrect password or Username")
      else:
        print("Username or Password doesn't exist")
    except:
      print("Username or Password doesn't exist")
  else:
    print("Pleas Enter a Value")

def home(option=None):
    option = int(input("for Register press 1 or login press 2: "))
    if option == 1:
      register()
    elif option == 2:
      access()
    else:
        print("Incorrect input")

home()








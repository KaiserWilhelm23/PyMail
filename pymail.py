
import smtplib
import sys
import phonenumbers 
from phonenumbers import geocoder 
import requests
import json
import base64




apple = 'smtp.mail.me.com'
gmail = 'smtp.gmail.com'
yahoo = 'smtp.mail.yahoo.com'
port = 587


help = '''

[*help]
  
  /[command]:
    
    /help {shows this message}
    
    /exit {exits the client}
    
    /info syscode {get system codes}
    
    /info [Error] {get info on Errors}
    
    /rcps_many {send email to multiple recpients run when '[>] To:' appears.} (optioanl)
    
    /sms {prints list of sms adresses}
    
    /test {tests all connections}
    
    /info num {searches the provider of a number and its location}
    
    /encode {run this when you see 'Message: '}
    
    /decode {run in main console. decode any message in a Base64 format}
    
    
  [==============================]
  '''
  
  
syscode = """
    [*]
   [========================]
   system codes are used to get info on errors [-EOR -(reason)]
   
   /info EOR-[reaosn]
   =========================
   /info EOR-L 
   /info EOR-C
 
    """  
    
pymail = """
   AppName = PyMail
   Version = 2.0
   Python Version = 3.6
   Current State = UnStable
                       
"""    

  
print('''[*]
  
  Supported email clients:
    [1] gmail
    [2] icloud
    [3] yahoo 
    
  [==============================]
  
  ''')
  
  
  
sms = """
List of SMS GateWay adresses:

  AT&T: number@txt.att.net (SMS), number@mms.att.net (MMS)

  Boost Mobile: number@sms.myboostmobile.com (SMS), number@myboostmobile.com (MMS)

  C-Spire: number@cspire1.com

  Consumer Cellular: number@mailmymobile.net

  Cricket: number@sms.cricketwireless.net (SMS), number@mms.cricketwireless.net (MMS)

  Google Fi (Project Fi): number@msg.fi.google.com (SMS & MMS)

  Metro PCS: number@mymetropcs.com (SMS & MMS)

  Mint Mobile: number@mailmymobile.net (SMS)

  Page Plus: number@vtext.com (SMS), number@mypixmessages.com (MMS)

  Red Pocket: Red Pocket uses AT&T or T-Mobile (for GSM SIMs) & Verizon for CDMA. See info. for those carriers.

  Republic Wireless: number@text.republicwireless.com (SMS)

  Simple Mobile: number@smtext.com (SMS)

  Sprint: number@messaging.sprintpcs.com (SMS), number@pm.sprint.com (MMS)

  T-Mobile: number@tmomail.net (SMS & MMS)

  Ting: number@message.ting.com (SMS for CDMA), number@tmomail.net (SMS for GSM)

  Tracfone: number@mmst5.tracfone.com (MMS)

  U.S. Cellular: number@email.uscc.net (SMS), number@mms.uscc.net (MMS)

  Verizon: number@vtext.com (SMS), number@vzwpix.com (MMS)

  Virgin Mobile: number@vmobl.com (SMS), number@vmpix.com (MMS)

  Xfinity Mobile: number@vtext.com (SMS), number@mypixmessages.com (MMS)

"""
  
  

  
  
  
  
  
def test():
  try:
    s = smtplib.SMTP(apple,port)
    s.starttls()
    
    s1 = smtplib.SMTP(gmail, port)
    s1.starttls()
    
    s2 = smtplib.SMTP(yahoo, port)
    s2.starttls()
    print('[*] Connections Made Successfuly.')
    
  except Exception as e:
    print(e)
    
    
def getCarrier(number):
  try:
    url = 'https://api.telnyx.com/v1/phone_number/1' + number
    html = requests.get(url).text
    data = json.loads(html)
    data = data["carrier"]
    carrier = data["name"]
    return carrier
  except Exception as e:
    print(e)

  
def number_search():
  try:
    id = input('[>] Country Code: ')
    phone_number1 = input('[>] Phone number: ')
    plus = '+'
    g = plus+id+phone_number1
    print('[==================================]')
    print('[*] '+ getCarrier(phone_number1))
    phone_number = phonenumbers.parse(g)  
    print('[*] ' + geocoder.description_for_number(phone_number, 'en'))    
    print('[==================================]')
  except Exception as e:
    print(e)
    print('[==================================]')
    
def decode(arg):
  decode_data = base64.b64decode(arg)
  return decode_data
    
def encrypt(arg):
  message_bytes = arg.encode('ascii')
  base64_bytes = base64.b64encode(message_bytes)
  base64_message = base64_bytes.decode('ascii')
  return base64_bytes
    
  
def emailchoose():
    
    
    def log_send_email_gmail():
      server.starttls()

  
      username = input('[>] Gmail: ')
      
      if username == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
      elif username == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
      
      username = username+'@gmail.com'
      password = input('[>] Password: ')
    
      try:
        server.login(username, password)
        print(f'[*1 -L] Logged in {username}')
        print('[=====================================]')
      
      except Exception:
        print('[* -EOR-L]')
        print('[=====================================]')
        emailchoose()


      while True:
        to = input('[>] To: ')
        
        if to == '/rcps_many':
          
          to = [] # list to  store the inputs

          while True: 
            data = input('To: ') 
            if data == 'end': 
              break
            else:
              to.append(data) 
        
      
        if to == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
        elif to == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
          
        sub = input('[>] Subject:')
        mssg = input('[>] Message: ')
        
        if mssg == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
        elif mssg == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
          
        elif mssg == '/encrypt':
          user = input('[>] Message To Encrypt: ')
          f = encrypt(user)
          mssg = f
          print(f)
      
        mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
        
    
        server.sendmail(username, to, mssg)
        print(f'[*1 -S] {username} has sent a message to: {to}')
        print('[=====================================]')
    
# end Gmail code
  
  
    def log_send_email_icloud():
      server1.starttls()
  
      username = input('[>] Icloud: ')
      
      if username == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
      elif username == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
      
      username = username+'@icloud.com'
      password = input('[>] Password: ')
      try:
        server1.login(username, password)
        print(f'[*1 -L] Logged in {username}')
        print('[=====================================]')
    
      except Exception:
        print('[* -EOR-L] ')
        print('[=====================================]')
        emailchoose()
    


      while True:
        to = input('[>] To: ')
        
        if to == '/rcps_many':
          
          to = [] # list to  store the inputs

          while True: 
            data = input('To: ') 
            if data == 'end': 
              break
            else:
              to.append(data) 
          
          
        sub = input('[>] Subject:')
      
      if to == '/exit':
        print('[*E] Gmail Client has been killed')
        print('[=====================================]')
        emailchoose()
        
      elif to == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
      
      mssg = input('[>] Message: ')
      
      if mssg == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
      elif mssg == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
          
      elif mssg == '/encrypt':
        user = input('[>] Message To Encrypt: ')
        f = encrypt(user)
        mssg = f
        print(f)
      
      mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
      
    
      server1.sendmail(username, to, mssg)
      print(f'[*1 -S] {username} has sent a message to: {to}')
      print('[=====================================]')
    
# end Icloud code 
    def log_send_email_yahoo():
      server2.starttls()
  
      username = input('[>] Yahoo: ')
      
      if username == '/exit':
          print('[*E] Yahoo Client has been killed')
          print('[=====================================]')
          emailchoose()
        
      elif username == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
      
      username = username+'@yahoo.com'
      password = input('[>] Password: ')
      try:
        server1.login(username, password)
        print(f'[*1 -L] Logged in {username}')
        print('[=====================================]')
    
      except Exception:
        print('[* -EOR-L] ')
        print('[=====================================]')
        emailchoose()
    


      while True:
        to = input('[>] To: ')
        
        if to == '/rcps_many':
          
          to = [] # list to  store the inputs

          while True: 
            data = input('To: ') 
            if data == 'end': 
              break
            else:
              to.append(data) 
          
          
        sub = input('[>] Subject:')
      
      if to == '/exit':
        print('[*E] Yahoo Client has been killed')
        print('[=====================================]')
        emailchoose()
        
      elif to == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
      
      mssg = input('[>] Message: ')
      
      if mssg == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
      elif mssg == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
          
      elif mssg == '/encrypt':
        user = input('[>] Message To Encrypt: ')   
        f = encrypt(user)
        mssg = f
        print(f)
      
      mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
    
      server1.sendmail(username, to, mssg)
      print(f'[*1 -S] {username} has sent a message to: {to}')
      print('[=====================================]')
    

      
      
# choose email service

    client = input('[>] Choose Email Client: ')

    if client == '1':
      try:
        global server
        server = smtplib.SMTP(gmail, port)
        print(f'[*1 -C] Connected to {gmail} on port: 587')
        print('[=====================================]')
        log_send_email_gmail()
      except Exception:
        print('[* -EOR-C] ')
        emailchoose()
  
  
    
    elif client == '2':
      try:
        global server1
        server1 = smtplib.SMTP( apple, port )
        print(f'[*1 -C] Connected to {apple}on port: 587')
        print('[=====================================]')
        log_send_email_icloud()
      
      except Exception:
        print('[* -EOR-C]  ')
        print('[=====================================]')
        emailchoose()
    
  
    elif client == '3':
      try:
        global server2
        server2 = smtplib.SMTP(yahoo, port)
        print(f'[*1 -C] Connected to {yahoo} on port 465')
        log_send_email_yahoo()
      except Exception:
        print('[* -EOR-C]')
        print('[=====================================]')
        emailchoose()
    
  
    elif client == '/help':
      print(help)
      emailchoose()
   
    elif client == '/exit':
      print('[*E] pymail killed')
      sys.exit()
    
    elif client.lower() == '':
      emailchoose()
    
    elif client == "/info EOR-C":
      print("[*] if you get this error check internet connection")
      emailchoose()
      
    elif client == "/info EOR-L":
      print("[*] Log in errors are generaly because you havent allowed a 'less secure app' to connect to your email")
      emailchoose()
      
    elif client == "/info syscode":
      print(syscode)
      emailchoose()
      
    elif client == "/info pymail":
      print(pymail)
      emailchoose()
      
    elif client == '/sms':
      print(sms)
      emailchoose()
    
    elif client == '/test':
      test()
      emailchoose()
      
    elif client == '/info num':
      number_search()
      emailchoose()
      
    elif client == '/decode':
      user = input('[>] Decode Message: ')
      f = decode(user)
      print(f'[*] Decrpted Message: {f}')
      emailchoose()
  
  
emailchoose()



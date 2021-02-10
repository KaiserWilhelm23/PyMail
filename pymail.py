import smtplib
import sys

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
      
        mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
        if mssg == '/exit':
          print('[*E] Gmail Client has been killed')
          print('[=====================================]')
          emailchoose()
        
        elif mssg == '/exit all':
          print('[*E] pymail Client has been killed')
          print('[=====================================]')
          sys.exit()
    
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
      
      mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
      if mssg == '/exit':
        print('[*E] Gmail Client has been killed')
        print('[=====================================]')
        emailchoose()
        
      elif mssg == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
    
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
        print('[*E] Yahoo Client has been killed')
        print('[=====================================]')
        emailchoose()
        
      elif to == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
      
      mssg = input('[>] Message: ')
      
      mssg = 'Subject: {}\n\n{}'.format(sub, mssg)
      
      if mssg == '/exit':
        print('[*E] Yahoo Client has been killed')
        print('[=====================================]')
        emailchoose()
        
      elif mssg == '/exit all':
        print('[*E] pymail Client has been killed')
        print('[=====================================]')
        sys.exit()
    
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
  
  
emailchoose()



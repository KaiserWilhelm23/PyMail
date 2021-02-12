# PyMail
A python program written with smtplib to send emails and use the sms-gateway

# Requirments
- Python 3.6 or higher
- smtplib
- sys
- phonenumbers

to get phonenumbers on windows:
``` pip install phonenumbers```

to get phonenumbers on linux distros:
``` pip3 install phonenumbers```


NOTE: All modules come with python except "phonenumbers"

# Usage [sending emails]
Sending a email to one person

```
[>] To: email@domain.com
[>] Subject:m anything
[>] Message: anything
```

Sending email to multiple recipents:

```
[>] To: /rcps_many
To: user1@domain.com
To: user2@domain.com
To: user3@domain.com
To: end
[>] Subject:anything
[>] Message: anything
```

# Usage [sending sms messages]

Sending a text message to one person

```
[>] To: number@domain.com
[>] Subject:m anything
[>] Message: anything
```

Sending text messages to multiple recipents:

```
[>] To: /rcps_many
To: number1@domain.com
To: number2@domain.com
To: number3@domain.com
To: end
[>] Subject:anything
[>] Message: anything
```
# Help commands:
```
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
    
```

This program helps to send sms notification to specified mobile.

Pre-Requisite : 
    - Twilio account, Its Account, Token And Moblile number.
    OR
    - way2sms account, its apikey & secret code.

Usage : 
<pre>
1. To use way2sms for sending sms set below environement variable.
     way2sms=True
     apikey=<API KEY of way2sms account>
     secret=<Secret of way2sms account>
     
     Windows syntax : set <Environment Variable name>=<Value>
     Linux syntax   : export <Environment variable name>=<Value> 
    OR
    To use Twilio account specfiy twilio detials config.json in file encoded using base64.b64encode()
2. Using Program to send sms.
   python sendSms.py [Message needs to be sent]
3. Using module in other script to nofiy via sms.
    from nofiySms import sendSms
    sendSms.send_sms("Message body",[To Number])
</pre>
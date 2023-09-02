from twilio.rest import Client
acc = 'YourTwilioAccess'
tok = 'YourTwilioToken'
client = Client(acc,tok)
call = client.calls.create(
     twiml='<Response><Say>Hello Adarsh, this is luffy i just wanna say i am gonna be king of pirates</Say></Response>',
     to='+919320333578',
     from_='+14065057207'
     )
print(call.sid) 

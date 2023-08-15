from twilio.rest import Client
acc = 'AC835f868c368001b858f11dc6a999c544'
tok = '40c29c764ee9ce2f2af7e6dbf525e014'
client = Client(acc,tok)
call = client.calls.create(
     twiml='<Response><Say>Hello Adarsh, this is luffy i just wanna say i am gonna be king of pirates</Say></Response>',
     to='+919320333578',
     from_='+14065057207'
     )
print(call.sid) 
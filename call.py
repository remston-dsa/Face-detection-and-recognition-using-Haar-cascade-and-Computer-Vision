import os
from twilio.rest import Client
account_sid="**********************************"
auth_token="********************************"
client=Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+91XXXXXXXXXX',
                        from_='+1XXXXXXXXXX'
                    )

print(call.sid)

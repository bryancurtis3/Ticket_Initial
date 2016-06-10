"""
from twilio.rest import Client

account_sid = "ACfff41970ce6b32bfd79415faf2455d3d" # Your Account SID from www.twilio.com/console
auth_token  = "08eee0fc2c0bebf2132ddeaaaf173576"  # Your Auth Token from www.twilio.com/console

client = Client(account_sid, auth_token)

message = client.messages.create(to="+14232404107", 
    from_="+14232914011",
    body="A new support ticket is available!")

print(message.sid)
"""




"""

if "totalunresolveditems" in line[x]:
    sep = 'totalunresolveditems='
    unresolved = line[n].split(sep, 1)[1]

    for dig in range(len(unresolved)):
        if unresolved[dig].isdigit() == False:
            unresolved[dig] = ''
"""


#from kayako import Ticket, TicketAttachment, TicketNote, TicketPost, TicketPriority, TicketStatus, TicketType
from kayako import KayakoAPI
API_URL = 'https://support.fused.com/api/'
API_KEY = '0b85616f-556b-8234-6146-acafbe3d5552'
SECRET_KEY = 'NDMwMGFiZDEtZmJiMC02NDE0LTE5MjMtNDJlMzI4MzExNmViODE2ZjUwMzMtMDA0Ny1lMmE0LTI5OGItZTg5ZjI1M2NkZTFh'
api = KayakoAPI(API_URL, API_KEY, SECRET_KEY)


print(api.get_all(TicketCount))
#print(api.get_all(Ticket, 5, ticketstatusid=4))







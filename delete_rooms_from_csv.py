import requests

def sendDELETE(url):
    response = requests.delete(url,
                           headers={"Accept" : "application/json",
                                    "Content-Type":"application/json",
                                    "Authorization": "Bearer "+bearer})
    return response

bearer = "BEARER_TOKEN" #your bearer token
filepath = "rooms.csv" #each roomId on a new line.

lines = []
with open(filepath, 'r') as f:
    lines = f.readlines()

delete_url = 'https://api.ciscospark.com/v1/rooms/{0}'
failure = False
for line in lines[1:]:#basically, this is 'for every ID in the list'
    room_id = line.strip('\r\n')
    print("RoomId to delete is: {0}".format(room_id)) #we'll just print this roomId.
    print("Deleting room...")
    result = sendDELETE(delete_url.format(room_id))
    print("Delete result (204 is success): {0}".format(result.status_code))

import httplib, urllib, json,  random, sys, ConfigParser

#def getData(auth_string, id):
def getData():
    global auth_token
    s = random.randint(100000, 1000000)
    id_str = str(s)
    conn = httplib.HTTPSConnection("api.genius.com")
    request_uri = "/songs/" + id_str
    headersMap = {
            "User-Agent": "CompuServe Classic/1.22",
            "Accept": "application/json",
            "Authorization": "Bearer " + auth_token
    }
    conn.request("GET", request_uri, headers=headersMap)
    response = conn.getresponse()
    ### Output the HTTP status code and reason text...
    #print response.status, response.reason
    data = response.read()
    result = json.loads(data)

    output = "[" + id_str + "] "
    if response.status == 200:
        title = result["response"]["song"]["full_title"]
        song_uri = result["response"]["song"]["path"]
        return title
        print "[" + id_str + "] " + title + "\nLink: https://genius.com" + song_uri + "\n"
    else:
        if response.status == 404:
           #Just in case the song was not found, try again recursively and then continue with the for-loop
           getData()
        else:
           print "unknown error: " + str(response.status) +  " "  + str(response.reason)

#Copy auth.cfg.sample to auth.cfg and fill in your auth token
Config = ConfigParser.ConfigParser()
Config.read('auth.cfg')
auth_token = Config.get('Auth', 'Token')

#if no argument (count) is given, set default to 1
c = 0
if (len(sys.argv) == 1):
    c = 1
else:
    c = int(sys.argv[1])

#Concerning the docs, the song id is a 6-digit number
for i in range(0, c):
    getData()

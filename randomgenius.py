import requests, json, random, sys, configparser

#def getData(auth_string, id):
def getData():
    global auth_token
    s = random.randint(100000, 1000000)
    id_str = str(s)
    request_url = "http://api.genius.com/songs/" + id_str
    headersMap = {
            "User-Agent": "CompuServe Classic/1.22",
            "Accept": "application/json",
            "Authorization": "Bearer " + auth_token
    }
    response = requests.get(request_url, headers=headersMap)
    ### Output the HTTP status code and reason text...
    #print response.status, response.reason
    result = json.loads(response.content)
    output = "[" + id_str + "] "
    if response.status_code == 200:
        title = result["response"]["song"]["full_title"]
        song_uri = result["response"]["song"]["path"]
        if not title:
            return getData()
        return title
    else:
        return getData()

#Copy auth.cfg.sample to auth.cfg and fill in your auth token
Config = configparser.ConfigParser()
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

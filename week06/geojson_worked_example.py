import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Please enter location: ")
    if (len(address) < 1):
        break
    
    url = serviceurl + urllib.parse.urlencode(
        {"address": address}
    )
    print("Retrieving:", url)
    
    data = urllib.request.urlopen(url).read().decode()
    print("Retrieving", len(data), "characters")
    
    try:
        js = json.loads(data)
    except:
        js = None
        
    if js is None or "status" not in js or js["status"] != "OK":
        print("Retrieving failed")
        print(js)
        continue
    
    print(json.dumps(js, indent=4))
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat:", lat, "lng:", lng)
    location = js["results"][0]["formatted_address"]
    print("location:", location)
import re
import urllib.request

#https://www.weather-forecast.com/locations/Paris/forecasts/latest

city=input("Enter your city:")

url="https://www.weather-forecast.com/locations/"+ city +"/forecasts/latest"

data=urllib.request.urlopen(url).read()
data1=data.decode("utf-8")

#print(data1)

m=re.search('span class="phrase">',data1)

start=m.end()

end=start+200

new=data1[start:end]

#print(new)

m=re.search("</span>",new)

end=m.start()-1

final=new[0:end]

print(final)

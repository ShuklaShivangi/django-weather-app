from django.shortcuts import render

import urllib.request
import json
import pycountry

def get_country_name(country_code):
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name if country else country_code
    except Exception as e :
        return country_code

def index(request):
    if request.method == 'POST' :
        city = request.POST['city']
        source = urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=en&lang=hi&units=metric&lat=33.44&lon=-94.04&exclude=hourly,daily&appid=f829db39e10f7b3981e6708a37bdae17'
).read()


# 'https://api.openweathermap.org/data/3.0/weather?q={}&lang=en&lang=hi&units=metric&lat=33.44&lon=-94.04&exclude=hourly,daily&appid=f829db39e10f7b3981e6708a37bdae17'

        
        list_of_data = json.loads(source)

        country_code = list_of_data['sys']['country']
        country_name = get_country_name(country_code)

        data = {
            "place_name"     : str(list_of_data['name']),
            "country_code"   : country_name,
            "temp"           : str(list_of_data['main']['temp']),
            "pressure"       : str(list_of_data['main']['pressure']),
            "humidity"       : str(list_of_data['main']['humidity']),
            "main"           : str(list_of_data['weather'][0]['main']),
            "icon"           : (list_of_data['weather'][0]['icon']),
        }
        print(data)

    else :
        data = {}

    return render(request,"main/index.html" , data)



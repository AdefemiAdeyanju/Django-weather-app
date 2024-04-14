from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method =='POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7e3146eb4307d23ce87b589140a476c5').read()
        json_data = json.loads(res)
        data = {
            'temp': str(json_data['main']['temp'])+'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),
        }
    else:
        city=''
        data = {}
    return render(request, 'index.html', {'city':city, 'data':data})
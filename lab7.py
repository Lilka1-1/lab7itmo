import json, requests 

def city_weather():
    city_name = 'Paris'
    key = '7e4f09b0c528f83e8a67a0338b9aedce'
    response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
    result = json.loads(response.text)
    print(f"Погода в городе {city_name}:\nТемпература: {result['main']['temp']-273:.1f}\nВлажность: {result['main']['humidity']}\nДавление: {result['main']['pressure']}")

def iss_info():
    iss = requests.get("http://api.open-notify.org/iss-now.json").json()
    astros = requests.get("http://api.open-notify.org/astros.json").json()


    pos = iss['iss_position']
    print(f" МКС: {pos['latitude']}°, {pos['longitude']}°")
    print(f" Экипаж: {astros['number']} человек")

    for p in astros['people']:
        print(f"   - {p['name']} ({p['craft']})")



if __name__ == '__main__':
    city_weather()
    print()
    iss_info()

   
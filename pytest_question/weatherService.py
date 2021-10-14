import requests

# a very simple version of the weather getter
def TempGetter(city):
        url_template = (
            'http://api.openweathermap.org/data/2.5/'
            'weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1')
        response = requests.get(url_template.format(city))
        return response.json()

if __name__ == '__main__':
    w = TempGetter('Athlone')
    print(w)

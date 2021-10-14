from threading import Thread
import json
import requests
import time

class MyWorkerThread(Thread):
    CITIES = ['Athlone', 'Dublin', 'Galway', 'Belfast', 'London', 'Cork', 'Lund', 'Kista']
    def __init__(self, city):
        Thread.__init__(self)        
        self.city = city

    def run(self):
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=48f2d5e18b0d2bc50519b58cce6409f1'.format(self.city))
        data = json.loads(response.text)       
        self.temperature = data['main']['temp'] 
        self.description = data['weather'][0] ['description']
        self.speed = data['wind']['speed'] 

        print ('Temperate = {}, Description = {}, speed = {}'.format(self.temperature, self.description, self.speed))

def main():   
    threads = [MyWorkerThread(city) for city in MyWorkerThread.CITIES]
    t0 = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    t1 = time.time()
    print('Execution took {} seconds for threads {}'.format((t1-t0), len(threads)))    

if __name__ =='__main__':
    main()
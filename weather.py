from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

place = input('Укажите город:')
config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('4b9ea152afe596ebd2d2f89f9084d3f8', config_dict)

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)#Локация в которой надо узнать погоду 
w = observation.weather
temperature = w.temperature('celsius')['temp']#Показывает температуру в цельсиях 
pogoda = w.detailed_status #Показывает погоду на данный момент 

print ('В городе ' + place + ' сейчас : ' + str(temperature) + ' градусов.\nВ городе ' + pogoda + '.\nХорошего дня!')

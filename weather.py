from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

place = input('Specify city:')
config_dict = get_default_config()
config_dict['language'] = 'en'
owm = OWM('4b9ea152afe596ebd2d2f89f9084d3f8', config_dict)

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temperature = w.temperature('celsius')['temp']
pogoda = w.detailed_status 

print ('In city' + place + ' now : ' + str(temperature) + ' degrees.\nIn city ' + pogoda + '.\nGood day!')

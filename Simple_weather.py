#Simple weather
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('dbb542714624b3d6d31350a48b5100b2')
mgr = owm.weather_manager()

place = input("В какой стране/городе?: ")

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']

print("В городе " + place + " сейчас " + w.detailed_status )
print("Температура сейчас примерно около " + str(temp))

if temp < 10:
    print("На улице сейчас довольно холодно, советую оставаться дома.")
    
elif temp < 20:
    print("На улице сейчас прохладно, одевайтесь пожалуйста потеплее")

else:
    print("Температура норм, кэп! Можно смело гулять!")

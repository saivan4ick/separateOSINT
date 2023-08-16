import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from rich.progress import track
import time
def phone_osint():
	for n in track(range(100), description="Идет процесс загрузки / Download process in progress..."):
		time.sleep(0.07)
	number = input('Введите номер телефона: ')
	phoneNumber = phonenumbers.parse(number) 
	carrier = carrier.name_for_number(phoneNumber, 'ru')
	reg = geocoder.description_for_number(phoneNumber, 'ru') 
	timeZone = timezone.time_zones_for_number(phoneNumber)
	valid = phonenumbers.is_valid_number(phoneNumber)
	print(valid)
	if valid:
		print(carrier)
		print(reg)
		print(timeZone)
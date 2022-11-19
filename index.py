import  phonenumbers
from  phonenumbers import  timezone,geocoder,carrier


numbers=input("Entered the number  : ")

phone=phonenumbers.parse(numbers)

time=timezone.time_zones_for_number(phone)

sim=carrier.name_for_number(phone,"en")

registration=geocoder.description_for_number(phone,"en")


print(numbers)
print(phone)
print(time)
print(sim)
print(registration)


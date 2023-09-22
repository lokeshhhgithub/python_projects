import phonenumbers
from phonenumbers import timezone,carrier, geocoder

num = input('Enter your number: ')
phone = phonenumbers.parse(num)
print(phone)
print(timezone.time_zones_for_number(phone))
print(carrier.name_for_number(phone,"en"))
print(geocoder.description_for_number(phone, "en"))

































# import phonenumbers

# from phonenumbers import timezone, carrier,geocoder

# number = input("Enter your number:   ")
# phone = phonenumbers.parse(number)
# time = timezone.time_zones_for_number(phone)
# car = carrier.name_for_number(phone, "en")
# reg = geocoder.description_for_number(phone,"en")
# print(phone)
# print(time)
# print(car)
# print(reg)



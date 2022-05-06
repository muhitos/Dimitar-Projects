import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

number = "YOUR PHONE NUMBER"

ch_number = phonenumbers.parse(number, "CH")
service_number = phonenumbers.parse(number, "RO")

print(geocoder.description_for_number(ch_number, "en"))
print(carrier.name_for_number(service_number, "en"))

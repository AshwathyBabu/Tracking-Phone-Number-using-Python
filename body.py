#imports the phone number you want to track to the body.py file
import phonenumbers
from text import number

#It provides geographical coordinates corresponding to a location
from phonenumbers import geocoder, carrier

#history of the phone number from its country by parsing two parameters. CH -> Country History
ch_number= phonenumbers.parse(number,"CH")

# You want the info to display in English
print(geocoder.description_for_number(ch_number, "en"))

#Carrier is a function. It helps you get the name of the service provider of the phone number you’re tracking
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))
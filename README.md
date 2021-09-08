# track_ph_num_loc
Printing the phone number country and the network provider name. Src: https://python.plainenglish.io/how-to-track-phone-number-location-with-python-526bbf06c89e

1. import the module phonenumbers, whihc imports the phone number you want to track to the body.py file
2. The numberr which needs to be tracked specifically can be added in the text.py file along with the country code
3. we will import geocoder and carrier functions from phonenumders module
4. We get the history of the phone number from its country by parsing two parameters. "CH" -> Country History, and the inforamtion needs to be displayed in English
5. Carrier is a function which helps you get the name of the service provider of the phone number you’re tracking. RO stands for Romania in ISO Alpha-2 which are basically Codes for the representation of names of countries 

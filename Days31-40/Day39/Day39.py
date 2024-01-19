import os
import requests
import smtplib
from datetime import datetime
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

#This file will need to use the DataManager, FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# ---------- VARIABLES ---------- #
dataManager = DataManager()
flightSearch = FlightSearch()
flightData = FlightData()

# Berlin	BER																								
# Switzerland	ZRH																								
# Sydney	SYD																								
# Auckland	AKL																								
# Christchurch	CHC																								
# Wellington	WLG																								
# Queenstown	ZQN																								
# Hawaii	LIH	

flightData.checkPricetoSheet()

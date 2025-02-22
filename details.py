import amadeus
from amadeus import Client,ResponseError
from dotenv import load_dotenv
import os

load_dotenv()

class utils:

    def __init__(self):

        self.api_key=os.getenv('amadeus_id')
        self.api_secret=os.getenv('amadeus_secret')

        self.client=Client(
            client_id=self.api_key,
            client_secret=self.api_secret
        )

    def iATA(self,place):
        responce=amadeus.reference_data.locations.get(
            keyword=place,
            subType='CITY'
        )
        return responce.data[0]['iataCode'],responce.data[0]['geoCode']
    
    def getFlights(self,From,destination,date,adults,childs):
        try:
            responce=amadeus.shopping.flight_offers_search.get(
                originLocationCode=From,
                destinationLocationCode=destination,
                departureDate=date,
                adults=adults,
                children=childs,
                max=3
            )
            flights=responce.data
            fl=[]
            for flight in flights:
                fl.append(flight['itineraries'])
            return fl
        
        except ResponseError as e:
            print(e)
    
    def getHotels(self,city):
        try:
            responce=amadeus.shopping.hotel_offers_search.get(
                cityCode=city
            )
            hotels=responce.data[:5]
            hot=[]
            for hotel in hotels:
                hot.append(hotel)
            return hot
        except ResponseError as e:
            print(e)

    def geTSpots(self,lat,long):
        pass
            
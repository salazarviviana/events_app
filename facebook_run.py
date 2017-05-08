import facebook
import requests
import os
import json

from dotenv import load_dotenv, find_dotenv     # Enviroment to hide the facebook access token
load_dotenv(find_dotenv())


#funtion to create lists base on the value on a key in a list of dictionaries
def create_list(listOfDicts, key):
    new_list = []
    for subVal in listOfDicts:
        if key in subVal:
            new_list.append(subVal[key])
    return new_list

event_ids = []

def search_events(city, num_results):
	graph = facebook.GraphAPI(access_token= os.environ['FACEBOOK_ACCESS_TOKEN'])  #Facebook initiator
	events_search = graph.request("search",{ 'q' : city, 'type' : 'event', 'limit' : num_results}) # performs the search of events
	events_search_list = events_search['data']  # stores the search in a list 
	event_ids = create_list(events_search_list, 'id') # creates a list of event ID for the get.objects method
	events_info = graph.get_objects(ids= event_ids, fields='interested_count,name,start_time,place') # list of dicts with only relevant info. Source https://facebook-sdk.readthedocs.io/en/latest/api.
	sorted_list = sorted(events_info.items(), key=lambda x: x[1]['interested_count'], reverse=True) # sort a dict of dicts. Source: Stackoverflow
	return sorted_list

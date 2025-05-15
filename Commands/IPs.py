import json
import socket
import os

# This script fetches the IP address of a list of websites and saves the information in a JSON file.
webinfo = {}
sites = ["google.com", "youtube.com", "facebook.com", "instagram.com", "whatsapp.com",
"web.whatsapp.com","amazon.in", "amazon.com", "flipkart.com", "wikipedia.org", "twitter.com",
"linkedin.com", "quora.com", "hotstar.com", "netflix.com", "amazonprimevideo.com",
"cricbuzz.com", "ndtv.com", "zomato.com", "swiggy.com", "snapdeal.com", "irctc.co.in",
"redbus.in", "makeinindia.gov.in", "sarkariresult.com", "canva.com", "search.brave.com"]







# # Save the information to a JSON file
# with open (f"{os.getcwd()}//Address.json", 'w') as file:
#     json.dump(webinfo, file, indent=4)

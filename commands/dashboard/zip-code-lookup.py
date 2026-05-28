#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Zip Code Lookup
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 📍

# Documentation:
# @raycast.author Kailash Yellareddy
# @raycast.authorURL https://github.com/kyellareddy
# @raycast.argument1 { "type": "text", "placeholder": "ZIP code", "optional": false }

from uszipcode import SearchEngine

import sys

engine = SearchEngine()
zipcode = engine.by_zipcode(sys.argv[1])

input = sys.argv[1]

military_states = {
    "AE": "Armed Forces Europe",
    "AP": "Armed Forces Pacific",
    "AA": "Armed Forces Americas"
}
military_cities = {
    "Apo": "Army/Air Force Post Office",
    "Fpo": "Fleet Post Office",
    "Dpo": "Diplomatic Post Office"
}
if zipcode and zipcode.zipcode:
    state = zipcode.state
    city = zipcode.major_city

    if city in military_cities:
        print(military_cities[city])
    else:
        print("City:", city)

    if zipcode.county:
        print("County:", zipcode.county)

    if state in military_states:
        print(military_states[state])
    else:
        print("State:", state)
else:
    print("Zip code not found.")

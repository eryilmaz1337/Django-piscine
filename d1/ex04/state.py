import sys
def capital_city(name):
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    val = ""
    for key, value in capital_cities.items():
        if value == name:
            val = key

    for key, value in states.items():
        if value == val:
             print(key)
    if (val == ""):
        print("Unknown state")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        capital_city(sys.argv[1])
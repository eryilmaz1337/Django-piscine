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

    try:
        capital_city = capital_cities[states[name]]
        print(capital_city)
    except KeyError:
        print("Unknown state")

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        capital_city(sys.argv[1])
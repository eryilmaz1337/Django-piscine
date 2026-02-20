import antigravity
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py <latitude> <longitude> <precision>")
        return
    
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3].encode('utf-8') # byte çeviriyoruz fonk öyle bekliyor
        antigravity.geohash(latitude, longitude, datedow)

    except ValueError:
        print("Error: Invalid input")
        return
    except Exception as e:
        print("Error: " + str(e))
        return

if __name__ == "__main__":
    main()
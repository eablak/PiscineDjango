import sys
import antigravity

if __name__ == "__main__":
    
    args = sys.argv
    
    if len(args) == 5:
        try:
            latitude = float(args[1])
            longitude = float(args[2])
        except ValueError as error:
            print(error, "\nlatitude and longitude must be float")
            sys.exit(1)

        date = args[3]
        dow = args[4]
        datedow = date + "-" + dow
        datedow = datedow.encode("utf-8")

        antigravity.geohash(latitude, longitude, datedow)
    else:
        print("use like latitude, longitude, date, dow_jones")

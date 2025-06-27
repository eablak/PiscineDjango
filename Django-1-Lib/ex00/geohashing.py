import sys
import antigravity

def main():
    if len(sys.argv) == 5:
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
        except ValueError as error:
            print(error, "\nlatitude and longitude must be float")
            sys.exit(1)

        date = sys.argv[3]
        dow = sys.argv[4]
        datedow = date + "-" + dow
        datedow = datedow.encode("utf-8")

        antigravity.geohash(latitude, longitude, datedow)
    else:
        print("use like latitude, longitude, date, dow_jones")


if __name__ == "__main__":
    main()
    
    
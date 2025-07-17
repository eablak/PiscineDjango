import sys
import antigravity

def main():
    if len(sys.argv) == 4:
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
        except ValueError as error:
            print(error, "\nlatitude and longitude must be float")
            sys.exit(1)

        date_dow = sys.argv[3]
        date_dow = date_dow.encode("utf-8")

        antigravity.geohash(latitude, longitude, date_dow)
    else:
        print("use like latitude, longitude, date_dow")


if __name__ == "__main__":
    main()
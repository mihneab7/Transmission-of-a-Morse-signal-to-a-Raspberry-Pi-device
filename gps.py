import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

for line in lines:
    try:
        data = line.split(",")
        if data[0] == '$GPGLL':
            # Convert NMEA data to decimal
            nmeaLatitude = data[1]
            # Get the first 2 digits
            latitudeDegrees = nmeaLatitude[:2]
            # Check the hemishpere
            if data[2] == 'S':
                # Turn the string into a float in order to multiply by -1 if necessary
                laitudeDegrees2 = float(latitudeDegrees) * -1
            else:
                laitudeDegrees2 = float(latitudeDegrees)
            # Conversion to float add .0, so convert back to string and remove it
            laitudeDegrees2 = str(laitudeDegrees2).strip('.0')
            # Get the rest of the digits
            # DDMM.MMMM format
            latitudeActualDegrees = nmeaLatitude[2:10]
            latitudeMinutes = float(latitudeActualDegrees) / 60
            latitudeMinutes = str(latitudeMinutes).strip('.0')[:8]
            latitude = laitudeDegrees2 + "." + latitudeMinutes

            nmeaLongitude = data[3]
            longitudeDegrees = nmeaLongitude[0:3]
            if longitudeDegrees[0] == "0":
                longitudeDegrees = longitudeDegrees[1:]
            if data[4] == 'W':
                longitudeDegrees2 = float(longitudeDegrees) * -1
            else:
                longitudeDegrees2 = float(longitudeDegrees)
            longitudeDegrees2 = str(longitudeDegrees2).strip('.0')
            longitudeActualDegrees = nmeaLongitude[3:10]
            longitudeMinutes = float(longitudeActualDegrees) / 60
            longitudeMinutes = str(longitudeMinutes).strip('0.')[:8]
            longitude = longitudeDegrees2 + "." + longitudeMinutes
            print("Longitude: " + longitude + " Latitude: " + latitude)
            file2 = open("coordinates.txt", 'w')
            file2.write(longitude)
            file2.write(" ")
            file2.write(latitude)
    except Exception:
        print("The data acquired by the GPS module is not usable.")

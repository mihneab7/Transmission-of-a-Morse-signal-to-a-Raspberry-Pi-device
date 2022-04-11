import sys

file = open(sys.argv[1], 'r')
lines = file.readlines()

for line in lines:
    try:
        data = line.split(",")
        if data[0] == '$GPGLL':
            # Convert NMEA data to decimal
            lat_nmea = data[1]
            # Get the first 2 digits
            lat_degrees = lat_nmea[:2]
            # Check the hemishpere
            if data[2] == 'S':
                # Turn the string into a float in order to multiply by -1 if necessary
                latitude_degrees = float(lat_degrees) * -1
            else:
                latitude_degrees = float(lat_degrees)
            # Conversion to float add .0, so convert back to string and remove it
            latitude_degrees = str(latitude_degrees).strip('.0')
            # Get the rest of the digits
            # DDMM.MMMM format
            lat_dd = lat_nmea[2:10]
            lat_mmm = float(lat_dd) / 60
            lat_mmm = str(lat_mmm).strip('.0')[:8]
            latitude = latitude_degrees + "." + lat_mmm

            long_nmea = data[3]
            long_degrees = long_nmea[0:3]
            if long_degrees[0] == "0":
                longDegrees = long_degrees[1:]
            if data[4] == 'W':
                longitude_degrees = float(long_degrees) * -1
            else:
                longitude_degrees = float(long_degrees)
            longitude_degrees = str(longitude_degrees).strip('.0')
            long_ddd = long_nmea[3:10]
            long_mmm = float(long_ddd) / 60
            long_mmm = str(long_mmm).strip('0.')[:8]
            longitude = longitude_degrees + "." + long_mmm
            print("Longitude: " + longitude + " Latitude: " + latitude)
            file2 = open("coordinates.txt", 'w')
            file2.write(longitude)
            file2.write(" ")
            file2.write(latitude)
    except Exception:
        print("The data acquired by the GPS module is not usable.")

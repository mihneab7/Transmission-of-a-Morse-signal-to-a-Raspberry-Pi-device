import serial

try:
    gps = serial.Serial('com3', baudrate = 9600)

    while True:
        ser_bytes = gps.readline()
        # print(ser_bytes)
        decoded_bytes = ser_bytes.decode("utf-8", "ignore")
        # print(decoded_bytes)
        data = decoded_bytes.split(",")
        # print(data)
        # if data[0] == '$GPRMC':
        #     print(data)
        #     lat_nmea = data[3]
        #     lat_degrees = lat_nmea[:2]
        #     if data[6] == 'S':
        #         latitude_degrees = float(lat_degrees) * -1
        #     else:
        #         latitude_degrees = float(lat_degrees)
        #     latitude_degrees = str(latitude_degrees).strip('.0')
        #     lat_ddd = lat_nmea[2:10]
        #     lat_mmm = float(lat_ddd) / 60
        #     lat_mmm = str(lat_mmm).strip('.0')[:8]
        #     latitude = latitude_degrees + "." + lat_mmm
        #
        #     long_nmea = data[5]
        #     long_degrees = long_nmea[1:3]
        #     if data[6] == 'W':
        #         longitude_degrees = float(long_degrees) * -1
        #     else:
        #         longitude_degrees = float(long_degrees)
        #     longitude_degrees = str(longitude_degrees).strip('.0')
        #     long_ddd = long_nmea[3:10]
        #     long_mmm = float(long_ddd) / 60
        #     long_mmm = str(long_mmm).strip('0.')[:8]
        #     longitude = longitude_degrees + "." + long_mmm
        #     print("Longitude: " + longitude + "Latitude: " + latitude)

except serial.SerialException:
    print("There's no GPS connected.")
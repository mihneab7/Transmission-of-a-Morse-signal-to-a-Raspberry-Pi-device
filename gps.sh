echo "" > gpslog.txt
echo "" > coordinates.txt
while true;
do $(cat /dev/ttyUSB0 > gpslog.txt)
done


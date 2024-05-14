import serial
import csv
import os
from datetime import datetime

# Replace '/dev/ttyUSB0' with your actual device file
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# File path
file_path = '/home/mithun/Desktop/serial_data.csv'

# Check if the file already exists
file_exists = os.path.isfile(file_path)

# Open a CSV file for appending
with open(file_path, mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header only if the file is new
    if not file_exists:
        writer.writerow(['Timestamp', 'Channel', 'Value1', 'Value2', 'Value3', 'Value4'])
    
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if line:  # Check if the data is not empty
                # Parse the line assuming the format 'A:;0.00;;;'
                parts = line.split(';')
                if len(parts) >= 5:  # Ensure there are enough parts
                    data_type = parts[0]
                    value1 = parts[1]
                    value2 = parts[2]
                    value3 = parts[3]
                    value4 = parts[4]
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    writer.writerow([timestamp, data_type, value1, value2, value3, value4])
                    print(f"{timestamp}: {data_type}, {value1}, {value2}, {value3}, {value4}")
                    file.flush()  # Ensure the data is written to the file

import obd

# Replace with your port (e.g., "COM3" on Windows, "/dev/ttyUSB0" on Linux/Mac)
port = "/dev/tty.usbserial-113011297675"  # Adjust this based on Step 3

# Create connection
connection = obd.OBD(port)

# Check connection status
print("Connection status:", connection.status())

# Test a basic command (e.g., RPM)
if connection.is_connected():
    response = connection.query(obd.commands.RPM)
    if not response.is_null():
        print("Engine RPM:", response.value)
    else:
        print("RPM command failed or not supported.")
else:
    print("Failed to connect to OBDLink SX.")
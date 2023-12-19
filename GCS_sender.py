import sys
sys.path.append("path/to/generated/mavlinkv2")
# This is where we put out new custom messages file.


# The custom_messages and MAVLink_rfid_control_message class has to be inspected in the .py file generated by the XML file after we put in the MavLink folder.
from custom_messages import MAVLink_rfid_control_message
from pymavlink import mavutil

# Connect to your vehicle or ground station
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')
master.wait_heartbeat()

# Function to send an RFID control command
def send_rfid_command(target_system, target_component, command):
    msg = MAVLink_rfid_control_message(target_system, target_component, command)
    master.mav.send(msg)

# Turn off reading from the RFID.
send_rfid_command(master.target_system, master.target_component, 0)

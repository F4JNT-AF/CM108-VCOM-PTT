import serial
import time
import atexit
import hid
import sys

#CONFIG
GPIO = 3 #PTT control pin GPIOX , where X should be 1,2,3,4 - GPIO3 on most devices
serial_port = "COM3"
delay_ms = 10 #delay (in ms) between two serial RTS/CTS check
CM108_VID = 0x0D8C
CM108_PID = 0x013C #some older chips may use 0x013A

message_PTT_start = [bytearray(b'\x00\x00\x01\x01\x00'),bytearray(b'\x00\x00\x02\x02\x00'),bytearray(b'\x00\x00\x04\x04\x00'),bytearray(b'\x00\x00\x08\x08\x00')]
PTT_status = False

ser = serial.Serial(serial_port, rtscts=True)

CM108_USB = hid.device()
CM108_USB.open(CM108_VID, CM108_PID)

print("Starting PTT monitoring.")

def exit_handler():
    ser.close()
    CM108_USB.close()

atexit.register(exit_handler)

while 1:
    cts_status = ser.cts

    if cts_status and not PTT_status:
        CM108_USB.write(message_PTT_start[GPIO-1])
        PTT_status = True
        print("PTT ON")

    if not cts_status and PTT_status:
        CM108_USB.write(bytearray(b'\x00\x00\x00\x00\x00'))
        PTT_status = False
        print("PTT OFF")    
    
    time.sleep(delay_ms/1000)

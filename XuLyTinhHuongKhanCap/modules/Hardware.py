import serial
import time

Opened_UART = 1
try:
    ser = serial.Serial('/dev/ttyUSB0', 115200)
    #ser.open()
    print(ser)
except serial.serialutil.SerialException:
    print("Cannot Find UART")
    Opened_UART = 0

def Call(SoDienThoai:str):
    n = "Call" + SoDienThoai
    if(Opened_UART):
        data = n.encode()
        print("Data gửi đi:", data)
        ser.write(n.encode())

def GetTemp():
    n = "GetTemp"
    if(Opened_UART):
        data = n.encode()
        print("Data gửi đi:", data)
        ser.write(n.encode())
        time.sleep(0.1)
        data_raw = ser.readline()
        data = str(ser.readline())
        print("Data nhận được: ", data)
        data = data.split('"')
        temp = float(data[1])
        print("Nhiệt độ: ", temp)


    
  
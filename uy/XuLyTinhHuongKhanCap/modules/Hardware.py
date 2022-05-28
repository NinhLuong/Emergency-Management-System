import serial
import time

Opened_UART = 1
try:
    ser = serial.Serial('COM5', 115200)
    #ser.open()
    print(ser)
except serial.serialutil.SerialException:
    print("Cannot Find UART")
    Opened_UART = 0

def Call(SoDienThoai:str):
    global Opened_UART
    try:
        if(Opened_UART):
            n = "Call" + SoDienThoai  
            data = n.encode()
            print("Data gửi đi:", data)
            ser.write(n.encode())  
    except serial.serialutil.SerialException:
        print("Cannot Find Device")
        Opened_UART = 0
    

def GetTemp():
    global Opened_UART
    try:
        n = "GetTemp"
        if(Opened_UART):
            data = n.encode()
            print("Data gửi đi:", data)
            ser.write(n.encode())
            time.sleep(0.1)
            data_raw = ser.readline()
            data = str(ser.readline())
            print("Data nhận được: ", data)
            if(data.find("Temp:") != -1):
                data = data.split('"')
                temp = float(data[1])
                print("Nhiệt độ: ", temp)
                return temp
            return -1
    except serial.serialutil.SerialException:
        print("Cannot Find Device")
        Opened_UART = 0


    
  
import socket
import time
from tkinter import *


s = socket.socket()
s.bind(('192.168.1.241', 502))
s.listen(1)
conn, addr = s.accept()
mes = b''


def Xminus():
    global mes
    mes = b'X-'


def Xplus():
    global mes
    mes = b'X+'


def Yminus():
    global mes
    mes = b'Y-'


def Yplus():
    global mes
    mes = b'Y+'


def Zminus():
    global mes
    mes = b'Z-'


def Zplus():
    global mes
    mes = b'Z+'    
    

root = Tk()
Button(text='  -  ', command=Xminus).place(x=10, y=10)
Button(text='  +  ', command=Xplus).place(x=80, y=10)
Label(text='X').place(x=55, y=10)
Button(text='  -  ', command=Yminus).place(x=10, y=40)
Button(text='  +  ', command=Yplus).place(x=80, y=40)
Label(text='Y').place(x=55, y=40)
Button(text='  -  ', command=Zminus).place(x=10, y=70)
Button(text='  +  ', command=Zplus).place(x=80, y=70)
Label(text='Z').place(x=55, y=70)


while True:
    send = mes + b'1\r\n'
    conn.send(send)
    data = conn.recv(1024)
    print(data)
    if data == b'Xok\r\n' or data == b'Yok\r\n' or data == b'Zok\r\n':
        mes = b''

    root.update()

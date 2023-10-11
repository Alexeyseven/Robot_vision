import socket
import time
from tkinter import *


s = socket.socket()
s.bind(('192.168.1.241', 502))
s.listen(1)
conn, addr = s.accept()
send_mes = False


def send():
    global send_mes
    send_mes = True


root = Tk()
X = IntVar()
Y = IntVar()
Label(text='X:').place(x=10, y=10)
Entry(textvariable=X).place(x=40, y=10)
Label(text='Y:').place(x=10, y=40)
Entry(textvariable=Y).place(x=40, y=40)
Button(text='Translate', command=send).place(x=70, y=70)


while True:
    if send_mes:
        conn.send(str.encode(f'{X.get()}') + b',' + str.encode(f'{Y.get()}') + b'\r\n')
    else:
        conn.send(b'j\r\n')
    data = conn.recv(1024)
    print(data)
    send_mes = False
    root.update()

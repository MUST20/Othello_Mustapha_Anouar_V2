import socket
import json


def receiveJSON(socket):
    fullreceive = False
    message = ''
    while not fullreceive:
        message += socket.recv(512).decode('utf8')
        try:
            data = json.loads(message)
            fullreceive = True
        except json.JSONDecodeError:
            pass
    return data

def sendJSON(socket, data):
    data = json.dumps(data).encode('utf8')
    totalsend = 0
    while totalsend < len(data):
        sent = socket.send(data[totalsend:])
        totalsend += sent

def subscribe(port,name):
    port = int(port)
    message = {"request": "subscribe","port": port,"name": name,"matricules": ["195150", ""]}
    s = socket.socket()
    s.connect(('localhost',3000))
    sendJSON(s, message)
    s.close()
    #boucle de réception de requêtes
    listening = True
    while listening == True:
        s = socket.socket()
        s.bind(('0.0.0.0', port))
        s.listen()
        client, address = s.accept()
        serverrequest = receiveJSON(client)
        if serverrequest['request'] == 'ping':
            sendJSON(client, {'response': 'pong'})
            listening = False


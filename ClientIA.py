import socket
import sys
from ConnectManager import sendJSON,receiveJSON,Timeout
from MoveManager import BestMove, possibleMoves


def SENDmove(server_request):
    try :
        PossibleMoves,PawnsDestroyed = possibleMoves(server_request)
        return {
                    "response": "move",
                    "move": BestMove(PossibleMoves,PawnsDestroyed),
                    "message": "good"
                }
    except Exception as e :
                    print("SendMoveError")
                    print(e)


if __name__ == '__main__':
    args = sys.argv[1:]

    print(args[0])
    client=socket.socket()
    client.connect(('localhost',3000))
#le client se connecte sur le port 3000	
    sendJSON(client,
        {
            "request": "subscribe",
            "port": args[0],
            "name": "MousAnouaIA",
            "matricules": ["195150", "195116"]
    })

#Le client envoie l'incription au serveur

    respond = receiveJSON(client)
#le client recoie OK	
    print('reponse1duserver= ' , respond['response'])
    s = socket.socket()
#le client crée une nouvelle socket et écoute le serveur
    s.bind(('0.0.0.0',int(args[0])))
    s.listen() 
#le client écoute le serveur et se connecte avec l'adresse IP & port
    print('le serveur est connecté')
    while True :
        try:
            server, addressServer = s.accept()

            respond = receiveJSON(server,10)

            rep=respond['request']
            print('requete serveur= ',rep)
            try:
                if rep == 'ping' :
                    sendJSON(server,
                        {
                            "response": "pong"
                        })
            except Exception as e :
                print("Ping Error")
                print(e)
#après que le serveur répond OK ,le client envoie ping et le serveur répond pong pour vérifier si client est toujours à l'écoute					
            if rep == "play" : 
                state = respond['state'] 
                print(state)
                try :         
                    message = SENDmove(state)
                    print("message :",  message)
                    sendJSON(server, message)
                except Exception as e :
                    print("send Json Error")
                    print(e)    
                
        except Timeout:
            print('erreurservertimeout')
        except Exception:
            print("main Error")
            print('Exception')


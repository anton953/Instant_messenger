import socket
import threading

import json

class ServerClient():
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def receive_messages(self, address):
        # data = 
        json.loads(data.decode())

    def connect(self, ):
        try:
            self.client.connect((self.host, self.port))
            # Запускаем поток для приёма сообщений
            receive_thread = threading.Thread(target=self.receive_messages, args=(self.client,))
            receive_thread.daemon = True
            receive_thread.start()


        except:
            print("error")
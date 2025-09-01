import socket
import threading

import json

class Server():
    def __init__(self, host='127.0.0.1', port=55555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <- Вот эта строка
    
        self.host = host
        self.port = port

        self.clients = []
        self.nicknames = []
    
    def start_server(self):
        self.server.bind((self.host, self.port))
        self.server.listen(10)
        print(f"Сервер запущен на {self.host}:{self.port}")
        
        while True:
            try:
                # Принимаем подключение от клиента
                client, address = self.server.accept()
                print(f"Подключился клиент с адресом: {str(address)}")
                # Запрашиваем у клиента никнейм и добавляем его в список
                client.send('NICK'.encode('utf-8'))
                nickname = client.recv(1024).decode('utf-8')
                self.nicknames.append(nickname)
                self.clients.append(client)

                print(f'Никнейм клиента: {nickname}')
                broadcast(f'{nickname} присоединился к чату!'.encode('utf-8'), None)
                client.send('Подключение к серверу успешно!'.encode('utf-8'))

                # Запускаем отдельный поток для обработки сообщений от этого клиента
                thread = threading.Thread(target=handle_client, args=(client,))
                thread.daemon = True  # Поток завершится вместе с главным
                thread.start()
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break
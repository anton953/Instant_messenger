import socket
import threading

# Список для хранения всех активных клиентских подключений
clients = []
nicknames = []

# Функция для трансляции сообщения всем подключенным клиентам
def broadcast(message, current_client):
    for client in clients:
        # Не отправляем сообщение тому, кто его прислал
        if client != current_client:
            try:
                client.send(message)
            except:
                # Если отправка не удалась, считаем, что клиент отключился
                clients.remove(client)

# Функция для обработки сообщений от клиента
def handle_client(client):
    while True:
        try:
            # Получаем сообщение от клиента
            message = client.recv(1024)
            if message:
                print(f"Received message: {message.decode('utf-8')}")
                broadcast(message, client)
            else:
                # Если сообщение пустое, соединение разорвано
                raise Exception("Client disconnected")
        except:
            # Если возникла ошибка, удаляем клиента и закрываем соединение
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} покинул чат!'.encode('utf-8'), None)
            nicknames.remove(nickname)
            break

# Основная функция для запуска сервера
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # <- Вот эта строка
    
    host = '127.0.0.1'
    port = 55555
    server.bind((host, port))
    server.listen(10)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        try:
            # Принимаем подключение от клиента
            client, address = server.accept()
            print(f"Подключился клиент с адресом: {str(address)}")
            # Запрашиваем у клиента никнейм и добавляем его в список
            client.send('NICK'.encode('utf-8'))
            nickname = client.recv(1024).decode('utf-8')
            nicknames.append(nickname)
            clients.append(client)

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

    server.close()

if __name__ == "__main__":
    start_server()
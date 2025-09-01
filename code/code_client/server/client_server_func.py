import socket
import threading
import json

# Функция для получения сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            # Получаем сообщение от сервера
            message = client_socket.recv(1024).decode('utf-8')
            
            # Первое сообщение от сервера - запрос ника
            if message == 'NICK':
                print("Введите ваш никнейм:", end=' ')
                nickname = input()
                client_socket.send(nickname.encode('utf-8'))
            else:
                # Все остальные сообщения - чат
                print(message)
        except:
            # Если произошла ошибка (например, разрыв соединения), закрываем сокет
            print("Произошла ошибка соединения с сервером!")
            client_socket.close()
            break

# Функция для отправки сообщений на сервер
def send_message(client_socket):
    while True:
        message = input('')  # Ждём ввод пользователя
        if message.lower() == 'exit':  # Команда для выхода
            break
        # Форматируем и отправляем сообщение
        client_socket.send(message.encode('utf-8'))

def start_client():
    # Настраиваем клиентский сокет
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    host = '127.0.0.1'  # Адрес сервера
    port = 55555        # Порт сервера

    try:
        # Пытаемся подключиться к серверу
        client.connect((host, port))
        print(f"Подключились к серверу {host}:{port}")
    except:
        print(f"Не удалось подключиться к серверу {host}:{port}")
        return

    # Запускаем поток для приёма сообщений
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.daemon = True
    receive_thread.start()

    # В главном потоке отправляем сообщения
    send_message(client)

    # После выхода из цикла отправки закрываем соединение
    client.close()

if __name__ == '__main__':
    start_client()
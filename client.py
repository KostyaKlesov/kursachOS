import socket



class Client:
    def __init__(self) -> None:
        self.sock = socket.socket()
        print("Введите номер желаемого сервера:")
        number_s = int(input())
        if number_s == 1:
            self.sock.connect(('localhost', 9090))
            print("Выполнено подключение к первому серверу.")
            self.serverOne()
        elif number_s == 2:
            self.sock.connect(('localhost', 9091))
            print("Выполнено подключение ко второму серверу.")
            self.serverTwo()


    def reconect(self, number):
        self.sock.close()
        self.sock = socket.socket()
        if number == 1:
            self.sock.connect(('localhost', 9090))
            print("Выполнено подключение к первому серверу.")
            self.serverOne()
        elif number == 2:
            self.sock.connect(('localhost', 9091))
            print("Выполнено подключение ко второму серверу.")
            self.serverTwo()
            

    def serverOne(self):
        print("Доступные варианты для вывода:")
        print("1. Получить имя компьютера и имя пользователя")   
        print("2. Переместить серверное окно, согласно заданным координатам и вернуть результат")
        print("3. Переключиться на второй сервер")
        print("4. Закончить программу")
        option = int(input())
        if option == 1:
            self.sock.send(b"name")
            data = self.sock.recv(1024)
        elif option == 2:
            self.sock.send(b"coordinate")
            data = self.sock.recv(1024)
        elif option == 3:
            self.reconect(2)
        elif option == 4:
            exit()
        if data:
            print(data.decode())


    def serverTwo(self):
        print("Доступные варианты для вывода:")
        print("1. Получить приоритет процесса сервера")   
        print("2. Узнать, разрешен ли сбор данных SQM")
        print("3. Переключиться на первый сервер")
        print("4. Закончить программу")
        option = int(input())
        if option == 1:
            self.sock.send(b"priority")
            data = self.sock.recv(1024)
        elif option == 2:
            self.sock.send(b"SQM")
            data = self.sock.recv(1024)
        elif option == 3:
            self.reconect(1)
        elif option == 4:
            exit()
        if data:
            print(data.decode())
if __name__ == "__main__":
    client = Client()           
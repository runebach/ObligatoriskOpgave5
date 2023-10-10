from socket import *
import time
import json

# Vi angiver en server host og en server port
serverName = "127.0.0.1"
serverPort = 12000

# Vi opretter en TCP client socket og connecter denne
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


while True:


    # Vi tager et brugerinput og sender dette til serversocketen.
    time.sleep(1)
    Operator = input("Please input 'Random', 'Add' or 'Subtract'. Type 'Over' to quit")
    Operand1 = input("Please input a number")
    Operand2 = input("Please input a second number")


    # Vi tager vores input og laver et dictionary
    Dictionary = {"operator": f"{Operator}",
                "operand1": f"{Operand1}",
                "operand2": f"{Operand2}"}
    
    # Vi parser dictionary til json
    JsonFile = json.dumps(Dictionary)
    

    if(Operator == "Over"):
        break

    # clientSocket.sendall for at sende json
    clientSocket.sendall(bytes(JsonFile, encoding = "utf-8"))

    answer = clientSocket.recv(1024)
    answer = answer.decode()

    print("The answer is:", answer)
    time.sleep(2)





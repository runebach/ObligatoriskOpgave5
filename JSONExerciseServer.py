from socket import *
import threading
import random
import json

# Vores overordnede funktion, der meget gerne skulle kunne køre igen og igen.
def HandleClient(connectionSocket, address):
    print(address[0])
    communicate = True

    # Hvis communicate er true, receiver vi et input fra client
    while communicate == True:
        # Vi bruger json så vi bruger json.loads for at parse til dict format
        calculation = connectionSocket.recv(1024).decode("utf-8")
        calculation = json.loads(calculation)

        result = "Sorry. Please input a proper message"
        if calculation == "close":
            communicate = False
            result = "You have quit the calculator."

        # Vi henter vores attributter fra dictionary
        operator = calculation["operator"]
        operand_1 = calculation["operand1"]
        operand_2 = calculation["operand2"]

        # Vi parser vores operander til floats. Herefter tjekker vi operanden.
        num_1 = float(operand_1)
        num_2 = float(operand_2)

        if operator == "Random":
            result = random.randint(num_1, num_2)
        if operator == "Add":
            result = num_1 + num_2
        if operator == "Subtract":
            result = num_1 - num_2

        # Vi sender resultatet tilbage til serveren efter at have konverteret til en streng
        print("Sending result to client")

        output = str(result)
        print(output)
        connectionSocket.send(output.encode())
    # Vi lukker forbindelsen
    connectionSocket.close()

# Vi angiver serverPort og serverHost og danner en ServerSocket. Vi begynder at lytte.
serverPort = 12000
serverHost = "127.0.0.1"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("Server is ready")

# Vi kører et permanent while loop, der kører HandleClient metoden.
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=HandleClient, args=(connectionSocket, addr)).start()

        




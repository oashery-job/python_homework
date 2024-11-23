from common import ARITHMETIC_OPERATIONS
from consts import CLIENT_HOST, CLIENT_PORT, SERVER_HOST, SERVER_PORT
from logger import log_function
from logger import logger
import json
import socket


class Client:
    @log_function
    def start(self):
        num1, num2, operation = self.get_user_input()
        result = self.send_data_to_server(num1, num2, operation)
        print(f"The result is {result}")

    @log_function
    def get_user_input(self):
        while True:
            try:
                print("\n Hello, please follow the instructions: \n")
                num1 = int(input("Please enter the first number (Integer) ?"))
                num2 = int(input("Please enter the second number (Integer) ?"))

                print("Select an operation:")
                for i, (key, value) in enumerate(ARITHMETIC_OPERATIONS.items(), start=1):
                    print(f"{i}. {key}")

                answer_action = int(input("Enter the number of your selected operation: "))
                operation = list(ARITHMETIC_OPERATIONS.keys())[answer_action - 1]
                return num1, num2, operation
            except Exception as e:
                logger.error(e)
                print(f"\nPlease try to enter a valid parameters. \n")

    @log_function
    def send_data_to_server(self, num1, num2, operation):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.bind((CLIENT_HOST, CLIENT_PORT))
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            data_to_send = {
                "num1": num1,
                "num2": num2,
                "operation": operation,
            }
            client_socket.sendall(json.dumps(data_to_send).encode('utf-8'))
            response = client_socket.recv(1024)
            return response.decode('utf-8')


if __name__ == "__main__":
    client_a = Client()
    client_a.start()

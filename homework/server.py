from common import ARITHMETIC_OPERATIONS
from consts import SERVER_PORT, SERVER_HOST
from logger import log_function
from logger import logger
import json
import socket


class Server:

    @log_function
    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((SERVER_HOST, SERVER_PORT))
            server_socket.listen()
            logger.info("Server started and waiting for connection...")
            conn, addr = server_socket.accept()
            with conn:
                logger.info(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    client_data = json.loads(data.decode('utf-8'))
                    logger.info(f"Received data: {client_data}")
                    operation = client_data["operation"]
                    num1 = int(client_data["num1"])
                    num2 = int(client_data["num2"])
                    result = self.perform_operation(num1, num2, operation)
                    conn.sendall(str(result).encode())
                    logger.info(f"Sent result: {result}")

    @log_function
    def perform_operation(self, num1, num2, operation):
        operation_class = ARITHMETIC_OPERATIONS[operation]
        result = operation_class().execute(num1, num2)
        logger.info(f"Operation result: {result}")
        return result


if __name__ == "__main__":
    server_a = Server()
    server_a.start()

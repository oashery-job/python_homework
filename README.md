#Arithmetic Client-Server Application

Overview

This project is a Python-based client-server system designed to perform basic arithmetic operations. It demonstrates the use of socket programming, object-oriented principles, and robust input validation. The application supports essential mathematical functions, including addition, subtraction, multiplication, and division, while providing clear and user-friendly feedback.

Features

	•	Supported Arithmetic Operations:
	•	Addition (+)
	•	Subtraction (-)
	•	Multiplication (*)
	•	Division (/)
	•	Input Validation:
	•	Ensures user input is valid, with retries allowed for incorrect entries.
	•	Handles invalid operations and displays helpful error messages.
	•	Logging:
	•	Detailed logs are maintained for function calls, server-client communication, and errors.
	•	Configurable Parameters:
	•	Host and port settings for both the client and server are easily adjustable.

Architecture

Client

The client application:
	•	Collects two numbers and an arithmetic operation from the user.
	•	Validates input and ensures it matches the expected format.
	•	Communicates with the server by sending the data in JSON format.
	•	Receives the result from the server and displays it to the user.

Server

The server application:
	•	Listens for client connections on a configurable port.
	•	Receives data from the client, processes the requested operation, and sends back the result.
	•	Implements arithmetic operations using polymorphism to simplify future extensions.

Requirements

	•	Python 3.7 or newer.
	•	No external dependencies; the application uses Python’s standard libraries.

Setup and Usage

Step 1: Clone the Repository

git clone <repository-url>
cd <repository-directory>

Step 2: Start the Server

Run the server on the desired host and port:

python server.py

Step 3: Start the Client

Run the client to interact with the server:

python client.py

Configuration

To customize the client or server settings, edit the consts.py file:

CLIENT_HOST = '127.0.0.1'  # Client's host address
CLIENT_PORT = 27012        # Client's port number

SERVER_HOST = '127.0.0.1'  # Server's host address
SERVER_PORT = 54342        # Server's port number

Example Interaction

Client Session

Hello, please follow the instructions:

Please enter the first number (Integer): 12
Please enter the second number (Integer): 8
Select an operation:
1. '+'
2. '-'
3. '*'
4. '/'

Enter the number of your selected operation: 3

Client Output

The result is 96

Server Log

INFO - Server started and waiting for connection...
INFO - Connected by ('127.0.0.1', 54321)
INFO - Received data: {'num1': 12, 'num2': 8, 'operation': '*'}
INFO - Operation result: 96
INFO - Sent result: 96

Improvements and Enhancements

The client now limits the number of retries to three when entering invalid inputs, preventing infinite loops and improving the user experience. The user receives clear error messages and is guided to correct their input. After exceeding the retry limit, the program exits gracefully with an appropriate log entry.

Future Enhancements

	•	Add support for concurrent client connections to enable multiple users simultaneously.
	•	Implement advanced operations such as modulus and exponentiation.
	•	Integrate environment variable support for runtime configuration changes.

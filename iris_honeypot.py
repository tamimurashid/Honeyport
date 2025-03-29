import socket
import logging
import threading
import random
import sys

# Configure logging
logging.basicConfig(filename="iris_hport.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Fake directory structure
fake_dirs = {
    "/": ["home", "etc", "var", "usr", "bin"],
    "/home": ["admin", "guest"],
    "/home/admin": ["secret.txt", "config.cfg"],
    "/etc": ["passwd", "shadow", "hosts"],
}

def fake_ls(path):
    return "  ".join(fake_dirs.get(path, [])) if path in fake_dirs else "ls: cannot access"

def fake_pwd(path):
    return path if path in fake_dirs else "/"

def handle_client(client_socket, addr, port):
    logging.info(f"Connection from {addr} on Port {port}")
    client_socket.send(b"Iris_Hport Login: ")
    username = client_socket.recv(1024).decode().strip()
    client_socket.send(b"Password: ")
    password = client_socket.recv(1024).decode().strip()

    logging.info(f"Login attempt - Username: {username}, Password: {password} from {addr}")

    client_socket.send(b"Access Denied\n")

    # Fake terminal
    client_socket.send(b"\nWelcome to Iris_Hport Terminal\n")
    current_dir = "/"
    
    while True:
        client_socket.send(f"iris_Hport:{current_dir}$ ".encode())
        command = client_socket.recv(1024).decode().strip()
        
        if not command or command.lower() == "exit":
            break

        if command.startswith("ls"):
            client_socket.send(f"{fake_ls(current_dir)}\n".encode())
        elif command.startswith("pwd"):
            client_socket.send(f"{fake_pwd(current_dir)}\n".encode())
        elif command.startswith("cd"):
            _, *path = command.split()
            new_path = "/".join(path) if path else "/"
            if new_path in fake_dirs:
                current_dir = new_path
            else:
                client_socket.send(b"No such directory\n")
        else:
            client_socket.send(b"Command not found\n")

        logging.info(f"Command from {addr}: {command}")

    client_socket.close()
    logging.info(f"Connection closed for {addr}")

def start_honeypot(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", int(port)))
    server.listen(5)
    print(f"Honeypot running on port {port}...")

    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client, addr, port)).start()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python iris_honeypot.py <port>")
    else:
        start_honeypot(sys.argv[1])
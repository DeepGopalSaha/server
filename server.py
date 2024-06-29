import socket


def start_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    print(f"Listening on {host}:{port}...")

    conn, addr = s.accept()
    print(f"Connection from {addr}")

    while True:
        command = input("Shell> ")
        if command.lower() == "exit":
            conn.send(b"exit")
            break

        conn.send(command.encode())

        response = conn.recv(4096)
        print(response.decode())

    conn.close()
    s.close()


if __name__ == "__main__":
    start_server("0.0.0.0", 27000)

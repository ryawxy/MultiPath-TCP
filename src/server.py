import socket
import threading

def start_listener(port, path_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print(f" [Server] Listening on {path_name} (Port {port})...")
        
        conn, addr = server.accept()
        print(f" [Server] Connection established on {path_name} from {addr}")
        
        while True:
            data = conn.recv(1024)
            if not data: break
            print(f" [Server] Received on {path_name}: {data.decode()}")
            
        conn.close()
    except Exception as e:
        print(f" [Server] Error on {path_name}: {e}")

t1 = threading.Thread(target=start_listener, args=(8000, "PATH_A"))
t2 = threading.Thread(target=start_listener, args=(8001, "PATH_B"))

t1.start()
t2.start()
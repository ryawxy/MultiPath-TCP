import socket
import time
import csv
import os

if not os.path.exists('../results'):
    os.makedirs('../results')

def run_client():
    print("--- Starting MPTCP Client Simulation ---")
    
    try:
        s_primary = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_primary.connect(('127.0.0.1', 8000))
        print(" [Client] Connected to Primary Path (Path A)")
        
        s_backup = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_backup.connect(('127.0.0.1', 8001))
        print(" [Client] Connected to Backup Path (Path B)")
    except ConnectionRefusedError:
        print(" Error: Start the server first!")
        return

    with open('../results/transmission_log.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Packet_ID', 'Path_Used_Value'])
        
        print("\n--- Sending Data Stream (20 Packets) ---")
        
        for i in range(1, 21):
            msg = f"Packet_{i}"
            path_val = 0

            
            try:
                if i >= 10: 
                    if i == 10: print("\n SIMULATING LINK FAILURE ON PATH A \n")
                    raise ConnectionError("Path A Broken")
                
                s_primary.send(msg.encode())
                print(f" Sent {msg} via PRIMARY PATH")
                path_val = 1 
                
            except Exception:
                print(f"  Primary Failed! Rerouting {msg} via BACKUP PATH...")
                try:
                    s_backup.send(msg.encode())
                    path_val = 2 
                except:
                    print(" Both paths failed!")

            writer.writerow([i, path_val])
            time.sleep(0.5) 

    print("\n--- Transmission Complete ---")
    s_primary.close()
    s_backup.close()

if __name__ == "__main__":
    run_client()
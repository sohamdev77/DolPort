from colorama import Fore, Style, init
init()

# Print the DolPort logo
print(Fore.YELLOW + Style.BRIGHT + r"""
  ____        _     ____            _   
 |  _ \  ___ | |_  |  _ \ ___  _ __| |_ 
 | | | |/ _ \| __| | |_) / _ \| '__| __|
 | |_| | (_) | |_  |  __/ (_) | |  | |_ 
 |____/ \___/ \__| |_|   \___/|_|   \__|
           DOLPORT v2.0 by Soham
""" + Style.RESET_ALL)

# Example code for port scanning
import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()
    except Exception as e:
        pass

def main():
    ip = input("Enter the IP address: ")
    ports = input("Enter the port range (e.g., 1-100): ").split('-')
    start_port, end_port = int(ports[0]), int(ports[1])

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()

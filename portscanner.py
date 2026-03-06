import socket
import time

if __name__ == "__main__":
    target = input("Enter target IP or hostname: ")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname")
        exit()

    open_ports = 0

    print(f"\nScanning {target_ip}...\n")

    start_time = time.time()

    for port in range(1, 1025):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                print(f"[OPEN]   Port {port}")
                open_ports += 1
            else:
                print(f"[CLOSED] Port {port}")

    end_time = time.time()

    print(f"\nScan completed in {end_time - start_time:.2f} seconds")
    print(f"Open ports found: {open_ports}")
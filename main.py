from scapy.all import IP, ICMP, send
import time


def main():
    while True:
        target_ip = input("Enter an IP Address or a hostname to ping: ").strip()

        if not target_ip:
            print("[-] Target IP/hostname cannot be empty.")
            continue

        payload = input("Enter a payload to send: ")

        if not payload:
            print("[-] Payload cannot be empty.")
            continue

        try:
            packet_send = int(input("How many times do you want to send the packet? "))
        except ValueError:
            print("[-] Packet count must be a whole number.")
            continue

        if packet_send <= 0:
            print("[-] Packet count must be greater than 0.")
            continue

        return target_ip, payload, packet_send


def create_packet(target_ip, payload, packet_send):

    print("[*] Processing...")
    time.sleep(1)

    try:
        # Create the packet once
        ping_packet = IP(dst=target_ip) / ICMP() / payload

        # Send it multiple times
        for pp in range(packet_send):
            try:
                send(ping_packet, verbose=False)

                print(
                    f"[*] Sending packet "
                    f"{pp + 1:,}/{packet_send:,}..."
                )

                time.sleep(1)

            except PermissionError:
                print("[-] Permission denied. Try running with appropriate privileges.")
                return

            except Exception as e:
                print(f"[-] Error while sending packet: {e}")
                return

        print("\n[+] Finished sending packets!")

    except Exception as e:
        print(f"[-] Failed to create/send packet: {e}")


# Start the program
if __name__ == "__main__":
    try:
        target_ip, payload, packet_send = main()
        create_packet(target_ip, payload, packet_send)

    except KeyboardInterrupt:
        print("\n[-] Program interrupted by user.")

    except Exception as e:
        print(f"[-] Unexpected error: {e}")
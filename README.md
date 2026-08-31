SCAPY ICMP PACKET SENDER

Author: CyberPersian

DESCRIPTION

This is a beginner Python networking and cybersecurity project created to learn how to construct and send ICMP packets using Scapy.

The program allows the user to:

* Enter an IP address or hostname
* Enter a custom payload
* Choose the number of packets to send
* Construct an IP and ICMP packet using Scapy
* Send the packet multiple times
* Handle invalid input and common errors

WHAT I LEARNED

This project helped me practice:

* Python functions
* While loops
* For loops
* User input
* Input validation
* Exception handling
* Formatted strings
* The time module
* Basic networking concepts
* IP packets
* ICMP
* Packet construction with Scapy
* Sending packets with Scapy

REQUIREMENTS

* Python 3.x
* Scapy
* Appropriate privileges for raw packet operations

INSTALLATION

1. Install Python 3.x.

2. Clone or download this repository.

3. Open a terminal inside the project directory.

4. Install the required dependency by running:

pip install -r requirements.txt

RUNNING THE PROGRAM

Run the following command:

python main.py

The program will ask for:

1. Target IP address or hostname
2. Payload
3. Number of packets to send

EXAMPLE

Enter an IP Address or website to ping: 192.168.1.1
Enter a payload to send: Hello
How many times do you want to send the packet? 3

The program will then construct the ICMP packet and send it the specified number of times.

RESPONSIBLE USE

This project was created for educational purposes.

Only use this program on systems, devices, or networks that you own or have explicit permission to test.

Do not use this program to intentionally disrupt, overload, or interfere with systems or networks.

FUTURE IMPROVEMENTS

Possible improvements for future versions include:

* Better hostname handling
* Command-line arguments
* Configurable packet delay
* Improved logging
* More detailed packet information
* Additional ICMP options
* A cleaner command-line interface

PROJECT STATUS

Beginner educational project.

This project is part of my learning journey in Python, networking, and cybersecurity.

AUTHOR

CyberPersian

Created as a personal learning project.
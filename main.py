import socket   # To connect to ports
from termcolor import colored   # To print coloured outputs

try:
    def scan(ipaddresses, ports):
        """
        Passes the number of ports to be scanned to scan_port() function for each IP address in the argument.\n
        :param ipaddresses: List of ip addresses
        :param ports: Number of ports to scan
        :return: None
        """
        for ipaddress in ipaddresses:
            ip = colored(ipaddress, 'blue', attrs=['underline', 'bold'])    # To print the ipaddress in appropriate texture.
            print(f'\nScanning {ip} for open ports:')
            for port in range(1, ports+1):
                scan_port(ipaddress, port)


    def scan_port(ipaddr, port):
        """
        Scans the specified port of the specified ip address.
        :param ipaddr: IP address
        :param port: The port to be scanned
        :return: None
        """
        try:
            sock = socket.socket()      # Establishing connection
            sock.connect((ipaddr, port))
        except socket.error:
            pass
        else:
            port = colored(port, 'green', attrs=['bold'])   # If connection established, then prints the port number
            print(f'\t[+] Port {port} is open')
            sock.close()

    ipaddress_list = input('Enter IP addresses separated by comma: ').split(',')    # User enters all IPs, separated by comma
    ports = int(input('How many ports do you want to scan?: '))
    ipaddresses = list(map(lambda x: x.strip(), ipaddress_list))    # In case the user enters values by putting space after comma, this line will eliminate those spaces.

    scan(ipaddresses, ports)

except KeyboardInterrupt:
    print(colored(f'\nProgram execution was terminated by the user!', 'red'))
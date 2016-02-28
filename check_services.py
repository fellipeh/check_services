#!/usr/bin/python

import sys
import getopt
import json
import datetime
import logging
import socket
import paramiko, base64

# #########################################
# ###  check_services.py
# ###
# ###  Script to check if some standard services is active, if not, try to start them.
# ###
# ### How to use:
# ###   1) create a standard port input file, named:  ports.json
# ###   2) run: python check_services.py IP
# ###
# ###   Ex:  check_services.py  192.168.1.259
# ############################################

LOG_FILE = './check_services.log'
SSH_USER = 'vagrant'
SSH_PASS = 'vagrant'


def log(msg):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  + "  -  " + msg)
    logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG)
    logging.debug(datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "  -  " + msg)


def does_service_exist(host, port):
    try:
        host_addr = socket.gethostbyname(host)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except:
        return False

    return True


def start_service(service):

    log("\terror on start..." + service)


def main(argv):
    ip_address = '127.0.0.1'
    port_file = './ports.json'
    try:
        opts, args = getopt.getopt(argv, "hi:f:", ["ip=", "file="])
    except getopt.GetoptError:
        print 'check_services.py -i <IP Address> -f <Port File>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'check_services.py -i <IP Address> -f <Port File>'
            sys.exit()
        elif opt in ("-i", "--ip"):
            ip_address = arg
        elif opt in ("-o", "--file"):
            port_file = arg

    print 'Using Port file: ', port_file
    print 'checking IP: ', ip_address, '...'

    with open(port_file) as data_file:
        data = json.load(data_file)

    log("Looking " + ip_address)

    for i in data:
        log("Checking: " + str(i["port"]))
        if does_service_exist(ip_address, i["port"]):
            log("\tstatus: Ok")
        else:
            log("\tstatus: Closed")
            log("\ttrying to start...")

            # trying to connect via shh to start the service...
            client = paramiko.SSHClient()
            try:
                client.connect(ip_address, username=SSH_USER, password=SSH_PASS)
                stdin, stdout, stderr = client.exec_command('sudo service ' + i["service"] + 'restart')
                for line in stdout:
                    print '\t... ' + line.strip('\n')
            finally:
                client.close()


if __name__ == "__main__":
    main(sys.argv[1:])

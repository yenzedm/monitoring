#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import psutil
import sys


def check_listening_port(port):
    result = 0
    for conn in psutil.net_connections(kind="inet"):
        if conn.status == "LISTEN" and str(conn.laddr.port) in str(port):
            result = int(conn.laddr.port)
    
    print(result)


if __name__ == '__main__':
    satellite_name = sys.argv[0]
    satellite_port = sys.argv[1]
    check_listening_port(satellite_port)
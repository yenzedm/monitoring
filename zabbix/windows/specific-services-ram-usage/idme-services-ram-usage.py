#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import psutil


def get_ram_usage_by_specific_service():
    service_ram_usage = 0
    
    # Get all processes and their memory usage
    for proc in psutil.process_iter(['name', 'memory_percent']):
        try:
            # Check if the process name contains -runner.exe
            if '-runner.exe' in proc.info['name']:
                service_ram_usage += proc.memory_percent()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print(service_ram_usage)


get_ram_usage_by_specific_service()
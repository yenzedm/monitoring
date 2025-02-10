#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import psutil


def get_cpu_usage_by_specific_service():
    service_cpu_usage = 0
    
    # Get all processes
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            # Check if the process name contains -runner.exe
            if '-runner.exe' in proc.info['name']:
                cpu_percent = proc.cpu_percent(interval=0.2)
                service_cpu_usage += cpu_percent
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print(float(service_cpu_usage))
    service_cpu_usage = 0


get_cpu_usage_by_specific_service()
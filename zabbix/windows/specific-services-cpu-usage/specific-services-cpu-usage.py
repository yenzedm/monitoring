#!C:\Users\admin\AppData\Local\Programs\Python\Python39\python.exe
import psutil
import sys

def proc_cpu_percent(name):
    proc_cpu_result = 0
    proc_info_cpu_count = psutil.cpu_count()
    for proc in psutil.process_iter(['pid', 'name', 'status']):
        try:
            proc_id = proc.info['pid']
            proc_info = psutil.Process(proc_id)
            proc_info_cpu_percent = proc_info.cpu_percent(interval=0.2)
            if name == proc.info['name'] and proc.info['status'] == 'running':
                proc_cpu_result = round(proc_info_cpu_percent / proc_info_cpu_count)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return proc_cpu_result

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print(0)
        else:
            service_name = sys.argv[1]
            print(proc_cpu_percent(service_name))
    except Exception as e:
        print(0)

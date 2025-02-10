#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import psutil


def get_cpu_usage_by_service():
    # Словарь для хранения общей загрузки CPU по службам с -runner.exe в названии
    service_cpu_usage = {}
    
    # Получаем все процессы
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            # Получаем имя процесса и его процент использования CPU
            process_name = proc.info['name']
            # Проверяем, если в названии процесса есть -runner.exe
            if '-runner.exe' in process_name:
                cpu_percent = proc.cpu_percent(interval=0.1)  # Интервал в 1 секунду для точности
                
                # Добавляем или обновляем данные в словаре
                if process_name in service_cpu_usage:
                    service_cpu_usage[process_name] += cpu_percent
                else:
                    service_cpu_usage[process_name] = cpu_percent
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Выводим информацию
    if service_cpu_usage:
        total_cpu_usage = sum(service_cpu_usage.values())
        print(float(f"{total_cpu_usage:.2f}"))


get_cpu_usage_by_service()
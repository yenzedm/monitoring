#!C:\Users\admin\AppData\Local\Programs\Python\Python313\python.exe
import psutil


def get_ram_usage_by_service():
    # Словарь для хранения использования RAM по службам с -runner.exe в названии
    service_ram_usage = {}
    
    # Получаем все процессы и их использование памяти
    for proc in psutil.process_iter(['name', 'memory_percent']):
        try:
            # Получаем имя процесса и его использование RAM
            process_name = proc.info['name']
            # Проверяем, если в названии процесса есть -runner.exe
            if '-runner.exe' in process_name:
                memory_percent = proc.memory_percent()
                
                # Добавляем или обновляем данные в словаре
                if process_name in service_ram_usage:
                    service_ram_usage[process_name] += memory_percent
                else:
                    service_ram_usage[process_name] = memory_percent
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Выводим информацию
    if service_ram_usage:
        total_ram_usage = sum(service_ram_usage.values())
        print(float(f"{total_ram_usage:.2f}"))


get_ram_usage_by_service()
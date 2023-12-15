import getpass
import win32gui
import win32con
import socket
import win32process
import win32api
import os
import win32con
import ctypes


#Функции для первого сервера
appname = 'Администратор: Командная строка'
xpos = 50
ypos = 100
width = 800
length = 600

def move_window(hwnd, x, y, w, h):
    try:
        win32gui.MoveWindow(hwnd, x, y, w, h, True)
    except Exception as e:
        return f"Ошибка: не удалось переместить окно. Подробности: {str(e)}"
    return "Успех: окно перемещено."

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if appname in win32gui.GetWindowText(hwnd):
            result = move_window(hwnd, xpos, ypos, width, length)
            if result.startswith("Ошибка"):
                print(result) 
            else:
                print(result)

# Функции для второго сервера
def getPriority():
    script_pid = os.getpid()
    process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, script_pid)
    priority = win32process.GetPriorityClass(process_handle)

    return f"Приоритет запущенного python-скрипта: {priority}"


def is_sqm_enabled():
    try:
        settings_key = r"SOFTWARE\Microsoft\SQMClient"
        hKey = None
        reg_result = ctypes.windll.advapi32.RegOpenKeyExA(ctypes.c_int(0x80000002), ctypes.c_char_p(settings_key.encode()), 0, ctypes.c_int(0x20019), ctypes.byref(hKey))
        if reg_result == 0:
            value_type = ctypes.c_int()
            value_length = ctypes.c_int(4)  # DWORD size
            value = ctypes.c_int()
            query_result = ctypes.windll.advapi32.RegQueryValueExA(hKey, ctypes.c_char_p("OptIn".encode()), None, ctypes.byref(value_type), ctypes.byref(value), ctypes.byref(value_length))
            if query_result == 0:
                if value.value == 1:
                    return "Сбор данных SQM разрешен."
            else:
                print("Не удалось получить значение реестра.")
        else:
            print("Не удалось открыть ключ реестра.")
    except Exception as e:
        pass
    
    return "Сбор данных SQM запрещен."

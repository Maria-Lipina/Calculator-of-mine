import ui
from datetime import datetime as dt

history = {}

def log_it(record):
    global history
    new_rec = {dt.now().strftime('%d/%m/%Y %H:%M'): record}
    history = new_rec | history
    print(history)

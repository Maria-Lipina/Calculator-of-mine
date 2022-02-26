from datetime import datetime as dt

def log_it(record):
    date = dt.now().strftime('%d/%m/%Y %H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{date}; {record}\n')
    file.close()

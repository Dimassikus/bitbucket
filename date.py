import re
from datetime import datetime

def is_valid_date(date_str):
    # Регулярное выражение для проверки формата
    pattern = r'^\d{1,2} (Янв|Фев|Мар|Апр|Май|Июн|Июл|Авг|Сен|Окт|Ноя|Дек), \d{4}$'
    
    if not re.match(pattern, date_str):
        return False
    
    # Попробуем преобразовать строку в дату
    try:
        date_obj = datetime.strptime(date_str, '%d %b, %Y')
        return True
    except ValueError:
        return False

# Пример использования
date_input = "21 Янв, 1978"
if is_valid_date(date_input):
    print("Дата корректна.")
else:
    print("Дата некорректна.")

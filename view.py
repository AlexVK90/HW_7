def get_operation_mark():
    return input("Введите операцию или '=' что бы показать итог)")

def get_expression():
    return input("Введите число или арифметическое выражение: ")

def print_result(data, is_final = False):
    if is_final:
        print('='*40)
        print('Итого:', data)
    else:    
        print("Результат: ", data) 

def print_zerodivision_error():
    print (f"Ошибка: деление на ноль")     


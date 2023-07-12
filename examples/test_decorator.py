# # Функция-декоратор
# def dec(f_arg):
#     def wrapper ():
#         # Доп. функциональность "ДО"
#         print("Before")
#         f_arg()
#         # Доп. функциональность "ПОСЛЕ"
#         print("After") 
#     return wrapper

def foo():
    def dec(f_arg):
        def wrapper ():
            # Доп. функциональность "ДО"
            print("Before")
            f_arg()
            # Доп. функциональность "ПОСЛЕ"
            print("After") 
        return wrapper
    return dec

# Новый способ декорирования
# @dec
@foo()

# Целевая функция
def func_1():
    print("Hello!")

# Старый способ декорирования
# func_1 = dec(func_1)

# Вызов целевой функции
func_1()
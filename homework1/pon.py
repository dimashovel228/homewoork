def get_values():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    d = int(input("Введите значение d: "))
    return a, b, c, d

def solve_equation(a, b, c, d):
    return (-3 + a**2) * b - 16 - 2 * c - 2 * d
  
result = solve_equation(a, b, c, d)
print(f"Результат выражения: {result}")


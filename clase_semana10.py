

"""
def sum_all(*numbers):
    total = 0
    for number in numbers:
        total = total + number
 
    print(f"Total {total}")
 
sum_all(1, 20, 2, 10)
"""
 
"""
def print_client_data(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
 
print_client_data(name="Jose", id=123, email="jose@example.com")        
"""
 
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 
print(factorial(2))
"""
 
personas = ["Juan", "Maria", "Jose"]
preferencias = ["UNIX", "Windows", "MAC"]
 
"""
for i in range(3):
    persona = personas[i]
    preferencia = preferencias[i]
 
    print(f"{persona} {preferencia}")
"""
#for persona, preferencia in zip(personas, preferencias):
#    print(f"{persona} {preferencia}")
 
#[print(f"{persona} {preferencia}") for persona, preferencia in zip(personas, preferencias)]

 
personas = ["Juan", "Maria", "Jose"]
preferencias = ["UNIX", "Windows"]
for persona, preferencia in zip(personas, preferencias):
    print(f"{persona} {preferencia}")
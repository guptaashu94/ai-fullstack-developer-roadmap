print("===== Without Functions =====")

name = input("Enter name: ")
print(f"Hello {name}")

name = input("Enter another name: ")
print(f"Hello {name}")

print("===== With Functions =====")

def greet():
    name = input("Enter name: ")
    print(f"Hello {name}")

greet()
greet()
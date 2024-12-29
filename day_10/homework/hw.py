# 1) შექმენით კალკულატორი, მომხმარებელს შეეკითხეთ ორი რიცხვი, შემდეგ შეეკითხეთ რა მოქმედების შესრულება სურს ამ ორ რიცხვზე და მისი პასუხიდან გამომდინარე შეასრულეთ მოქმედება და დაბეჭდეთ მაგალითად თუ მომხმარებელი შემოიტანს რიცხვებს 5 და 7 , და შემოიტანს მოქმედებას მაგალითად დამატებას თქვენ უნდა დაუბეჭდოთ 5 + 7 = 12

num1 = int(input("enter your first number: "))
num2 = int(input("enter your second number: "))
def calculator():
    print("1. multiply")
    print("2. division")
    print("3. addition")
    print("4. deduction")
    choose = input("choose: ")
    
    if choose == '1':
        return num1 * num2
    elif choose == '2':
        return num1 // num2
    elif choose == '3':
        return num1 + num2
    elif choose == '4':
        return num1 - num2
    else:
        return "error"
print(calculator())
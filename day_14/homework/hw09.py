# დაწერეთ ისეთი პროგრამა რომელიც მომხმარებელს უპრინტავს კვირის დღეს მომხმარებლის შემოტანილი რიცხვის მიხედვით (1 არის ორშაბათი, 2 სამშაბათი და ა.შ) გამოიყენეთ if elif else


user_text = input("შეიყვანე კვირის დღე: ")


if user_text == "1":
    print("ორშაბათი")
elif user_text == "2":
    print("სამშაბათი")
elif user_text == "3":
    print("ოთხშაბათი")
elif user_text == "4":
    print("ხუთშაბათი")
elif user_text == "5":
    print("პარასკევი")
elif user_text == "6":
    print("შაბათი")
elif user_text == "7":
    print("კვირა")
else:
    print("არასწორია")
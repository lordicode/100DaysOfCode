print("Tip culture is not good. Pay workers more instead.")
print("Nonetheless, welcome to the Tip Calculator!\n")
bill = input("What was the total bill? \n->")
bill = float(bill)
q_of_service = input("How much did you like the service from 1 to 3 (3 highest)?\n->")
q_of_service = int(q_of_service)

match q_of_service:
    case 3:
        tip = (bill / 100) * 20
        print(f"The tip amount will be {(bill / 100) * 20}")
    case 2:
        tip = (int(bill) / 100) * 10
        print(f"The tip amount will be {(bill / 100) * 10}")
    case 1:
        tip = (int(bill) / 100) * 8
        print(f"The tip amount will be {(bill / 100) * 8}")

split_bill = input("How many people to split bill between?")
print(f"Overall each person should pay {(bill + tip) / int(split_bill)}")

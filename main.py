def main():
    income = float(input("Whats your monthly income? "))

    bills = {}
    while True:
        name = input("Enter Bill name: ")
        if name.lower() == 'done':
            break
        amount = float(input(f"Enter Amount for {name}: "))
        bills[name] = amount

    total_bills = sum(bills.values())
    percent_bills = (total_bills / income) * 100
    leftover = income - total_bills

    print("\n=== Summary ===")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Bills: ${total_bills:.2f}")
    print(f"Bills are: ${percent_bills:.2f} % of your income")
    print(f"Income after Bills: ${leftover:.2f}")

    print("\n=== 50/30/20 Rule Breakdown ===")
    print(f"Needs (50%): ${income * 0.50:.2f}")
    print(f"Wants (30%): ${income * 0.30:.2f}")
    print(f"Savings (20%): ${income * 0.20:.2f}")

if __name__ == "__main__":
    main()
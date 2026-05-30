# Stock prices
stocks = {
    "GOOGLE": 3000,
    "RELIANCE": 4000,
    "HDFC": 5000,
    "INFOSYS": 6000,
    "TATA": 2000
}

total = 0

# Number of stocks user owns
n = int(input("How many stocks do you own? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        price = stocks[stock_name]
        investment = price * quantity

        print("Investment in", stock_name, "=", investment)

        total = total + investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)

# Save result to file
file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total))
file.close()

print("Result saved in portfolio.txt")
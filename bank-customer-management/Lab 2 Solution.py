Interest_rate = 0.125
minimum_balance = 50
maximum_balance = 2000000.00

# create a class
class ClassName:
    def __init__(self, name, opening_balance):
        self.name = name
        self.opening_balance = opening_balance
        self.closing_balance = 0
        self.customer_type = "none"
# create a method to calculate the closing balance of the customers

    def calculateClosingBalance(self):
        self.closing_balance = self.opening_balance + (self.opening_balance * Interest_rate)
        return self.closing_balance

## create a method to calculate the customer type

    def determineCustomerType(self):
        if self.closing_balance <= 90000:
            self.customer_type = "Bronze"
        elif 90000 <= self.closing_balance < 100000:
            self.customer_type = "Silver"
        elif 100000 <= self.closing_balance <= 150000:
            self.customer_type = "Gold"
        elif self.closing_balance > 150000:
            self.customer_type = "Diamond"
        return self.customer_type

#formatting to print the information of the customer
    def displayTabularInfo(self):
        #calculate the interest
        interest_calculated = self.opening_balance * Interest_rate
        fmtHdr = "{:20}{:<20}{:>20.2f}{:>20.2f}{:>20.2f}"
        print(fmtHdr.format(self.name,self.customer_type,self.opening_balance,interest_calculated, self.closing_balance))

# Input the number of customers user wants to input

num_of_customers = int(input("Enter the number of customers you have in this bank: "))
# input validation
while num_of_customers <= 0:
    prompt = "{} is not valid no. of students. Try again: ".format(num_of_customers)
    num_of_customers = int(input(prompt))
#create a list that stores the input info of the customers
customers = []

#create a loop in the range of number of customers to store information for each customer
for idx in range(num_of_customers):
    name_of_customer = input("Enter the customer {}'s name: ".format(idx+1))
    balance = float(input("Enter customer {}'s opening balance: ".format(idx+1)))
    while (balance < minimum_balance) or (balance > maximum_balance):
        balance = float(input("{} is not valid. Try again: ".format(balance)))
    customers.append(ClassName(name_of_customer, balance))
    customers[idx].closing_balance = customers[idx].calculateClosingBalance()
    customers[idx].customer_type = customers[idx].determineCustomerType()

#format the header for the table
fmt = "{:20}{:<20}{:>20}{:>20}{:>20}"
print(fmt.format("Customer Name","Customer Type","Opening($)", "Interest($)","Closing($)"))
print("*" * 100)

for customer in customers:
    customer.displayTabularInfo()

print("*" * 100)





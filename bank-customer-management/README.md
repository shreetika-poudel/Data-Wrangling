# Bank Customer Management

This project contains a Python script for managing customer information in a bank. The script allows users to input details for multiple customers, calculates their closing balances with interest, determines customer types, and displays the information in a tabular format.

## Features

- **Customer Class:**
  - Constructor to initialize customer name and opening balance.
  - `calculateClosingBalance` method to compute the closing balance with a 12.5% interest rate.
  - `determineCustomerType` method to classify customers based on closing balance.

- **Input Validation:**
  - Ensures each customer has a minimum opening balance of $50 and a maximum of $2,000,000.00.

- **Tabular Display:**
  - `displayTabularInfo` method prints a table with customer details including name, opening and closing balances, interest, and customer type.

## How to Use

1. Run the script.
2. Enter the number of customers.
3. For each customer, input the name and opening balance within the specified range.
4. View the generated table displaying customer information.

## Example

```bash
$ python your_nku_user_id_Lab2.py
Enter the number of customers: 3

Customer 1:
Name: John Doe
Opening Balance: 1000.00

Customer 2:
Name: Jane Smith
Opening Balance: 75000.00

Customer 3:
Name: Robert Johnson
Opening Balance: 2000000.00

Table of Customer Information:

| Customer Name    | Opening Balance | Closing Balance | Interest | Customer Type |
|------------------|------------------|------------------|----------|----------------|
| John Doe         | 1000.00          | 1125.00          | 125.00   | Bronze         |
| Jane Smith       | 75000.00         | 84375.00         | 9375.00  | Gold           |
| Robert Johnson   | 2000000.00       | 2250000.00       | 250000.00| Diamond        |

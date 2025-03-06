"""This module contains a program that reads through transaction records
and reports the results.

Example:
    $ python pixell_transaction_report.py
"""

__author__ = "ACE Faculty"
__version__ = "0.11.2024"

import csv
import os
 
valid_transaction_types = ['deposit', 'withdraw']
customer_data = {}
rejected_transactions = []
transaction_count = 0
transaction_counter = 0
total_transaction_amount = 0
is_valid_record = True
error_message = ''

# Clears the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Get the directory the script is saved to
SCRIPT_DIRECTORY = os.path.dirname(__file__)

# The name of the data file
DATA_FILENAME = "bank_data.csv"

# The absolute path to the data file
DATA_FILE_PATH = f"{SCRIPT_DIRECTORY}/{DATA_FILENAME}"
try:

        with open(DATA_FILE_PATH, 'r') as csv_file:
            reader = csv.reader(csv_file)

    # Skip heading line
            next(reader)

            for transaction in reader:
        # Reset valid record and error message for each iteration
                is_valid_record = True
                error_message = ''

        # Gets the customer ID from the first column
                customer_id = transaction[0]
        
        # Gets the transaction type from the second column
                transaction_type = transaction[1]

        ### VALIDATION 1 ###
                try:
                        if transaction_type not in valid_transaction_types:
                            is_valid_record = False
                            error_message = f'The transaction type "{transaction_type}" is invalid.'
                            raise TypeError
                except TypeError as e:
                        print(f'The transaction type "{transaction_type}" is invalid.')

        ### VALIDATION 2 ###
        # Gets the transaction amount from the third column
                try:
                        transaction_amount = float(transaction[2])
                except ValueError as e:
                        is_valid_record = False
                        error_message += f' Non-numeric transaction amount.'
                        print(f'"{transaction[2]} is an invalid transaction amount.')
                        
                if is_valid_record == False:
                    rejected_transactions.append((transaction, error_message))

                if is_valid_record:
            # Initialize the customer's account balance if it doesn't 
            # already exist
                    if customer_id not in customer_data:
                        customer_data[customer_id] = {'balance': 0, 'transactions': []}
            # Update the customer's account balance based on the 
            # transaction type
                    if transaction_type == 'deposit':
                        customer_data[customer_id]['balance'] += transaction_amount
                        transaction_count += 1
                        total_transaction_amount += transaction_amount
                        transaction_counter += 1
                    elif transaction_type == 'withdraw':
                        customer_data[customer_id]['balance'] += transaction_amount
                        transaction_count += 1
                        total_transaction_amount += transaction_amount
                        transaction_counter += 1
            
            # Record transactions in the customer's transaction history
                    customer_data[customer_id]['transactions'].append(
                        (transaction_amount, transaction_type)
                        )
        
        ### COLLECT INVALID RECORDS ###

        # Formatting for the report        
            report_title = "PiXELL River Transaction Report"
            print(report_title)
            print('=' * len(report_title))

            # Print the final account balances for each customer
            for customer_id, data in customer_data.items():
                balance = data['balance']
                print(f"Customer {customer_id} has a balance of ${balance:,.2f}.")
        
                # Print the transaction history for the customer
                print("Transaction History:")
                for rejected_transaction in data['transactions']:
                    amount, type = rejected_transaction
                    print(f"{type.capitalize():>16}: ${amount:,.2f}")
            # Correcting ZeroDivisionError
            try:
                    if transaction_counter > 0:
                        average_transaction_amount = total_transaction_amount / transaction_counter
                        print(f"AVERAGE TRANSACTION AMOUNT: ${average_transaction_amount:,.2f}")
            except ZeroDivisionError as e:
                        print("No valid transactions to calculate average.")
            # Print rejected records to the console
            rejected_report_title = "REJECTED RECORDS"
            print(rejected_report_title)
            print('=' * len(rejected_report_title))

            for rejected_transaction in rejected_transactions:
                print("REJECTED:", rejected_transaction)
except FileNotFoundError as e:
        print(f"The bank data file ({DATA_FILENAME}) cannot be found.")
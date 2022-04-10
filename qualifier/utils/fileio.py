# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import sys
import questionary
from pathlib import Path

def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = questionary.text("What's your credit score?").ask()
    debt = questionary.text("What's your current amount of monthly debt?").ask()
    income = questionary.text("What's your total monthly income?").ask()
    loan_amount = questionary.text("What's your desired loan amount?").ask()
    home_value = questionary.text("What's your home value?").ask()

    credit_score = int(credit_score)
    debt = float(debt)
    income = float(income)
    loan_amount = float(loan_amount)
    home_value = float(home_value)

    return credit_score, debt, income, loan_amount, home_value

def save_qualifying_loans(qualifying_loans):
    """Handles user interaction to confirm save of qualifying loans & calls save_csv function if user indicates 'Y'

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # @TODO: Complete the usability dialog for savings the CSV Files.
    # YOUR CODE HERE!
    # Set the output file path

    save_yes_no = questionary.confirm("Would you like to save the results as a CSV file?").ask()
    
    if save_yes_no == True:
        if not qualifying_loans:
            print("There are 0 qualifying loans.")
            sys.exit("Thanks and have an awesome day!!")
        else:
            output_path = questionary.text("Enter file path to save CSV file:").ask()
            output_path = Path(output_path)
            save_csv(qualifying_loans, output_path)
        
    elif save_yes_no == False:
        sys.exit("Thanks and have an awesome day!")

    
def save_csv(qualifying_loans, output_path):
    """Saves the qualifying loans to a CSV file.
    
     Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    with open(output_path, 'w', newline = '') as csvfile:
        loan_writer = csv.writer(csvfile)
        for loan in qualifying_loans:
            loan_writer.writerow(loan)

def interest_data(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_data(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
   # Convert interest rate to decimal
    interest_rate = interest_rate / 100
    
    # Print loan details
    print("Principal:   ${:.2f}".format(principal_amount))
    print("Interest rate: {:.2f}%".format(interest_rate * 100))
    print("Monthly payment: ${:.2f}".format(payment))
    print("----------------------------------")
    print("Month   Interest   Payment   Balance")
    print("----------------------------------")
    
    # Initialize balance and month
    balance = principal_amount
    month = 0
    
    # Calculate and print data for each month
    while balance > 0:
        # Increment month
        month += 1
        
        # Calculate interest for the month
        interest = balance * (interest_rate / 12)
        
        # Determine actual payment for the month
        if balance + interest < payment:
            payment = balance + interest
        
        # Calculate remaining balance after payment
        balance = balance + interest - payment
        if balance < 0:
            balance = 0
        
        # Print data for the month
        print("{:4d}     ${:.2f}    ${:.2f}    ${:.2f}".format(
            month, interest, payment, balance))
    
    # Return final balance
    return balance
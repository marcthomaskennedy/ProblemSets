# This programs calculates a credit card balance after one year if the person
# only pays the minimum monthly payment required by the credit card company
# each month.

def calculateBalance(balance, annualInterestRate, monthlyPaymentRate, numOfMonths):
    '''(number, float, float, int) => float Raises AssertionError
    Returns the outstanding balance on a credit card with an annualInterestRate
    and monthlyPaymentRate over numOfMonths.
    >>> calculateBalance(42, 0.2, 0.04, 12)
    31.38
    >>> calculateBalance(484, 0.2, 0.04, 12)
    361.61
    '''
    # Check if parameters are of the correct type.
    assert type(balance) == int or type(balance) == float, "balance should be\
            a int or float"
    assert type(annualInterestRate) == float, "annualInterestRate should be of\
            type float"
    assert type(monthlyPaymentRate) == float, "monthlyPaymentRate should be of\
            type float"
    assert type(numOfMonths) == int, "numOfMonths should be of type int"

    # Helper functions
    def calculateMinimumMonthlyPayment(currentBalance, monthlyPaymentRate):
        '''(number, float) => float
        Returns the minimum monthly payment required by the credit card company
        >>> calculateMinimumMonthlyPayment(5000, 0.02)
        100.0
        '''
        return round(currentBalance * monthlyPaymentRate, 2)

    def calculateUnpaidBalance(currentBalance, minimumPayment):
        '''(number, float) => float
        Returns the unpaid balance after subtracting minimumPayment from
        currentBalance
        >>> calculateUnpaidBalance(5000, 100.0)
        4900.00
        '''
        return round(currentBalance - minimumPayment, 2)

    def calculateInterest(unpaidBalance, annualInterestRate):
        '''(float, float) => float
        Returns the interest on unpaidBalance with an annualInterestRate
        >>> calculateInterest(4900.00, 0.18)
        73.50
        '''
        return round(annualInterestRate / 12.0 * unpaidBalance ,2)

    def calculateNewBalancePlusInterest(unpaidBalance, interestOnBalance):
        '''(float, float) => float
        Returns the sum of unpaidBalance and interestOnBalance
        >>> calculateNewBalancePlusInterest(4900.00, 73.50)
        4973.50
        '''
        return round(unpaidBalance + interestOnBalance, 2)

    # Tests
    def TestCalculateMinimumMonthlyPayment():
        assert calculateMinimumMonthlyPayment(5000, 0.02) == 100.0,\
                "Minimum payment should be 100.0"
        assert calculateMinimumMonthlyPayment(4973.50, 0.02) == 99.47,\
                "Minimum payment should be 99.47"
        assert calculateMinimumMonthlyPayment(4947.14, 0.02) == 98.94,\
                "Minimum payment should be 98.94"
        print("minimumMonthlyPayment() - All tests pass!")

    def TestCalculateUnpaidBalance():
        assert calculateUnpaidBalance(5000, 100.0) == 4900.00,\
                "Unpaid balance should be 4900.00"
        assert calculateUnpaidBalance(4973.50, 99.47) == 4874.03,\
                "Unpaid balance should be 4874.03"
        assert calculateUnpaidBalance(4947.14, 98.94) == 4848.20,\
                "Unpaid balance should be 4848.20"
        print("calculateUnpaidBalance() - Alll tests pass!")

    def TestCalculateInterest():
        assert calculateInterest(4900.00, 0.18) == 73.50,\
                "Interest should be 73.50"
        assert calculateInterest(4874.03, 0.18) == 73.11,\
                "Interest should be 73.11"
        assert calculateInterest(4848.20, 0.18) == 72.72,\
                "Interest should be 72.72"
        print("calculateInterest() - All tests pass!")

    def TestCalculateNewBalancePlusInterest():
        assert calculateNewBalancePlusInterest(4900.00, 73.50) == 4973.50,\
                "New balance should be 4973.50"
        assert calculateNewBalancePlusInterest(4874.03, 73.11) == 4947.14,\
                "New balance should be 4947.14"
        assert calculateNewBalancePlusInterest(4848.20, 72.72) == 4920.92,\
                "New balance should be 4920.92"
        print("calculateNewBalancePlusInterest() - All tests pass!")

    TestCalculateMinimumMonthlyPayment()
    TestCalculateUnpaidBalance()
    TestCalculateInterest()
    TestCalculateNewBalancePlusInterest()

    currentBalance = balance

    for i in range(numOfMonths):
        minPayment = calculateMinimumMonthlyPayment(currentBalance, monthlyPaymentRate)
        unpaidBalance = calculateUnpaidBalance(currentBalance, minPayment)
        interestOnBalance = calculateInterest(unpaidBalance, annualInterestRate)
        currentBalance = calculateNewBalancePlusInterest(unpaidBalance, interestOnBalance)

    return currentBalance

# Main program
print("Remaining balance:", calculateBalance(42, 0.2, 0.04, 12))
print("Remaining balance:", calculateBalance(484, 0.2, 0.04, 12))


"""
A simple program for Coursera Python $ Function

Try to practise the return value 
"""
def computePay(hours, rate):
    if hours > 40:
        pay = 1.5 * rate * (hours-40) + rate * 40
    elif hours <= 40:
        pay = rate * 40    
    return pay
    
Hour = float(raw_input("Enter Hours: "))
Rate = float(raw_input("Enter Rate: "))
Pay = computePay(Hour,Rate)
print Pay
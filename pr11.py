principle=input("enter principle amount: ")
time=input("enter time  in years: ")
rate=input("enter the interest rate per year in percentage: ")
def compound_interest(principle,time ,rate):
    c=principle*(1+rate/100.0)**time
    return c
print "compound interest is %f"%compound_interest(principle,rate,time)

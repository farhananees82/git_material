# Scenario 
# usd, gbp, pkr, value 
def pkr_to_usd(pkr):
    rate = 250
    amount = pkr / rate
    return amount

pkr = int(input("Enter the pkr amount: "))
print(f'Your amount in USD: {pkr_to_usd(pkr)}')
print(f'Your amount in GBP: {pkr_to_gbp(pkr)}')
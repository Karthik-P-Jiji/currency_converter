from forex_python.converter import CurrencyRates
try:
    cr=CurrencyRates()
    amount=int(input("enter the amount you want to convert:"))
    from_currency=input("please enter the currency code that has to be converted:").upper()
    to_currency=input("please enter the currency code to convert:").upper()
    print("you are converting",amount,from_currency,"to",to_currency,".")
    output=cr.convert(from_currency,to_currency,amount)
    print("converted rate is:",output)
except:
    print("cant convert")
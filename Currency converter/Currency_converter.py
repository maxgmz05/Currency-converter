import requests

def currency_converter(a,b,x): #a function that takes a from currency as 'a', a to currency as 'b', and the amount to be converted as 'x' and returns the converted value
    url = f"https://api.apilayer.com/fixer/convert?to={b}&from={a}&amount={x}"

    payload = {}
    headers= {
    "apikey": "AZzo1VzjOz9TqTRj1L3i5UBlzg1iRhkJ" #for conversion I used fixer api, I started a new subscription and used my api key
    }
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    if response.json()['success']==False:
        err = response.json()['error']['type']
        print("ERROR")
        print("Error response:", err)
        quit()
    
    result = response.json()['result']
    
    return(result)

def currency_rate(a,b): #a function that takes a from currency as 'a', a to currency as 'b' and returns the rate 
    url = f"https://api.apilayer.com/fixer/convert?to={b}&from={a}&amount=1"

    payload = {}
    headers= {
    "apikey": "AZzo1VzjOz9TqTRj1L3i5UBlzg1iRhkJ"
    }
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    if response.json()['success']==False:
        err = response.json()['error']['type']
        print("ERROR")
        print("Error response:", err)
        quit()
        
    rate = response.json()['info']['rate']
    
    return(rate)

flag = True

while flag:
    from_curr = input("Enter the currency to convert from:")
    to_curr = input("Enter the currency to convert to:")
    flag2= int(input("\n\nChoose\n1. Convert currency\n2. Get rates\n:"))
    
    if flag2==1:
        amount = float(input("Enter the amount to convert:"))
        
        if amount <= 0:
            print("invalid input")
        
        result=currency_converter(from_curr,to_curr,amount)
        
        print(f"\n\n{amount} in {from_curr} is {result} in {to_curr}")
        
    elif flag2==2:
        rate=currency_rate(from_curr,to_curr)
        
        print(f'\n\n1 {from_curr} is {rate} {to_curr}')
        

    again= input("\n\nConvert again?[Y/N]\n")
    print("\n\n")
    
    if again in ['yes','Yes','YES','y','Y']:
        flag= True
        
    else:
        flag= False
        
import requests

KEY = "12cffd8f3bbe9e3c51f8eb45b049f0c9"

def main():
    base = "EUR"
    other = input("Exchange Currency(ies) or enter for all: ")
    #res = requests.get("https://api.fixer.io/latest",
                       #params={"base": base, "symbols": other})
    URL = "http://data.fixer.io/api/latest?access_key="+KEY
    res = requests.get(URL,
                      params= {"base": base, "symbols": other})
    data = res.json()

    if data['success'] == False:
            raise Exception(f"ERROR: {data['error']['code']} - {data['error']['type']}" )
    

    rates = data['rates']
    print("\nEUR translation rate to the following currencies:")
    print("\nCurrency    Today's Rate\n-------------------------")
    for currency, rate in rates.items():
        print(f"{currency} {rate:>20,.4f}")

if __name__ == "__main__":
    main()

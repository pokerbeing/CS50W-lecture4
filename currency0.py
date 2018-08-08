import requests

KEY = "12cffd8f3bbe9e3c51f8eb45b049f0c9"

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key="+KEY+"&base=EUR&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)
    print(f"Today's conversion rate from Euros to US Dollars is {data['rates']['USD']}.")

if __name__ == "__main__":
    main()

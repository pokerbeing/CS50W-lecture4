import requests

KEY = "12cffd8f3bbe9e3c51f8eb45b049f0c9"

def main():
    base = "USD"
    other = input("Second Currency: ")
    #res = requests.get("https://api.fixer.io/latest",
                       #params={"base": base, "symbols": other})
    res = requests.get("http://data.fixer.io/api/latest?access_key=12cffd8f3bbe9e3c51f8eb45b049f0c9",
                      params= {"base": base, "symbols": other})
    data = res.json()
    print(data)

    if res.status_code != 200:
        if data['error']['code'] == 105:
            raise Exception("ERROR: API base currency restricted to EUR.")
        if res.status_code == 202:
            raise Exception("ERROR: API request of invalid currency code.")
        raise Exception("ERROR: API request unsuccessful.")
    

    rate = data['rates'][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()

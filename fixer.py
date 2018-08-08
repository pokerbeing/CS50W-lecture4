import requests

KEY = "12cffd8f3bbe9e3c51f8eb45b049f0c9"

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key="+KEY)
    data =
    print(res.text)

if __name__ == "__main__":
    main()

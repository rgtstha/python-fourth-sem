import requests
from fact import Fact

api_url = "https://catfact.ninja/fact"

def get_random_fact(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        fact = Fact(data)
        return fact
    else:
        return None

random_fact = get_random_fact(api_url)
print(random_fact.fact)
print(random_fact.length)
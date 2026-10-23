import requests

def get_advice():
    try:
        response = requests.get("https://api.adviceslip.com/advice", timeout= 5)
        return response.json()["slip"]["advice"]
    except Exception:
        return "meow [ no internet :( ]"

print(get_advice())
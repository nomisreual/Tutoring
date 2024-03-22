import requests


def get_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()["value"]
    else:
        joke = "No joke"

    return joke


def len_joke():
    joke = get_joke()
    return len(joke)


if __name__ == "__main__":
    joke = get_joke()
    print(joke)

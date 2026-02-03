import requests

API_KEY = "d72d6d2fb6634c23a0e969e8cfd92038"


def get_top_news():

    url = "https://newsapi.org/v2/everything?q=tesla&" \
          "sortBy=publishedAt&apiKey=" \
          "d72d6d2fb6634c23a0e969e8cfd92038"

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])
    body = ""

    for article in articles:
        if article["title"] is not None:
            body = body + article["title"] + "\n" + str(article["description"]) + 2 * "\n"

    body = body.encode("utf-8")
    return body

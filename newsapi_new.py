import requests

API_KEY = "d72d6d2fb6634c23a0e969e8cfd92038"

def get_top_news():
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",     # change to "in" for India
        "apiKey": API_KEY,
        "pageSize": 5        # number of articles
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = data.get("articles", [])
    news_list = []
    body = ""
    for article in articles:
        if article["title"] is not None:
            title = article["title"]
            description = article["description"]
            url = article["url"]
            news_list.append(f"{title}\n{description}\nRead more: {url}\n")

    return "\n".join(news_list)

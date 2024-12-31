import requests

def get_top_news():
    api_key = "your_newsapi_key"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        if articles:
            return articles[0]['title']
    return "No news found."

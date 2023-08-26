import requests
import time

def fetch_and_display_news():
    api_key = ""  # Replace with your API key
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={api_key}"

    while True:
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200 and data["status"] == "ok":
                articles = data["articles"]

                for article in articles:
                    title = article["title"]
                    author = article.get("author", "Unknown Author")
                    description = article.get("description", "No description available")
                    content = article.get("content", "No content available")
                    published_at = article.get("publishedAt", "Unknown Date")
                    source = article.get("source", {}).get("name", "Unknown Source")
                    article_url = article.get("url", "")

                    # Display article information with appropriate formatting
                    print("Title:", title)
                    print("Author:", author)
                    print("Description:", description)
                    print("Content:", content)
                    print("Published At:", published_at)
                    print("Source:", source)
                    print("URL:", article_url)
                    print("\n")

                # Wait for 300 seconds (5 mins) before fetching and displaying news again
                time.sleep(300)

            else:
                print("Failed to fetch technology news.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_and_display_news()
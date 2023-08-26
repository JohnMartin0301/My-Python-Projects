import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def fetch_technology_news():
    api_key = ""  # Replace with the API key
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={api_key}"

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
                url = article.get("url", "")

                # Display article information with appropriate formatting
                news_text.insert(tk.END, f"Title: {title}\n", "title")
                news_text.insert(tk.END, f"Author: {author}\n", "content")
                news_text.insert(tk.END, f"Description: {description}\n", "content")
                news_text.insert(tk.END, f"Content: {content}\n", "content")
                news_text.insert(tk.END, f"Published At: {published_at}\n", "content")
                news_text.insert(tk.END, f"Source: {source}\n", "content")
                news_text.insert(tk.END, f"URL: {url}\n", "url")
                news_text.insert(tk.END, "\n")
        else:
            news_text.insert(tk.END, "Failed to fetch technology news.")

    except requests.exceptions.RequestException as e:
        news_text.insert(tk.END, f"An error occurred: {e}")

def open_article(url):
    if url:
        messagebox.showinfo("Full Article", f"Opening article: {url}")
        # Open the article in a web browser or perform any desired action

# Main window
window = tk.Tk()
window.title("Latest Technology News")
window.geometry("680x700")
window.configure(bg="#101010")

# Styling
style = ttk.Style()
style.configure("TFrame", background="#101010")
style.configure("TLabel", background="#101010", foreground="#00C8FF", font=("Arial", 20, "bold"))
style.configure("TButton", background="#101010", foreground="#101010", font=("Arial", 16))
style.configure("TText", background="#101010", foreground="#00C8FF", font=("Arial", 16))
style.configure("title.TLabel", font=("Arial", 20, "bold"), foreground="#00C8FF")
style.configure("content.TLabel", font=("Arial", 16), foreground="#FFFFFF")
style.configure("url.TLabel", font=("Arial", 14, "underline"), foreground="#00C8FF")

# Frame
frame = ttk.Frame(window)
frame.pack(padx=80, pady=110)

# labeling
title_label = ttk.Label(frame, text="Latest Technology News", style="TLabel")
title_label.pack(pady=20)

# Text widget to display news headlines
news_text = tk.Text(frame, height=10, width=80, wrap=tk.WORD, relief=tk.FLAT, bg="#101010", fg="#C0C0C0", font=("Arial", 20))
news_text.tag_configure("title", font=("Arial", 16, "bold"))
news_text.tag_configure("content", font=("Arial", 16))
news_text.tag_configure("url", font=("Arial", 14, "underline"))
news_text.pack(pady=20)

# Button to fetch news
fetch_button = ttk.Button(frame, text="Fetch News", command=fetch_technology_news)
fetch_button.pack(pady=5)

# GUI event loop
window.mainloop()
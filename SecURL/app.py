import tkinter as tk  # Import the Tkinter library for GUI
import urllib3  # Import the urllib3 library for making HTTP requests

def is_safe_url(url):
    http = urllib3.PoolManager()
    try:
        response = http.request('GET', url)  # Send a GET request to the specified URL
        if response.status < 400:  # Check if the response status is less than 400 (indicating a successful request)
            return True  # Return True if the URL is safe
        else:
            return False  # Return False if the URL is not safe
    except urllib3.exceptions.MaxRetryError:  # Handle MaxRetryError in case of connection failure
        return False  # Return False if there is an error

def check_url_safety():
    url = entry.get()  # Get the URL entered in the entry field
    if is_safe_url(url):  # Check if the URL is safe
        result_label["text"] = f"The URL {url} is safe."  # Update the result label with a safe message
        result_label["fg"] = "green"  # Set the text color of the result label to green
    else:
        result_label["text"] = f"The URL {url} is not safe."  # Update the result label with a not safe message
        result_label["fg"] = "red"  # Set the text color of the result label to red

root = tk.Tk()  # Create the root window
root.title("SecURL")  # Set the title of the GUI window
root.geometry("500x300")  # Set the size of the GUI window
root.configure(bg="#282a36")  # Set the background color of the GUI window

instruction_label = tk.Label(root, text="Enter a URL to check its safety:", font=("Arial", 16), fg="white", bg="#282a36")
instruction_label.pack(pady=20)  # Pack the instruction label into the window with padding

entry = tk.Entry(root, font=("Arial", 16), width=30, bg="#44475a", fg="white")
entry.pack(pady=10)  # Pack the entry field into the window with padding

button = tk.Button(root, text="Check URL Safety", font=("Arial", 16), command=check_url_safety, bg="#6272a4", fg="white", activebackground="#bd93f9", activeforeground="white")
button.pack(pady=10)  # Pack the button into the window with padding

result_label = tk.Label(root, text="", font=("Arial", 16), fg="white", bg="#282a36")
result_label.pack(pady=20)  # Pack the result label into the window with padding

root.mainloop()  # Run the GUI main loop
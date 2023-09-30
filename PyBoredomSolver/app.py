import requests

def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"An error occured : {str(e)}")
        return None

def main():
    while True:
        api_url = "https://www.boredapi.com/api/activity"

        api_data = fetch_api_data(api_url)

        if api_data:
            print("Data fetched successfully:")
            print(api_data)

        choice = input("Do you want to (R)Refresh or (T)Terminate? ").strip().lower()

        if choice == 't':
            print("Program terminated.")
            break
        elif choice != 'r':
            print("Invalid choice. Please enter 'R' to refresh or 'T' to terminate.")

if __name__ == "__main__":
    main()
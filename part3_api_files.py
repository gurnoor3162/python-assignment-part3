import requests

def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
        data = response.json()
        
        with open("python_notes.txt", "w") as file:
            file.write(str(data))
        
        print("Data saved to python_notes.txt")

    except Exception as e:
        with open("error_log.txt", "w") as file:
            file.write(str(e))
        
        print("Error occurred. Logged in error_log.txt")


def main():
    fetch_data()


if __name__ == "__main__":
    main()

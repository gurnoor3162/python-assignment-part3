import requests

def fetch_data():
    try:
        url = "https://jsonplaceholder.typicode.com/posts/1"
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Write data to file
        with open("python_notes.txt", "w") as file:
            file.write(str(data))

        print("Data saved successfully!")

    except Exception as e:
        # Log error
        with open("error_log.txt", "w") as file:
            file.write(str(e))

        print("Error occurred. Check error_log.txt")


def main():
    fetch_data()


if __name__ == "__main__":
    main()

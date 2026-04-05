import requests

# -------------------- WRITE NOTES --------------------

notes = [
  "Python is easy to learn",
  "Lists store multiple values",
  "Dictionaries store key value pairs",
  "Loops help repeat tasks"
]

try:
  file = open("python_notes.txt", "w")

  for line in notes:
    file.write(line + "\n")

  file.close()
  print("Notes written successfully")

except Exception as e:
  print("Error writing file:", e)


# -------------------- READ NOTES --------------------

try:
  file = open("python_notes.txt", "r")

  print("\nReading notes:")
  for line in file:
    print(line.strip())

  file.close()

except Exception as e:
  print("Error reading file:", e)


# -------------------- ERROR HANDLING --------------------

try:
  x = int(input("\nEnter a number: "))
  result = 10 / x
  print("Result:", result)

except ValueError:
  print("Invalid input, not a number")

except ZeroDivisionError:
  print("Cannot divide by zero")

except Exception as e:
  print("Some error occurred:", e)

  # log error
  file = open("error_log.txt", "a")
  file.write(str(e) + "\n")
  file.close()


# -------------------- API CALL --------------------

try:
  url = "https://jsonplaceholder.typicode.com/posts/1"
  response = requests.get(url)

  data = response.json()

  print("\nAPI Data:")
  print("Title:", data["title"])
  print("Body:", data["body"])

except Exception as e:
  print("API error:", e)

  file = open("error_log.txt", "a")
  file.write("API Error: " + str(e) + "\n")
  file.close()

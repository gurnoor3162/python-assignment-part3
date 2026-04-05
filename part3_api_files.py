with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data\n")
    f.write("Topic 2: Lists are ordered\n")
    f.write("Topic 3: Dictionaries store key value pairs\n")
    f.write("Topic 4: Loops repeat tasks\n")
    f.write("Topic 5: Exception handling prevents crashes\n")

print("File written")

#appending 2 lines
with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Extra: Python is simple\n")
    f.write("Extra: Practice makes perfect\n")

print("More lines added")

#task1
with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(len(lines)):
    print(str(i+1) + ".", lines[i].strip())

print("Total lines:", len(lines))

#keyword search
key = input("Enter keyword: ").lower()
found = False

for line in lines:
    if key in line.lower():
        print(line.strip())
        found = True

if not found:
    print("Nothing found")

#task2
import requests

try:
    res = requests.get("https://dummyjson.com/products?limit=5", timeout=5)
    data = res.json()

    print("\nProducts:")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except:
    print("Error fetching products")

#filter rating
filtered = []
for p in data["products"]:
    if p["rating"] >= 4.5:
        filtered.append(p)

print("\nHigh rated:")
for p in filtered:
    print(p["title"])

#category search
try:
    res = requests.get("https://dummyjson.com/products/category/laptops", timeout=5)
    data2 = res.json()

    print("\nLaptops:")
    for p in data2["products"]:
        print(p["title"], p["price"])

except:
    print("Error fetching laptops")

#POST request
try:
    res = requests.post("https://dummyjson.com/products/add", json={
        "title": "Test Product",
        "price": 500
    })
    print("\nProduct added:", res.json()["title"])

except:
    print("POST failed")

#task3
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("a", 2))

def read_file_safe(name):
    try:
        with open(name, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Done")

print(read_file_safe("python_notes.txt"))
print(read_file_safe("wrong.txt"))

#task3
while True:
    user = input("Enter product id or quit: ")

    if user == "quit":
        break

    if not user.isdigit():
        print("Invalid input")
        continue

    pid = int(user)

    if pid < 1 or pid > 100:
        print("Out of range")
        continue

    try:
        res = requests.get(f"https://dummyjson.com/products/{pid}", timeout=5)

        if res.status_code == 404:
            print("Not found")
        else:
            p = res.json()
            print(p["title"], "-", p["price"])

    except:
        print("Error")

#task4
from datetime import datetime

def log_error(msg):
    with open("error_log.txt", "a") as f:
        f.write(str(datetime.now()) + " - " + msg + "\n")

#connection error
try:
    requests.get("https://fake-url-xyz.com", timeout=3)
except:
    log_error("Connection error")

#404 error
res = requests.get("https://dummyjson.com/products/999")
if res.status_code != 200:
    log_error("Product 999 not found")

#showing logs
print("\nLogs:")
with open("error_log.txt", "r") as f:
    print(f.read())

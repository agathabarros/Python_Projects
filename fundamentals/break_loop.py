cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...!")
        continue
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
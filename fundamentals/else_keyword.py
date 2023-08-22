cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
all_successful = True

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...!")
        all_successful = False
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else:
    print("All cars built successfully. No faulty cars!")
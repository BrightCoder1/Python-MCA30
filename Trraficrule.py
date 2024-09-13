signal = input("Enter the signal: ")

if signal == "red":
    print("Car has to stop.")
elif signal == "yellow":
    print("Car has to wait.")
elif signal == "green":
    print("Car is allowed to move.")
else:
    print("Unrecognized Signal.")
    
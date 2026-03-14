import datetime

log_file = "keystroke_log.txt"

print("Safe Keylogging Simulation")
print("Type something and press Enter (type 'exit' to stop)\n")

while True:
    user_input = input("Input: ")

    if user_input.lower() == "exit":
        print("Simulation ended.")
        break

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {user_input}\n")

print(f"Logged inputs saved to {log_file}")
import os

def display_banner():
    print("\n      ██████████████████████████████             ")
    print("    ██████████████████████████████████              ")
    print("   ████████████     ███     ███████████             ")
    print("  ██████████         █         █████████           ")
    print(" █████████     ███████████     ██████████          ")
    print("████████     ██    ███    ██     ████████           ")
    print("███████      █      █      █      ███████          ")
    print("███████      █      █      █      ███████")
    print("████████     ██    ███    ██     ████████")
    print(" █████████     ███████████     █████████ ")
    print("  ██████████         █         █████████  ")
    print("   ████████████     ███     ███████████   ")
    print("    ██████████████████████████████████    ")
    print("      ██████████████████████████████      ")


    print("\n\n")
    print("  ██  ██████  ██  █████      ██   ██   ████     ████    ██████  ██████  ")
    print("  ██  ██  ██  ██  ██         ██   ██  ██  ██   ██   ██  ██  ██  ██  ")
    print("  ██  ██ ██   ██  █████         ██    ██  ██   ██   ██  ██████  █████   ")
    print("  ██  ██  ██  ██     ██         ██    ██  ██   ██   ██  ██    ██  ██  ")
    print("  ██  ██   ██ ██  █████       ██████   ████    ██   ██  ██    ██  ")

    print("[1] Start SSH Honeypot (Port 2222)")
    print("[2] Start Telnet Honeypot (Port 2323)")
    print("[3] Exit\n")

def main():
    while True:
        display_banner()
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            print("\nLaunching SSH Honeypot on Port 2222...\n")
            os.system("python iris_honeypot.py 2222")
        elif choice == "2":
            print("\nLaunching Telnet Honeypot on Port 2323...\n")
            os.system("python iris_honeypot.py 2323")
        elif choice == "3":
            print("Exiting Iris_Hport. Goodbye!")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
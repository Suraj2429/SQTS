import os 
import shutil
from datetime import datetime, timedelta

FOLDER_PATH = "test_folder"
LOG_FILE = "log.txt"

def log(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")

def organize_files():
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]
            new_folder = os.path.join(FOLDER_PATH, ext)

            if not os.path.exists(new_folder):
                os.makedirs(new_folder)
            
            shutil.move(file_path, os.path.join(new_folder, file))
            log(f"Moved {file} to {ext}/")

    print("Files organized successfully...!")

def rename_files():
    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            ext = file.split(".")[-1]
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            new_name = f"{timestamp}_{file}"
            new_path = os.path.join(FOLDER_PATH, new_name)

            os.rename(file_path, new_path)
            log(f"Renamed {file} to {new_name}")

    print("Files renamed successfully...!")

def delete_old_files():
    days = int(input("Enter the number of days to delete files older than: "))
    now = datetime.now()

    for file in os.listdir(FOLDER_PATH):
        file_path = os.path.join(FOLDER_PATH, file)

        if os.path.isfile(file_path):
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if now - file_time > timedelta(days=days):
                os.remove(file_path)
                log(f"Deleted {file}")

    print("Old files deleted successfully...!")

def view_log():
    try:
        with open(LOG_FILE, "r") as f:
            print("\nLogs:\n")
            print(f.read())
    except FileNotFoundError:
        print("Log file not found.")

try:
    while True:
        print("\nFILE MANAGEMENT SYSTEM\n")
        print("1. Organize Files")
        print("2. Rename Files")
        print("3. Delete Old Files")
        print("4. View Log")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            organize_files()
        elif choice == "2":
            rename_files()
        elif choice == "3":
            delete_old_files()
        elif choice == "4":
            view_log()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

except KeyboardInterrupt:
    print("\nProgram stopped safely")
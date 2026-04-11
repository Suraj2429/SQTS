import os
import shutil
import pandas as pd
from datetime import datetime, timedelta

FOLDER_PATH = "test_folder"


# FILE ORGANIZER
def organize_files():
    try:
        for file in os.listdir(FOLDER_PATH):
            file_path = os.path.join(FOLDER_PATH, file)

            if os.path.isfile(file_path):
                ext = file.split('.')[-1]

                folder = os.path.join(FOLDER_PATH, ext)

                if not os.path.exists(folder):
                    os.makedirs(folder)

                shutil.move(file_path, os.path.join(folder, file))

        print("Files organized by type!")

    except Exception as e:
        print("Error:", e)


# CSV CLEANER + REPORT
def clean_csv():
    try:
        file = input("Enter CSV file name: ")

        data = pd.read_csv(file)

        print("\nOriginal Data:\n", data)

        cleaned = data.drop_duplicates()

        cleaned.to_csv("cleaned_data.csv", index=False)

        print("\nSummary Report:")
        print("Total rows:", len(data))
        print("After cleaning:", len(cleaned))

        print("Cleaned file saved!")

    except Exception as e:
        print("Error:", e)


# DELETE OLD FILES
def delete_old_files():
    try:
        days = int(input("Delete files older than (days): "))
        now = datetime.now()

        for file in os.listdir(FOLDER_PATH):
            file_path = os.path.join(FOLDER_PATH, file)

            if os.path.isfile(file_path):
                file_time = datetime.fromtimestamp(os.path.getmtime(file_path))

                if now - file_time > timedelta(days=days):
                    os.remove(file_path)
                    print(f"Deleted: {file}")

        print("Old files deleted!")

    except Exception as e:
        print("Error:", e)


# CV SELECTION
def select_cv():
    role = input("Enter job role (python/web/java): ").lower()

    keywords = {
        "python": ["python", "ml", "ai", "data"],
        "web": ["html", "css", "javascript", "react"],
        "java": ["java", "spring"]
    }

    folder = "cvs"

    print("\nMatching CVs:\n")

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        with open(path, "r") as f:
            content = f.read().lower()

            score = 0

            for word in keywords.get(role, []):
                if word in content:
                    score += 1

            if score > 0:
                print(f"{file} → Match Score: {score}")


# MAIN MENU
while True:
    print("\n===== AUTOMATION TOOL =====")
    print("1. Organize Files")
    print("2. Clean CSV Data")
    print("3. Delete Old Files")
    print("4. CV Selection")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        organize_files()
    elif choice == '2':
        clean_csv()
    elif choice == '3':
        delete_old_files()
    elif choice == '4':
        select_cv()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
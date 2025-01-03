import os
import sys

def create_quest_folder(number):
    # Create folder name
    folder_name = f"Quest {number}"
    
    # Create the folder
    try:
        os.makedirs(folder_name, exist_ok=True)
        print(f"Folder '{folder_name}' created successfully.")
        
        # Create 3 input files inside the folder
        for i in range(1, 4):
            file_path = os.path.join(folder_name, f"input{i}.txt")
            with open(file_path, 'w') as file:
                file.write(f"")
            print(f"Created {file_path}")

        file_path = os.path.join(folder_name,f"q{number}.py")
        with open(file_path, 'w') as file:
                file.write(f"")
        print(f"Created {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Check if an argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        create_quest_folder(number)
    except ValueError:
        print("Please provide a valid integer.")

if __name__ == "__main__":
    main()
import csv
import os

def create_contact_csv(file_path):
    """
    Creates a new CSV file for contacts.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Number'])  # Write header row

def read_contact_csv(file_path):
    """
    Reads and prints the contents of a CSV file.
    """
    if not os.path.exists(file_path):
        print(f"{file_path} does not exist.")
        return

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))  # Print each row

def write_contact_csv(file_path, contacts):
    """
    Writes names and phone numbers to a CSV file, overwriting existing data.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Number'])  # Write header row
        for contact in contacts:
            writer.writerow(contact)  # Write each contact

def append_contact_csv(file_path, contacts):
    """
    Appends names and phone numbers to a CSV file.
    """
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow(contact)  # Append each contact

def list_csv_files(directory):
    """List all CSV files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.csv')]

def prompt_user_for_file(files):
    """Prompt the user to select a file from the list."""
    print("Please select a contact book:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    choice = int(input("Enter the number of the file you wish to open: ")) - 1
    return files[choice]

def get_contacts_from_user():
    """Get contacts from the user."""
    contacts = []
    while True:
        name = input("Enter name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        number = input("Enter phone number: ")
        contacts.append((name, number))
    return contacts

def main():
    directory = './'  # You can change this to the directory where your CSV files are located
    while True:
        # Display menu options
        print("1. Create a new contact book")
        print("2. Read a contact book")
        print("3. Write to a contact book")
        print("4. Append to a contact book")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the file path for the new contact book: ")
            create_contact_csv(file_path)
        elif choice == '2':
            csv_files = list_csv_files(directory)
            if not csv_files:
                print("No CSV files found in the directory.")
                continue
            selected_file = prompt_user_for_file(csv_files)
            read_contact_csv(os.path.join(directory, selected_file))
        elif choice == '3':
            csv_files = list_csv_files(directory)
            if not csv_files:
                print("No CSV files found in the directory.")
                continue
            selected_file = prompt_user_for_file(csv_files)
            contacts = get_contacts_from_user()
            write_contact_csv(os.path.join(directory, selected_file), contacts)
        elif choice == '4':
            csv_files = list_csv_files(directory)
            if not csv_files:
                print("No CSV files found in the directory.")
                continue
            selected_file = prompt_user_for_file(csv_files)
            contacts = get_contacts_from_user()
            append_contact_csv(os.path.join(directory, selected_file), contacts)
        elif choice == '5':
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

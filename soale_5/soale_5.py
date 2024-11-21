import os
import zipfile
import datetime

def backup_directory():
    try:
        dir_to_backup = input("Enter directory to back up: ")
        if not os.path.exists(dir_to_backup):
            print("Error: The specified directory does not exist.")
            return
        backup_dest = input("Enter backup destination: ")

        if not os.path.exists(backup_dest):
            os.makedirs(backup_dest)

        backup_file = os.path.join(backup_dest,
                                   f"{os.path.basename(dir_to_backup)}_backup_{datetime.datetime.now().strftime('%Y-%m-%d')}.zip")

        with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(dir_to_backup):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, os.path.join(dir_to_backup, '..')))

        print(f"Backup successful! Backup saved as {backup_file}")

    except Exception as e:
        print(f"An error occurred during backup: {e}")


def restore_backup():
    try:
        backup_dest = input("Enter the backup folder path: ")
        backup_files = [f for f in os.listdir(backup_dest) if f.endswith('.zip')]

        if not backup_files:
            print("No backup files found.")
            return

        print("Available Backups:")
        for i, backup_file in enumerate(backup_files):
            print(f"{i + 1}. {backup_file}")

        choice = int(input("Choose a backup to restore: ")) - 1

        if choice < 0 or choice >= len(backup_files):
            print("Invalid choice.")
            return

        restore_dest = input("Enter destination for restoration: ")

        if not os.path.exists(restore_dest):
            os.makedirs(restore_dest)

        with zipfile.ZipFile(os.path.join(backup_dest, backup_files[choice]), 'r') as zipf:
            zipf.extractall(restore_dest)

        print("Restoration successful!")

    except Exception as e:
        print(f"An error occurred during restoration: {e}")


def main():
    while True:
        print("\n1. Backup Directory")
        print("2. Restore Backup")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            backup_directory()
        elif choice == '2':
            restore_backup()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
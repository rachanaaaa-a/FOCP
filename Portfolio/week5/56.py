#6Write a program that takes the name of a file as a command-line argument, and creates a backup copy of that file. The backup should contain an exact copy of the
#contents of the original and should, obviously, have a different nam Hint: By now, you should be getting the idea that there is a built-in way to do the heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the doc
import shutil
import sys

def create_backup(original_file, backup_file):
    try:
        shutil.copyfile(original_file, backup_file)
        print(f"Backup of '{original_file}' created as '{backup_file}'")
    except FileNotFoundError:
        print(f"Error: The file '{original_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_backup.py <original_file> <backup_file>")
    else:
        create_backup(sys.argv[1], sys.argv[2])

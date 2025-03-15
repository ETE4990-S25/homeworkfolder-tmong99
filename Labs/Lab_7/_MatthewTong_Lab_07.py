import os
import hashlib
from collections import defaultdict

def change_to_shah256(file_path):
    """
    Calculate the SHA-256 checksum of the file.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f: # rb is read as binary
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except(IOError, OSError):
        return None

def find_duplicate_files(start_path):
    """
    Find Identical Files by it's sha-256 hash
    """
    hash_dict = defaultdict(list) # Initialize a dictionary with a list as a key

    # Walk through the directory
    for root, _, files in os.walk(start_path):
        for file in files:
            full_path = os.path.join(root, file) # Gets file path of example.txt ex: "user/documents"
            file_hash = change_to_shah256(full_path)
            if file_hash:
                hash_dict[file_hash].append(full_path)

    duplicates = {hash_val: paths for hash_val, paths in hash_dict.items() if len(paths) > 1}

    return duplicates

def print_duplicates(duplicates):
    """
    Print the Duplicate files and their paths
    """
    if not duplicates:
        print("You Have No Duplicate Files")
    else:
        for hash_val, paths in duplicates.items():
            print(f"Duplicate files with hash {hash_val}:")
            for path in paths:
                print(f"  {path}")
            print()

if __name__ == "__main__":
    start_directory = input("Enter the directory to search: ")

    if os.path.isdir(start_directory):
        duplicates = find_duplicate_files(start_directory)
        print_duplicates(duplicates)
    else:
        print("Invalid directory")
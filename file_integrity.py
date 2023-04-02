import os
import hashlib
import time
import logging

logging.basicConfig(filename='file_integrity.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_hash(filename):
    # Calculate the hash value of a file
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def monitor_files(directory):
    # Monitor files in a directory for changes
    files = {}
    for filename in os.listdir(directory):
        files[filename] = get_hash(os.path.join(directory, filename))

    while True:
        for filename in os.listdir(directory):
            path = os.path.join(directory, filename)
            if not os.path.isfile(path):
                continue
            current_hash = get_hash(path)
            if current_hash != files.get(filename):
                logging.warning("File %s has been modified!" % filename)
                files[filename] = current_hash
        time.sleep(5)

if __name__ == '__main__':
    monitor_files('/var/log')

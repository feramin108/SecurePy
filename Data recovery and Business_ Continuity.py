import os
import shutil
import datetime

# Define source and destination directories
src_dir = "C:\\data\\"
dst_dir = "D:\\backup\\"

# Define log file
log_file = "D:\\logs\\backup_log.txt"

# Create backup directory if it does not exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

# Get current date and time
now = datetime.datetime.now()

# Log start time
with open(log_file, "a") as f:
    f.write(f"Backup started at {now}\n")

# Backup files
for root, dirs, files in os.walk(src_dir):
    for file in files:
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dst_dir, os.path.relpath(src_file, src_dir))
        shutil.copy2(src_file, dst_file)

# Log end time
now = datetime.datetime.now()
with open(log_file, "a") as f:
    f.write(f"Backup completed at {now}\n")

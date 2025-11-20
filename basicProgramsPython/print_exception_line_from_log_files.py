import os

def search_logs(log_dir, keyword):
    # Loop through all files in the log directory
    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)

        # Only process files (skip folders)
        if os.path.isfile(file_path):
            with open(file_path, "r", errors="ignore") as f:
                for line in f:
                    if keyword.lower() in line.lower():
                        print(f"[{filename}] {line.strip()}")

# Example usage
search_logs("/path/to/logs", "exception")

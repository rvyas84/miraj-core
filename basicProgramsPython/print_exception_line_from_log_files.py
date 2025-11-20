import os

def search_logs(log_dir, keywords):
    # Normalize all keywords to lowercase
    keywords = [k.lower() for k in keywords]

    for filename in os.listdir(log_dir):
        file_path = os.path.join(log_dir, filename)

        if os.path.isfile(file_path):
            with open(file_path, "r", errors="ignore") as f:
                for line in f:
                    lower_line = line.lower()
                    # Check if any keyword exists in the line
                    if any(k in lower_line for k in keywords):
                        print(f"[{filename}] {line.strip()}")

# Example usage
search_logs("/path/to/logs", ["exception", "error"])

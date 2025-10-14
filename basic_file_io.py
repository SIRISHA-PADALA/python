FILE_NAME = "sample_output.txt"
data_to_write = ["Line 1: Hello GitHub!", "Line 2: This is a file I/O demo.", "Line 3: End of file."]

# --- Write to File ---
try:
    with open(FILE_NAME, 'w') as file:
        for line in data_to_write:
            file.write(line + '\n')
    print(f"Successfully wrote {len(data_to_write)} lines to {FILE_NAME}")

    # --- Read from File ---
    print(f"\n--- Content of {FILE_NAME} ---")
    with open(FILE_NAME, 'r') as file:
        content = file.read()
        print(content)

except IOError as e:
    print(f"An I/O error occurred: {e}")
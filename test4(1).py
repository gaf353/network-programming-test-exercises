import os

while True:
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"'{filename}' was not found.")
        choice = input("Try another filename? (y/n): ")
        if choice.lower() == 'y':
            continue          
        else:
            print("Exiting.")
            break
    else:

        numbered_lines = []
        for i, line in enumerate(lines, start=1):
            numbered_line = f"{i}: {line.rstrip(chr(10))}"
            print(numbered_line)
            numbered_lines.append(numbered_line)


        base_name = os.path.splitext(filename)[0]
        save_name = base_name + ".sav"
        with open(save_name, 'w', encoding='utf-8') as out:
            for nl in numbered_lines:
                out.write(nl + "\n")
        print(f"Saved with line numbers as {save_name}")
        break
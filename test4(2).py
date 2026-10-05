while True:
    filename = input("Enter filename to read: ")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"'{filename}' was not found.")
        choice = input("Try another filename? (y/n): ")
        if choice.lower() == 'y':
            continue
        else:
            print("Exiting.")
            break
    else:
        char_count = sum(1 for ch in content if not ch.isspace())
        word_count = len(content.split())
        line_count = len(content.split("\n"))

        print(f"characters : {char_count}")
        print(f"words      : {word_count}")
        print(f"lines      : {line_count}")
        break
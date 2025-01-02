class Handler:
    try:
        with open("text.txt", 'r') as f:
            text = f.read()
            words = text.split()
            word_count = len(words)
        print("Words have been counted.")       

        with open("Count.txt", 'w+') as o:
            o.write(f"Total number of words: {word_count}\n")
        print(f"Word count written to file Count.txt")

    except FileNotFoundError:
        print("Requested File cannot be found")

Handler()
    
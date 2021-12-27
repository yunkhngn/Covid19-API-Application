LANGUAGE = "English"

text = "Hello World"

while True:
    if LANGUAGE == "English":
        print("Switch to english")
        text = "Hello World"
        print(text)
        print("------------------------------------------------")
    elif LANGUAGE == "Vietnamese":
        print("Switch to vietnamese")
        text = "Xin chào thế giới"
        print(text)
        print("------------------------------------------------")
    choice = input("Enter your choice: ")
    if choice == "1":
        LANGUAGE = "English"
        print(text)
    elif choice == "2":
        LANGUAGE = "Vietnamese"
        print(text)
    else:
        exit()
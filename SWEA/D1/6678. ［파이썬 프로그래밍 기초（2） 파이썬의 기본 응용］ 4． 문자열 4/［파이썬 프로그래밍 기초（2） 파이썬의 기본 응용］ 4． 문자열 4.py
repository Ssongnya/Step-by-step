while True:
    try:
        text = input()

        if text == "":
            break

        print(f">> {text.upper()}")
    except EOFError:
        break

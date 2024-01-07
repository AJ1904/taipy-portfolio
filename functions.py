def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)  # Adjust the delay (in seconds) for typing speed
    print()  # Move to the next line after typing the entire text

# for text in typing_texts:
#     type_text(text)
#     # Optional: add a delay between each text
#     time.sleep(1)  # Adjust the delay (in seconds) between each text
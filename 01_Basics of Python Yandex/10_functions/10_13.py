__data = set()


def modern_print(text):
    global __data
    if text not in __data:
        print(text)
        __data.add(text)


modern_print("Hello!")
modern_print("Hello!")
modern_print("How do you do?")
modern_print("Hello!")

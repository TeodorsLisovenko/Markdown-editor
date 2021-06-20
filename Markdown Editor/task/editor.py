# write your code here

text_container = ""


def apply_bold():
    global text_container
    user_text = input("Text: ")
    text_container += f"**{user_text}**"


def apply_italic():
    global text_container
    user_text = input("Text: ")
    text_container += f"*{user_text}*"


def apply_header():
    global text_container
    header_level = int(input("Level: "))
    user_text = input("Text: ")

    if header_level in range(1, 6):
        text_container += "#" * header_level + f" {user_text}\n"
    else:
        print("The level should be within the range of 1 to 6")


def apply_link():
    global text_container
    label = input("Label: ")
    url = input("URL: ")
    text_container += f"[{label}]({url})"


def apply_inline_code():
    global text_container
    user_text = input("Text: ")
    text_container += f"`{user_text}`"


def apply_newline():
    global text_container
    text_container += "\n"


def apply_plain():
    global text_container
    user_text = input("Text: ")
    text_container += user_text


available_formatters = (
    "plain", "bold", "italic", "header", "link", "inline-code", "new-line")
special_commands = ("!help", "!done")

while True:
    user_action = input("Choose a formatter: ")
    if user_action in available_formatters:

        if user_action == available_formatters[1]:
            apply_bold()
        elif user_action == available_formatters[2]:
            apply_italic()
        elif user_action == available_formatters[3]:
            apply_header()
        elif user_action == available_formatters[4]:
            apply_link()
        elif user_action == available_formatters[5]:
            apply_inline_code()
        elif user_action == available_formatters[6]:
            apply_newline()
        else:
            apply_plain()

        print(text_container)


    elif user_action in special_commands:
        if user_action == special_commands[0]:
            print("Available formatters: " + " ".join(available_formatters) + "\nSpecial_commands: " + " ".join(
                special_commands))
        else:
            break
    else:
        print("Unknown formatting type or command")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Введіть ім'я користувача та номер телефону"
        except ValueError:
            return "Введіть номер телефону у вірному форматі"
        except KeyError:
            return "Такого користувача не знайдено"
    return inner

contacts = {}

@input_error
def hello(*args):
    return "Як я можу вам допомогти?"

@input_error
def add(name, phone):
    contacts[name] = phone
    return f"Контакт {name} з номером телефону {phone} був успішно доданий"

@input_error
def change(name, phone):
    contacts[name] = phone
    return f"Номер телефону для контакту {name} був успішно змінений"

@input_error
def phone(name):
    return f"Номер телефону для контакту {name}: {contacts[name]}"

@input_error
def show_all(*args):
    return "\n".join([f"Контакт {name} з номером телефону {phone}" for name, phone in contacts.items()])

@input_error
def exit(*args):
    return "До побачення!"

HANDLERS = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "good bye": exit,
    "close": exit,
    "exit": exit,
}

def parse_command(command):
    command = command.lower().split()
    if command[0] == "show" and command[1] == "all":
        command_name = "show all"
        command_args = command[2:]
    else:
        command_name = command[0]
        command_args = command[1:]
    return command_name, command_args


def handle_command(command_name, command_args):
    if command_name in HANDLERS:
        return HANDLERS[command_name](*command_args)
    else:
        return "Неправильна команда"

def main():
    while True:
        command = input()
        command_name, command_args = parse_command(command)
        response = handle_command(command_name, command_args)
        print(response)
        if command_name in ["good bye", "close", "exit"]:
            break

if __name__ == "__main__":
    main()

def choice_validation(max_choice: int) -> str:
    while True:
        try:
            user_resp = int(input("CHOICE: "))

            if user_resp < 0 or user_resp > max_choice:
                raise ValueError()
        except ValueError:
            print(f"Invalid Answer: Please enter a number between 1 and {max_choice}")
            continue
        else:
            return user_resp


def remove_special_chars(value: str) -> str:
    return "".join(i for i in value if i.isalnum() or i.isspace())


def string_validation(value: str):
    return remove_special_chars(input(f"Enter {value}: "))


# def number_validation(min_val:int, max_val:int):

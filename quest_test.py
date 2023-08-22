import questionary


class NumberValidation(questionary.Validator):
    def validate(self, document):
        if len(document.text) == 0:
            raise questionary.ValidationError(
                message="Please enter a value", cursor_position=len(document.text)
            )
        if not document.text.isdigit():
            raise questionary.ValidationError(
                message="Please enter a valid number", cursor_position=len(document.text)
            )


def number_range_validation(val_number, low: int = 1, high: int = 100):
    "val_number has to be equal to or between low and high range"
    val_number = int(val_number)
    if val_number < low or val_number > high:
        print(f"Number should be between [{low} - {high}]")
        return False
    return True


number = -1
while not number_range_validation(number, 1, 10):
    number = questionary.text(
        "Please enter a number:", validate=NumberValidation, validate_while_typing=False
    ).ask()


questionary.confirm("")

# test = questionary.checkbox("What do you want to do", choices=["1", "2", "3", "4"]).ask()

# print("Saved value was:", test)


# answers = questionary.form(
#     first = questionary.select("Choose an option", ["Game Settings", "Character Select", "Play Game"]),
#     confimed = questionary.confirm("Are you happy with your choice?")
# ).ask()

# print(answers)


# questions = [
#     {"type": "text", "name": "first_name", "message": "What is your first name"},
#     {"type": "text", "name": "last_name", "message": "What is your last name"},
# ]

# answers = questionary.prompt(questions)

# print(answers)

import questionary 


test = questionary.checkbox("What do you want to do",
                   choices=['1','2','3','4']).ask()

print("Saved value was:", test)



questions = [
    {
        'type':'input',
        'name':'first_name',
        "message": "What is your first name"
    },
    {
        'type':'input',
        'name':'last_name',
        "message": "What is your last name"  
    }
]

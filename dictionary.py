#opening the file:
import json
from difflib import get_close_matches
data = json.load(open("data.json"))
data["rain"]

def translate(user_input):
    user_input = user_input.lower()
    if user_input in data:
        return data[user_input]
    elif user_input.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[user_input.title()]
    elif user_input.upper() in data:
        return data[user_input.upper()]
    elif len(get_close_matches(user_input, data.keys())) > 0:
        #if user_input.capitalize() == get_close_matches(user_input, data.keys())[0]:
            #return data[user_input.capitalize()]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(user_input, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(user_input, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry"
    else:
        return "The word doesn't exist. Please double check it"

user_input = input("Enter the word: ")

output = translate(user_input)


if type(output) == list:
    for element in output:
        print(element)
else:
    print(output)




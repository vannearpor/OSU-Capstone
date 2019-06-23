#Receives input from engine and understands what the user is trying to accomplish

#List of possible actions, directions, items, and characters that the user can choose from

class Parser:
    
    ACTIONLIST = ["look", "look at", "take", "drop", "view", "go", "fight", "interact"]
    DIRECTIONLIST = ["north", "south", "east", "west"]
    ITEMLIST = ["sword", "boat", "key", "statue", "tree", "cage", "bones", "dung", "gate", "sign", "tools", "furnace"]
    CHARLIST = ["behemoth", "lyn", "fisherman", "elder"]
    
    def parse_command(userInput):
        command = userInput.lower()
        command_words = userInput.split()

        #First word should be the action word
        if command_words:
            temp_action = command_words[0]
            if temp_action in Parser.ACTIONLIST:
                action = Parser.ACTIONLIST[temp_action]
                del command_words[0]
            else:
                action = None
        else:
            action = None

        #If action word is invalid, nothing can happen return None for all
        if action is None:
            print("Please enter a valid command.")
            return (None, None, None, None)

        if action == "go":

            #have user find which way to go, north south east or west
            direction = None
            if command_words:
                for word in command_words:
                    if word in Parser.DIRECTIONLIST:
                        direction = Parser.DIRECTIONLIST[word]
                        break

            #user provides go with no more words in the command word list
            if direction is None:
                print("You provided a \"go\" command with no direction. Please enter a valid command.")
                return (None, None, None, None)

            return (action, direction, None, None)

        else:
            item = None
            character = None

            if command_words:
                for word in command_words:
                    if word in Parser.ITEMLIST:
                    item = Parser.ITEMLIST[word]

                    if word in Parser.CHARLIST:
                    character = Parser.CHARLIST[word]

            return (action, None, item, character)








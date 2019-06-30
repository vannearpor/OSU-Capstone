#Receives input from engine and understands what the user is trying to accomplish

#List of possible actions, directions, items, and characters that the user can choose from

class Parser:
    
    ACTIONLIST = ["look", "look at", "take", "drop", "view", "go", "fight", "interact", "quit", "help"]
    DIRECTIONLIST = ["north", "south", "east", "west"]
    ITEMLIST = ["sword", "boat", "key", "statue", "tree", "cage", "bones", "dung", "gate", "sign", "tools", "furnace"]
    CHARLIST = ["behemoth", "lyn", "fisherman", "elder"]
    
    def parse_command(userInput):
        command = userInput.lower()
        command_words = userInput.split()

        #First word should be the action word
        if command_words:
            temp_action = command_words[0]
            action_list_length = len(Parser.ACTIONLIST)
            
            for i in range(action_list_length):
                if temp_action == Parser.ACTIONLIST[i]:
                    action = Parser.ACTIONLIST[i]
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

def main():
    #parser will keep running until a valid command is given
    while True:
        print('\n')
        print('\n')

        cmd_line_input = input("What would you like to do next?\n")

        print('\n')

        if cmd_line_input == "quit":
            print("Shutting down...")
            break

        action, direction, item, character = Parser.parse_command(cmd_line_input)

        print("Command:\n")

        if action:
            print("Action: {0}".format(action))

            if direction:
                print("Direction: {0}".format(direction))

            if item:
                print("Direction: {0}".format(item))

            if character:
                print("Character: {0}".format(character))

        else:
            print("Please enter a valid command\n")
            print("Enter HELP if you would like a list of valid commands\n")

if __name__ == "__main__":
    main()

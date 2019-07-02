#Receives input from engine and understands what the user is trying to accomplish

#List of possible actions, directions, items, and characters that the user can choose from

class Parser:
    
    action_list = ["look", "lookat", "take", "drop", "view", "go", "fight", "interact", "quit", "help"]
    direction_list = ["north", "south", "east", "west"]
    item_list = ["sword", "boat", "key", "statue", "tree", "cage", "bones", "dung", "gate", "sign", "tools", "furnace"]
    character_list = ["behemoth", "lyn", "fisherman", "elder"]
    
    def parse_command(self, userInput):
        command = userInput.lower()
        command_words = command.split()

        #First word should be the action word
        if command_words:
            temp_action = command_words[0]
            
            if len(command_words) > 1:
                if command_words[0] == "look" and command_words[1] == "at":
                    temp_action = "lookat"
            
            action_list_length = len(Parser.action_list)
            
            for i in range(action_list_length):
                #print("Test - Scanning through action list finding {0}".format(temp_action))
                #print("Test - Matching with {0}".format(Parser.action_list[i]))
                if temp_action == Parser.action_list[i]:
                    action = Parser.action_list[i]
                    del command_words[0]
                    break
                else:
                    action = None
        else:
            print("No Command Words")
            action = None

        #If action word is invalid, nothing can happen return None for all
        if action is None:
            print("Please enter a valid command.")
            return (None, None, None, None)

        if action == "go":
            #print("Test - Action is GO")
            #have user find which way to go, north south east or west
            direction = None
            if command_words:
                direction_list_length = len(Parser.direction_list)
                
                for word in command_words:
                    for i in range(direction_list_length):
                        if word == Parser.direction_list[i]:
                            direction = Parser.direction_list[i]
                            break

            #user provides go with no more words in the command word list
            if direction is None:
                print("You provided a \"go\" command with no direction. Please enter a valid command.")
                return (None, None, None, None)

            return (action, direction, None, None)

        else:
            item_list_length = len(Parser.item_list)
            char_list_length = len(Parser.character_list)
            item = None
            character = None

            if command_words:
                for word in command_words:
                    for i in range(item_list_length):
                        if word == Parser.item_list[i]:
                            item = Parser.item_list[i]
                            break
                    for i in range(char_list_length):
                        if word == Parser.character_list[i]:
                            character = Parser.character_list[i]
                            break

            return (action, None, item, character)

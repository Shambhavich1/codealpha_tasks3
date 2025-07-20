


#Basic Chatbot:-
def greet_user(InputGreetings):

    greetingsList = ["Hi!", "I'm fine, thanks!:)", "Goodbye!"]
    
    if InputGreetings == "Hello!":
      print(greetingsList[0])
    
    elif InputGreetings == "How are you?":
      print(greetingsList[1])
    
    elif InputGreetings == "Bye!":
      print(greetingsList[2])

InputGreetings = input("Write here: ")
greet_user(InputGreetings)



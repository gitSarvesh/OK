import webbrowser
def chatbot():
    responses = {
        "hello":"How can i help u?",
        "google":"opening google",
        "amazon":"opening amazon",
        "bye":"thank you.",
        "default":"i dont understand"
    }

    web = ["google", "amazon"]
    print("-------------------Welcome to the chatbot-------------------")
    
    while True:
        userInput = input("You : ").lower()
        response = responses.get(userInput, responses["default"])
        if userInput == "bye":
            print("Bot : ", response)
            break
        elif userInput in web:
            print("Bot : ", response)
            webbrowser.open("www."+userInput+".com")
        elif userInput:
            print("Bot : ", response)

chatbot()
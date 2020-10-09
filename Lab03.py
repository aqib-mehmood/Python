# Task 01
# Write a program to create a basic chatbot application.

'''
response = ["Hi, How may I help you?", "I hope you enjoy this conversation. \nGood bye take care.",
            "RAM is Random-access memory is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code.", 
            "Sorry, I didn't get you!", 
            "Computer is an Electronic machine that accept data as input and provide output by processing that data.",
            "You can google it to find more."]

print("Hi I am a Computer Specialist Ask me anything.")
while True:
    quest1 = input("YOU : ")

    if ("hi" in quest1 or "hello" in quest1):
        print("BOT : " + response[0])

    elif ("bye" in quest1 or "exit" in quest1):
        print("BOT : "+response[1])
        break

    elif ("what" in quest1 and "ram" in quest1 or "RAM" in quest1):
        print("BOT : "+response[2])

    elif ("what" in quest1 and "COMPUTER" in quest1 or "computer" in quest1):
        print("BOT : "+response[4])

    elif ("why" in quest1 or "keyborad" in quest1 or "ROM" in quest1 or "hardisk" in quest1):
        print("BOT : "+response[5])

    else:
        print("Sorry, I didn't get you!")
'''

# Task 02
# Make a questionnaire about yourself and get response from AI based chatbots before and after providing your information. Note: You can take assistance from chatbot examples on the internet.

response = ["Hi, Welcome!",
            "Please Introduce Yourself and tell me for what job are you applying for?", 
            "I hope you enjoy this conversation. \nGood bye take care.", 
            "what is web development?",
            "what is software development?",
            "what are your weeknesses?",
            "Why I hire you for this post?"]

print("Hi I am your Mentor for practicing Inteview Question.")

while True:
    quest2 = input("YOU : ")

    if ("hi" in quest2 or "hello" in quest2):
        print("BOT : " + response[0] + " \n" +response[1])

    elif ("bye" in quest2 or "exit" in quest2):
        print("BOT : "+response[2])
        break

    elif ("web develop" in quest2):
        print("BOT : "+response[3])  

    elif ("software" in quest2):
        print("BOT : "+response[4]) 

    elif ("development" in quest2):
        print("BOT : "+response[5])

    elif ("perfect" in quest2 or "motivated" in quest2 or "hardworking" in quest2 or "work hard" in quest2):
        print("BOT : "+response[6])
    
    else:
        print("Great, So what else you know about the post.")
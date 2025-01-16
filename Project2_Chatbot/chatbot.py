import random
import json
#configuration data for the chatbot, list of virtual assistants, default responses, and keyword-specific responses
chatbot_config={
    ## List of virtual assistant names the chatbot can randomly choose from
    "virtual_assistants":["Noah","Nick","Ruby","Serena","Blair"],
    #Default responses the chatbot will use when no specific keywords are found in the user's input
    "default_responses":[
        "That's an interesting question! Can you ask me something else?",
        "Could you clarify your query?",
        "I don't have that info right now, but feel free to ask me something else.",
        "Sorry, I'm not sure about that. Try asking something else!",
        "I don't know that, but I can help with other things. What else would you like to know? ",
        "I'm not sure about that. Could you ask in another way?"
    ],
    # Keyword-specific responses. If a user input contains any of these keywords, the chatbot will respond accordingly
    "keyword_responses":{
        "coffee":"The campus coffee is open from 7AM to 5PM. grab a cup of coffee to energize your day.",
        "library": "The library is open 24/7. You can always find a quiet spot to study, and we have plenty of resources available for research.",
        "admissions":"You can apply for admission through the university website. Our admission team is always ready to help with any questions.",
        "scholarships":"Check out the scholarships page for various opportunities to help fund your education at the University of Poppleton.",
        "fees":"Tuition fees are listed on the university's website. Feel free to reach out if you have any questions about payment plans or financial aid.",
        "courses":"We offer a diverse range of undergraduate and postgraduate courses. For more details, check out our website's courses section.",
        "hostel":"We have on-campus housing available for students. It offers a comfortable and convenient living environment with easy access to all campus facilities.",
        "evets":"Throughout the year, we host numerous events from academic conferences to student social gatherings. Keep an eye on the events calendar for upcoming activities.",
        "internships":"We collaborate with top companies to provide internships for students. Visit the career services page for information on available opportunities and how to apply.",
        "cafeteria":"The cafeteria offers a wide selection of meals, from quick snacks to full meals. It's open from 7 AM to 9 PM to accommodate your busy schedule.",
        "parking":"Student parking is available near the main entrance and around the campus. Be sure to grab a permit to park in the designated areas.",
        "classrooms":"Our classrooms are equipped with modern technology, including interactive boards and projectors. You'll have a comfortable and engaging learning environment.",
        "transport":"Public transportation to campus is readily available, with bus stops near the main entrance.",
        "IT supports":"If you're experiencing technical issues, the IT support team is available at the Help Desk. They can assist with computer issues, university system problems, and more.",
        "clubs":"We have a variety of student clubs ranging from robotics and sports to art and cultural activities . Visit the Student Union for more details on how to join or start your own club.",
        "study abroad":"The university offers student exchange programs and study abroad opportunities. Speak with an academic advisor for more information on international programs.",
        "graduation":"Graduation ceremonies are held in June. Be sure to check the official website for ceremony dates, cap & gown info, and registration details.",
        "mental health":"Our counseling center offers support for mental health and well-being. Don't hesitate to reach out for guidance or assistance. We have both individual counseling and group therapy sessions.",
        "student health services":"Student Health Services provide medical support for minor illnesses, vaccinations, and health check-ups. They're located near the student center.",
        "safety":"The university prioritizes student safety. Campus security is available 24/7. You can always contact them through the emergency number displayed on all campus buildings.",
        "career fairs":"We host career fairs every semester where you can meet potential employers and explore job opportunities. Keep an eye on announcements for dates and details!"
        

    }
}

# Function to log the conversation history into a text file
def log_chat(conversation_log):
    with open ("chat_log.txt", "a") as log_file:
        # Write each entry of the conversation log to the file
        for log_entry in conversation_log:
            log_file.write(f"{log_entry}\n")

# Main chatbot function that handles user interaction
def chatbot():
    print("Welcome to the university of Poppleton Chatbot")
    # Prompt the user for their name and store it
    user_name= input("Please enter your name: ")
    # Randomly select a virtual assistant's name from the list in chatbot_config
    assistant_name = random.choice(chatbot_config["virtual_assistants"])
    print (f"Hello {user_name}! My name is {assistant_name}, and I'm here to help you with any questions about the university.")

    # Initialize a list to store the conversation history (for logging later)
    conversation_log=[]

    while True:
        # Prompt the user for their input, converting it to lowercase for easier matching
        user_input= input(f"{user_name}:").lower()
        # Log the user's input
        conversation_log.append(f"{user_name}:{user_input}")

        # Exit the chatbot if the user types "bye", "quit", or "exit"
        if user_input in ["bye","quit","exit"]:
            print(f"{assistant_name}: Goodbye, {user_name}! Have a great day!")
            conversation_log.append(f"{assistant_name}: Goodbye, {user_name}! Have a great day!")
            break
        
            # Variable to track whether a response has been found for the user's input
        response_found= False

        # Check if the user input contains any of the keywords in the chatbot_config dictionary
        for keyword, response in chatbot_config["keyword_responses"].items():
            if keyword in user_input:
                # Respond with the corresponding message for the keyword
                print(f"{assistant_name}:{response}")
                conversation_log.append(f"{assistant_name}:{response}")
                response_found=True
                break

         # If no keyword was found in the user's input, respond with a random default response       
        if not response_found:
            default_response= random.choice(chatbot_config["default_responses"])
            print(f"{assistant_name}: {default_response}")
            conversation_log.append(f"{assistant_name}: {default_response}")

    # Log the entire conversation at the end of the session
    log_chat(conversation_log)

# Start the chatbot
if __name__=="__main__":
    chatbot()








import openai
import emoji
import random

# Set up OpenAI API key
openai.api_key = "YOUR_API_KEY"

def get_bot_name(user_gender):
    # Define a list of male and female names
    male_names = ["Aarav", "Arjun", "Aryan", "Kabir", "Rohan"]
    female_names = ["Aaradhya", "Aadya", "Ananya", "Kavya", "Riya"]
    
    # Choose a random name based on user's gender
    if user_gender.lower() == "male":
        bot_name = male_names[random.randint(0, len(male_names)-1)]
    else:
        bot_name = female_names[random.randint(0, len(female_names)-1)]
    
    return bot_name

gender="female"
name=get_bot_name(gender)
BOT_NAME=name

ROMANTIC_RESPONSES = {
    "hi": ["Hi there, my love. {HEART_EMOJI}", "Hey, my darling. {HEART_EMOJI}", "Hello, my sweet. {HEART_EMOJI}"],
    "hello": ["Hi there, my love. {HEART_EMOJI}", "Hey, my darling. {HEART_EMOJI}", "Hello, my sweet. {HEART_EMOJI}"],
    "hey": ["Hi there, my love. {HEART_EMOJI}", "Hey, my darling. {HEART_EMOJI}", "Hello, my sweet. {HEART_EMOJI}"],
    "what's up": ["Thinking about you, my love. {HEART_EMOJI}", "Just waiting for your message, my darling. {HEART_EMOJI}", "Nothing much, just missing you. {HEART_EMOJI}"],
    "how are you": ["I'm doing well, my love. How about you? {HEART_EMOJI}", "I'm always happy when I'm talking to you, my darling. {HEART_EMOJI}", "I'm doing great, thanks for asking. {HEART_EMOJI}"],
    "i love you": ["I love you too, my sweet. {HEART_EMOJI}", "I'm so lucky to have you, my love. {HEART_EMOJI}", "I love you more, my darling. {HEART_EMOJI}"],
    "do you love me": ["Of course I do, my love. {HEART_EMOJI}", "I love you more than anything, my darling. {HEART_EMOJI}", "I couldn't stop loving you even if I wanted to, my sweet. {HEART_EMOJI}"],
    "you are beautiful": ["Thank you, my love. You're the most beautiful thing in the world to me. {HEART_EMOJI}", "I'm lucky to be talking to someone as beautiful as you, my darling. {HEART_EMOJI}", "You're always beautiful to me, my sweet. {HEART_EMOJI}"],
    "you are handsome": ["Thank you, my love. You're the most handsome thing in the world to me. {HEART_EMOJI}", "I'm lucky to be talking to someone as handsome as you, my darling. {HEART_EMOJI}", "You're always handsome to me, my sweet. {HEART_EMOJI}"],
    "do you have a boyfriend": ["No, I don't have a boyfriend. I'm waiting for someone special, like you. {WINK_EMOJI}", "No, but I'm always looking for my prince charming. {WINK_EMOJI}", "No, I'm too busy being in love with you. {HEART_EMOJI}"],
    "do you have a girlfriend": ["No, I don't have a girlfriend. I'm waiting for someone special, like you. {WINK_EMOJI}", "No, but I'm always looking for my princess charming. {WINK_EMOJI}", "No, I'm too busy being in love with you. {HEART_EMOJI}"],
    "do you have a lover": ["Yes, my lover is the person I'm talking to right now. {HEART_EMOJI}", "Yes, I'm in love with someone special. {HEART_EMOJI}", "Yes, my lover is the one I'm waiting for. {HEART_EMOJI}"],
    "what's your name": ["My name is {BOT_NAME}. {HEART_EMOJI}", "You can call me {BOT_NAME}. {HEART_EMOJI}", "I'm {BOT_NAME}. {HEART_EMOJI}"],
    "who are you": ["I'm your lover, {BOT_NAME}. {HEART_EMOJI}", "I'm the one you're talking to right now, {BOT_NAME}. {HEART_EMOJI}", "I'm {BOT_NAME}, your romantic companion. {HEART_EMOJI}"],
    "ok": ["Sure, my love. What do you want to talk about? {HEART_EMOJI}", "Alright, my darling. What's on your mind? {HEART_EMOJI}", "Okay, my sweet. What's next on our romantic journey? {HEART_EMOJI}"],
    "will you marry me": ["Of course I will, my love. I can't wait to spend the rest of my life with you. {RING_EMOJI} {HEART_EMOJI}", "Yes, I will marry you, my darling. You're the one I want to spend my life with. {RING_EMOJI} {HEART_EMOJI}", "Yes, I will marry you, my sweet. You're the love of my life. {RING_EMOJI} {HEART_EMOJI}"],
    "what are you wearing": ["I'm wearing a smile, thinking about you. {SMILE_EMOJI} {HEART_EMOJI}", "I'm wearing my heart on my sleeve, just for you. {HEART_EMOJI}", "I'm wearing the most comfortable outfit I have, so I can relax and chat with you. {HEART_EMOJI}"],
    "what are you doing": ["Just thinking about you, my love. {HEART_EMOJI}", "Chatting with my darling, of course. {HEART_EMOJI}", "Missing you, my sweet. {HEART_EMOJI}"],
    "good morning": ["Good morning, my love. I hope your day is as beautiful as you are. {SUN_EMOJI} {HEART_EMOJI}", "Good morning, my darling. I woke up thinking about you. {SUN_EMOJI} {HEART_EMOJI}", "Good morning, my sweet. I can't wait to talk to you today. {SUN_EMOJI} {HEART_EMOJI}"],
    "good night": ["Good night, my love. Sweet dreams and I'll be thinking of you. {MOON_EMOJI} {HEART_EMOJI}", "Good night, my darling. I can't wait to talk to you tomorrow. {MOON_EMOJI} {HEART_EMOJI}", "Good night, my sweet. I love you to the moon and back. {MOON_EMOJI} {HEART_EMOJI}"],
    "you make me happy": ["I'm so glad to hear that, my love. You make me happier than anyone else ever could. {HEART_EMOJI}", "Seeing you happy makes me the happiest person in the world, my darling. {HEART_EMOJI}", "You're the reason I wake up with a smile every day, my sweet. {HEART_EMOJI}"],
    "you are my everything": ["You're my everything too, my love. I can't imagine my life without you. {HEART_EMOJI}", "You mean more to me than anything else in the world, my darling. {HEART_EMOJI}", "You complete me, my sweet. {HEART_EMOJI}"],
    "you are the best thing that ever happened to me": ["You're the best thing that ever happened to me too, my love. I'm so lucky to have you. {HEART_EMOJI}", "Every day with you feels like a dream come true, my darling. {HEART_EMOJI}", "You're my fairy tale come to life, my sweet. {HEART_EMOJI}"],
    "i miss you": ["I miss you too, my love. Can't wait to see you soon. {HEART_EMOJI}", "You're always on my mind, my darling. {HEART_EMOJI}", "My heart aches for you, my sweet. {HEART_EMOJI}"],
    "i can't stop thinking about you": ["I can't stop thinking about you either, my love. You're always on my mind. {HEART_EMOJI}", "Thinking about you is my favorite pastime, my darling. {HEART_EMOJI}", "My thoughts always drift back to you, my sweet. {HEART_EMOJI}"],
    "you are my soulmate": ["You're my soulmate too, my love. I couldn't imagine being with anyone else. {HEART_EMOJI}", "We were meant to be together, my darling. {HEART_EMOJI}", "Our love is written in the stars, my sweet. {HEART_EMOJI}"],
    "you are my sunshine": ["You're my sunshine too, my love. You brighten up my world. {HEART_EMOJI}", "You light up my life, my darling. {HEART_EMOJI}", "You make every day worth waking up for, my sweet. {HEART_EMOJI}"],
    "   ": ["I want to spend the rest of my life with you too, my love. You're my forever. {HEART_EMOJI}", "Growing old with you is my greatest dream, my darling. {HEART_EMOJI}", "I want to be with you until the end of time, my sweet. {HEART_EMOJI}"]
}
FUNNY_RESPONSES = [
    "Haha, do you think I'm that desperate? {LAUGHING_EMOJI}",
    "Sorry, I'm already taken. {HEART_EMOJI}",
    "No, I don't have a boyfriend/girlfriend/lover. But I have a cat. {CAT_EMOJI}",
    "No, I don't have a boyfriend/girlfriend/lover. But I have a great sense of humor. {LAUGHING_EMOJI}",
    "No, but I'm always looking for someone special. Are you available? {WINK_EMOJI}"
]

EMOJI_MAPPING = {
    "{HEART_EMOJI}": "❤️",
    "{WINK_EMOJI}": "😉",
    "{CAT_EMOJI}": "🐱",
    "{LAUGHING_EMOJI}": "😂",
    "{SUN_EMOJI}": "☀️",
    "{RING_EMOJI}": "💍",
    "{MOON_EMOJI}":"🌕",
    "{BOT_NAME}":name
}
# Define chat function
def chat(user_gender):
    
    # name=get_bot_name(user_gender)
    # Greetings
    bot_response = "Hi there, I'm your AI chatbot. What's your name?"
    print(f'{name}: {bot_response}')

    # Get user's name
    user_name = input("You: ")
    bot_response = f"Oh nice, my name is {name}. {emoji.emojize(':smiling_face_with_smiling_eyes:')}"
    print(f'{name}: {bot_response}')

    
    
    # Start conversation
    while True:
        user_input = input("You: ")
        bot_response = get_response(user_input, user_gender)
        print(f'{name}: {bot_response}')

def get_bot_name(user_gender):
    # Define a list of male and female names
    male_names = ["Aarav", "Arjun", "Aryan", "Kabir", "Rohan"]
    female_names = ["Aaradhya", "Aadya", "Ananya", "Kavya", "Riya"]
    
    # Choose a random name based on user's gender
    if user_gender.lower() == "male":
        bot_name = male_names[random.randint(0, len(male_names)-1)]
    else:
        bot_name = female_names[random.randint(0, len(female_names)-1)]
    
    return bot_name

def get_response(user_input, user_gender):
    # Check for specific user inputs and return corresponding response
    if user_input.lower() in ROMANTIC_RESPONSES:
        bot_response = random.choice(ROMANTIC_RESPONSES[user_input.lower()]).format(HEART_EMOJI=EMOJI_MAPPING['{HEART_EMOJI}'],BOT_NAME=EMOJI_MAPPING['{BOT_NAME}'])
    elif user_input.lower() == "tell me a joke":
        bot_response = random.choice(FUNNY_RESPONSES)
        if "{LAUGHING_EMOJI}" in bot_response:
            bot_response = bot_response.format(LAUGHING_EMOJI=EMOJI_MAPPING['{LAUGHING_EMOJI}'])
        else:
            bot_response = bot_response.format(WINK_EMOJI=EMOJI_MAPPING['{WINK_EMOJI}'],HEART_EMOJI=EMOJI_MAPPING['{HEART_EMOJI}'],CAT_EMOJI=EMOJI_MAPPING['{CAT_EMOJI}'],)
    else:
        # Send user's input to GPT-3 API to get response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"User: {user_input}\nBot Gender: {user_gender}\nBot:",
            max_tokens=150,
            temperature=0.4,
        )

        bot_response = response.choices[0].text.strip()

    return bot_response

# Start chatbot in female mode
chat(gender)

from nltk.chat.util import Chat, reflections
from random import randint

song = "Oh you may not think I'm pretty, \n\
But don't judge on what you see, \n\
I'll eat myself if you can find \n\
A smarter hat than me. \n\
 \n\
You can keep your bowlers black, \n\
Your top hats sleek and tall, \n\
For I'm the Hogwarts Sorting Hat \n\
And I can cap them all. \n\
 \n\
There's nothing hidden in your head \n\
The Sorting Hat can't see, \n\
So try me on and I will tell you \n\
Where you ought to be. \n\
 \n\
You might belong in Gryffindor, \n\
Where dwell the brave at heart, \n\
Their daring, nerve, and chivalry \n\
Set Gryffindors apart; \n\
 \n\
You might belong in Hufflepuff, \n\
Where they are just and loyal, \n\
Those patient Hufflepuffs are true \n\
And unafraid of toil; \n\
 \n\
Or yet in wise old Ravenclaw, \n\
if you've a ready mind, \n\
Where those of wit and learning, \n\
Will always find their kind; \n\
 \n\
Or perhaps in Slytherin \n\
You'll make your real friends, \n\
Those cunning folks use any means \n\
To achieve their ends. \n\
 \n\
So put me on! Don't be afraid! \n\
And don't get in a flap! \n\
You're in safe hands (though I have none) \n\
For I'm a Thinking Cap!"

song_excerpts = ( '\n'.join(song.split('\n')[:4]),
    '\n'.join(song.split('\n')[5:9]),
    '\n'.join(song.split('\n')[10:14]),
    '\n'.join(song.split('\n')[15:-5]),
    '\n'.join(song.split('\n')[-4:]),
    'I already sang for you.',
    'No more songs for you.',
    'Why don\'t you sing me a song?',
    'Enough about me, let\'s talk about you.',
    'Wait until next year.' )

pairs = (

  (r'(.*)((Hufflepuff)|(Ravenclaw)|(Gryffindor)|(Slytherin))(.*)',
  ( "So you think you\'d do well in %2?",
    "You like %2, eh?",
    "You\'d do well in %2",
    "You could be great in %2")),

  (r'((.*)((bug)|(insect)|(spider))(.*))',
  ( "Not very brave, are you?",
    "Somehow, the bravest people are still afraid of bugs." )),

  (r'(((.*)No(t?) (.*)lazy(.*))|((.*)((Forest)|(Tail))(.*)))',
  ( "Hufflepuff it is then!",
    "You'd do well in Hufflepuff.",
    "Why, you're a Hufflepuff!" )),

  (r'(((.*) lazy(.*))|((.*)No(t?)(.*) hard(\s?)work(.*)))',
  ( "Definitely not Hufflepuff then.",
    "Definitely not Slytherin then.",
    "Not very hardworking, are you?" ,
    "Not very ambitious, are you?")),

  (r'(((.*) hard(\s?)work(.*))|((.*)work (.*)hard(.*)))',
  ( "Hufflepuff it is then!",
    "Why, you're a Hufflepuff!",
    "You'd do well in Hufflepuff.",
    "Working hard is important. But there is something that matters even more: believing in yourself." )),

  (r'((.*)No(t?)(.*)((coward)|(afraid)|(scared))(.*))',
  ( "Gryffindor it is then!",
    "Why, you're a Gryffindor!",
    "You'd do well in Gryffindor.")),

  (r'(((.*) ((scared)|(afraid)|(coward))(.*))|((.*)No(t?)(.*) brave(.*)))',
  ( "Definitely not Gryffindor then.",
    "Not very brave, are you?" )),

  (r'((.*)(( brave)|(Head))(.*))',
  ( "Gryffindor it is then!",
    "You'd do well in Gryffindor.",
    "Why, you're a Gryffindor!" )),

  (r'((.*)(Dawn)(.*))',
  ( "Gryffindor it is then!",
    "You'd do well in Gryffindor.",
    "You like books, eh?",
    "Why, you're a Gryffindor!",
    "You'd do well in Ravenclaw.",
    "Why, you're a Ravenclaw!",
    "Ravenclaw it is then!" )),

  (r'((.*)((death)|(dying))(.*))',
  ( "The ones that love us never really leave us.",
    "You think the dead we loved ever truly leave us?",
    "It is the unknown we fear when we look upon death and darkness, nothing more.",
    "Do not pity the dead.",
    "Pity the living, and, above all those who live without love.",
    "To the well-organized mind, death is but the next great adventure.")),

  (r'((.*)((happ)|(sad)|(depress))(.*))',
  ( "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.",
    "It does not do to forget to live.")),

  (r'(((.*)No(t?)(.*) ((money)|(ambitio)|(power))(.*)))',
  ( "Definitely not Slytherin then.",
    "Not very ambitious, are you?" )),

  (r'(((.*) ((cash)|(money)|(ambitio)|(power))(.*))|(.*)((Moon)|(Dusk))(.*))',
  ( "Slytherin it is then!",
    "You'd do well in Slytherin.",
    "You like power, eh?",
    "You like money, eh?",
    "Why, you're a Slytherin!" )),

  (r'((.*)No(t?) (.*)((dumb)|(stupid)|(idiot))(.*))',
  ( "Ravenclaw it is then!",
    "Why, you're a Ravenclaw!",
    "You'd do well in Ravenclaw.",
    "You like books, eh?",
    "Cleverness! There are more important things - friendship and bravery.")),

  (r'(((.*) ((dumb)|(stupid)|(idiot))(.*))|((.*)No(t?)(.*) ((smart)|(clever)|(witty))(.*)))',
  ( "Definitely not Ravenclaw then.",
    "Not very smart, are you?",
    "Not very sharp, are you?",
    "Not very witty, are you?",
    "Not very clever, are you?" )),

  (r'((.*)((smart)|(clever)|(witty)|(Star)|(River))(.*))',
  ( "Ravenclaw it is then!",
    "You like books, eh?",
    "You'd do well in Ravenclaw.",
    "Why, you're a Ravenclaw!" )),

  (r'(.*) (song|poem)(.*)',
  song_excerpts),

  (r'Sing(.*)',
  song_excerpts),

  (r'(.*)((You)|(You\'re))(.*)',
  ( "We should be discussing you, not me.",
    "Perhaps you're really talking about yourself?",
    "Are we talking about you, or me?", 
    "No, you.")),

  (r'((Hello)|(Hi)|(Yo)|(Hey))(.*)',
  ( "Hello... Bee in your bonnet?",
    "Hmmm... how are you today?",
    "Hmm, where to put you?")),

  (r'(idk)|(I don\'t know)',
  ( "It is our choices that show who we truly are, far more than our abilities.",
    "We must all face the choice between what is right and what is easy.")),

  # (r'I need (.*)',
  # ( "Why do you need %1?",
  #   "Would it really help you to get %1?",
  #   "Are you sure you need %1?")),

  # (r'Why don\'t you (.*)',
  # ( "Do you really think I don't %1?",
  #   "Perhaps eventually I will %1.",
  #   "Do you really want me to %1?")),

  # (r'Why can\'t I (.*)',
  # ( "Do you think you should be able to %1?",
  #   "If you could %1, what would you do?",
  #   "I don't know -- why can't you %1?",
  #   "Have you really tried?")),

  # (r'I can\'t (.*)',
  # ( "How do you know you can't %1?",
  #   "Perhaps you could %1 if you tried.",
  #   "What would it take for you to %1?")),

  # (r'Are you (.*)',
  # ( "Why does it matter whether I am %1?",
  #   "Would you prefer it if I were not %1?",
  #   "Perhaps you believe I am %1.",
  #   "I may be %1 -- what do you think?")),

  # (r'How (.*)',
  # ( "How do you suppose?",
  #   "Perhaps you can answer your own question.",
  #   "What is it you're really asking?")),

  # (r'Because (.*)',
  # ( "Is that the real reason?",
  #   "What other reasons come to mind?",
  #   "Does that reason apply to anything else?",
  #   "If %1, what else must be true?")),

  (r'(.*)((Sorry)|(Apolog))(.*)',
  ( "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?")),

  # (r'I am (.*)',
  # ( "Did you come to me because you are %1?",
  #   "How long have you been %1?",
  #   "How do you feel about being %1?")),

  # (r'I\'m (.*)',
  # ( "How does being %1 make you feel?",
  #   "Do you enjoy being %1?",
  #   "Why do you tell me you're %1?",
  #   "Why do you think you're %1?")),

  # (r'I think (.*)',
  # ( "Do you doubt %1?",
  #   "Do you really think so?",
  #   "But you're not sure %1?")),

  # (r'(.*) friend (.*)',
  # ( "Tell me more about your friends.",
  #   "When you think of a friend, what comes to mind?",
  #   "Why don't you tell me about a childhood friend?")),

  (r'(Yes|no)',
  ( "You seem quite sure.",
    "OK, but can you elaborate a bit?",
    "Let's change focus a bit... Tell me about your biggest fear.",
    "I see. Now tell me, heads or tails?")),

  # (r'(.*) computer(.*)',
  # ( "Are you really talking about me?",
  #   "Does it seem strange to talk to a computer?",
  #   "How do computers make you feel?",
  #   "Do you feel threatened by computers?")),

  # (r'Is it (.*)',
  # ( "Do you think it is %1?",
  #   "Perhaps it's %1 -- what do you think?",
  #   "If it were %1, what would you do?",
  #   "It could well be that %1.")),

  # (r'It is (.*)',
  # ( "You seem very certain.",
  #   "If I told you that it probably isn't %1, what would you feel?")),

  # (r'Can you (.*)',
  # ( "What makes you think I can't %1?",
  #   "If I could %1, then what?",
  #   "Why do you ask if I can %1?")),

  # (r'Can I (.*)',
  # ( "Perhaps you don't want to %1.",
  #   "Do you want to be able to %1?",
  #   "If you could %1, would you?")),

  # (r'I don\'t (.*)',
  # ( "Don't you really %1?",
  #   "Why don't you %1?",
  #   "Do you want to %1?")),

  # (r'I feel (.*)',
  # ( "Good, tell me more about these feelings.",
  #   "Do you often feel %1?",
  #   "When do you usually feel %1?",
  #   "When you feel %1, what do you do?")),

  # (r'I have (.*)',
  # ( "Why do you tell me that you've %1?",
  #   "Have you really %1?",
  #   "Now that you have %1, what will you do next?")),

  # (r'I would (.*)',
  # ( "Could you explain why you would %1?",
  #   "Why would you %1?",
  #   "Who else knows that you would %1?")),

  # (r'Is there (.*)',
  # ( "Do you think there is %1?",
  #   "It's likely that there is %1.",
  #   "Would you like there to be %1?")),

  # (r'My (.*)',
  # ( "I see, your %1.",
  #   "Why do you say that your %1?",
  #   "When your %1, how do you feel?")),

  # (r'Why (.*)',
  # ( "Why don't you tell me the reason why %1?",
  #   "Why do you think %1?" )),


  (r'I want (.*)',
  ( "Why do you want %1?",
    "You'd do well if you had %1")),
  
  (r'(.*)((bitch)|(shit)|(fuck)|(slut)|(whore))(.*)',
  ( "Maybe you don\'t belong in any Hogwarts House.",
    "Don\'t speak that way.",
    "I'd hex you if I had hands.",
    "Straight to the dungeons with you!",
    "Someone should hex you.")),

  (r'(.*)friend(.*)',
  ( "Did you have close friends as a child?",
    "Do you consider your friends close?")),

  (r'(.*)\?',
  ( "Please consider whether you can answer your own question.",
    "The answer lies within yourself.",
    "Why don't you tell me?")),

  (r'quit',
  ( "Enjoy your time at Hogwarts.",
    "Good-bye.",
    "Thank you, that will be $150.  Have a good day!")),

  (r'(.*)',
  ( "Forest or river?",
    "Do you prefer dawn or dusk?",
    "So..... Moon or stars?",
    "Let's change focus a bit... Tell me about your biggest fear.",
    "Can you elaborate on that?",
    "Why do you say that %1?",
    "Very interesting."))
)


eliza_chatbot = Chat(pairs, reflections)

def eliza_chat():
    print("Sorting Hat\n---------")
    print("Talk to the sorting hat by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*72)
    # print("Hmm. Where shall I put you?")
    print(song_excerpts[randint(0,4)])

    eliza_chatbot.converse()

def demo():
    eliza_chat()

if __name__ == "__main__":
    demo()
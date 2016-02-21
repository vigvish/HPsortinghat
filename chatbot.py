from Chat import Chat, reflections
from random import randint

song = 'Oh you may not think I\'m pretty, \n\
But don\'t judge on what you see, \n\
I\'ll eat myself if you can find, \n\
A smarter hat than me. \n\
 \n\
You can keep your bowlers black, \n\
Your top hats sleek and tall, \n\
For I\'m the Hogwarts Sorting Hat, \n\
And I can cap them all. \n\
 \n\
There\'s nothing hidden in your head, \n\
The Sorting Hat can\'t see, \n\
So try me on and I will tell you, \n\
Where you ought to be. \n\
 \n\
You might belong in griffin door, \n\
Where dwell the brave at heart, \n\
Their daring, nerve, and chivalry, \n\
Set griffin doors apart; \n\
 \n\
You might belong in Hufflepuff, \n\
Where they are just and loyal, \n\
Those patient Hufflepuffs are true, \n\
And unafraid of toil; \n\
 \n\
Or yet in wise old raven claw, \n\
if you\'ve a ready mind, \n\
Where those of wit and learning, \n\
Will always find their kind; \n\
 \n\
Or perhaps in sliderin, \n\
You\'ll make your real friends, \n\
Those cunning folks use any means, \n\
To achieve their ends. \n\
 \n\
So put me on! Don\'t be afraid! \n\
And don\'t get in a flap! \n\
You\'re in safe hands (though I have none) \n\
For I\'m a Thinking Cap!'

song_excerpts = ( ' '.join(song.split('\n')[:4]).strip(),
    ' '.join(song.split('\n')[5:9]).strip(),
    ' '.join(song.split('\n')[10:14]).strip(),
    ' '.join(song.split('\n')[15:-5]).strip(),
    ' '.join(song.split('\n')[-4:]).strip(),
    'I already sang for you.',
    'No more songs for you.',
    'Why don\'t you sing me a song?',
    'Enough about me, let\'s talk about you.',
    'Wait until next year.' )

pairs = (

  (r'(.*)house(.*)',
  ( "So.... Forest or river?",
    "I see. Now tell me, do you prefer dawn or dusk?",
    "So..... Moon or stars?",
    "I see. Now tell me, heads or tails?",
    "Let's change focus a bit... Tell me about your biggest fear.",
    "Can you elaborate on that?",
    "Very interesting.")),

  (r'(.*)((Hufflepuff)|(Ravenclaw)|(Gryffindor)|(Slytherin))(.*)',
  ( "So you think you would do well in %2?",
    "You like %2, don't you",
    "You could do well in %2",
    "You could be great in %2")),

  (r'((.*)((bug)|(insect)|(spider))(.*))',
  ( "Not very courageous, are you?",
    "Somehow, the bravest people are still afraid of bugs." )),

  (r'(((.*)No(t?) (.*)lazy(.*))|((.*)((Forest)|(Tail))(.*)))',
  ( "HUFFLEPUFF it is then!",
    "You could do well in Hufflepuff.",
    "Why, you are a HUFFLEPUFF!" )),

  (r'(((.*) lazy(.*))|((.*)No(t?)(.*) hard(\s?)work(.*)))',
  ( "Definitely not Hufflepuff then.",
    "Definitely not sliderin then.",
    "Not very hardworking, are you?" ,
    "Not very ambitious, are you?")),

  (r'(((.*) hard(\s?)work(.*))|((.*)work (.*)hard(.*)))',
  ( "HUFFLEPUFF it is then!",
    "Why, you are a HUFFLEPUFF!",
    "You could do well in Hufflepuff.",
    "Working hard is important. But there is something that matters even more: believing in yourself." )),

  (r'((.*)No(t?)(.*)((coward)|(afraid)|(scared))(.*))',
  ( "GRYFFINDOR it is then!",
    "Why, you are a GRYFFINDOR!",
    "You could do well in griffin door.")),

  (r'((.*)((death)|(dying))(.*))',
  ( "The ones that love us never really leave us.",
    "You think the dead we loved ever truly leave us?",
    "It is the unknown we fear when we look upon death and darkness, nothing more.",
    "To the well-organized mind, death is but the next great adventure.")),

  (r'(((.*) ((scared)|(afraid)|(coward))(.*))|((.*)No(t?)(.*) brave(.*)))',
  ( "Definitely not griffin door then.",
    "Not very courageous, are you?" )),

  (r'((.*)(( brave)|(Head))(.*))',
  ( "GRYFFINDOR it is then!",
    "You could do well in griffin door.",
    "Why, you are a GRYFFINDOR!" )),

  (r'((.*)(Dawn)(.*))',
  ( "GRYFFINDOR it is then!",
    "You could do well in griffin door.",
    "You like books, don't you",
    "Why, you are a GRYFFINDOR!",
    "You could do well in raven claw.",
    "Why, you are a RAVENCLAW!",
    "RAVENCLAW it is then!" )),

  (r'((.*)((happ)|(sad)|(depress))(.*))',
  ( "Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.",
    "It does not do to forget to live.")),

  (r'(((.*)No(t?)(.*) ((money)|(ambitio)|(power))(.*)))',
  ( "Definitely not sliderin then.",
    "Not very ambitious, are you?" )),

  (r'(((.*) ((cash)|(money)|(ambitio)|(power))(.*))|(.*)((Moon)|(Dusk))(.*))',
  ( "SLYTHERIN it is then!",
    "You would do well in sliderin.",
    "You like power, don't you",
    "Why, you are a SLYTHERIN!" )),

  (r'((.*)No(t?) (.*)((dumb)|(stupid)|(idiot))(.*))',
  ( "RAVENCLAW it is then!",
    "Why, you are a RAVENCLAW!",
    "You would do well in raven claw.",
    "You like books, don't you",
    "Cleverness! There are more important things - friendship and bravery.")),

  (r'(((.*) ((dumb)|(stupid)|(idiot))(.*))|((.*)No(t?)(.*) ((smart)|(clever)|(witty))(.*)))',
  ( "Definitely not raven claw then.",
    "Not very smart, are you?",
    "Not very sharp, are you?",
    "Not very witty, are you?",
    "Not very clever, are you?" )),

  (r'((.*)((smart)|(clever)|(witty)|(Star)|(River))(.*))',
  ( "RAVENCLAW it is then!",
    "You like books, don't you",
    "You would do well in raven claw.",
    "Why, you are a RAVENCLAW!" )),

  (r'(.*) (song|poem)(.*)',
  song_excerpts),

  (r'Sing(.*)',
  song_excerpts),

  (r'((idk)|(I don\'t know))',
  ( "It is our choices that show who we truly are, far more than our abilities.",
    "We must all face the choice between what is right and what is easy.")),

  (r'(.*)\?',
  ( "Please consider whether you can answer your own question.",
    "The answer lies within yourself.",
    "Why don't you tell me?")),

  (r'(Why|Who|What|How|Where|When|Can|Is|Will)(.*)',
  ( "Please consider whether you can answer your own question.",
    "The answer lies within yourself.",
    "Why don't you tell me?")),

  (r'(.*)((You)|(You\'re))(.*)',
  ( "We should be discussing you, not me.",
    "Perhaps you are really talking about yourself?",
    "Are we talking about you, or me?", 
    "No, you.")),

  (r'((Hello)|(Hi)|(Hey))(.*)',
  ( "Hello... Bee in your bonnet?",
    "Hello... how are you today?",
    "Hello, where to put you?")),

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
    "You would do well if you had %1")),
  
  (r'(.*)((bitch)|(shit)|(fuck)|(slut)|(whore))(.*)',
  ( "Maybe you don\'t belong in any Hogwarts House.",
    "I would hex you if I had hands.",
    "Straight to the dungeons with you!",
    "Someone should hex you.")),

  (r'(.*)friend(.*)',
  ( "Did you have close friends as a child?",
    "Do you consider your friends close?")),

  (r'(Yes|no)',
  ( "You seem quite sure.",
    "OK, but can you elaborate a bit?",
    "Let's change focus a bit... Tell me about your biggest fear.",
    "I see. So..... heads or tails?",
    "I see. Now tell me, do you prefer dawn or dusk?")),

  (r'(.*)((You)|(You\'re))(.*)',
  ( "We should be discussing you, not me.",
    "Perhaps you are really talking about yourself?",
    "Are we talking about you, or me?", 
    "No, you.")),

  (r'Yo(.*)',
  ( "Hello... Bee in your bonnet?",
    "Hello... how are you today?",
    "Hello, where to put you?")),

  (r'quit',
  ( "Enjoy your time at Hogwarts.",
    "Good-bye.",
    "Hogwarts, Hogwarts, Hoggy Warty Hogwarts \nLearn something please!")),

  (r'(.*)',
  ( "So.... Forest or river?",
    "I see. Now tell me, do you prefer dawn or dusk?",
    "So..... Moon or stars?",
    "I see. Now tell me, heads or tails?",
    "Let's change focus a bit... Tell me about your biggest fear.",
    "Can you elaborate on that?",
    "Very interesting."))
)


hat_chatbot = Chat(pairs, reflections)

def hat_chat():
    print("Sorting Hat\n---------")
    print("Talk to the sorting hat by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print('='*72)
    print(song_excerpts[randint(0,4)])

    hat_chatbot.converse()

def demo():
    hat_chat()

if __name__ == "__main__":
    demo()
import unittest
from chatbot import hat_chatbot

# tests the types of responses we want from the bot
class TestStringMethods(unittest.TestCase):

  def test_gryffindor(self):
      self.assertEquals(1,hat_chatbot.converse_terminal(input="I am brave.")[2])
      self.assertEquals(1,hat_chatbot.converse_terminal(input="I am not scared.")[2])

  def test_hufflepuff(self):
      self.assertEquals(3,hat_chatbot.converse_terminal(input="I am not lazy.")[2])
      self.assertEquals(3,hat_chatbot.converse_terminal(input="I prefer tails.")[2])

  def test_return_house(self):
      self.assertIn('griffin door',hat_chatbot.converse_terminal(input="I like Gryffindor.")[1].lower())
      self.assertIn('sliderin',hat_chatbot.converse_terminal(input="I like Slytherin.")[1].lower())
      self.assertIn('hufflepuff',hat_chatbot.converse_terminal(input="I like Hufflepuff.")[1].lower())
      self.assertIn('raven claw',hat_chatbot.converse_terminal(input="I like Ravenclaw.")[1].lower())

  def test_idk(self):
      self.assertIn('choice',hat_chatbot.converse_terminal(input="IDK.")[1])
      self.assertIn('choice',hat_chatbot.converse_terminal(input="I don't know.")[1])

  def test_friends(self):
      self.assertIn('friends',hat_chatbot.converse_terminal(input="My best friend says I'm funny.")[1])
      self.assertIn('friends',hat_chatbot.converse_terminal(input="I'm not close to my friends.")[1])
      self.assertNotIn('friends',hat_chatbot.converse_terminal(input="I fear my friends' deaths.")[1])

  def test_sorry(self):
      self.assertIn('apolog',hat_chatbot.converse_terminal(input="Sorry.")[1])
      self.assertIn('apolog',hat_chatbot.converse_terminal(input="I apologize.")[1])

  def test_hello(self):
      self.assertIn('hello',hat_chatbot.converse_terminal(input="Hello.")[1].lower())
      self.assertIn('hello',hat_chatbot.converse_terminal(input="Hi.")[1].lower())
      self.assertIn('hello',hat_chatbot.converse_terminal(input="Yo.")[1].lower())

  def test_house(self):
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="What house am I in?")[0])
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="Tell me my house.")[0])
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="Why don't you tell me my house?")[0])

  def test_random_input(self):
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="blah blah blah")[0])
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="Everything sucks")[0])
      self.assertNotEquals(0,hat_chatbot.converse_terminal(input="OMG yay wow!")[0])

if __name__ == '__main__':
    unittest.main()
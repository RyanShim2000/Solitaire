import pygame
import random
class Card:
	""" A card is made up of a suit and a value
	Attributes: value,suit
	"""

	def  __init__(self,value,suit):
		self.value = value
		self.suit = suit

	def __str__(self):
		self.value_translate = [1,2,3,4,5,6,7,8,9,10,'jack','queen','king']
		self.suit_translate = ['diamond','club','heart','spade']

		return "{}_{}.png".format(self.value_translate[self.value],self.suit_translate[self.suit])

class Deck(Card):
	""" A standard deck of 52 playing cards"""

	def __init__(self):

		self.deck_lst = []
		for s in range(4):
			for val in range(13):
				card = str(Card(val,s))
				self.deck_lst.append(card)


	def __str__(self):

		res = []
		for card in self.deck_lst:
			res.append(str(card))
		return '\n'.join(res)

	def pop_card(self, i=-1):
		"""Removes and returns a card from the deck.

		i: index of the card to pop; by default, pops the last card.

	    """

		return self.deck_lst.pop(i)


	def add_card(self,card_name):
		return self.deck_lst.append(card_name)

	def shuffle(self):
		"""Shuffles the cards in this deck."""
		random.shuffle(self.deck_lst)


	def pile(self, num):
		self.card_info_lst = []
		self.pile1_lst = []
		x = 120+(num*90)
		x2 = 40
		y = 75
		for i in range(num):
			self.card_info_lst.append(self.pop_card())

			self.card_info_lst.append(x)

			self.card_info_lst.append(y)
			self.pile1_lst.append(self.card_info_lst)
			y+=25
			self.card_info_lst = []

		return self.pile1_lst


def card_image(card_name):
    suits = ['diamond','club','heart','spade']
    values_face = ['jack','queen','king']
    image_dic = dict()
    c = 11

    for s in suits:

        for i in range(1,11):
            name = '{}_{}.png'.format(i,s)
            image = pygame.image.load( name)
            image_dic[name] = image

        for v in values_face:
            name = '{}_{}.png'.format(v,s)
            image = pygame.image.load( name)
            image_dic[name] = image
            
            c+=1

    return image_dic[card_name]



















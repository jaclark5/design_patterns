
"""
    Examples using OOP in Python
"""

import abc

# class Item(object): # py2 and py3
#class Item: # only py3
class Item(abc.ABC): # defines as an abstract class

    # Class attributes
    _count = 0 # because this is outside of a def, this can be used in any methods defined below. This variable is the same memory used by all instances of the class    

    def __init__(self, name):
        self.name = name # public
        self._private_name = "don't access" # private (protected)
        # private variables are used internal use, other people shouldn't depend on them
        self.__really_private = "don't access" # private (protected) can't access even if you try
        Item._count += 1 # take care to update the class variable using the class, this is actually unsafe....
# 1       #x = 1

# 1   def get_name(self):
# 1       # x # this is unknown from definition above

    @classmethod # we use a decorator to define a class method so that it's shared in all instances
    def print_count(cls):
        print("Count = ", cls._count)
    # Use this if only using class attributes, it won't interact with specifics of the class

    # static method doesn't have anything to do with the class or instance
    @staticmethod
    def print_date():
        print("Today is ..")

#    @abc.abstractmethod
    def calc_price(self):
        pass
        # having it pass makes this an abstract class, So it isn't complete and must be defined in an instance
        #print("calc the price")

# __________________________________________________________________#
#book_item = Item('Cats') # this no longer works with an abstract class

#print(Item)
#print(book_item)
#print(book_item.name)
#print(book_item._private_name)

##print(book_item.__really_private)

#book_item.print_count()

#another_item = Item(name="Pens")
#another_item.print_count()
#book_item.print_count()
#Item.print_count()

# __________________________________________________________________#
#                      Subclasses                                   #
# __________________________________________________________________3

class BookItem(Item):

    def __init__(self,name,author):
        self.author = author
        # we overwrote init so we need to call the parent
        super().__init__(name)

    def get_author(self):
        return "Sam"

    def calc_price(self):
        print("Price of book")

# __________________________________________________________________#

my_book = BookItem(name="Moon",author="Sam")
my_book.print_count()
print("Name: ", my_book.name)
my_book.calc_price()
#book_item.calc_price()

item = Item("myname")
print(item)

for i in (item, my_book):
    i.print_date()
    i.print_count()
    i.calc_price()


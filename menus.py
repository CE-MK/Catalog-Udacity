from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="marc.k1205@gmail.com")
session.add(User1)
session.commit()

# Menu for Burgers Kitchen
restaurant1 = Restaurant(name="Burgers Kitchen", user_id="1")

session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Cheese Burger,
                     description=" Our Favourite Burger, with some cheese"
                     "on top",
                     price="$3.99", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Meat Maddness",
                     description=" Burger with tripple"
                     "beef and cheese.",
                     price="$9.25",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Veggi Burger",
                     description="Burger bun with fresh"
                     "vegetables.",
                     price="$3.50", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()


# Menu for Noodle King
restaurant2 = Restaurant(name="Noodle King")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Spaghetti Bolognese,
                     description="Fresh homemade Spaghetti with Meatballs.",
                     price="$8.99", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Spaghetti Verdure",
                     description="Fresh homemade Spaghetti"
                     "with Vegetables and Cheese Sauce.",
                     price="$12",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(name="Spaghetti Cheeslover,
                     description="Spaghetti with 3 different cheese sauces",
                     price="$11.25", restaurant=restaurant2)

session.add(menuItem3)
session.commit()


print "Added menu items!"

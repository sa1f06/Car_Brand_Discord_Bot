# Car Brand Discord Bot

A Discord bot made in python which retrieves key information about different car brands by web scraping Wikipedia.

Features:
- Retrieves car brand details, such as the date it was founded, founder or founders, where the headquarters are based, and the revenue.
- Only displays data available, so if the user types something invalid, like pizza, the bot will return "Sorry, I can't find any information for Pizza".

Testing:

Whilst testing, I found that the bot would return the correct information to the user every time.

 However, some information was missing depending on the car brand. For example, if revenue wasn't in the infobox (in the html) in the wikipedia page of a certain car brand, it would not be returned to the user, so some car brands have more information returned to the user than others.

 Examples:

 ![BMW example](images/bot_bmw.png)
 ![Ferrari example](images/bot_ferrari.png)
 ![Audi example](images/bot_audi.png)
 ![Pizza example](images/bot_pizza.png)
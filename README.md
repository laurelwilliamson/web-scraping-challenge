# web-scraping-challenge
This "Mission to Mars" project scrapes info from three websites.

It gathers the most recent article title and summary from a Mars news site.
It gathers images, URLs, and titles from a Mars image site.
It gathers a table of information about the planet.

Using a flask app, a python script containing a dictionary of the scraped data is sent to a Mongo database.

This database is scraped and used to create the landing page.

Clicking "Scrape New Data" will send current scraped information to the Mongo database, and refreshing will update the landing page.


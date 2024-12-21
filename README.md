Implemented web scraping on some specific product features from Petlebi website.

Petlebi website link: https://www.petlebi.com/

File descriptions:

petlebi_scrapy.py: The program file that scrapped data collection from website and load the data to "petlebi_products.json" file with a class that inherit Scrapy.

import_products.py: The file, read data from "petlebi_products.json" file, and insert these data to local MySQL database.

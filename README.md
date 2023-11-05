# scrapy_c1pemilu2019

Scrapper tool to get the realcount data by KPU during Indonesia Election 2019. This data later on can be used to compare the data with the source-crowd based real count.
The output is data in TPS level.

### Prerequisite:
- Scrapy (https://docs.scrapy.org/en/latest/intro/install.html)
- Python v 3.x.x
- 

### Usage
run the scrapper with below command to output in json file:

``
scrapy crawl pilpres -o [filename.json]
``

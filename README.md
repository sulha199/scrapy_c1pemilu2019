# scrapy_c1pemilu2019

Scrapper tool to get the realcount data by KPU during Indonesia Election 2019. This data later on can be used to compare the data with the source-crowd based real count.
The output is data in TPS level.

### Prerequisite:
- Scrapy (https://docs.scrapy.org/en/latest/intro/install.html)
- Python v 3.x.x
- 
https://3.0.devk8s.azavista.com/s/event/64145d37103a8edfd98bec44?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaW5rdG9rZW4iOiI2NDlhZGI0Y2UwZGVlZjJkNTVlYjNkYWQiLCJlbWFpbCI6InNodWxoYS55YWh5YUBhemF2aXN0YS5jb20iLCJlbnRpdHlfaWQiOiI2NDcwNjg4NTJhYzhiMDJlYzhhMzRhMGQiLCJ0eXBlIjoiUGFydGljaXBhbnQiLCJjbCI6IkFaQVZJU1RBLUxJTktUT0tFTiIsInQiOiJhdXRoIiwiaWF0IjoxNjg3ODcwMjg0LCJleHAiOjE3MTk0MDYyODR9.wsSexzVBKtdH5gtUmvvP2Sag9zPqlxyB5mI5v0eApOE&target_id=64972294fb3172db1ba5420f&email_id=649adb4c2832ea049e669494
### Usage
run the scrapper with below command to output in json file:

``
scrapy crawl pilpres -o [filename.json]
``

# OLX Web Crawler
A web crawler that scrapes smartphone listings data from OLX.bg (a popular buy and sell website in Bulgaria).

# Instructions
Go to your Terminal, in your project directory and type:
```console
scrapy crawl electronics
```
The *third parameter* is the name of the spider that you want to run. It is set in the name property of the created Spider class.  
You can disable the debugger if you don’t want to see debugging information:
```console
scrapy crawl --nolog electronics
```
# Output
It returns a .csv file that contains objects for item listings in the following format:
```yaml
{
  "title": "SAMSUNG J4 Perfektno Sastoyanie", 
  "price": "149 lv.", 
  "location": "Kamenitsa 1, gr. Plovdiv, Oblast Plovdiv", 
  "condition": "izpolzvano", 
  "url": "https://www.olx.bg/ad/samsung-j4-perfektno-sastoyanie-CID632-ID8q8fz.html"
}
```

The extracted data can then be used to perform statistics and extract useful information

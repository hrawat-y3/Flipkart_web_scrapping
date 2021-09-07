# Flipkart_web_scrapping

This is a Scrapy project to scarp product details from Flipkart and storing the data in MongoDB cloud/localhost for further analysis when needed.

# Extracted Data

This project extract Item name, brand, original price, selling price, discount percentage, image url, product category and product page url.

```
{

  "name": ["Men Slim Fit Printed Slim Collar Casual Shirt", ...], 
  "brand": ["ASIAN & FITCH", ...], 
  "original_price": ["1,287", ...], 
  "sale_price": ["455", ...], 
  "image_url": ["//static-assets-web.flixcart.com/www/linchpin/fk-cp-zion/img/fa_62673a.png", ...],
  "product_category": ["Topwear"], 
  "product_page_url": "https://www.flipkart.com/clothing-and-accessories/topwear/pr?          sid=clo%2Cash&otracker=categorytree&p%5BD=facets.ideal_for%255B%255D%3DMen&page=3"
  
  },
```

# Spiders 

This project contains one spider 

```
$ scrapy list
flip_spider
```

# Running Spider and Saving data
The spider can be run by command:

```
$ scrapy crawl flip_spider
```

To save the data in .json:

```
$ scrapy crawl flip_spider -o items.json
```


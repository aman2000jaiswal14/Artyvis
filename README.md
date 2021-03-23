## Artyvis
### Scrapping details
- https://www.houseofindya.com/
- https://www.houseofindya.com/zyra/necklace-sets/cat


### Dir Structure
```
scrapping
  │   output.csv
  │   output.json
  │   requirements.txt
  │   scrapy.cfg
  │   
  └───scrapping
      │   items.py
      │   middlewares.py
      │   pipelines.py
      │   settings.py
      │   __init__.py
      │   
      └───spiders
             main_code.py
             __init__.py

```

<h3>  <span style="color: green">Code is written in main_code.py </span></h1>

## Test Project
 - open pycharm
 - choose conda python 3.8 interpreter
 - install requirements
    - pip install -r requirements.txt
 - run
    - scrapy crawl NecklaceSets -o NAME_OF_OUTPUTFILE.json


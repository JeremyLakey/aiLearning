from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import collections

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver=webdriver.Chrome(options=options)

def scrap_recipe(url):
    driver.get(url)
    print(" ")
    print(url)

    eles = driver.find_elements(By.TAG_NAME, 'script')
    for e in eles:
        tex = e.get_attribute('innerText')

        if "\"recipeIngredient\"" in tex:
            meta = json.loads(tex)
            if type(meta) is dict:
                if "name" in meta:
                    print(meta["name"])
                else:
                    for key in meta["@graph"]:
                        if key["@type"] == 'Recipe':
                            print(key["name"])
                            print(key["recipeIngredient"])
                            for step in key["recipeInstructions"]:
                                print(step['text'])
            else:
                print(meta[0]["name"])
            i = tex.find("\"recipeIngredient\"")
            j = tex[i:].find("]")
            result = json.loads( '{ ' + tex[i:i+j+1] + ' }')
            ingredients = result["recipeIngredient"]
            for ing in ingredients:
                print(ing)



urls = ["https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/","https://www.allrecipes.com/recipe/17481/simple-white-cake/"]

for u in urls:
    scrap_recipe(u)
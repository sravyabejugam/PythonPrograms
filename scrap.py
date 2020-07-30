import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import connection


flip_url="https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=21fbd33f-a8c4-4005-ac14-2b552a1454b8/?page="
page_num_MAX = eval(input("enter the number of pages to parse"))
dbname = input("enter the database name")
scrapped_list = []
connection.connect(dbname)

for page_num in range(1 , page_num_MAX):
    req = requests.get(flip_url + str(page_num))
    content = req.content

    soup = BeautifulSoup(content,"html.parser")

    all_laptops = soup.find_all("div",{"class":"_1UoZlX"})


    for laptop in all_laptops:
        laptop_dict = {}
        laptop_dict['name']=laptop.find("div",{"class":"_3wU53n"}).text  
        laptop_dict['price'] = laptop.find("div",{"class":"_1uv9Cb"}).text 
    
        try:
            laptop_dict['rating'] = laptop.find("div",{"class":"niH0FQ"}).text  
        except:
            pass

        parent_laptop_features = laptop.find("div",{"class":"_3ULzGw"})  

        feature_list=[]

        for feature in parent_laptop_features.find_all("li",{"class":"tVe95H"}):
            feature_list.append(feature.text)

        laptop_dict['features'] = ','.join(feature_list)
        scrapped_list.append(laptop_dict)

        connection.insert_into_table(dbname ,tuple(laptop_dict.values()))

dataframe = pd.DataFrame(scrapped_list) 
dataframe.to_csv("flipkart.csv")        
connection.get_info(dbname)

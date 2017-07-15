from bs4 import BeautifulSoup
import json
import re
import time
from datetime import datetime
import requests
import csv
import sys


HEADER_ROW = ['Address','Square','TOF','Floor','Room','Price','Date','Url']


def check_row_in_csv(row_array):
    # [address,square,TOF,floor,room,price,"https://www.ss.lv"+link]
    with open('file_name.csv', 'rt',encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row_array == row: # if the username shall be on column 3 (-> index 2)
                return True
        f.close()
    return False

# function to return obj of html page
def get_page(url):
        page = ''
        try:
            response = requests.get(url)
            page = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            # print("page errt",e)
            if "IncompleteRead" in str(e):
                response = requests.get(url)
                page = BeautifulSoup(response.text, 'html.parser')
                time.sleep(15)
                return page
        return page

def write_row_in_csv(sellers,file_name):
    with open(file_name+".csv", "a", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        if not check_row_in_csv(HEADER_ROW):
            writer.writerow(HEADER_ROW)


if __name__ == "__main__":
    print("start doing tasks here")




# Beautiful soup examples for quick start
# if not check_for_skipping_ad(one_page.find(id='msg_div_msg').text):
#                 address = one_page.find(id='tdo_11').text
#                 if address:
#                     address = address.replace(" [Карта]","")
#                 address = address.replace(',',' ')
#                 square = one_page.find(id='tdo_3').text.replace(',',' ')
#                 TOF = one_page.find(id='tdo_6').text.replace(',',' ')
#                 floor = one_page.find(id='tdo_4').text.replace(',',' ')
#                 room = one_page.find(id='tdo_1').text.replace(',',' ')
#                 price = one_page.find(id='tdo_8').text.replace(',',' ')
#                 row_to_insert = [address,square,TOF,floor,room,price,todays_date,"https://www.ss.lv"+link]
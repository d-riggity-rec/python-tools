import requests
import json
import pandas as pd
from PIL import Image
from io import BytesIO

ygo_path = 'ygo_card_data.json'        # file path for json data we're parsing, may need to adjust directory if downloaded locally
ygo_img_fle = 'c:/scripts/ygo_img/'    # new directory for downloaded .jpg files from json data

################### Read Local JSON file ##############################
with open(ygo_path, 'r') as ygo_data:
    ygo_json = json.load(ygo_data)
#######################################################################


################### Main Loop Starts Here #############################
for ygo_key, ygo_arr in ygo_json.items():
    ygo_val_arr = ygo_json[ygo_key]

    for ygo_itm in ygo_arr:    # ygo_itm is actually a dictionay, but also an index in ygo_arr
        ######################### Get Card Data ################################
        card_mktpx = '----no cardmarket price'
        card_tcgpx = '-----no tcgplayer price'
        box_set = '-----no box set'
        num_id = str(ygo_itm["id"])
        if 'card_prices' in ygo_itm.keys():

            #  fully troubleshoots both cardmarket_price and tcgplayer_price in card_prices
            #  keys below are inside the scope of card_prices dictionary
            card_mkt_tc_dict = ygo_itm["card_prices"][0]
            if 'cardmarket_price' in card_mkt_tc_dict.keys():
                card_mktpx = card_mkt_tc_dict["cardmarket_price"]
            if 'tcgplayer_price' in card_mkt_tc_dict.keys():       
                card_tcgpx = card_mkt_tc_dict["tcgplayer_price"]
        if 'card_sets' in ygo_itm.keys():
            box_set = ygo_itm["card_sets"][0]["set_name"]
        nme = ygo_itm["name"]
        ########################################################################

        ################  Fetch JPG file from web address ######################
        card_num_dict = ygo_itm["card_images"][0]['image_url']
        jpg_dir = ygo_img_fle + num_id + '.jpg'

        ### Only un-hash lines below if you've established a directory for 'ygo_img_fle' ###

        # response = requests.get(card_num_dict)
        # if response.status_code == 200:
        #     # Read the image data from the response
        #     image_data = response.content
        #     ygo_img = Image.open(BytesIO(image_data))
            # ygo_img.save(jpg_dir)
        ##############################################################


        ################# Print Dictionary Values ####################
        print(f'Name: {nme}; Card No.: {num_id}')

        ##############################################################

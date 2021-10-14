
import os 
import json 
import sys 

telegram_keys = open('../telegram_vc_sample/auth_telegram.txt', 'r')
robinhood_keys = json.load(telegram_keys)
API_KEY = robinhood_keys['API_KEY']
API_SECRET = robinhood_keys['API_HASH']
STRING_SESSION = robinhood_keys['STRING_SESSION']



# print(robinhood_keys)



    # json_data = json.load(telegram_keys)
    # print(json_data['8607483'])



# for line in telegram_keys:
#     if 'API_KEY' in line:
#         telegram_key = line(line.index('=')+1, len(line)-1)
#         print("API_KEY", telegram_key)








        # print(line[line.find('API_KEY')

    #     bot_token = line.split('=')[1].strip()
    # elif 'bot_username' in line:
    #     bot_username = line.split('=')[1].strip()



# print(telegram_keys.read())
# print(telegram_keys['API_KEY'])
# if not telegram_keys:
#     print("No keys found")
    # sys.exit(1)
# try:
#     # gatsby_keys = json.load(gatsby_key)
#     robinhood_keys = json.load(telegram_keys)
# except :
#     print("Error: Keys not found")
#     sys.exit()


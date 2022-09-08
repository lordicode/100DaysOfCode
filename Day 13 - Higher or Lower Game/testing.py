import pandas as pd

#parse the name of the file for the correct gamemode
file = 'YouTube.xlsx'

dict_for_game = {}#create a dictionary


#read excel file with pandas put the read data into a dataframe
excel = pd.read_excel(file)
#concatenate the title of the video with channel name
excel = excel['title'].astype(str) + " Channel: " + excel['channel_title']
#populate dictionary with values
for i in excel:
    dict_for_game[i] = '100'

for key, value in dict_for_game.items():
    print(key + "|\n" + value)



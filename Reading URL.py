import requests
import io
import os

os.chdir(r'C:\Users\komsi\Desktop\Smart Methods\Third Path\Reading URL\New tests') #this is only to change the directory of all files saved , you can delete this and the files will be saved in the working directory
user_URL = input('input the URL you want to read : ')
response = requests.get(user_URL)
k = int(input('if you want to save the HTML code of your URL press 1 , if it is a picture and you want to save it press 2  , if you want to know the status of your URL press 3 : '))
if k == 1:
    with open ('URL as html code.txt','wb') as f:
        f.write ((response.text).encode('utf-8'))
        print('Successfully saved')
if k == 2:
    with open ('URL tp pic.png','wb') as f:
        f.write(response.content)
        print('Successfully saved')
if k == 3:
    print(response.ok)
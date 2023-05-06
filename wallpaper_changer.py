#  imports the shit I need
import requests
import ctypes
import os

#  this is my access key and the url for unsplash api
access_key = "Your speacial access key will go here!"
url = f"https://api.unsplash.com/photos/random?client_id={access_key}&orientation=landscape" #  Gets the photo and only selects landscape

#  gets the image url and assigns it as the variable 'response'
response = requests.get(url)

#  this downloads the wallpaper and saves it to the correct file location
def download_wallpaper(url):
    if response.status_code == 200: #  This checks to see if the image was sucesfully imported
        image_url = response.json()['urls']['full'] #  This extracts the full version of the url (with image ID)
        image_data = requests.get(image_url).content #  This requests the Actual URL from the API
        file_path = os.path.join(os.getcwd(), "downloaded_wallpapers", "wallpaper.jpg") #  This saves the downloaded JPG to the correct location
        with open(file_path, 'wb') as handler: #  This is some magic python stuff that basically writes the file correctly for  JPG type file
            handler.write(image_data)
            print("Wallpaper downloaded successfully.") #  The sole purpose of this is so i know the wallpaper was sucessfully downloaded
    else:
        print(f"Error fetching random wallpaper: {response.status_code}") #  This returns the error code if there was an issue retrieving the JPG

def set_wallpaper():
    SPI_SETDESKWALLPAPER = 20 # This is the function to set the wallpaper for windows 
    {ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,  os.path.join(os.getcwd(), 
    "downloaded_wallpapers", "wallpaper.jpg"), 0)}  #  This calls the ctype mod so we can use windows commands to set the wallpaper

if __name__ == "__main__": #  This verifies that this program is running on this local machine
    download_wallpaper(url) # This runs the download function
    set_wallpaper() #  This runs the set wallpaper function


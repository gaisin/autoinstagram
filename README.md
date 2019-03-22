# Instapost: automating instagram image posting

Small scripts, allows you to fetch images from SpaceX's and Hubble's APIs, and post them to Instagram. 

### How to install

Python 3 has to be already installed.  
  
After cloning the repository, use `pip` (or `pip3` in case of conflicts with Python 2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use
  
#### Step one: fetch images using SpaceX's API
It's pretty simple, you just can run ```fetch_spacex.py``` script. It will save all images to ```images``` folder.  
  
#### Step two: fetch images using Hubble API
Pretty the same, just run ```fetch_hubble.py``` script, and your pictures will be downloaded to the same ```images``` folder. You can set up different collection name in the ```main``` function.  
  
#### Step three: publish!
You need an Instagram account. Put username and password to a .env file, check ```.env_example``` as example. Better not use you personal account, since it can be banned. After finishing with an account, you can run a script and make all images published by the script.  
  
**Warning**  
Since the library simulates the user's input from a mobile device, the bot can take a pause for five minutes in case of a large number of requests. Don't worry about that.

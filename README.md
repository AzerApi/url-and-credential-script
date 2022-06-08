# url-and-credential-script



a url and credentials generation script made with vs code and github copilot

scrambles a word to provide 5 unique urls


 ## usage
 
 ```
 dev -u -p -un
 
 -u --url: provide what you want to be scrambled into a url
 -p --password: generates a password
 -un --username: generates a username
 -h --help: provides help
 ```
 
## setup

### using z shell:
```
nano ~/.zshrc

in a new line type:
  alias dev ='python 3path/to/file/dev.py'
 
 ```
 
 ### using bash:
 
 ```
 nano ~/.bash_profile
 
 in a new line type:
  alias dev ='python3 path/to/file/dev.py'
 
 ```
 
 ### using python3
```
python3 path/to/file/dev.py
```
 ## Important
```
copy the following to a file called urlConfig.py
  url = {
      "urlPart1": "YourUsernameHere-",
      "urlPart2": "YourHostHere",
  }
  
  replace YourUserNamehere with the username you want plus a -
  replace yourhosthere with your host
  


``` 
 ## url config file
 ```
 to use the generator you need to have the urlConfig.py file in your directory with the dev.py script
 
 ```



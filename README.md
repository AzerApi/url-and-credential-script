# url-and-credential-script



a url and credentials generation script made with vs code and github copilot

scrambles a word to provide 5 unique urls


## setup

### using z shell:
```
nano ~/.zshrc

in a new line type:
  alias dev ='path/to/file/dev.py'
 
 ```
 
 ### using bash:
 
 ```
 nano ~/.bash_profile
 
 in a new line type:
  alias dev ='path/to/file/dev.py'
 
 ```
 ## Important
```
In the same dir as dev.py do the following:
Make a file called "urlConfig.py"
save the file
open the file with nano or a ide

write the following:
  url = {
      "urlPart1": "YourUsernameHere-",
      "urlPart2": "YourHostHere",
  }

``` 
 ### usage
 
 ```
 dev -u -p -un
 
 -u --url: provide what you want to be scrambled into a url
 -p --password: generates a password
 -un --username: generates a username
 -h --help: provides help
 ```
 
 ### url config file
 ```
 to use the generator you need to have the urlConfig.py file in your directory with the dev.py script
 
 ```

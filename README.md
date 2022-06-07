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
 ##Important
```
In the same dir as dev.py do the following:
Make a file called "urlConfig.py"
save the file
open the file with nano or a ide

type the following:
 url = {
    "urlPart1": "",
    "urlPart2": "",
 }
within the parentese write your preferd username(like Azzey-)in the spot 
after urlPart1  and write your hostname in de parentese after urlPart2 
``` 
 ### usage
 
 ```
 dev -arg -arg -arg
 
 -u --url: provide what you want to be scrambled into a url
 -p --password: provide a number than generates a password
 -un --username: provide a number then generates a username
 -h --help: provides help
 ```
 
 ### url config file
 ```
 to use the generator you need to have the urlConfig.py file in your directory with the dev.py script
 
 ```

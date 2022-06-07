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
 
 ### usage
 
 ```
 dev -arg -arg -arg
 
 -u --url: provide what you want to be scrambled into a url
 -p --password: provide a number than generates a password
 -un --username: provide a number then generates a username
 -h --help: provides help
 ``
 
 ### url config file
 ```
 to use the generator you need to have the urlConfig.py file in your directory with the dev.py script
 
 ```

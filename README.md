# url-and-credential-generator-script



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
   alias dev ='python3 path/to/file/dev.py'

  ```
 
  ### using bash:

  ```
  nano ~/.bash_profile

  in a new line type:
   alias dev ='python3 path/to/file/dev.py'

  ```
 
  ### using python3:
 ```
 python3 path/to/file/dev.py
 ```
 ### using powershell:
 #### create a profile(if you don't have one already)
 ```
 New-Item -Type file -Force $profile
 ```
 #### open the file using vs code
 ```
 code $profile
 ```
 #### in the profile file copy the following
 ```
 Set-Alias dev "python3 $HOME\path\to\dev.py"
 ```


 ## Important
```
rename the py.urlConfig.py  file to urlConfig.py

replace YourUserName with your preferd username plus a -
replace YourHostName with your host

save it to the same file location as the dev.py script
  
``` 




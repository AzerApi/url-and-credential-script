#! usr/bin/env/python3
# name: Dev tools py script
# author: @Azzey
# date: 2020-04-10
# version: 1.0
# description: This script is a tool to help you with development
# --help: use 1 or 2

import string
import time
import os
import urlConfig as cfg
import random
import argparse

parser = argparse.ArgumentParser()


#url argument
parser.add_argument(
    "--url",
     "-u", 
     default="test", 
     help="generate urls",
     type=str,
)
#password argument
parser.add_argument(
    "--password",
    "-p", 
    default="hallo",
    help="generate password",
    type=str,
)

#username argument
parser.add_argument(
    "--username", 
    "-un", 
    default="hallo", 
    help="generate username", 
    type=str,
)



#main function with args passed in
def main(args):


 if args.url:
     if args.url == "test":
         print("please provide a word")
     else:
        generate_urls(args.url)
     if args.password:
         if args.password == "test":
             print("please provide a word")
         else:
            generate_password()  
     if args.username:
         if args.username == "test":
             print("please provide a word")
         else:
            generate_username()

#funtion to generate permutations
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

#function to generate urls
def generate_urls(args):

    urlPart1 = cfg.url["urlPart1"]
    urlPart2 = cfg.url["urlPart2"]
    count= 0
    word = args


    list = all_perms(word)
    os.system("clear")
    print("de volgende urls zijn bedacht:")
    for word in list:
        print(f"{urlPart1}{word}{urlPart2}")
        count = count + 1
        if count == 5:
            print("5 urls zijn gegenereerd")
            break

#function to generate a random password
def generate_password():
    password = ""
    for i in range(8):
        password = password + random.choice(string.ascii_letters + string.digits)
    print(f"your password is: {password}")
    return password

#function to generate a random username
def generate_username():
    username = ""
    for i in range(8):
        username = username + random.choice(string.ascii_letters + string.digits)
    print(f"your username is: {username}")
    return username

#call main function with parsed args passed in
main(parser.parse_args())












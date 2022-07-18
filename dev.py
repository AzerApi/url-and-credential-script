import string
import time
import os
import urlConfig as cfg
import random
import argparse

path = cfg.path["path"]

# call parser
parser = argparse.ArgumentParser()


# add url argument
parser.add_argument(
    "--url",
    "-u",
    default="test",
    help="generate urls",
    type=str,
    required=True,
)
# add password argument
parser.add_argument(
    "--password",
    "-p",
    default="hallo",
    help="generate password",
    type=str,
    nargs="?",
    const="hallo",
    required=True,
)

# add username argument
parser.add_argument(
    "--username",
    "-un",
    default="hallo",
    help="generate username",
    type=str,
    nargs="?",
    const="hallo",
    required=True,
)

# main function with args passed in
def main(args):
    # if statement tree to call functions based on args passed in
    if args.url:
        if args.url == " ":
            print("please provide a word")
        else:
            generate_urls(args.url)
        if args.password:
            if args.password == " ":
                print("please provide a word")
            else:
                generate_password()
        if args.username:
            if args.username == " ":
                print("please provide a word")
            else:
                generate_username()
                new_line()


# funtion to generate permutations
def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


# function to generate urls
def generate_urls(args):

    urlPart1 = cfg.url["urlPart1"]
    urlPart2 = cfg.url["urlPart2"]
    count = 0
    date = time.strftime("%Y-%m-%d")
    Time = time.strftime("%H:%M:%S")
    dateAndTIme = date + " " + Time
    word = args
    f = open(f"{path}/url.links", "a")
    f.write(dateAndTIme)
    f.write("\n")
    list = all_perms(word)
    os.system("clear")

    for word in list:
        print(f"{urlPart1}{word}{urlPart2}")
        count = count + 1

        f.write(f"{urlPart1}{word}{urlPart2}\n")
        if count == 10:
            break
        # open url.links and append to file


# function to generate a random password
def generate_password():
    password = ""
    f = open(f"{path}/url.links", "a")
    for i in range(20):
        password = password + random.choice(string.ascii_letters + string.digits)
    print(f"your password is: {password}")
    f.write(f"your password is: {password}\n")
    return password


# function to generate a random username
def generate_username():
    username = ""
    f = open(f"{path}/url.links", "a")
    for i in range(8):
        username = username + random.choice(string.ascii_letters + string.digits)
    print(f"your username is: {username}")
    f.write(f"your username is: {username}\n")
    return username


# append new line function
def new_line():
    f = open(f"{path}/url.links", "a")
    f.write("\n\n")
    f.close()


# call main function with parsed args passed in
main(parser.parse_args())

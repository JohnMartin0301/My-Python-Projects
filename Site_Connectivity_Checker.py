# import urllib, # use urllib to get the data from the url, # write a function that takes a url, # return a response

import urllib.request as urllib

def main(url):
    print("Checking connectivity... ")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully")
    print("The response code is:", response.getcode())

print("This is a site connectivity checker program.")
input_url = input("Input the url of the site you want to check for connectivity: ")

main(input_url)
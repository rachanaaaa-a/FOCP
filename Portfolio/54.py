#4Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.
import sys
import requests
def check_website(url):
    try:
       
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The Website {url} working.")
        else:
            print(f"The Website {url} is not working.")
    except requests.exceptions.RequestException as e:
        
        print(f"Failed to reach {url}. Error: {e}")

if len(sys.argv) != 2:
    print("Please provide only URL as a command-line argument.")
else:
    
    url = sys.argv[1]
    check_website(url)
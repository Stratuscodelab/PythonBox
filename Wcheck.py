import pyfiglet
import requests



# This script checks if a website is up or down using the requests library. Very smol script.

result = pyfiglet.figlet_format("Website Checker", font = "banner3-D" )
print(result)

def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is up and running")
        else:
            print(f"{url} is down.")
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")

websites = ["",  ""]
for website in websites:
    check_website(website)
import requests
import sys
import time
import random
from paths import common_paths, userAgents

# prompt for normal search,
# vpn on off,
# add different user agents
success_list = []
delay = random.uniform(0.2, 0.3)


def fuzzy():
    attempts = 0
    num_of_common = len(common_paths)
    for path in common_paths:
        time.sleep(delay)
        fuzz = website_url + path
        statuscode = print_response(fuzz)
        # print(statuscode, fuzz)
        if statuscode == 200:
            # print("code 200 found", statuscode, fuzz)
            attempts += 1
            print(str(attempts) + "/" + str(num_of_common), path)
            success_list.append(fuzz)
        else:
            attempts += 1
            print(str(attempts) + "/" + str(num_of_common), path)


def print_response(website_url):
    response = requests.get(website_url)
    code = response.status_code
    # print(f"Status Code: {code}")
    return code


def chk_format(website_url):
    if (website_url.startswith("http://") or website_url.startswith("https://")) and "." in website_url:
        print("")
        print("URL Accepted")
        print("")
        if not website_url.endswith("/"):
            website_url = website_url + "/"
    else:
        print("")
        print("URL Not Properly formatted \nTry Again ")
        print("URL example: http://google.ca")
        sys.exit()

    return website_url  # Return the modified URL

def results():
    for x in success_list:
        print(x)

website_url = input("Enter the URL to Fuzz: ")
website_url = chk_format(website_url)
fuzzy()

print('')
print('Results:')
print('')
results()



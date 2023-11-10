Fuzzy
==============

Fuzzy represents a URL fuzzing tool equipped with nuanced functionalities designed to intelligently uncover URL paths while maintaining a balanced approach without overly aggressive scanning methodologies.


Brief description of url fuzzer
--------------
A URL fuzzer is a cybersecurity tool used in penetration testing and security assessments to discover potential vulnerabilities in web applications or websites. It operates by systematically generating and sending varied or mutated HTTP/S requests to different URLs or endpoints of a target web application.


Dependencies
-------------- 
Fuzzy requires:

```
import requests
import sys
import time
import random
from paths import common_paths, userAgents
```

*Make sure to put the "paths.py" file in the same directory as the "urlfuzzer.py"

Usage
--------------

The script will prompt the user to enter a url to fuzz, please note that the url must include protocol in the url ("http://" or "https://")

If the url is valid, a "URL Accepted" text will appear. If not then you need to properly format the url

Example Usage:

```
Enter the URL to Fuzz: https://www.xyz.store
```

Results
--------------

The script will then calculate the number of path extensions in the "paths.py" file. 
It will iterate though the list of common path extensions one by one.
There is a random delay between the requests to the server between 0.2 - 0.8 seconds
When the fuzzing is complete it will display the valid urls found with code 200 at the end of the script


```
Results:

http://www.xyz.store/robots.txt
http://www.xyz.store/admin
http://www.xyz.store/storage
http://www.xyz.store/superuser
```

Warning
--------------

URL fuzzers are powerful tools used in cybersecurity for probing web applications and discovering potential vulnerabilities. However, it's crucial to exercise extreme caution and ethical responsibility when using URL fuzzers. Only deploy these tools on web servers that you own or have obtained explicit permission to test.

Unauthorized or aggressive use of URL fuzzers on websites or servers without proper authorization is illegal and unethical. It can potentially disrupt services, violate laws, and cause harm to the targeted systems, leading to severe legal consequences.

It is imperative to emphasize that I, as the provider of information on URL fuzzers, cannot be held responsible for any misuse or unauthorized activities conducted using these tools. The user assumes sole responsibility for their actions, and it's crucial to act in compliance with laws, regulations, and ethical guidelines when performing security assessments or penetration tests. Always obtain explicit permission before using URL fuzzers on any web application or server.




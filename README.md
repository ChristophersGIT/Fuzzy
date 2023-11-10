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




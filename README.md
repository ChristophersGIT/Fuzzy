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

Make sure to put the "paths.py" file in the same directory as the "urlfuzzer.py"

Usage
--------------

The script will prompt the user to enter a url to fuzz, please note that the url must include protocol in the url ("http://" or "https://")



# SiteXS

WIP vulnerability scanner on sites, just does basics requests and logging data with DOM XSS vulnerabilities identification, will be adding XXE and other stuff soon.

**Example execution on vuilnerable site:**

```
~/Analysis/SiteXS$ python3 sitexs.py get http://127.0.0.1:8000/xss xss
===================================HEADER DATA===================================
Date: Thu, 22 Sep 2022 05:55:59 GMT
Server: WSGIServer/0.2 CPython/3.8.10
Content-Type: text/html; charset=utf-8
X-Frame-Options: DENY
Content-Length: 1765
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin
===================================XSS DATA===================================
Vulnerability #1: 

getElementById("difficulty")
----------------------------------------------------------------------
Vulnerability #2: 

getElementById("input")
----------------------------------------------------------------------
Vulnerability #3: 

getElementById("disp")
----------------------------------------------------------------------
Vulnerability #4: 

document.write(input)
----------------------------------------------------------------------
Vulnerability #5: 

<script>
            function filter(a)
            {
                
            }

            function validate()
            {
                var option = document.getElementById("difficulty").value;
                var input = document.getElementById("input").value;

                switch(option)
                {
                    case '6':

                    case '5':
                    
                    case '4':
                    
                    case '3':
                    
                    case '2':
                    document.getElementById("disp").innerHTML = input;
                    break;
                    
                    default: 
                    document.write(input);
                }
                return option;
            }
        </script>
----------------------------------------------------------------------
Vulnerability #6: 

innerHTML = input;
----------------------------------------------------------------------
None

```

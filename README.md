

# ProgImage API

A project provides API to allowing uploading, rotating and retrieving pictures,coverting the format.

## Running Environment
Windows  
Python 3.5.4  
Virtual environment  
Django 2.1.1  

## Quick Start

```bash
git clone https://github.com/doraemon1293/django_calc_sum.git
cd django_calc_sum
.\venv\Scripts\Activate.ps1
```
To run server
```bash
python manage.py runserver 5000
```
To run test
```bash
python manage.py test
```

## API
  Calculate the summation of list
  URL: http://localhost:5000/total/
   
  Method: POST
 
  PARAMETER: list
 
  FORMAT: JSON
 
  Example: 
  Use powershell to send the request
   
```bash
$paras = @{  "list"    = "[1,2,3,4,5]"
            }
Invoke-WebRequest -uri "http://localhost:5000/total/" -Method POST -Body $paras
```
   
```bash
StatusCode        : 200
StatusDescription : OK
Content           : {"total": 15}
RawContent        : HTTP/1.1 200 OK
                    X-Frame-Options: SAMEORIGIN
                    Content-Length: 13
                    Content-Type: application/json
                    Date: Mon, 04 Feb 2019 00:01:38 GMT
                    Server: WSGIServer/0.2 CPython/3.5.4

                    {"total": 15}
Forms             : {}
Headers           : {[X-Frame-Options, SAMEORIGIN], [Content-Length, 13], [Content-Type, application/json], [Date,
                    Mon, 04 Feb 2019 00:01:38 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 13
```
## TEST
```
python manage.py test  
```
1. class Test_calc_sum  
  test the api to calculate the summation of list(range(10000001))
  result should be ```{'total': 50000005000000}```

## Author
Yan HUANG

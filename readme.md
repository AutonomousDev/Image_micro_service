This project is made using Python 3.10

To install dependencies run `pip install -r requirements.txt`

To start the test server run `python manage.py runserver`

The debug api endpoint is http://127.0.0.1:8000/api/

The web view of the api has some helpers to show the different paths and request methods. 
The web view can also help with generating request if you switch to the raw data view

/api/image_file is the main end point this microservice will use.

# How to REQUEST data

```python
import requests
import json

# Request example 1: request a image and data set by image id
image_id = '1'
url = "http://127.0.0.1:8000/api/image_file/"

headers = {
    "Media type": "application/json"
}

response = requests.get(url+image_id, headers)
result = json.loads(response.content)

# Pretty Print JSON
json_formatted_str = json.dumps(result, indent=4)
print(json_formatted_str)
```

In this example the get request URL is built using the `http://127.0.0.1:8000/api/image_file/` path 
with the image id appended for a final path of `http://127.0.0.1:8000/api/image_file/1` 

The Header is formatted as json and includes a key specifying the `"Content-Type": "Media type": "application/json"`

Sending the request returns the response which is stored in the response variable

`response = requests.get(url+image_id, headers, json=body)`

In the response you will receive a lot of meta-data about the response, but the content you are interested in is in`response.content` 
formatted as json bytes. Convert it to a usable json type with `result = json.loads(response.content)`

result can now access all the data using the `.`operator.

The formatted print out at the end should display your requested data
```commandline
{
    "id": 1,
    "title": "Darth Vader at the beach",
    "description": "Darth Vader is able to take a break from ruling the galaxy to relax on the beach",
    "alt_text": "Darth Vader on the beach drinking from a coconut",
    "image_file": "http://127.0.0.1:8000/media/darth_vader_vacation_01.jpg"
}
```



# How to RECEIVE data

```python
import requests
import json

# Request example 2: Send a post request with a image

url = "http://127.0.0.1:8000/api/image_file"

post_data = {
    "title": "example",
    "description": "test description",
    "alt_text": "a read example image"
}
files = {
    "image_file": ("example.jpg", open('example.jpg', 'rb'), 'image/jpg')
}

response = requests.post(url, data=post_data, files=files)
result = json.loads(response.content)

# Pretty Print JSON
json_formatted_str = json.dumps(result, indent=4)
print(json_formatted_str)

```
Url is the end point for the post. Note the lack or a trailing slash.
`url = "http://127.0.0.1:8000/api/image_file"`

post data is a dictionary with all our text base content to post. 
``` python
    post_data = {
    "title": "example",
    "description": "test description",
    "alt_text": "a read example image"
}
```

files is where the image gets attached inside another dictionary. 

`"image_file": ("example.jpg", open('example.jpg', 'rb'), 'image/jpg')`
for this line, `"image_file":` is the key and must match what the API expects. 

`("example.jpg", open('example.jpg', 'rb'), 'image/jpg')` this tuple can be read as

`("File name of your choice", open('Path to the file here', 'rb'), 'image/jpg')` 


The post request is populated and the responce is stored in response.
`response = requests.post(url, data=post_data, files=files)`

To convert the response back to useable json run.
`result = json.loads(response.content)`

The last 2 lines print out the response as
```commandline
{
    "id": 7,
    "title": "example",
    "description": "test description",
    "alt_text": "a read example image",
    "image_file": "http://127.0.0.1:8000/media/example.jpg"
}

Process finished with exit code 0
```
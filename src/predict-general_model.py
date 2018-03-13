from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

print(app.tag_urls(['https://zivranch.s3.amazonaws.com/s3fs-public/photo/images/051414%20Male%20Bald%20Eagle%20to%20Clubhouse%20Nest%20GS.JPG']))


from os import listdir
from os.path import isfile, join, abspath

image_path = abspath('./images')
onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]

readme = '''# awesome-video-chat-backgrounds

Just in case you're at home on a video call and you haven't had time to tidy up your REAL background, here are some awesome backgrounds to help you get through your next video chat.  

## Contributing
* Please submit pull requests to add additional photos/images to this collection!
* Images should be minimum of 1080 (width) x 550 (height) pixels

## Image List

'''
for file in onlyfiles:
    title = file.split('.')[0].replace('_',' ').title()
    readme += '<a href="./images/{}" title="{}"> <img align="center" src="./images/{}" /></a>'.format(file, title, file)

with open('README.md','w+') as f:
    f.write(readme)


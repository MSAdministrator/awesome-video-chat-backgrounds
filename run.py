from os import listdir
from os.path import isfile, join, abspath

image_path = abspath('./images')
onlyfiles = [f for f in listdir(image_path) if isfile(join(image_path, f))]

readme = '''# awesome-video-chat-backgrounds

Awesome Video Chat Backgrounds

Below is a list of awesome video chat backgrounds!  Please submit pull requests to add additional photos/images to this collection!

## Image List

'''
for file in onlyfiles:
    list_name = file.split('.')[0].replace('_',' ').title()
    readme += '* [{}](./images/{})\n'.format(list_name, file)
    print('* [{}](./images/{})'.format(list_name, file))

with open('README.md','w+') as f:
    f.write(readme)
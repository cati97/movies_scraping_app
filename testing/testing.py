import json

with open('/home/cati/Desktop/movies_scraping/my_file.json', 'r') as f:
    content = f.read()

if content == '':
    with open('/home/cati/Desktop/movies_scraping/my_file.json', 'w') as file:
        json.dump([], file)



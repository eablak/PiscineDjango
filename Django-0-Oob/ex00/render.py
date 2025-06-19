import sys
import re

def create_html(content):

    html = [
        '<!DOCTYPE html>',
        '<html lang="en">',
        '<head>',
        '<meta charset="UTF-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
        '<title>Document</title>',
        '</head>',
        '<body>',
        content,
        '</body>',
        '</html>'
    ]

    with open("myCV.html","w") as html_f:
        html_f.write("\n".join(html))


def process(content):
    
    try:
        with open("settings.py","r") as file:
            for line in file:
                if "=" in line:
                    key, value = line.split("=")
                    key = key.strip()
                    value = value.strip().strip('"')
                    pattern = r"\{" + re.escape(key.strip()) + r"\}"
                    content = re.sub(pattern,value,content)
    except FileNotFoundError:
        print("File not Found!")
    create_html(content)
    return content


if __name__ == "__main__":
    
    n = len(sys.argv)
    
    if n != 2:
        raise Exception("Arg count should be two")
    if sys.argv[1].endswith(".template") == False:
        raise Exception("Second arg needs to end with .template")
    
    try:
        with open(sys.argv[1], "r+") as f:
            filled_content = process(f.read())
    except FileNotFoundError:
        print("File is not exist")
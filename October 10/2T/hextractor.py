import re
import sys


with open(sys.argv[1], encoding='utf-8') as file:
    html = file.read()

def find_title(html_site):
    pattern = r'<title>(.*?)</title>'
    title = re.findall(pattern, html_site)

    return title


def find_headings(html_site):
    pattern = r"<h[1-6]>(.*?)</h[1-6]>"
    headings = []

    headings.extend(re.findall(pattern, html_site))

    return headings


def convert_to_text(title, headings):
    htmlString = ''
    title = ''.join(title).strip()
    htmlString += f'{title}\n\n'
    for text in headings:
        string = ''.join(text).strip()
        htmlString += f'{string}\n'
    return htmlString

print(convert_to_text(find_title(html), find_headings(html)))
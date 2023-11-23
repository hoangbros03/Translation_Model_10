import argparse
import requests

from bs4 import BeautifulSoup
import nltk
import time

def process(url, output_file):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

    list_stories = soup.find_all('div', class_="col-xs-9 col-sm-6 col-md-5 col-title")

    # print(list_stories)

    a_tags = []
    for story in list_stories:
        a_tags.append(story.find('a'))

        hrefs = []
    for a in a_tags:
        hrefs.append(a.get('href'))

    # print(len(hrefs))
    # for link in hrefs:
    #     print(link)

    for i in range(len(hrefs)):
        hrefs[i] += 'chuong-1'

    # print(len(hrefs))
    # for link in hrefs:
    #     print(link)

    nltk.download('punkt')
    results = []
    for link in hrefs:
        print(link)
        tam_response = requests.get(link)
        if tam_response.status_code == 200:
            tam_soup = BeautifulSoup(tam_response.content, 'html.parser')
            paragraph = str(tam_soup.find('div', id = 'chapter-c').get_text)

            x = paragraph.find('</div>') + 6
            y = len(paragraph) - 1
            paragraph = paragraph[x:y]
            paragraph = paragraph.replace('<br/><br/>', ' . ')
            paragraph = paragraph.replace('</p><p><br/></p><p>', ' . ')
            paragraph = paragraph.replace('<br/>', ' . ')
            paragraph = paragraph.replace('<p><p><br/>', ' . ')
            paragraph = paragraph.replace('</p></p></div>', ' . ')
            paragraph = paragraph.replace('----------oOo----------', ' . ')
            paragraph = paragraph.replace('</div>', ' . ')
            paragraph = paragraph.replace('<p><p>', ' . ')
            paragraph = paragraph.replace('... .', '...')
            paragraph = paragraph.replace('...  .', '...')
            paragraph = paragraph.replace('<p>', ' . ')
            paragraph = paragraph.replace('</p>', ' . ')
            sentences = nltk.sent_tokenize(paragraph)

            for sentence in sentences:
                if (sentence == '*** .'):
                    break
                if (sentence != '.' 
                    and not sentence.startswith('.') 
                    and not sentence.startswith('…') 
                    and not sentence.startswith('*') 
                    and not sentence.startswith(' ')
                    and not sentence.startswith('!')
                    and not sentence.startswith('?')):
                    results.append(sentence)
            next_button = tam_soup.find('a', id="next_chap")
            next_link = next_button.get('href')
            dem = 0
            while (True): 
                print(dem + 1)
                if (next_button.get('title') != 'Không hoặc chưa có chương tiếp theo'):
                    next_link = next_button.get('href')
                    tam_response = requests.get(next_link)
                    if tam_response.status_code == 200:
                        tam_soup = BeautifulSoup(tam_response.content, 'html.parser')
                        paragraph = str(tam_soup.find('div', id = 'chapter-c').get_text)

                        x = paragraph.find('</div>') + 6
                        y = len(paragraph) - 1
                        paragraph = paragraph[x:y]
                        paragraph = paragraph.replace('<br/><br/>', ' . ')
                        paragraph = paragraph.replace('</p><p><br/></p><p>', ' . ')
                        paragraph = paragraph.replace('<br/>', ' . ')
                        paragraph = paragraph.replace('<p><p><br/>', ' . ')
                        paragraph = paragraph.replace('</p></p></div>', ' . ')
                        paragraph = paragraph.replace('----------oOo----------', ' . ')
                        paragraph = paragraph.replace('</div>', ' . ')
                        paragraph = paragraph.replace('<p><p>', ' . ')
                        paragraph = paragraph.replace('... .', '...')
                        paragraph = paragraph.replace('...  .', '...')
                        paragraph = paragraph.replace('<p>', ' . ')
                        paragraph = paragraph.replace('</p>', ' . ')
                        sentences = nltk.sent_tokenize(paragraph)

                        for sentence in sentences:
                            if (sentence == '*** .'):
                                break
                            if (sentence != '.' 
                                and not sentence.startswith('.') 
                                and not sentence.startswith('…') 
                                and not sentence.startswith('*') 
                                and not sentence.startswith(' ')
                                and not sentence.startswith('!')
                                and not sentence.startswith('?')):
                                results.append(sentence)

                        next_button = tam_soup.find('a', id="next_chap")
                        dem += 1
                    else:
                        time.sleep(60)
                else:
                    break
            break

    with open(output_file, 'w', encoding='utf-8') as file:
        for i in range (0, len(results)):
            if (i == 0):
                file.write(f'{results[i]}')
            else:
                file.write(f'\n{results[i]}')

if __name__ == "__main__":
    parser= argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="url", type=str, required=True)
    parser.add_argument("-o","--output_file", help="output file dir", type=str, required= True)
    args = parser.parse_args()
    process(args.url, args.output_file)
    
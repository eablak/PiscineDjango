import sys
import requests
from bs4 import BeautifulSoup


class Philosophy:

    def __init__(self, parameter):
        self.count = 0
        self.parameter = parameter
        self.visited_articles = []
        self.to_reach_philosophy(self.parameter)


    def get_data(self, parameter):

        URL = "https://en.wikipedia.org/wiki/" + parameter
        try:
            res = requests.get(url=URL)
            return res.text
        except:
            print("It leads to a dead end !")
            exit(1)
        

    def get_url(self, html_data):

        
        soup = BeautifulSoup(html_data, "html.parser")
        
        title = soup.find(id='firstHeading').text
        if title in self.visited_articles:
            print("It leads to an infinite loop !")
            exit(1)
        if title == "Philosophy":
            print(f"{len(self.visited_articles)} roads from {self.parameter} to philosophy !")
            exit(1)
        self.visited_articles.append(title)
        
        content = soup.find(id='mw-content-text')
        allLinks = content.select('p > a')
        
        for link in allLinks:
            if link.get('href') is not None \
                and link['href'].startswith('/wiki/')\
                and not link['href'].startswith('/wiki/Wikipedia:') \
                and not link['href'].startswith('/wiki/Help:'):
                    print(link["href"].split("/")[2])
                    return(link["href"].split("/")[2])
            
        print("It leads to a dead end !")
        exit(1)
            


    def to_reach_philosophy(self, parameter):
        self.html_data = self.get_data(parameter)
        self.link = self.get_url(self.html_data)
        self.to_reach_philosophy(self.link)


def main():

    if len(sys.argv) == 2:
        parameter = "_".join(sys.argv[1].split())
        Philosophy(parameter)
    else:
        print("Wrong argument count")


if __name__ == "__main__":
    main()
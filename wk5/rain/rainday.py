from bs4 import BeautifulSoup
import requests
import os
from rain import

BASE_URL = 'https://or.water.usgs.gov/precip/'


class RainStation:
    def __init__(self, url: str):
        self.url = url
        self.raw_text = self.scrape_station()
        name, address = self.parse_header()
        self.name = name
        self.address = address

        self.rain_data = list()

    def scrape_station(self):
        response = requests.get(self.url)
        raw_text = response.text
        return raw_text

        #  soup = BeautifulSoup(response.text, 'html.parser')  # html.parser tells what language we're speaking
        #  above soup not needed because we're importing csv, tsv

    def max_day(self):
        pass

    def max_year(self):
        pass

    def summary(self):
        pass

    def parse_header(self):
        # failed_station = list()
        # try:
        name, address = self.raw_text.splitlines()[0].split(' - ')
        # except ValueError:
        #     failed = self.url
        #     failed_stations.append(failed)

        return name, address

    def __repr__(self):
        message = 'RainStation(name={}, address={}, url={})'.format(self.name, self.address, self.url)
        return message

    def __str__(self):
        message = 'This is the station name(name={}, address={})'.format(self.name, self.address, self.url)
        return message

def stat_finder():   # Steve's function.


def max_day():
    text = self.raw_text
    self.

def compile_links():
    response = requests.get(BASE_URL)
    raw = response.text
    soup = BeautifulSoup(raw, 'html.parser')


    rengas = [link['href'] for link in soup.find_all('a') if '.rain' in linke['href']]


def run_links():
    links = compile_links()
    # rainstations = [Rainstation(url=link) for link in links]

    rain_stations = list()    # you can enter this list into the console.
    failed_links = list()
    counter = 0

    for link in links:              # Build a list of rainstation objects
        try:
            rs = RainStation(url=link)
        except ValueError:
            failed_links.append(link)
            rain_stations.append(rs)
            print(f'Failed station # {counter}')
        else:
            rain_stations.append(rs)
        finally:
            print(f'Built station # {counter}')

            counter += 1

            # failed = link
            # rain_stations.append(failed)

if __name__ == '__main__':
    run_links()





#
#
# class RainDay:
#     def __init__(self, date:str, total:str, hours: list):
#         self.date = date
#         self.total = total
#         self.hours = [int(h) for h in hours]
#
#     def __repr__ (self):
#         message = '{} Total: {}'.format(self.date, self.total)
#         return message
#
#     def max_hour(self):
#         hour, value = max(enumerate(rain), key=lambda t: t[1])
#         return hour
#
#
#
#

#!/usr/bin/env python
import requests
import argparse

from random import SystemRandom
from bs4 import BeautifulSoup


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Pick a random winner from a Meetup URL.')
    parser.add_argument('url', type=str, nargs=1,
        help='URL for the meetup.')

    args = parser.parse_args()

    random = SystemRandom()

    meetup_url = args.url[0]

    r = requests.get(meetup_url)
    soup = BeautifulSoup(r.text, 'html.parser')

    member_names = []
    for member in soup.find(id='rsvp-list').find_all(attrs={'class': 'member-name'}):
        member_names.append(member.text.strip())

    print("And the winner is...")
    print(member_names[random.randint(0, len(member_names))])

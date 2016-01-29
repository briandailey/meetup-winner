from random import SystemRandom
import requests
from bs4 import BeautifulSoup
random = SystemRandom()

meetup_url = 'http://www.meetup.com/PyNash/events/227729477/'
r = requests.get(meetup_url)
soup = BeautifulSoup(r.text, 'html.parser')

member_names = []
for member in soup.find(id='rsvp-list').find_all(attrs={'class': 'member-name'}):
    member_names.append(member.text.strip())

print("And the winner is...")
print(member_names[random.randint(0, len(member_names))])

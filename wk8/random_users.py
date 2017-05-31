""" 
# Fun with Networks

""""""
## Objective

Write a simple program that accesses a public JSON API and prints the results formatted in a readable way.

1. Create a new file called `random_users.py`
1. Fetch JSON representing 5 randomly generated people from the following URL:
   [http://api.randomuser.me/?results=5](http://api.randomuser.me/?results=5)
1. Print the results something like the following:

```
Name: Mr Aventino Lima
Email: aventino.lima@example.com
Username: heavybutterfly582
Registration date: 10/2/2002
Birth date: 6/5/1994

Name: Mrs Sheryl Gardner
Email: sheryl.gardner@example.com
Username: whiteduck688
Registration date: 8/11/2014
Birth date: 6/4/1983

# Repeat for the remaining people
```

_Hint: It might help you understand the structure of the returned JSON to run it through this [pretty printer](http://jsonprettyprint.com/)._

"""
import requests
from datetime import datetime
# https://docs.python.org/3/library/datetime.html

# Look up MAYA, datetime object YouTube presentation
# You can use a date time object as a dictionary key.


response = requests.get('http://api.randomuser.me/?results=5')

users = response.json().get('results')


def random_users():

    for user in users:
        title = user.get('name').get('title')
        first_name = user.get('name').get('first')
        last_name = user.get('name').get('last')
        email = user.get('email')
        username = user.get('login').get('username')
        registered = user.get('registered')
        reg, time = user.get('registered').split(' ')
        dt2 = datetime.strptime(reg, '%Y-%m-%d')
        dt2_format =  datetime.strftime(dt2, "%x")

        dob, time = user.get('dob').split(' ')
        dt1 = datetime.strptime(dob, '%Y-%m-%d')
        dt1_format = datetime.strftime(dt1, "%x")    # OPTION: "%Y-%B-%d"

        message =   f'''  
                    Name: {title}{first_name}{last_name}
                    Email: {email}
                    Username: {username}
                    Registration date: {dt2_format}
                    Birthdate: {dt1_format} 
                    '''

        print(message)

random_users()



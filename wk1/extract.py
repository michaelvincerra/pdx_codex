"""
Write a function named extract_domain that will print the first matching domain name in a given string.

>>> extract_domain("kieran@pdxcodeguild.com")
pdxcodeguild.com

>>> extract_domain("domain of jwackman@hvc.rr.com designates 2a00:1450:400c:c09::22d as permitted sender")
hvc.rr.com
"""


def extract_domain(data):
    results = data.split('@')[1]    # pass same argument as above(data); split at '@', which produces list of two items.
    print(results)                  # extract index[1] from that list.


def extract_domain(datum):
    results = datum.split('@')[1].split(' ')[0]     # pass argument as above(datum); split at '@', which produces list of two items.
    print(results)                                  # from index[1] of the sublist, split again at ' ' and extract index[0] from that

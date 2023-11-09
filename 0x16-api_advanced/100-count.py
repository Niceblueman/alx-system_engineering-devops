#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
"""
import re
import requests
import sys


def add_title(dictionary, hot_posts):
    """_summary_

    Args:
        dictionary (_type_): _description_
        hot_posts (_type_): _description_
    """
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """_summary_

    Args:
        subreddit (_type_): _description_
        dictionary (_type_): _description_
        after (_type_, optional): _description_. Defaults to None.

    Returns:
        _type_: _description_
    """
    u_agent = 'Mozilla/5.0'
    headers = {
        'User-Agent': u_agent
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                       headers=headers,
                       params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """_summary_

    Args:
        subreddit (_type_): _description_
        word_list (_type_): _description_
    """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for item in l:
            if item[1] is not 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")

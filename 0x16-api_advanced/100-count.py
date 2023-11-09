#!/usr/bin/python3
"""
Function that queries the Reddit API and prints
"""
import concurrent.futures
import requests
import threading

word_count = {}
lock = threading.Lock()


def process_posts(subreddit, word_list, posts):
    """_summary_

    Args:
        subreddit (_type_): _description_
        word_list (_type_): _description_
        posts (_type_): _description_
    """
    global word_count
    with lock:
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if (
                    title.count(word) > 0
                    and f" {word} " in title
                    and not (title.startswith(f"{word} ") or title.endswith(f" {word}"))
                ):
                    if word in word_count:
                        word_count[word] += title.count(word)
                    else:
                        word_count[word] = title.count(word)


def count_words(subreddit, word_list, after=None):
    """_summary_

    Args:
        subreddit (_type_): _description_
        word_list (_type_): _description_
        after (_type_, optional): _description_. Defaults to None.
    """
    global word_count

    if after is None:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot/.json",
            headers={"User-agent": "count_words"},
        )
    else:
        response = requests.get(
            f"https://www.reddit.com/r/{subreddit}/hot/.json?after={after}",
            headers={"User-agent": "count_words"},
        )
    if response.status_code != 200:
        return
    data = response.json()
    posts = data["data"]["children"]
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(word_list)) as executor:
        executor.submit(process_posts, subreddit, word_list, posts)

    after = data["data"]["after"]
    if after is not None:
        count_words(subreddit, word_list, after)
    else:
        sorted_word_count = sorted(
            word_count.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_word_count:
            print(f"{word}: {count}")

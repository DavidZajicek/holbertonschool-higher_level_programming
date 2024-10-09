#!/usr/bin/python3
"""
0. Read file
mandatory
Write a function that reads a text file (UTF8) and prints it to stdout:
"""
import json
import requests
import csv


def fetch_and_print_posts():
    """
    fetch and print posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=30)
    print(f'Status Code: {r.status_code}')
    if r.status_code == 200:
        posts = r.json()
        titles = {post['title'] for post in posts}
        for title in titles:
            print(title)


def fetch_and_save_posts():
    """
    fetch and save posts
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=30)
    if r.status_code != 200:
        return None

    with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for post in r.json():
            writer.writerow({k: v for k, v in post.items() if k in fieldnames})


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()

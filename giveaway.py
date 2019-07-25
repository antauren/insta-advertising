from instabot import Bot
from dotenv import dotenv_values

from tqdm import tqdm

from functools import partial

import json
import re

import sys


def find_insta_logins(text: str) -> list:
    return re.findall("@([a-zA-Z0-9._]{0,28})", text)


def pretty_print_json(data_json):
    print(json.dumps(data_json, indent=4, sort_keys=True, ensure_ascii=False))


def is_user_exist(username, bot):
    return bool(bot.get_user_id_from_username(username))


def get_giveaway_participants(media_link, bot):
    media_id = bot.get_media_id_from_link(media_link)

    info = bot.get_media_info(media_id)
    user_id = int(info[0]['user']['pk'])

    likers = set(map(int, bot.get_media_likers(media_id)))
    followers = set(map(int, bot.get_user_followers(user_id)))
    likers_and_followers = likers & followers

    comments = bot.get_media_comments_all(media_id)

    p_is_user_exist = partial(is_user_exist, bot=bot)

    unique_users = set()
    for comment in tqdm(comments, desc='filter_participants'):

        user = comment['user']['username']
        if user in unique_users:
            continue

        if comment['user_id'] not in likers_and_followers:
            continue

        logins = find_insta_logins(comment['text'])
        if not logins:
            continue

        if not list(filter(p_is_user_exist, logins)):
            continue

        unique_users.add(user)

    return sorted(unique_users)


if __name__ == '__main__':
    dotenv_dict = dotenv_values()
    username = dotenv_dict['USERNAME']
    password = dotenv_dict['PASSWORD']

    media_link = sys.argv[1]

    bot = Bot()
    bot.login(username=username, password=password)

    users = get_giveaway_participants(media_link, bot)
    print(users)

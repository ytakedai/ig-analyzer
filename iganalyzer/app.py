import sys
[sys.path.append(i) for i in ['.', '..']]

from iganalyzer import document_generator
import json
import os

followers = []
following = []
not_following = None
not_following_back = None
script_dir = None


def run():
    global script_dir
    script_dir = os.path.dirname(__file__)

    get_followers()
    get_following()
    get_not_following()
    get_not_following_back()
    document_generator.generate(not_following, not_following_back)


def get_not_following() -> None:
    global not_following
    not_following = list(filter(lambda name: name not in following, followers))

    path = os.path.join(script_dir, 'data/not_following.json')
    with open(path, 'w') as f:
        json.dump(not_following, f)

def get_not_following_back() -> None:
    global not_following_back
    not_following_back = list(filter(lambda name: name not in followers, following))

    path = os.path.join(script_dir, 'data/not_following_back.json')
    with open(path, 'w') as f:
        json.dump(not_following_back, f)

def get_followers() -> None:
    global followers

    path_followers = os.path.join(script_dir, 'input/followers.json')
    f_followers = open(path_followers)
    data_followers = json.load(f_followers)
    follower_data = data_followers['relationships_followers']
    followers = [profile_data['string_list_data'][0]['value'] for profile_data in follower_data]

    path = os.path.join(script_dir, 'data/followers_list.json')
    with open(path, 'w') as f:
        json.dump(followers, f)
    
    f_followers.close()

def get_following() -> None:
    global following

    path_following = os.path.join(script_dir, 'input/following.json')
    f_following = open(path_following)
    data_following = json.load(f_following)
    following_data = data_following['relationships_following']
    following = [profile_data['string_list_data'][0]['value'] for profile_data in following_data]

    path = os.path.join(script_dir, 'data/following_list.json')
    with open(path, 'w') as f:
        json.dump(following, f)

    f_following.close()

if __name__ == "__main__":
    run()
import json

followers = []
following = []

def main():
    get_followers()
    get_following()
    get_not_following()
    get_not_following_back()

def get_not_following() -> None:
    not_following = list(filter(lambda name: name not in following, followers))

    with open('./output/not_following.json', 'w') as f:
        json.dump(not_following, f)

def get_not_following_back() -> None:
    not_following_back = list(filter(lambda name: name not in followers, following))

    with open('./output/not_following_back.json', 'w') as f:
        json.dump(not_following_back, f)

def get_followers() -> None:
    global followers

    f_followers = open('./input/followers.json')
    data_followers = json.load(f_followers)
    follower_data = data_followers['relationships_followers']
    followers = [profile_data['string_list_data'][0]['value'] for profile_data in follower_data]

    with open('./output/followers_list.json', 'w') as f:
        json.dump(followers, f)
    
    f_followers.close()

def get_following() -> None:
    global following

    f_following = open('./input/following.json')
    data_following = json.load(f_following)
    following_data = data_following['relationships_following']
    following = [profile_data['string_list_data'][0]['value'] for profile_data in following_data]

    with open('./output/following_list.json', 'w') as f:
        json.dump(following, f)

    f_following.close()

main()
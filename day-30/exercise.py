facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    counter = 0
    for post in posts:
            try:
                counter += 1
                total_likes = total_likes + post['Likes']
            except KeyError:
                if 'Likes' not in facebook_posts:
                    facebook_posts[counter].update({'Likes': 0})

    return total_likes

count_likes(facebook_posts)

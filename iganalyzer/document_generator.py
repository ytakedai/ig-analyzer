from snakemd import Document
from iganalyzer import instagram_scraper

def generate(not_following, not_following_back) -> Document:
    
    doc = Document("Instagram Stats Analysis")

    doc.add_header("Instagram Stats Analysis", level = 1)

    ### Users you don't follow back
    doc.add_header("Users you don't follow back", level=2)
    
    total = len(not_following)
    counter = 0
    for username in not_following:
        counter += 1
        print(str(counter) + '/' + str(total) + ' ' + username)
        name = instagram_scraper.get_name(username)
        doc.add_paragraph(name + ' (@' + username + ')') \
            .insert_link('@' + username, 'https://www.instagram.com/' + username + '/')

    doc.add_header("Users that don't follow you back", level=2)
    total = len(not_following_back)
    counter = 0
    for username in not_following_back:
        counter += 1
        print(str(counter) + '/' + str(total) + ' ' + username)
        name = instagram_scraper.get_name(username)
        doc.add_paragraph(name + ' (@' + username + ')') \
            .insert_link('@' + username, 'https://www.instagram.com/' + username + '/')


    doc.check_for_errors()
    doc.output_page()
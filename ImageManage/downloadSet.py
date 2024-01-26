import os
import scrython
import requests
import time

IMAGE_PATH = './' # You can replace this with whatever path

def get_set_code():
    all_sets = scrython.sets.Sets()
    for i, set_object in enumerate(all_sets.data()):
        print(i, all_sets.data(i, "name"))

    choice = int(input("Select your set by number: "))

    code = all_sets.data(choice, "code")

    return code

def save_image(path, url, name, set):
    response = requests.get(url)
    imageFolderName = f'{path}cardImages'
    createFolder(imageFolderName)
    setfolder=f'{imageFolderName}/{set}/'
    createFolder(setfolder)

    with open('{}{}.png'.format(setfolder, name), 'wb') as f:
        f.write(response.content)

def createFolder(path):
    isExist = os.path.exists(path)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(path)
        print(f'The new directory at {path} is created!')

def get_all_pages(set_code):
    page_count = 1
    all_data = []
    while True:
        time.sleep(0.5)
        page = scrython.cards.Search(q='e:{}'.format(set_code), page=page_count)
        all_data = all_data + page.data()
        page_count += 1
        if not page.has_more():
            break

    return all_data

def get_all_cards(card_array):
    card_list = []
    for card in card_array:
        time.sleep(0.5)
        id_ = card['id']
        card = scrython.cards.Id(id=id_)
        print(card.name())
        card_list.append(card)

    return card_list

code = get_set_code()
card_list = get_all_pages(code)
card_list_objects = get_all_cards(card_list)

for card in card_list_objects:
    time.sleep(0.1)
    save_image(IMAGE_PATH, card.image_uris(0, 'normal'), card.name(), card.set_code())
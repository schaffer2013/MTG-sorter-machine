from mtgscan.text import MagicRecognition
from mtgscan.ocr.azure import Azure

azure = Azure()
rec = MagicRecognition(file_all_cards="all_cards.txt", file_keywords="Keywords.json")  # download card files from mtgjson if missing
#box_texts = azure.image_to_box_texts("https://user-images.githubusercontent.com/49362475/105632710-fa07a180-5e54-11eb-91bb-c4710ef8168f.jpeg")
img = 'Scanner/cardImages/jud/Wonder.png'
box_texts = azure.image_to_box_texts(img)
box_texts.save_image(img, 'box.png')

deck = rec.box_texts_to_deck(box_texts)
print(deck)
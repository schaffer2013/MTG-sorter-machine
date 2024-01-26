from mtgscan.text import MagicRecognition
from mtgscan.ocr.azure import Azure
from PIL import Image

class Scanner:
    FOLDER = "ImageManage\\"
    TEMP_FILE = f'{FOLDER}temp.png'

    def __init__(self):
        self.azure = Azure()
        self.rec = MagicRecognition(file_all_cards=f'{Scanner.FOLDER}all_cards.txt', file_keywords="Keywords.json")  # download card files from mtgjson if missing

    def nameFromImage(self, image:Image):    
        deck = self.deckFromFile(image)
        card = self.deckToCardName(deck)
        return (card)

    def deckFromFile(self, image:Image):
        self.saveToTemp(self.getUpperHalf(image))
        box_texts = self.azure.image_to_box_texts(Scanner.TEMP_FILE)
        # box_texts.save_image(img, 'box.png')
        deck = self.rec.box_texts_to_deck(box_texts)
        return deck
    
    def getUpperHalf(self, image:Image) -> Image:
        w, h = image.size
        area = (0, 0, w, h/2)
        cropped_img = image.crop(area)
        return cropped_img

    def deckToCardName(self, deck):
        if deck is None:
            raise Exception
        return list(deck.maindeck.cards.items())[0][0]

    def saveToTemp(self, image:Image):
        image.save(Scanner.TEMP_FILE)

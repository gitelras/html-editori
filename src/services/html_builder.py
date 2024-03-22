from repositories.html_repository import Save

class HTML_builder:
    def __init__(self):
        self.text = ""
    
    def import_text(self, text):
        self.text = text
        print(self.text)
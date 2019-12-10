from textblob import TextBlob

class TextProcessing:
    blob = None

    def init(self):
        blob = TextBlob("")

    def translate(self, text, language_to):        
        blob = TextBlob(text)
        return 101, blob.translate(to=language_to)

    def getNounsText(self, text):
        blob = TextBlob(text)
        return 101, blob.noun_phrases
class NewFile():
    def __init__(self):
        self.listNames = ""
        self.LetterContents = ""

    def retrieveLNames(self):
        with open("./Input/Names/invited_names.txt") as f:
            self.fileName = f.readlines()
            return self.fileName
    def retrieveLetterContents(self):
        with open("./Input/Letters/starting_letter.txt") as f:
            self.LetterContents = f.read()
            return self.LetterContents

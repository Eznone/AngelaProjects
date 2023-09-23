PLACEHOLDER = "[name]"

class Mail():
    def __init__(self):
        self

    def send_mail(self, lNames, lContent):
        for name in lNames:
            name = name.strip()
            letter = lContent.replace(PLACEHOLDER, name)
            with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as finishedLetter:
                finishedLetter.write(letter)
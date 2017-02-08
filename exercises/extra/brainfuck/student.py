class Brainfuck:
    def __init__(self, code, input, output):
        """
        Initialiseert een nieuwe Brainfuck machine.

        Code: string die de brainfuck code voorstelt
        Input: functie die kan opgeroepen worden (zonder argument) om de volgende stukje data te ontvangen
        Output: functie die kan opgeroepen worden (met 1 argument) om data te outputten
        """
        raise NotImplementedException()

    
    def memory(self, n):
        """
        Geeft de inhoud van geheugencel met index n.
        """
        raise NotImplementedException()

    
    def run(self):
        """
        Voert het programma uit.
        """
        raise NotImplementedException()

def plagiarism(files):
    """
    Vergelijkt alle gegeven bestanden en telt
    het aantal gemeenschappelijke regels.
    Bijvoorbeeld,
      a
      a
      b
      a
      c
    en
      x
      y
      c
      a
    hebben 2 regels gemeenschappelijk, nl. 'a' en 'c'.
    Het aantal keer dat een regel voorkomt, of de volgorde
    waarin ze voorkomen maakt niks uit.

    Het resultaat moet een lijst zijn van triplets
    (file1, file2, nlines) waarbij file1 en file2
    de vergeleken bestanden zijn en nlines
    het aantal regels dat ze gemeenschappelijk hebben.

    Elk koppel bestanden mag maar eenmaal voorkomen,
    dus ('a.txt', 'b.txt', 1) en ('b.txt', 'a.txt', 1)
    mogen niet beide voorkomen in de lijst.
    file1 moet alfabetisch 'kleiner' zijn dan file2,
    dus ('a.txt', 'b.txt', 1) maar niet ('b.txt', 'a.txt', 1).

    Deze lijst moet gesorteerd zijn op dalend
    aantal gemeenschappelijke regels.
    Bij een gelijk aantal gemeenschappelijke
    regels moet alfabetisch worden gesorteerd
    op de naam van de bestanden.
    """
    


if __name__ == '__main__':
    raise NotImplementedError()

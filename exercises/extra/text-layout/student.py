def split_lines_monospaced(string, line_width):
    """
    Splitst de string op in meerdere regels. Elke regel
    mag maximum line_width tekens bevatten.
    Splitsingen mogen enkel gebeuren waar
    spaties staan, m.a.w. niet in het midden van een woord.
    Elke regel moet zo lang mogelijk gemaakt worden:
    een regel per woord is dus bijvoorbeeld niet geldig.

    Bijvoorbeeld, stel regellengte 10 en string
        "What's orange and sounds like a parrot?"
    wordt opgesplitst als
        [ "What's orange",
          "and sounds like",
          "parrot?" ]
    
    Indien er een woord is dat langer is dan de maximale lijnlengte,
    moet deze op een aparte lijn gezet worden. Deze lijn mag
    dan uitzonderlijk langer zijn dan de maximale lijnlengte.
    """
    
    raise NotImplementedException()

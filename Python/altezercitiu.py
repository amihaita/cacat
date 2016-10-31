def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str

    Return the list of lines from file that begin with letter.     The lines should have thenewline removed.

   Precondition: len(letter) == 1
   """


    matches = []

    # CODE MISSING HERE
    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
    return matches
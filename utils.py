import string

def column_letter_to_number(column_letter):
    """Converts an Excel column letter to a column number.

    Args:
        column_letter: The column letter to convert.

    Returns:
        The column number.
    """
    column_number = 0
    for c in column_letter:
        if c in string.ascii_letters:
            column_number = column_number * 26 + (ord(c.upper()) - ord('A')) + 1
    return column_number

def column_number_to_letter(column_number):
    """Converts a column number to an Excel column letter.

    Args:
        column_number: The column number to convert.

    Returns:
        The column letter.
    """
    column_letter = ""
    while column_number > 0:
        column_number, remainder = divmod(column_number - 1, 26)
        column_letter = chr(65 + remainder) + column_letter
    return column_letter

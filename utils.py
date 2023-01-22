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

from Content import ContentEnum

def check_string(string:str):
    """
    This function takes a string as input and checks if the first character is "=" and if the entire string is a number or text.
    If the first character is "=" it returns "equal sign"
    If the entire string is a number, it returns "number".
    If the entire string is a letter, it returns "text".
    if the string is not a number or a text it returns "other"
    :param string: The input string to check
    :type string: str
    :return: "equal sign", "number", "text" or "other" depending on the input
    :rtype: str
    """
    if string[0] == "=":
        return ContentEnum.FORMULA

    try:
        val = int(string)
        return ContentEnum.NUMERICAL
    except:
        try:
            val = float(string)
            return ContentEnum.NUMERICAL
        except:
            return ContentEnum.TEXT

    # elif string.isdigit():
    #     return ContentEnum.NUMERICAL
    # else:
    #     return ContentEnum.TEXT
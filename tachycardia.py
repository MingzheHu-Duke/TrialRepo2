def data_input():
    """ Get the input which simulate the OCR String
    Parameters: None

    Outputs: The ocr_string
    """
    choice = "No"
    # Make sure the input is what you mean
    while choice == "No":
        print("Please input the string obtained from OCR:")
        ocr_string = input()
        print("The string we get is " + ocr_string + ". Is it correct?")
        print("Please enter Yes/No")
        choice = input()
    return ocr_string


def case_space_remove(a_string):
    """ Change Capital letters into lower format and remove the
        leading and trialing spaces
    Parameters:
    a_string: The string that you want to process

    Outputs:
    out: The string that has been processed
    """
    # Turn all the upper cases in string into lower cases
    a_string = a_string.lower()
    # Strip both the leading and trailing space
    out = a_string.strip(" ")
    return out

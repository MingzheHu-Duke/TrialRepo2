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

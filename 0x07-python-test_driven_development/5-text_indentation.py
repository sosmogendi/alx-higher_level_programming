def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis?")
        # Expected output:
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.
        
        Quonam modo?
        
        Utrum igitur tibi litteram videor an totas paginas commovere?
        
        Non autem hoc:
        
        igitur ne illud quidem.
        
        Fortasse id optimum, sed ubi illud:
        
        Plus semper voluptatis?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    formatted_text = ""
    for char in text:
        formatted_text += char
        if char in separators:
            formatted_text += "\n\n"

    print(formatted_text)

# Uncomment the following lines if you want to test the function with the provided example in the task.
# text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
# Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
# Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
# Plus semper voluptatis?""")


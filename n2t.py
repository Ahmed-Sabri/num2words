from num2words import num2words

def number_to_words(n, to=None, lang=None, currency=None):
    """
    Converts a number to its word representation using num2words.

    Args:
        n: An int or float (non-negative, up to 30 digits for int).
        to: Conversion type ('currency', 'ordinal', etc.), optional.
        lang: Language code ('en', 'fr', 'de', etc.), optional.
        currency: Currency code (e.g., 'USD', 'EGP'), optional.

    Returns:
        Capitalized string representation of the number in words,
        or an error message for invalid input.
    """
    if not (isinstance(n, (int, float)) and n >= 0):
        return "Invalid input: Please enter a non-negative number."

    try:
        kwargs = {}
        if to:
            kwargs['to'] = to
        if lang:
            kwargs['lang'] = lang
        if to == "currency" and currency:
            kwargs['currency'] = currency

        result = num2words(n, **kwargs)
        # For 'currency' output, use title case; otherwise, sentence case
        if to == "currency":
            return result.title()
        return result.capitalize()
    except Exception as e:
        return f"Error converting number: {e}"

def get_input(prompt, allow_blank=True):
    """Helper to get input, optionally allowing blank."""
    value = input(prompt).strip()
    return value if value or not allow_blank else None

if __name__ == "__main__":
    while True:
        num_str = input("Enter a non-negative number (integer or float, up to 30 digits): ").strip()
        try:
            num = float(num_str) if '.' in num_str else int(num_str)
            if num < 0:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a non-negative number.")
            continue

        to_param = get_input("Enter conversion type ('currency', 'ordinal', or leave blank): ")
        currency_param = None
        if to_param and to_param.lower() == "currency":
            currency_param = get_input("Enter currency code (e.g., 'USD', 'EGP'): ")
        lang_param = get_input("Enter language code (e.g., 'de', 'fr', leave blank for English): ")

        words = number_to_words(num, to=to_param or None, lang=lang_param or None, currency=currency_param)
        print(f"The number {num} in words is: {words}")
        break


# https://github.com/savoirfairelinux/num2words
# Currency example
#print(num2words(123.45, to='currency', currency='USD'))

# Ordinal example
#print(num2words(42, to='ordinal'))

# German example
#print(num2words(42, lang='de'))

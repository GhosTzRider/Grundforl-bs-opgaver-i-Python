def check_password(password):

    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()â_=+[{]}\|;:',<.>/?"

    if len(password) < min_length:
        return "Fejl: Passwordet skal vÃ¦re mindst 8 tegn langt."

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True

    if not has_uppercase:
        return "Fejl: Passwordet skal indeholde mindst Ã©t stort bogstav."
    if not has_lowercase:
        return "Fejl: Passwordet skal indeholde mindst Ã©t lille bogstav."
    if not has_digit:
        return "Fejl: Passwordet skal indeholde mindst Ã©t tal."
    if not has_special_char:
        return "Fejl: Passwordet skal indeholde mindst Ã©t specialtegn."

    return "Password er stÃ¦rk!"

password_input = input("Indtast dit password: ")
print(check_password(password_input))

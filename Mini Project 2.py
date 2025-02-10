def validate_email(email):
    # Tjek lÃ¦ngden af e-mailen
    if len(email) > 7 and len(email) < 30:
        if email.count('@') == 1:
            if email.endswith('.dk'):
                print("Valid email")
            else:
                print("Fejl: E-mail skal ende pÃ¥ '.dk'")
        else:
            print("Fejl: E-mail skal indeholde prÃ¦cis Ã©n '@'")
    else:
        print("Fejl: E-mailen skal vÃ¦re mellem 7 og 30 tegn")

email = input("Indtast en e-mail: ")
validate_email(email)





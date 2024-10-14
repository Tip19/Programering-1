#if either style is ove 8 then result is 2 but if either style is 2 or less than the result is 0
#if neither is 8 or 2 then result is 1

style_self = int(input ("how stylish are you on a scale of 1 - 10"))
style_partner = int(input("how stylish is your partner on a scal of 1 - 10"))

def bad_style(style_self, style_partner):
    if style_partner < 3 or style_self < 3:
        return 0
    elif style_partner >= 8 or style_self >= 8:
        return 2
    else:
        return 1    

result = bad_style(style_self, style_partner)
print(result)

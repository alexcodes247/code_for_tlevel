import os

while True:
    print("English to 'Chinese-style' translator") 
    sentence = input("Please enter a sentence: ")
    result = ""

    i = 0
    while i < len(sentence):
        letter = sentence[i]

        # Handle 'th' combination
        if i + 1 < len(sentence) and sentence[i:i+2].lower() == "th":
            if sentence[i:i+2] == "th":     
                result += "s"
            elif sentence[i:i+2] == "TH":
                result += "S"
            elif sentence[i:i+2] == "Th":
                result += "S"
            elif sentence[i:i+2] == "tH":
                result += "S"
            i += 2
            continue

        # Single letter replacements
        if letter == "l":
            letter = "r"
        elif letter == "L":
            letter = "R"
        elif letter == "v":
            letter = "w"
        elif letter == "V":
            letter = "W"

        result += letter
        i += 1

    print(result)

    # Speak using Yuna voice at a slower rate
    os.system(f'say -v Moira -r 120 "{result}"')

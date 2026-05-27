#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Roman Numerals
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔢

# Documentation:
# @raycast.author Kailash Yellareddy
# @raycast.authorURL https://github.com/kyellareddy

# @raycast.argument1 { "type": "text", "placeholder": "Roman Numeral", "optional": false }

import sys
import subprocess

roman_numeral = sys.argv[1] if len(sys.argv) > 1 else ""
r = roman_numeral.upper()

def speak(text):
    subprocess.run(["say", text])

def speak_roman(roman):
    return " ".join(roman)

def value(ch: str):
    if ch.upper() == 'I':
        return 1
    if ch.upper() == 'V':
        return 5
    if ch.upper() == 'X':
        return 10
    if ch.upper() == 'L':
        return 50
    if ch.upper() == 'C':
        return 100
    if ch.upper() == 'D':
        return 500
    if ch.upper() == 'M':
        return 1000
    return 0

def romanToDecimal(s):
    res = 0
    i = 0

    while i < len(s):
        s1 = value(s[i])
        if s1 == 0:
            return "That is not a valid Roman numeral."

        if i + 1 < len(s):
            s2 = value(s[i + 1])
            if s1 >= s2:
                res += s1
                i += 1
            else:
                res += s2 - s1
                i += 2
        else:
            res += s1
            i += 1

    return res

def decimalToRoman(n: int):
    if n <= 0:
        return None, "That is not a valid English numeral."

    vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M",  "CM","D", "CD","C","XC","L","XL","X","IX","V","IV","I"]

    out = []
    i = 0
    temp = n

    while temp > 0:
        while temp >= vals[i]:
            out.append(syms[i])
            temp -= vals[i]
        i += 1

    roman = "".join(out)

    if n > 3999:
        explanation = (
            "That number is too large for standard Roman numerals, "
            "which max out at 3999, but here is how you could say it."
        )
        return roman, explanation

    return roman, None

if len(sys.argv) < 2:
    message = "Usage: python script.py ROMAN_NUMERAL_OR_NUMBER"
    print(message)
    speak(message)
else:
    user_input = sys.argv[1].strip()

    # English numeral → Roman
    if user_input.isdigit():
        num = int(user_input)
        roman_result, explanation = decimalToRoman(num)

        if roman_result is None:
            print(explanation)
            speak(explanation)
        else:
            if explanation:
                print(explanation)
                speak(explanation)

            message = f"{num} is equal to {roman_result}"
            spoken_message = f"{num} is equal to {speak_roman(roman_result)}"
            print(message)
            speak(spoken_message)

    # Roman → English
    else:
        roman = user_input.upper()
        result = romanToDecimal(roman)

        if isinstance(result, str):
            print(result)
            speak(result)
        else:
            message = f"{roman} is equal to {result}"
            spoken_message = f"{speak_roman(roman)} is equal to {result}"
            print(message)
            speak(spoken_message)
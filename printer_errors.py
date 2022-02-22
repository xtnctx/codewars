"""

The colors used by the printer are recorded in a control string.
For example a "good" control string would be aaabbbbhaijjjm meaning that
the printer used three times color a, four times color b, one time color h
then one time color a...

Sometimes there are problems: lack of colors, technical malfunction
and a "bad" control string is produced e.g.
aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

"""

def printer_error(s):
    denominator = len(s)
    numerator = 0
    for i in s:
        if i not in "abcdefghijklm":
            numerator += 1
            print(i)
    return f"{numerator}/{denominator}"


st="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
print(printer_error(st))
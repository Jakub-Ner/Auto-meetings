MONTHS = {"stycz": 1,
          "lut": 2,
          "mar": 3,
          "kwie": 4,
          "maj": 5,
          "czerw": 6,
          "lip": 7,
          "sierp": 8,
          "wrze": 9,
          "dziernik": 10,
          "listopad": 11,
          "grud": 12}

KEYS = list(MONTHS.keys())


def convert_months_to_numbers(month):
    i = 0
    while (i < len(KEYS)):
        if (KEYS[i] in month):
            return MONTHS[KEYS[i]]
        i += 1


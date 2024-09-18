import random

onset = [
  'm', 'n', 'ŋ', 
  'pʰ', 'p', 'b', 
  'tʰ', 't', 'd', 
  'kʰ', 'k', 'g', '',
  't͡sʰ', 't͡s', 'd͡z', 
  't͡ʃʰ', 't͡ʃ', 'd͡ʒ',
  'f', 'v',
  's', 'z',
  'ʃ', 'ʒ', 
  'ç', 'h',
  'l', 'j', 'w',
  'r'
]

coda = [
  'm', 'n', 'ŋ', 
  'p', 'b', 
  't', 'd', 
  'k', 'g', '',
  't͡s', 'd͡z', 
  't͡ʃ', 'd͡ʒ',
  'f', 'v',
  's', 'z',
  'ʃ', 'ʒ', 
  'l', 'j', 'w',
  'r'
]

vowels = [
  'a', 'e', 'i', 
  'o', 'u', 'ə', 
]

def random_word(syllables:int = random.randint(1, 3)):
  word = ''
  for i in range(syllables):
    word += random.choice(onset)
    word += random.choice(vowels)
    word += random.choice(coda)
    if i < syllables - 1:
      word += '.'
  return word

import csv

verbs = []
with open("Downloads/verbs.csv") as csvfile:
  reader = csv.reader(csvfile)
  for row in reader: 
    verbs.append(row[0])
        
translated_verbs = []
translations = []
seen = set()
dupes = []
def assign_verbs():
    used_translations = set()
    for verb in verbs:
        # Ensure indices are in bounds
        onsetchar = onset[(ord(verb[0]) - 96) % len(onset)]
        vowel_index = 2 if len(verb) > 2 else 1  # Check if verb is long enough
        vowelchar = vowels[(ord(verb[vowel_index]) - 96) % len(vowels)]
        codachar = coda[(ord(verb[1]) - 96) % len(coda)]
        onsetchar2 = onset[(ord(verb[-1]) - 96) % len(onset)]

        translation = onsetchar + vowelchar + codachar + onsetchar2

        # Check for conflicts and resolve with additional characters if needed
        if translation in used_translations:
            for i in range(10):
                vowelchar2 = vowels[(ord(verb[vowel_index]) - 96 + i) % len(vowels)]
                codachar2 = coda[(ord(verb[1]) - 96 + i) % len(coda)]
                onsetchar3 = onset[(ord(verb[-1]) - 96 + i) % len(onset)]
                translation = onsetchar + vowelchar + codachar + onsetchar2 + vowelchar2 + codachar2 + onsetchar3
                if translation not in used_translations:
                    break  # Exit once a unique translation is found

        translated_verbs.append(verb + ", " + translation)
        translations.append(translation)
        used_translations.add(translation)

    for x in translations:
        if x in seen:
            dupes.append(x)
        else:
            seen.add(x)

assign_verbs()
print("\n".join(translated_verbs))
# print(dupes)

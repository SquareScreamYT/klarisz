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

for _ in range(10):
  print(random_word())

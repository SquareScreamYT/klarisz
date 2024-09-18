consonants = [
    'm', 'n', 'ŋ', 
    'pʰ', 'p', 'b', 
    'tʰ', 't', 'd', 
    'kʰ', 'k', 'g', 'ʔ',
    'tsʰ', 'ts', 'dz', 
    'tʃʰ', 'tʃ', 'dʒ',
    'f', 'v',
    's', 'z',
    'ʃ', 'ʒ', 
    'ç', 'h',
    'l', 'j', 'w',
    'r'
]

onset = [
    'm', 'n', 'ŋ', 
    'pʰ', 'p', 'b', 
    'tʰ', 't', 'd', 
    'kʰ', 'k', 'g', '.', # if after consonant replace with nothing else glottal stop
    'tsʰ', 'ts', 'dz', 
    'tʃʰ', 'tʃ', 'dʒ',
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
    'ts', 'dz', 
    'tʃ', 'dʒ',
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

diphthongs = [
    "aə", "ai", "au",
    "eə", "ei", "eu",
    "əu",
    "ia", "ie", "iə", "", "io", "iu",
    "oə", "oi", "ou",
    "ua", "ue", "uə", "ui", "uo"
]

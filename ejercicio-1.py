from typing import List

def find_words(words: List[str]) -> List[str]:
    
    row1 = set('qwertyuiop')
    row2 = set('asdfghjkl')
    row3 = set('zxcvbnm')
    
    result = []

    for word in words:
        lower_word = set(word.lower())
        if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
            result.append(word)
    
    return result

def main():
    assert find_words(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    print('1-pass')
    assert find_words(["omk"]) == []
    print('2-pass')
    assert find_words(["adsdf", "sfd"]) == ["adsdf", "sfd"]
    print('3-pass')
    print('ok')

main()

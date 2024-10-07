from typing import List

def find_peaks(mountain: List[int]) -> List[int]:

    peaks = []

    for i in range(1, len(mountain) - 1):
  
        if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
            peaks.append(i)
    
    return peaks

def main():
    assert find_peaks([2, 4, 4]) == []
    print('1-pass')
    
    assert find_peaks([1, 4, 3, 8, 5]) == [1, 3]
    print('2-pass')
    
    print('ok')

main()

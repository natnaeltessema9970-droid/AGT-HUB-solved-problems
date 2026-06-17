from collections import Counter

class Solution(object):
    def countCharacters(self, words, chars):
        master_counts = Counter(chars)
        total_length = 0
        
        for word in words:
            word_counts = Counter(word)
            can_form = True
            
            for char, count in word_counts.items():
                if master_counts[char] < count:
                    can_form = False
                    break
            
            if can_form:
                total_length += len(word)
                
        return total_length

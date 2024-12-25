class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # TC--> O(N), SC -->O(1)
        n = len(sentence)
        if sentence[0] != sentence[n-1]: # first and last char comparison
            return False
        for i in range(1,n-1): # Start for the index 1 till n-2 
            if sentence[i] == ' ': # checking with the spaces
                if sentence[i-1] != sentence[i+1]: 
                    return False
        return True
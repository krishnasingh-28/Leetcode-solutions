class Solution:
    # TC -->O(M+N), SC --> O(N+M)
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        count_2 = defaultdict(int)# represents the maximum character requirements for any word in words2
        for w in words2:
            count_w = Counter(w)#to count the frequency of characters in the current word.
            for c, cnt in count_w.items():
                count_2[c] = max(count_2[c], cnt)# to ensure it contains the maximum frequency of each character across all words in words2
        res = []
        for w in words1:
            count_w = Counter(w)#to count the frequency of characters in the current word
            flag = True
            for c, cnt in count_2.items():
                if count_w[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res

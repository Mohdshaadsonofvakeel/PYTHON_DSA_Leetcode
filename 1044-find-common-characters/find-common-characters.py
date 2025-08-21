class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        intersect = set(A[0])
        
        for word in A[1:]:
            intersect = intersect.intersection(set(word))
        
        counter = {}
        for key in intersect:
            counter[key] = sys.maxsize
        
        for key in intersect:
            for word in A:
                counter[key] = min(counter[key], word.count(key))
        
        results = []
        for key, value in counter.items():
            for i in range(value):
                results.append(key)
            
        return results
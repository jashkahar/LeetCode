class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def hasNum(input):
            return any(char.isdigit() for char in input)
        
        letterLog, digitLog = [], []

        for i, log in enumerate(logs):
            vals = log.split(" ")
            if hasNum(vals[1:]):
                digitLog.append(log)
            else:
                letterLog.append([' '.join(vals[1:]), vals[0], i])
        res = []

        for log in sorted(letterLog):
            res.append(logs[log[2]])

        return res + digitLog
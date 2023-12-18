import re
words = []
totNum = 0
allNums = []
number_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

with open("day 1.txt") as file:
    for word in  file.read().split('\n'):
        matches = []
        reMatches = re.findall(r"(\d)", word)
        for i, match in enumerate(reMatches):
            try:
                realNum = match
                match = number_mapping[match]
                reMatches[i + 1] = realNum[-1] + reMatches[i + 1]
            except:
                try:
                    match = re.findall(r"(\d|one|two|three|four|five|six|seven|eight|nine)", match)[0]
                    match = number_mapping[match]
                except:
                    try:
                        int(match)
                    except:
                        match = ""
            matches.append(match)
        nums = "".join(matches)
        if(len(nums) == 1): 
            nums = nums + nums
        if(len(nums)): 
            totNum += int("".join([nums[0], nums[-1]]))

print(totNum)

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"(\w+ \w+) bags contain |(\d+ \w+ \w+).*"

test_str = ("dull magenta bags contain 3 drab black bags, 5 dim purple bags, 3 mirrored bronze bags.\n"
	"dull white bags contain 1 clear teal bag, 2 faded violet bags, 4 dull bronze bags, 2 dotted gold bags.\n"
	"clear green bags contain 3 pale crimson bags.\n"
	"dark bronze bags contain 4 shiny cyan bags, 5 shiny white bags.\n"
	"vibrant red bags contain 2 dark tomato bags, 3 muted crimson bags.\n"
	"striped brown bags contain 4 pale yellow bags.\n"
	"light bronze bags contain 5 drab silver bags, 5 wavy purple bags.\n"
	"vibrant tomato bags contain 4 mirrored orange bags, 3 faded teal bags.\n"
	"bright coral bags contain 4 clear maroon bags, 3 dim chartreuse bags.\n"
	"shiny green bags contain 2 muted crimson bags, 5 pale tan bags, 3 drab black bags, 3 striped teal bags.\n"
	"mirrored green bags contain 2 light black bags, 5 posh purple bags, 1 posh tan bag, 1 mirrored orange bag.\n"
	"dull tan bags contain 3 bright tomato bags.\n"
	"muted indigo bags contain 3 wavy coral bags.\n"
	"shiny blue bags contain 1 wavy black bag, 2 dull maroon bags.\n"
	"posh beige bags contain 5 dim crimson bags, 1 posh white bag, 2 mirrored teal bags, 2 vibrant chartreuse bags.\n"
	"dim plum bags contain 2 vibrant chartreuse bags, 2 posh teal bags, 3 drab white bags.\n"
	"vibrant teal bags contain 2 dim tomato bags, 2 dim teal bags, 4 drab chartreuse bags.\n"
	"wavy olive bags contain 5 vibrant gold bags, 2 drab black bags, 2 shiny lime bags, 2 light coral bags.\n"
	"faded white bags contain 4 posh cyan bags, 1 bright red bag, 2 pale olive bags, 3 plaid olive bags.\n"
	"pale indigo bags contain 5 dim crimson bags, 1 dim tan bag, 5 plaid green bags.\n"
	"pale fuchsia bags contain 4 light purple bags, 4 clear beige bags, 3 muted teal bags, 3 light blue bags.\n"
	"faded gray bags contain 1 clear maroon bag, 2 dim fuchsia bags, 5 bright purple bags, 4 striped turquoise bags.")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

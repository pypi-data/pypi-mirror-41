# Introduction

This is a simple regular expression program.
It implements NFA to DFA, DFA minimization and automaton visualization.

To enable plotting feature, you may need to install `graphviz`

# Usage
```
from automaton_tools import DFA as MyDFA
myinput = "abc12.+qs{2,}(yui){1,2}?"
dfa = MyDFA.fromRegex(myinput)

# check whether the string matches the pattern from the beginning or not
ismatch = dfa.match("yuiyui")

# plot the transition graph
dfa.drawGraph("dfa")
# it will generate dfa.png file
```

## Known bug

It cannot handle `.` or `\w` properly. 
Because they are considered as a special kind of characters.
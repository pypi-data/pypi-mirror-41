# rockstarfoxdot
Using using the RockStar EsoLang to make music in FoxDot

## To install (I think)
 * use python3
 * pip3 install numpy timeout_decorator watchdog rockstarfoxdot
 * pip3 install -U git+https://github.com/yanorestes/rockstar-py.git

### Instructions

Start up FoxDot as normal

Before trying to run any Rockstar run this line

```
from rockstarfoxdot import *
```


#### rockstar(lyrics, namespace=None, printname=None)
Use rockstar in-line
```
rockstar('''
Papa was a rolling stone
''', locals())
```

When run this will exec this python in your FoxDot
```
Papa = 175
```

#### rockstar(filename, namespace=None, printname=None)
Use rockstar from a file
```
rsf("FizzBuzz.rock", locals(), "fizzbuzz")
p1 >> bass(fizzbuzz, dur=PDur(17, 24))
```

When run this will exec the rockstar from "FizzBuzz.rock" in your FoxDot and place anything you 'Shout'ed 'Said' or 'Scream'ed into a list called fizzbuzz.

Then it will play those notes on the bass in FoxDot player p1

**rockstar()** has a timeout protecting you from infinite loops in the code



#### rs(lyrics, namespace=None, printname=None)
Use rockstar in-line
```
rockstar('''
Papa was a rolling stone
''', locals())
```

When run this will exec this python in your FoxDot
```
Papa = 175
```

#### rsf(filename, namespace=None, printname=None)
Use rockstar from a file
```
rsf("FizzBuzz.rock", locals(), "fizzbuzz")
p1 >> bass(fizzbuzz, dur=PDur(17, 24))
```

When run this will exec the rockstar from "FizzBuzz.rock" in your FoxDot and place anything you 'Shout'ed 'Said' or 'Scream'ed into a list called fizzbuzz.

Then it will play those notes on the bass in FoxDot player p1

**rsf()** has a timeout protecting you from infinite loops in the rockstar

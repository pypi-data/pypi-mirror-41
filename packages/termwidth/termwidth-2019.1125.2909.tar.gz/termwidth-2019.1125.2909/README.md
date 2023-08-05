# Terminal width determination library #

This library exports exactly one function:

```Python
import termwidth
w, h = termwidth.getTermWidth()

print(" " * w / 2 + "Hello" + " " * w / 2)
```

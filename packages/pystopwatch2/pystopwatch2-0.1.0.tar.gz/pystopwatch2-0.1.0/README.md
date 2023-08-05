# pystopwatch
Multi-functional Simple Stopwatch for Python.

- Multiple Stopwatch by Tags
- Manage elapsed times by tags
- Example of use : profiling python codes(latency by functions, ...)

## Install

```
$ pip install pystopwatch2
```

## Usage

```python
from pystopwatch import PyStopwatch

w = PyStopwatch()
w.start(tag='a')
time.sleep(1)
w.pause('a')
e = w.get_elapsed('a')

# e = 1.0xxx

e.clear('a')
```

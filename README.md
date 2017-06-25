# pseudo-random

A simple Markov process to generate a new random text based on likely co-occurances in the given text.

Book of Genesis and the novella ["Invisible Cities"](https://www.goodreads.com/book/show/9809.Invisible_Cities) by Italo Calvino provided for testing.

### useage

`./prand.py -i /path/to/input-file -o /path/to/output-file -w number-of-words`

ex

`./prand.py -i invisible-cities -o myOutpuy -w 25`

### to-do
- [ ] use set instead of list to speed up cache process
- [ ] import "Genesis" and "Invisible Cities" prob distributions as modules, so that they are pre-compiled as .pyc files
- [ ] add "blend" function to combine two sources (e.g. "Genesis" and "Invisible Cities") to create joint weighted prob dist.



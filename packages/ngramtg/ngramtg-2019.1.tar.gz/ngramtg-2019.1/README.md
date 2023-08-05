# Ngram TextGen
A simple n-gram-based random text generator written in Python.

## Requirements and Installation
#### Requirements
This module requires Python 3.6+ due to the use of f-strings.
#### Installation
```bash
pip install ngramtg
```

## Usage
Create a simple script, e.g.

```python
from ngramtg.ngram import NgramTextGen
import sys

if __name__ == "__main__":
    my_object = NgramTextGen(sys.argv[1], auto=True)
    print(my_object.sentence())
```
Save it (e.g. `myscript.py`) and provide a corpus file to it:

    $ python myscript.py corpus.txt
    Compassion will make you.

## Release History
* 2019.01
    * Initial release

## Development and License
Developed by Paul Wicking – [@DocWicking][tweet-link].

Distributed under the MIT license. See `LICENSE` for more information.
The source code lives on [GitHub][repo-link].

[tweet-link]: https://twitter.com/DocWicking
[repo-link]: https://github.com/docwicking/ngramtg
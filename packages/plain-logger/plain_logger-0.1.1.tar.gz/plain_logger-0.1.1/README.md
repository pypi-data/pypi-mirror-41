# plain_logger - Make logging simple and easy

An easy to use helper pip package to help you log details at any point in code.

## Assumptions

+ Assuming python is installed on your system.


## Installation

Install `plain_logger` on your system using : 

```
pip install plain_logger
```

## Usage

### LogInfo
Logs data with 'INFO' tag.

Example:
``` 
from simple_logger import LogInfo

def foo():
    fname = "John"
    lname = "Doe"
    LogInfo ("Name = {} {}".format(fname, lname))
```

Output:
```
[2019-01-25 19:30:02] INFO: Name = John Doe
```


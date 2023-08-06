# nicehr
Nice Autoscaling Horizontal Rules for Python. The horizontal line will autosize itself to the current size of the terminal. You can make it a wild rainbow if you want.

Works on Python 3.6 and 3.7.

# Setup
```bash
pip install -r requirements.txt
python setup.py install
```

# Usage
Just import nicehr and you should be good to go!

nicehr.nice_hr() is the function you are looking for.

# Example
```python
import sys

import nicehr

def main():
    print("This is an example script for nicehr. Here is a simple * line.")
    print(nicehr.nice_hr("*"))
    print("Here is a sample line with a message in the middle of the line.")
    print(nicehr.nice_hr("*", " Look at this Line "))
    print("Here is a red version of the line above.")
    print(nicehr.nice_hr("*", " Look at this Line ", color="red"))
    print("Here is a black version of the line above.")
    print(nicehr.nice_hr("*", " Look at this Line ", color="black"))
    print("Finally, here is a rainbow version!")
    print(nicehr.nice_hr("*", " Look at this Line ", colorful=True))
    print("Thank you for taking a look.")

if __name__ == '__main__':
    sys.exit(main())
```

The output should look like:

![example output](https://github.com/dagonis/nicehr/static/nicehr.png "Nice HR Output")

This code is in the bin/ folder if you want to run it yourself.
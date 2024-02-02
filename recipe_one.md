1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

ADDITIONAL QUESTIONS FOR CLIENT:
Q: do you want a number back or a formatted string? A: formatted string
Q: do you want the time in minutes only or hours, seconds, days etc. A: minutes only for now
Q: do you want to have the option to alter the reading speed A: yes, as an optional argument def. 200
Q: how accurate do you want the time? To the nearest minute? A: fractions of a minute to 1decimal place

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def estimate_read_time(text, wpm=200):
    """returns time to read text in minutes if user can read 200 wpm

    Parameters: (list all parameters and their types)
        text: a string containing words a section to text to read e.g. "the cat sat on the mat"
        wpm: optional words per minute reading speed as an int, default is 200 e.g. 180


    Returns: (state the return value and its type)
        an estime of how long to read text e.g. 200 words / 200 wpm speed == 1 minute

    Side effects: (state any side effects)
        none
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

sample_100 = "pretend this has 100 words"
sample_200 = "pretend this has 200 words"
sample_300 = "pretend this has 300 words"
sample_400 = "pretend this has 400 words"
sample_500 = "pretend this has 500 words"
sample_600 = "pretend this has 600 words"
sample_700 = "pretend this has 700 words"
sample_800 = "pretend this has 800 words"
"""
Given empty string 
It returns 0 minutes
"""
estimate_read_time("") => "At 200wpm this 0 word text would take you 0 minutes to read."

"""
Given 200 word string 
It returns 1 minutes
"""
estimate_read_time(sample_200) => "At 200wpm this 200 word text would take you 0 minutes to read."

"""
Given 100 word string
It returns 0.5 minutes
"""
estimate_read_time(sample_100) => "At 200wpm this 100 word text would take you 0.5 minutes to read."

"""
Given a 700 word string
It returns 3.5 minutes
"""
estimate_read_time(sample_700) => "At 200wpm this 700 word text would take you 3.5 minutes to read."

"""
Given a 600 word sting and 60 wpm reading speed
It returns 10 minutes
"""
estimate_read_time("") => "At 60wpm this 600 word text would take you 10 minutes to read."

"""
Given a None value
It raises an exception
"""
estimate_read_time(None) => "Text sample must be a string."

"""
Given a non-string value
It raises a value exception
"""
estimate_read_time(1) => "Text sample must be a string."

"""
Given a non-int value for optional second wpm argument
It raises a value exception
"""
estimate_read_time(sample_100, "200wpm") => "Words per Minute (wpm) must be an integer."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!

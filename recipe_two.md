1. Describe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark. (? ! or .)

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_grammar(text):
    """
    Returns True if text starts with an uppercase alpha and ends with a punctuaiton mark

    Parameters: (list all parameters and their types)
        text: a string containing a typical sentence "Hello, how are you?"

    Returns: (state the return value and its type)
        True if first character is uppercase alpha and the last character is an appropriate puncuation mark

    Side effects: (state any side effects)
        none
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given empty string
Returns False
"""
check_grammar("") => "Text argument must be a non-empty string."

"""
Given lowercase first character
Returns False
"""
check_grammar("hello, how are you?") => False

"""
Given no ending punction
Returns False
"""
check_grammar("Hello, how are you") => False

"""
Given incorrect ending punction
Returns False
"""
check_grammar("Hello, how are you,") => False

"""
Given a non-string input
Raises Exception "Text argument must be a string."
"""
check_grammar(None) => "Text argument must be a non-empty string."
check_grammar(1) => "Text argument must be a non-empty string."
check_grammar([]) => "Text argument must be a non-empty string."
check_grammar({}) => "Text argument must be a non-empty string."

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

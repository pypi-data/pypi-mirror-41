# is-idiot

> Returns true if someone is an idiot.

Please consider following this project's author, [Ryan Broman](https://github.com/ryanbroman), and consider starring the project to show your :heart: and support.

## Install

Install with [pip](https://pip.pypa.io/en/stable/):

```sh
$ pip install is-idiot
```

## Why is this needed?

In Python, it's insanely hard to check that someone is an idiot. This library makes your life much easier because it's extremely lightweight and doesn't affect your application's performance so much!

## Usage

```py
from isidiot import is_idiot
```

### true

```py
is_idiot("me");                    # true
is_idiot("you");                   # true
is_idiot("node.js developers");    # true
is_idiot('Every JS "programmer"'); # true
```

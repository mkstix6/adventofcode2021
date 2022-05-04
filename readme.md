# [Advent of Code 2021](https://adventofcode.com/2021) – Mark Stickling

[stickling.co.uk](https://stickling.co.uk/posts/advent-of-code-2021)

This year's Advent of Code story was about exploring a deep ocean trench in a mini-submarine and solving problems with the instruments and navigation as you diver deeper and deeper.

This year I decided to break from my JavaScript day-to-day and attempt every puzzle using **Python**:

 - I practiced a lot of data manipulation in Python.
 - Learned how to use *List Comprehensions* where I would usually reach for JavaScript `Array.prototype.map()`
 - Understood that I had to import `reduce` rather than relying on it just being there as in JavaScript.
 - Noted the differences between `copy` and `deepcopy`.
 - Used a *Lambda function* or two which <em>feel</em> a lot like JavaScript Arrow Functions.
 - Figured out basic *unit-testing*. As Python's `unittest` is readily importable this was much nicer than the JavaScript experience of having to decide which of many test runners to choose.
 - Used *type hinting* to tighten the feedack loop of errors and warnings.
 - Setting up VSCode for Python work and utilising the built in debugger.

I managed a score of *21\**. A little better than last year. Looking forward to completing every star one year 💪.

## Unit testing

Python version `3.10.0`

### Scripts

- Run all tests
  - `python3 -m unittest`
- Run a single test file:
  - `python3 -m unittest test_dayXX`

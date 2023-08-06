# Brief

convenient to join file path in a chain manner:

```python
s = Path('.')
s = s.join('a', 'b').join('..')
# s == 'a'
```

it uses `os.path.join` and always normalizes the path with `os.path.normpath`  
while `os.path.join` join the `'a', '..'` to `'a/..'`


# Change Log

## v0.1.3, 2019-2-9
* change to run with python3

## v0.1.2, 2018-6-7

* *improve comment and change to English*  
* *change directory structure and update setup.py*  
* *add tests.py*  

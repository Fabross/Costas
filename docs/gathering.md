#Data Gathering Module

Here are found the functions that help to gather the data from the source.

## cut(data)

Cut the data by a pattern defined and return a tuple.
```python
Keyword arguments:
    data -- the data to cut, list
```
    
## parser(data)

Transform data from source txt to an structure and return a pd.DataFrame.
```python
Keyword arguments:
    data -- the data to transform, list
```

## grades():
Ask for grades to keyboard input and return a list with the keyboard input.
```python
Keyword input form:
    A,...,D -- the grades that are required to analyze.
```

## mags():
Ask for magnitudes to keyboard input and return a tuple.
```python
Keyword input form:
    A,...,D -- the grades that are required to analyze.
```
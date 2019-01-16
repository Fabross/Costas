#Preprocessing Module

The sets of functions here help from the perspective of preprocessing, complementing the module of data gathering and features extraction.

## outliers_iqr(ys)

Delete atypical data.
```python
Keyword argument:
    ys -- the data, np.narray
```

## high_photometric_errors(data)

Delete high photometric errors and return a np.narray.
```python
Keyword argument:
    data -- the data to analyze, np.narray
```

## preprocessing(data, aperture)

Preprocess data for an aperture and return a tuple.
```python
Keyword arguments:
    data -- the data to analyze, pd.DataFrame
    aperture -- the aperture index, str
```

## grade_filter(df, grades, mags)

Filter the data to preprocess and return a tuple.
```python
Keyword arguments:
    df -- the data to analyze, pd.DataFrame
    grades -- the grades to analyze, list
    mags -- the magnitudes to analyze, tuple
```

## Sort(tup)

Sort a tuple in descending order and return a tuple.
```python
Keyword arguments:
    tup -- tuple to sort, tuple
```
        
## graph(data, path, title)

Graph in a scatter type and save to a folder as title.png.
```python
Keyword arguments:
    data -- the data to graph, tuple
    path -- the path to save, str
    title -- the graph title, str
```
#Data Acquisition Module

Here are found the functions that help to gather the data from the source.

------------------------------------------

## parser(data)

It filters the input list of strings with a pattern adjusted to the ASAS format
```txt
'#     HJD      MAG_1  MAG_0  MAG_2  MAG_3  MAG_4    MER_1 MER_0 MER_2 MER_3 MER_4 GRADE FRAME'
```
saving all the values found to a structure, with the right ascension and declination, that is converted to a pd.DataFrame and returned.

#### Args:
`data(list)`: The list of strings of the text in a ASAS register.

#### Returns:
`pd.DataFrame`: The light curve's data information: DEC, FRAME,GRADE, HJD, MAG_0, MAG_1, MAG_2, MAG_3, MAG_4, MER_0, MER_1, MER_2, MER_3, MER_4 and RA.

#### Example:
The input data:
```python
[ '#nskip_4= 0\n',
 '#ra=   17.000018  17:00:00.1\n',
 '#dec= -24.121600 -24:07:17.8\n',
 '#     HJD      MAG_1  MAG_0  MAG_2  MAG_3  MAG_4    MER_1 MER_0 MER_2 MER_3 MER_4 GRADE FRAME\n',
 '   2140.48752 12.253 12.299 12.194 12.162 12.187    0.020 0.038 0.017 0.018 0.021  A 30120\n',
 '   2384.87500 11.893 11.977 11.846 11.806 11.814    0.018 0.034 0.019 0.021 0.024  A 773\n',
 '   2385.89474 11.916 12.083 11.843 11.807 11.784    0.034 0.057 0.032 0.034 0.040  D 984\n']
```
The return:

|   |           DEC          |  FRAME  | GRADE |     HJD    | ... | MER_3 | MER_4 |          RA          |
|---|:----------------------:|:-------:|:-----:|:----------:|:---:|:-----:|:-----:|:--------------------:|
| 0 | -24.121600 -24:07:17.8 | 30120.0 | A     | 2140.48752 | ... | 0.018 | 0.021 | 17.000018 17:00:00.1 |
| 1 | -24.121600 -24:07:17.8 | 773.0   | A     | 2384.87500 | ... | 0.021 | 0.024 | 17.000018 17:00:00.1 |
| 2 | -24.121600 -24:07:17.8 | 984.0   | D     | 2385.89474 | ... | 0.034 | 0.040 | 17.000018 17:00:00.1 |

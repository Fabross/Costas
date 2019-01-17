#Features Extraction Module

Here are found the functions that help to extract the data's features.

------------------------------------------

## get_statistics(t,y)
Perform linear and parabolic fit obtaining \( m_{linear} \) and \( m_{parabolic} \), respectively, with
$$ m_{linear} = (a_0 \pm e_{a_0})+(a_1 \pm e_{a_1})t$$
$$ m_{parabolic} = (b_0 \pm e_{b_0})+(b_1 \pm e_{b_1})t + (b_2 \pm e_{b_2})t^2 $$
Where \( m_{fit type} \) represents the magnitude, meanwhile \( a_0 \), \( a_1 \), \( b_0 \), \( b_1 \) and \( b_2 \) are the coefficients of each adjust; \( e_{a_0} \), \( e_{a_1} \), \( e_{b_0} \), \( e_{b_1} \) and \( e_{b_2} \) are the coefficient's errors.

We obtain \( Q_1' \) and \( Q_2' \) for each adjust
$$ Q_1' = \frac{a_1}{e_{a_1}} $$



#### Args:
`t(np.narray)`: The data to fit.
`a`: The first number parameter.
`b`: The second number parameter.

#### Returns:
`np.array`: The parameter m.

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

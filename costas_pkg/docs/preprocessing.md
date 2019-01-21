#Preprocessing Module

The sets of functions here help from the perspective of preprocessing, complementing the module of data gathering and features extraction.

## high_photometric_errors(data)

Found high photometric errors in MER,  with \( \bar{x} \) and \( \sigma \) as mean and standard deviation of MER data array, respectively, based on error limit
$$ \varepsilon_l =  \bar{x} + 3 \sigma$$
and the condition
$$ x_i \geq \varepsilon_l $$

#### Args
`data(np.narray)`: MER to analyze.

#### Returns
`np.narray`: MER's index with high photometric errors.

-------------

## outliers_iqr(ys)

Found magnitudes out of interquartile range (iqr) based on quartile 1 and quartile 3, \( q_1 \) and \(q_3 \) respectively, with 
$$ iqr = q_3-q_1 $$ 
and condition
$$ (ys > U_b)\ or \ (ys < L_b)$$
where \(U_b = q_3+ 1.5iqr\) and \(L_b = q_1- 1.5iqr\) are the Upper bound and Lower bound, respectively.

#### Args
`data(np.narray)`: MER to analyze.

#### Returns
`np.narray`: MER's index out of interquartile range.

-------------

## preprocessing(data,aperture)

Analyze light curve's data with specific aperture, executing high_photometric_errors and outliers_iqr, filtering all the don't wanted values.

#### Args
`data(pd.DataFrame)`: The data to analyze, like the returning example shown in [parser(data)](datadq.md).

`aperture(str)`: The index to analyze MAG_i, with \( i=0,1,2,3\).

#### Returns
`tuple`: HJD and MAG_i values associated.

-------------

## grade_filter(data, grades)

Found and return all the values in light curve's data that has a GRADE parameter in grades set.

#### Args
`data(pd.DataFrame)`: The data to analyze, like the returning example shown in [parser(data)](datadq.md).

`grades(list of str)`: Some combination (or all) of A,B,C,D.

#### Returns
`tuple`: Data filtered containing only values with GRADE specified in grades.

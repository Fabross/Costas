#Preprocessing Module

The sets of functions here help from the perspective of preprocessing, complementing the module of data gathering and features extraction.

## high_photometric_errors(data, aperture='0')

Found high photometric errors in MER,  with \( \bar{x} \) and \( \sigma \) as mean and standard deviation of MER data array, respectively, based on error limit
$$ \varepsilon_l =  \bar{x} + 3 \sigma$$
and the condition
$$ x_i \geq \varepsilon_l $$

#### Args
`data({astropy.table.table.Table, np.array, astropy.table.column.Column})`: MER's Data or table to analyze.

`aperture(str)`: Specific aperture in data to analyze, default='0'.

#### Returns
`astropy.table.table.Table`: Table with corresponding MER aperture analyzed.

-------------

## outliers_iqr(ys)

Found magnitudes out of interquartile range (iqr) based on quartile 1 and quartile 3, \( q_1 \) and \(q_3 \) respectively, with 
$$ iqr = q_3-q_1 $$ 
and condition
$$ (ys > U_b)\ or \ (ys < L_b)$$
where \(U_b = q_3+ 1.5iqr\) and \(L_b = q_1- 1.5iqr\) are the Upper bound and Lower bound, respectively.

#### Args
`data({astropy.table.table.Table, np.array, astropy.table.column.Column})`: MAG's Data or table to analyze.

`aperture(str)`: Specific aperture in data to analyze, default = '0'.

#### Returns
`astropy.table.table.Table`: Table with corresponding MAG aperture analyzed.

-------------

## preprocessing(data, aperture)

Analyze light curve's data with specific aperture, executing high_photometric_errors and outliers_iqr, filtering all the don't wanted values.

#### Args
`data(astropy.table.table.Table)`: Data table to analyze.

`aperture(str)`: Specific aperture to analyze in data.

#### Returns
`astropy.table.table.Table`: Table with the specific aperture's data analyzed.
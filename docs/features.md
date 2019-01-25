#Features Extraction Module

Here are found the functions that help to extract the data's features.

------------------------------------------

## get_statistics(t,y)
Obtain characteristics parameters performing linear and parabolic fit, \( m_{linear} \) and \( m_{parabolic} \), respectively, with
$$ m_{linear} = (a_0 \pm e_{a_0})+(a_1 \pm e_{a_1})t$$
$$ m_{parabolic} = (b_0 \pm e_{b_0})+(b_1 \pm e_{b_1})t + (b_2 \pm e_{b_2})t^2 $$
Where \( m_{fit\ type} \) represents the magnitude, meanwhile \( a_0 \), \( a_1 \), \( b_0 \), \( b_1 \) and \( b_2 \) are the coefficients of each adjust; \( e_{a_0} \), \( e_{a_1} \), \( e_{b_0} \), \( e_{b_1} \) and \( e_{b_2} \) are the coefficient's errors.

With these we obtain \( Q_1' \) and \( Q_2' \) for each adjust
$$ Q_1' = \frac{a_1}{e_{a_1}} $$
$$ Q_2' = \frac{b_2}{e_{a_2}} $$
and indicators \( C_1 \) and \( C_2 \)
$$ C_1 = 1 - \frac{DEFL}{DEP} $$
$$ C_2 = 1 - \frac{DEFP}{DEFL} $$
where
$$ DEP = \sqrt{ \sum_i^n \frac{(y_i-\bar{y})^2}{n}} $$
$$ DEFL =  \sqrt{ \sum_i^n \frac{(y_{i}^{lfit}-\bar{y}^{lfit})^2}{n}}$$
$$ DEFP =  \sqrt{ \sum_i^n \frac{(y_{i}^{pfit}-\bar{y}^{pfit})^2}{n}} $$
are the magnitude, linear fit and parabolic fit standard deviation for each one.

#### Args
`t(np.narray)`: The HJD data to analyze.

`y(np.narray)`: The MAG data to analyze.

#### Returns
`list`: Q1', C1, Q2' and C2, respectively.

------------------------------------------

<!-- ## get_Q(data) [SOON]
Obtain parameters \( Q_1 \) and \( Q_2 \) based on 
$$ Q_1 = Q_1' - \bar{Q}_c $$
$$ Q_2 = Q_2' - \bar{Q}_c $$
with \( c \) the field where the star being analyze belongs.
#### Args
`data(astropy.table.table.Table)`: The light curve's data to analyze with columns Qp1 and Qp2.

#### Returns
`data(astropy.table.table.Table)`: The data with columns Q1 and Q2.

------------------------------------------
-->

## get_ra_dec(data)
get the right ascension and declination of the input data.

#### Args
`data(astropy.table.table.Table)`: The data to analyze.

#### Returns
`tuple`: The RA and DEC of data, respectively.
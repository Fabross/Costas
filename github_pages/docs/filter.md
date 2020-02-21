#Filter Module

There are functions to help to select the wanted data.

-------------

## grade_filter(data, grades)

Found and return all the rows in data table that has a GRADE parameter in grades list.

#### Args
`data(astropy.table.table.Table)`: The data to filter, like the returning example shown in [parser(data)](datadq.md).

`grades(list of str)`: Some combination (or all) of A,B,C,D.

#### Returns
`tuple`: Data filtered containing only values with GRADE specified in grades.

-------------

## stars_Cfilter(data, ThC1=0.02, ThC2=0.02)
Selects only the data's magnitudes that satisfy the conditions
$$ C_1 > \text{ThC1} $$
$$ C_2 > \text{ThC2} $$

#### Args
`data(astropy.table.table.Table)`: The light curve's data with the columns RA, DEC, C1 and C2, see [features extraction module](features.md) for more information about those parameters.

`ThC1`: The threshold number for \( C_1 \), value by default: 0.02.

`ThC2`: The threshold number for \( C_2 \), value by default: 0.02.

#### Returns
`astropy.table.table.Table`: The data filtered.

-------------

## stars_Qfilter(data, ThQ1=4, ThQ2=4)
Selects only the data's magnitudes that satisfy the conditions
$$ Q_1 \geq \text{ThQ1} $$
$$ Q_2 \geq \text{ThQ2} $$

#### Args
`data(astropy.table.table.Table)`: The light curve's data with the columns RA, DEC, Q1 and Q2, see [features extraction module](features.md) for more information about those parameters.

`ThQ1`: The threshold number for \( Q_1 \), value by default: 4.

`ThQ2`: The threshold number for \( Q_2 \), value by default: 4.

#### Returns
`astropy.table.table.Table`: The data filtered.
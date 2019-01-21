#Selection Module

There are functions to help to select the wanted data.

-------------

## stars_Cfilter(data, ThC1=0.02, ThC2=0.02)
Selects only the data's magnitudes that satisfy the conditions
$$ C_1 > \text{ThC1 (default: 0.02)} $$
$$ C_2 > \text{ThC2 (default: 0.02)} $$

#### Args
`data(pd.DataFrame)`: The light curve's data with the columns RA, DEC, C1 and C2, see [features extraction module](features.md) for more information about those parameters.

`ThC1`: The threshold number for \( C_1 \).

`ThC2`: The threshold number for \( C_2 \).

#### Returns
`pd.DataFrame`: The data filtered.

-------------

## stars_Qfilter(data, ThQ1=4, ThQ2=4)
Selects only the data's magnitudes that satisfy the conditions
$$ Q_1 \geq \text{ThQ1  (default: 4)} $$
$$ Q_2 \geq \text{ThQ2  (default: 4)} $$

#### Args
`data(pd.DataFrame)`: The light curve's data with the columns RA, DEC, Q1 and Q2, see [features extraction module](features.md) for more information about those parameters.

`ThQ1`: The threshold number for \( Q_1 \).

`ThQ2`: The threshold number for \( Q_2 \).

#### Returns
`pd.DataFrame`: The data filtered.

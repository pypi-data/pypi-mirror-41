[![pipeline status](https://gitlab.com/xgrg/atn/badges/master/pipeline.svg)](https://gitlab.com/xgrg/atn/commits/master)
[![coverage report](https://gitlab.com/xgrg/atn/badges/master/coverage.svg)](https://gitlab.com/xgrg/atn/commits/master)

# atn

Based on the A/T/N/ classification scheme for Alzheimer's disease biomarkers
[Jack et al., 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4970664/),
what this Python module does is basically applying predefined thresholds to a
given [DataFrame](https://pandas.pydata.org/) (containing biomarker data such
  as cerebrospinal fluid (CSF) levels of _ABeta42_, _ptau_, _ttau_) and building
  multiple lists of subjects with distinct profiles according to
their CSF biomarkers.

Example (with random data):

```
import random
n = 10

abeta42 = [random.randrange(600e3, 1800e3)/1e3 for e in range(0, n)]
ptau = [random.randrange(4e3, 80e3)/1e3 for e in range(0, n)]
ttau = [random.randrange(97e3, 500e3)/1e3 for e in range(0, n)]
data = pd.DataFrame(data=[abeta42, ptau, ttau], index=['abeta42', 'ptau', 'ttau']).transpose()
data
```

> |   | abeta42  | ptau   | ttau    |
> |---|----------|--------|---------|
> | 0 | 1142.327 | 76.636 | 375.448 |
> | 1 | 833.484  | 77.321 | 181.75  |
> | 2 | 951.601  | 6.981  | 309.215 |
> | 3 | 1623.797 | 65.063 | 232.303 |
> | 4 | 920.706  | 62.899 | 310.1   |
> | 5 | 704.215  | 58.526 | 160.826 |
> | 6 | 1687.357 | 53.335 | 422.249 |
> | 7 | 1701.997 | 68.676 | 173.33  |
> | 8 | 1774.046 | 37.214 | 255.638 |
> | 9 | 939.946  | 21.128 | 164.803 |


```
import atn
staging = atn.stage(data, thresholds = {'abeta42':1100, 'ptau':19.2, 'ttau':242})
staging
```

> |    | A     | T     | N     |
> |----|-------|-------|-------|
> | ID |       |       |       |
> | 0  | FALSE | TRUE  | TRUE  |
> | 1  | TRUE  | TRUE  | FALSE |
> | 2  | TRUE  | FALSE | TRUE  |
> | 3  | FALSE | TRUE  | FALSE |
> | 4  | TRUE  | TRUE  | TRUE  |
> | 5  | TRUE  | TRUE  | FALSE |
> | 6  | FALSE | TRUE  | TRUE  |
> | 7  | FALSE | TRUE  | FALSE |
> | 8  | FALSE | TRUE  | TRUE  |
> | 9  | TRUE  | TRUE  | FALSE |


```
print(atn.staging_summary(staging))
```

> CSF amyloid (A) positive/negative: 5/5
> CSF ptau (T) positive/negative: 9/1
> CSF ttau (N) positive/negative: 5/5
>
> A+T+: 4
> A+T-: 1
> A-T-: 0
> A-T+ (SNAPs): 5
>
> A+T+N+: 1
> A+T+N-: 3
> A-T+N+: 3
> A-T+N-: 2
> A-T-N-: 0
> A-T-N+: 0
> Total subjects: 10

So yes, it is simple, stupid. But this allows one to quickly select groups of
subjects as follows:

```
groups = atn.groups(staging)
data.loc[groups['A+'].index]
```

> |    | abeta42 | ptau   | ttau    |
> |----|---------|--------|---------|
> | ID |         |        |         |
> | 1  | 833.484 | 77.321 | 181.75  |
> | 2  | 951.601 | 6.981  | 309.215 |
> | 4  | 920.706 | 62.899 | 310.1   |
> | 5  | 704.215 | 58.526 | 160.826 |
> | 9  | 939.946 | 21.128 | 164.803 |

# Dependencies

- Python >= 3.5
- Pandas >= 0.24.1

# Install

First make sure you have installed all the dependencies listed above. Then you can install **atn** by running the following command in a command prompt:

> pip install atn

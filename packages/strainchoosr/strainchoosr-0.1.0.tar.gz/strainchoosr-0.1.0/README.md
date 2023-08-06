[![Build status](https://travis-ci.org/lowandrew/StrainChoosr.svg?master)](https://travis-ci.org/lowandrew)
[![codecov](https://codecov.io/gh/lowandrew/StrainChoosr/branch/master/graph/badge.svg)](https://codecov.io/gh/lowandrew/StrainChoosr)


# StrainChoosr

StrainChoosr examines phylogenetic trees and will give you the X strains that represent the most diversity
within your tree.

### Installation

Install via pip/pip3:

`pip install strainchoosr`

### Usage

From the command line, the following will print to screen your representative strains:

`diversitree.py -t /path/to/newick/formatted/treefile -n number_of_representative_strains`

Within a script:

```python
from strainchoosr import strainchoosr
dt = strainchoosr.StrainChoosr(tree_file='path/to/newick/formatted/treefile')
# Create a linkage matrix using SciPy
linkage = dt.create_linkage()
# Find desired number of clusters
clusters = dt.find_clusters(linkage=linkage, desired_clusters=3)  # Or whatever other number you want
# Print cluster representatives
for cluster in clusters:
    print(dt.choose_best_representative(cluster))
```

# DADpy

The swiss army :knife: for discharge abstract database!

## About

DADpy provides a set of functions for using the DAD dataset for machine learning and visualization. The package does not include the dataset. Academic researchers can request the DAD dataset from CIHI. This is an unofficial repo and is not affiliated with CIHI. Please retain the disclaimer below in forks. [Read docs](https://dermatologist.github.io/dadpy/)

## Installation

```
git clone https://github.com/dermatologist/dadpy.git
cd dadpy
pip install -e .
```

## Usage

```
from dadpy import DadLoad
from dadpy import DadRead
from dadpy import DadEmbedding

# csv file is also supported
dl = DadLoad('/path/to/dad/sample/spss/sav/file/clin_sample_spss.sav')
dr = DadRead(dl.sample)
de = DadEmbedding(dl.sample)

# records with obesity as pandas df
print(dr.has_diagnosis('E66'))
# Partial gastrectomy for repair of gastric diverticulum
print(dr.has_treatment('1NF80'))

# comorbidities as dict for visualization
print(dr.comorbidity('E66')) # Obesity
# co-occurance of treatments as dict
print(dr.interventions('1NF80')) # Partial gastrectomy for repair of gastric diverticulum

# Get the one-hot-encoded vector for machine learning
dr.vector(dr.has_diagnosis('E66'), significant_chars=3, include_treatments=True)

# Play with embeddings
print(de.embedding().wv.most_similar_cosmul(['J90'])) #neighbours of 'pleural effusion' -> E877 Fluid overload.

```

* See notebooks folder for visualizations

## Development

* PR welcome. Please see CONTRIBUTING.md
* Add jupiter notebooks to the notebook folder. Include the disclaimer below.

### Disclaimer

Parts of this material are based on the Canadian Institute for Health Information Discharge Abstract Database Research Analytic Files (sampled from fiscal years 2016-17). However the analysis, conclusions, opinions and statements expressed herein are those of the author(s) and not those of the Canadian Institute for Health Information.

## Author(s)

* [Bell Eapen](https://nuchange.ca)

## See Also

* [Dadage: Reinforcement Learning env based on Discharge Abstract Database](https://github.com/dermatologist/dad-gym-env)

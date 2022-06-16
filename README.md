# ToxicityPredictor
This repository is Python API of [Toxicity Predictor](http://mmi-03.my-pharm.ac.jp/tox1/prediction_groups/new): a QSAR platform for drug safety prediction and computational toxicology ([Kurosaki *et al.* **2020**](https://pubmed.ncbi.nlm.nih.gov/33113912/)). You can easely get optimal three dimensional molecular structures and toxic predicton results through Python.

# Installation of packages
Please install packages by following command.
```bash
conda install -y -f conda_requirements.txt
```
# Usage
```
python toxicity_predictor.py user_email user_password absolute_path_to_sdf --headless
```
If not use option ```--headless```, the chrome GUI starts up.

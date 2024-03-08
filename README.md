# Kidney-Disease-Classification-Deep-Learning


## workflows

1.update config.yaml

2.update secrets.yaml 

3.update params.yaml

4.update the entity

5.Update the configuration manager in src config

6.Update the components

7.Update the pipeline

8.Update the main.py

9.Update the dvc.yaml

10.app.py

# STEP 01- Create a conda environment after opening the repository
```bash
conda create -n kidney python=3.8 -y 
```

```bash
conda activate kidney
```

# STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

# Finally run the following command
```bash
python app.py
```

# dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/raghavpatel2507/Kidney-Disease-Classification-Deep-Learning.mlflow \
MLFLOW_TRACKING_USERNAME=raghavpatel2507 \
MLFLOW_TRACKING_PASSWORD=ee9963e0e31b32b22da0a6fba87181560614bee1 \
python script.py

Run this to export as env variables:
```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/raghavpatel2507/Kidney-Disease-Classification-Deep-Learning.mlflow 

export MLFLOW_TRACKING_USERNAME=raghavpatel2507 
export MLFLOW_TRACKING_PASSWORD=ee9963e0e31b32b22da0a6fba87181560614bee1

```

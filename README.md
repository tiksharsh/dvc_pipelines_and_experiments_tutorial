## First: installing DVC as a Python library

```
$ mkdir dvc_tutorial
$ cd dvc_tutorial
$ python -m venv .env
$ source .env/bin/activate
(.env)$ pip install dvc
(.env)$ git init
(.env)$ dvc init
```

## 1 - Create a `params.yaml` file

```
# file params.yaml
prepare:
    categories:
        - comp.graphics
        - sci.space
```

## 2 - Create the `prepare.py` script

Save the file `prepare.py` file (it's available here on this repo) inside `/src`. Your folder structure should look like this:

```
├── params.yaml
└── src
    └── prepare.py
```

## 3 - Create the `prepare.py` stage usinf DVC

The steps for doing that are:

* Write a python script: `prepare.py`
* Save the parameters: `categories` inside `params.yaml`
* Specify the files the script depends on: `prepare.py`
* Specify the files the script generates: the folder `data/prepared`
* Defined the command line instruction to run this step

```
(.env)$ pip install pyyaml scikit-learn pandas

(.env)$ dvc run -n prepare -p prepare.categories -d src/prepare.py -o data/prepared python src/prepare.py
```

## 4 - Create the scripts and the stages for all the other steps

```
(.env)$ dvc run -n featurize -d src/featurize.py -d data/prepared -o data/features python src/featurize.py data/prepared data/features

(.env)$ dvc run -n train -p train.alpha -d src/train.py -d data/features -o model.pkl python src/train.py data/features model.pkl

(.env)$ dvc run -n evaluate -d src/evaluate.py -d model.pkl -d data/features --metrics-no-cache scores.json --plots-no-cache plots.json python3 src/evaluate.py model.pkl data/features scores.json plots.json
```

## 5 - Change parameters

```
# file params.yaml
prepare:
    categories:
        - comp.graphics
        - rec.sport.baseball
train:
    alpha: 0.8
```

## 6 - Run the pipeline

```
(.env)$ dvc repro
```

## 7 - Compare the metrics

```
(.env)$ dvc params diff

(.env)$ dvc metrics diff
```

## 8 - Visualize and compare metrics using plots

```
(.env)$ dvc plots show -y precision -x recall plots.json

(.env)$ dvc plots diff --targets plots.json -y precision
```

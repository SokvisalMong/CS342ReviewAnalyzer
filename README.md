# CS342 Artificial Intelligence Group Project
## Members
- Rithy Phal (Leader)
- Pichchansomanea Khloeung
- Sokvisal Mong

## Running
```bash
pip install -r requirements.txt
```

```bash
py src/main.py
```

*Make sure you are using python 3.7*
## Requirements
This project was built using Python 3.7 specifically.
The reason being pickle5 is no longer available in python 3.7>.

Download the dataset [here](https://www.kaggle.com/datasets/nabamitachakraborty/amazon-reviews) and place it in the `datasets` folder

## Notes

The `review_anal_model_v1.h5` is built using the 0.4 million entities file.
The `review_anal_model_v2.h5` is built using the 3.6 million entities file.

The reason being, the 0.4 million file is the testing dataset, and the 3.6 million file is the training dataset.

## TODO
- Write a docker file for this project similiar to the prof's.
- 
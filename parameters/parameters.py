import os

FILE_NAME = "energydata_complete.csv"
DATA_FOLDER = "data"

main_path = os.getcwd()

file_path = os.path.join(os.path.join(main_path, DATA_FOLDER), FILE_NAME)


autogluon_params = {
"save_path": 'artefacts/models_regression',
"time_limit": 60,
"label": "Appliances",
"problem_type": "regression"
}

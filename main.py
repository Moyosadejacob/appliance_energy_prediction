# main Entrypoint
from parameters.parameters import file_path,autogluon_params
# from data_ingestion.ingest import appliance_energy_data
from data_ingestion.ingest import get_data
from model_building.build_model import autogluon_model_build
import time
# Stage 0- Data Ingestion
print("starting Data Ingestion")
start_time = time.time()
appliance_energy_data = get_data(file_path)
end_time = time.time()
print(f"Execution for data Ingestion is {end_time-start_time} seconds")
print(appliance_energy_data.shape)
print(appliance_energy_data.head())


# stage 1

# stage 2 - Model Building
print("Starting Model Building...")
start_time = time.time()
train_data, test_data, predictor=(
    autogluon_model_build(appliance_energy_data,autogluon_params)
)
end_time = time.time()
print(f"Execution time for Building model is {end_time-start_time} seconds")
print(f"Size of Train data is {train_data.shape}")
print(f"Size of Test data is {test_data.shape}")

# Stage 3 _ Model Evaluation
print("Starting Model Evaluation...")
start_time = time.time()
print(predictor.leaderboard(silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Train) is {end_time-start_time} seconds")
start_time = time.time()
print(predictor.leaderboard(test_data, silent=True))
end_time = time.time()
print(f"Execution time for Model Evaluation (Test) is {end_time-start_time} seconds")

import pandas as pd
from config.core import config
from pipeline import sba_pipe_x, sba_pipe_y
from processing.data_manager import load_dataset, save_pipeline
from sklearn.model_selection import train_test_split
from pathlib import Path


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.app_config.training_data_file)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.model_config.features],  # predictors
        data[config.model_config.target],
        test_size=config.model_config.test_size,
        # we are setting the random seed here
        # for reproducibility
        random_state=config.model_config.random_state,
    )
    y_train = sba_pipe_y.fit_transform(pd.DataFrame(y_train))

    # fit model
    sba_pipe_x.fit(X_train, y_train.values.ravel())

    # Test data set 
    X_test.to_csv(Path(f"{DATASET_DIR}/test.csv"), index=False)

    # persist trained model
    save_pipeline(pipeline_to_persist=sba_pipe_x)


if __name__ == "__main__":
    run_training()

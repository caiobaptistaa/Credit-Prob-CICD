from gbc_model.config.core import config
from gbc_model.processing.features import BinaryAssign


def test_newexist(sample_input_data):
    transformer = BinaryAssign(
        variables=config.model_config.binary_vars,
    )

    subject = transformer.fit_transform(sample_input_data)

    assert subject["NewExist"].isnull().sum() >= 1

from gbc_model.predict import make_prediction


def test_make_prediction(sample_input_data):
    # Given
    expected_no_predictions = 134875

    # When
    result = make_prediction(input_data=sample_input_data)

    # Then
    predictions = result.get("predictions")
    predictions = predictions.tolist()
    assert isinstance(predictions, list)
    # assert isinstance(predictions[0], np.int64)
    assert result.get("errors") is None
    assert len(predictions) == expected_no_predictions
    assert predictions[0] <= 1.0
    assert predictions[0] >= 0.0

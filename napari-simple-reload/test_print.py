from napari_simple_reload._widget import example_factory


def test_false_inputs():
    values_to_test = [False, 0, None]
    for value in values_to_test:
        wdg = example_factory(input_string={"value": str(value)})
        result = wdg()
        assert result == f"You entered {value}!"


if __name__ == "__main__":
    test_false_inputs()

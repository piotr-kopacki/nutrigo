from core.names import names


def test_names_is_dict():
    assert isinstance(names, dict)


def test_names_keys_are_ids():
    assert all([isinstance(k, int) for k in names])


def test_names_values_are_lists():
    assert all([isinstance(v, list) for v in names.values()])

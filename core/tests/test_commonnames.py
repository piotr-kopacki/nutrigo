from core.commonnames import common_names

def test_common_names_is_dict():
    assert isinstance(common_names, dict)

def test_common_names_keys_are_ids():
    assert all([isinstance(k, int) for k in common_names])

def test_common_names_values_are_str():
    assert all([isinstance(v, str) for v in common_names.values()])
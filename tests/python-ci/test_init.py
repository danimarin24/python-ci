from python_ci import generate_list


def test_generate_list() -> None:
    assert generate_list() == 42

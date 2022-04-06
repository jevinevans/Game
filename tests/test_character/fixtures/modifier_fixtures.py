import pytest


# Modifier Fixtures
@pytest.fixture
def add_mods():
    return {
        "valid": {"attack": 43, "defense": -20},
        "invalid": {
            "attack": -34,
            "error": -32,
            "energy": 20,
        },
    }


@pytest.fixture
def mult_mods():
    return {
        "valid": {"health": 0.33, "energy": -0.6},
        "invalid": {
            "health": -0.10,
            "error": 23,
            "defense": 0.4,
        },
    }


@pytest.fixture
def new_add_modifier():
    return {"health": 34, "defense": 60}


@pytest.fixture
def new_mult_modifier():
    return {"energy": 0.56, "attack": 0.25}


@pytest.fixture
def modifier_get_expectation(add_mods, mult_mods):
    return {"adds": add_mods["valid"], "mults": mult_mods["valid"]}


@pytest.fixture
def modifier_export_expectation(add_mods, mult_mods):
    return {
        "name": "Test Export",
        "adds": add_mods["valid"],
        "mults": mult_mods["valid"],
    }


@pytest.fixture
def modifier_str_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base = f"""{' '*indent}Modifier: Output Test:
{' '*(indent+2)}Attack
  {' '*(indent+2)}+43\n
{' '*(indent+2)}Defense
  {' '*(indent+2)}-20\n
{' '*(indent+2)}Health
  {' '*(indent+2)}+33.0%\n
{' '*(indent+2)}Energy
  {' '*(indent+2)}-60.0%\n
"""
        expectations.append(base)
    return expectations

@pytest.fixture
def modifier_details_expectation():
    expectations = []
    for indent in range(0, 11, 2):
        base = f"""
{' '*indent}Output Test:
{' '*(indent+2)}Attack
  {' '*(indent+2)}+43\n
{' '*(indent+2)}Defense
  {' '*(indent+2)}-20\n
{' '*(indent+2)}Health
  {' '*(indent+2)}+33.0%\n
{' '*(indent+2)}Energy
  {' '*(indent+2)}-60.0%\n
"""
        expectations.append(base)
    return expectations
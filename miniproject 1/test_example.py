import pytest

# make sure the first word matches your package/folder name
from IcecreamMachine import IceCreamMachine
from IcecreamMachine import STAGE
#this is an example test showing how to cascade fixtures to build up state

from IcecreamExceptions import ExceededRemainingChoicesException, OutOfStockException

@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
@pytest.fixture
def machine1():
    icm1 = IceCreamMachine()
    return icm1
@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

def test_production_line(second_order):
    assert second_order is not None

# UCID: sp2927
# Date: 21 Oct 2022
def test_first_selection(machine):
    assert machine.currently_selecting.name == STAGE.Container.name

# UCID: sp2927
# Date: 21 Oct 2022
def test_flavour_in_stock(machine):
    # setting available quantity to 1 for testing convenience
    machine.flavors[0].quantity = 1
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    try:
        machine.handle_flavor("vanilla")
        assert machine.flavors[0].quantity == -1
    except OutOfStockException:
        assert False

# UCID: sp2927
# Date: 21 Oct 2022
def test_toppings_in_stock(machine):
    # setting available quantity to 1 for testing convenience
    machine.toppings[0].quantity = 1
    machine.handle_container("cup")
    machine.handle_flavor("next")
    machine.handle_toppings("sprinkles")
    try:
        machine.handle_toppings("sprinkles")
        assert machine.toppings[0].quantity == -1
    except OutOfStockException:
        assert False

# UCID: sp2927
# Date: 21 Oct 2022
def test_max_scoops(machine):
    machine.handle_container("cup")
    # loop to choose (maximum - 1) number of scoops
    for scoop in range(machine.MAX_SCOOPS - 1):
        machine.handle_flavor("Chocolate")
    try:
        machine.handle_flavor("Chocolate")
        assert machine.remaining_scoops == 0
    except ExceededRemainingChoicesException:
        assert False

# UCID: sp2927
# Date: 21 Oct 2022
def test_max_toppings(machine):
    machine.handle_container("cup")
    machine.handle_flavor("next")
    # loop to choose (maximum - 1) number of toppings
    for scoop in range(machine.MAX_TOPPINGS - 1):
        machine.handle_toppings("Peanuts")
    try:
        machine.handle_toppings("Peanuts")
        assert machine.remaining_toppings == 0
    except ExceededRemainingChoicesException:
        assert False

# UCID: sp2927
# Date: 21 Oct 2022
def test_total_cost(machine1):
    machine1.reset()
    machine1.handle_container("cup")
    machine1.handle_flavor("vanilla")
    machine1.handle_flavor("Chocolate")
    machine1.handle_flavor("Strawberry")
    machine1.handle_flavor("next")
    machine1.handle_toppings("Sprinkles")
    machine1.handle_toppings("Chocolate Chips")
    machine1.handle_toppings("M&Ms")
    machine1.handle_toppings("done")
    assert machine1.calculate_cost() == '4.75'

# UCID: sp2927
# Date: 21 Oct 2022
def test_total_sales(machine1):
    machine1.handle_container("cup")
    machine1.handle_flavor("vanilla")
    machine1.handle_flavor("Chocolate")
    machine1.handle_flavor("next")
    machine1.handle_toppings("Sprinkles")
    machine1.handle_toppings("done")
    iceCreamCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost1, str(iceCreamCost1))

    machine1.handle_container("Waffle Cone")
    machine1.handle_flavor("Strawberry")
    machine1.handle_flavor("next")
    machine1.handle_toppings("Chocolate Chips")
    machine1.handle_toppings("M&Ms")
    machine1.handle_toppings("done")
    iceCreamCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost2, str(iceCreamCost2))

    assert machine1.total_sales == iceCreamCost1 + iceCreamCost2

# UCID: sp2927
# Date: 21 Oct 2022
def test_total_icecreams(second_order, machine1):
    machine1.handle_container("cup")
    machine1.handle_flavor("Chocolate")
    machine1.handle_flavor("next")
    machine1.handle_toppings("done")
    iceCreamCost1 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost1, str(iceCreamCost1))

    machine1.handle_container("Waffle Cone")
    machine1.handle_flavor("next")
    machine1.handle_toppings("M&Ms")
    machine1.handle_toppings("done")
    iceCreamCost2 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost2, str(iceCreamCost2))

    machine1.handle_container("Sugar Cone")
    machine1.handle_flavor("next")
    machine1.handle_toppings("Peanuts")
    machine1.handle_toppings("done")
    iceCreamCost3 = float(machine1.calculate_cost())
    machine1.handle_pay(iceCreamCost3, str(iceCreamCost3))

    assert second_order.total_icecreams == 2 and machine1.total_icecreams == 3
"""
Elisha Internet Cafe calculators.

PyScript lets Python respond to events in the webpage. An event is something
that happens, such as a visitor clicking a button or changing a selection.
"""

from pyscript import document
from pyscript import when
from math import isfinite


PRINT_RATES = {
    "bw": 3,
    "color": 5,
}


def peso(amount):
    """Format a number as a Philippine peso value with two decimal places."""
    return f"₱{amount:,.2f}"


@when("change", "#print-type")
def update_print_rate(event):
    """Update the shown sample rate when the printing choice changes."""
    print_type = document.querySelector("#print-type").value
    rate = PRINT_RATES[print_type]
    document.querySelector("#sample-rate").innerText = f"₱{rate} / page"


@when("click", "#calculate-print")
def calculate_print_total(event):
    """Read the page count, validate it, calculate, and show the estimate."""
    page_input = document.querySelector("#page-count").value
    result = document.querySelector("#print-result")

    # Inputs arrive as text, so Python converts the value after checking it.
    try:
        pages = int(page_input)
        if pages <= 0:
            raise ValueError
    except (TypeError, ValueError):
        result.innerText = "Please enter a whole number of pages greater than zero."
        result.className = "result-box result-error"
        return

    print_type = document.querySelector("#print-type").value
    rate = PRINT_RATES[print_type]
    service_name = "Black-and-white" if print_type == "bw" else "Colored"
    total = pages * rate

    # Python updates the result text directly in the page after the click event.
    result.innerText = (
        f"{service_name} printing · {pages} page(s) · sample rate "
        f"{peso(rate)} / page · estimated total {peso(total)}. "
        "Confirm actual prices with the owner."
    )
    result.className = "result-box result-success"


@when("click", "#calculate-rental")
def calculate_rental_cost(event):
    """Validate visitor-entered hours and rate, then show an estimate."""
    hours_input = document.querySelector("#rental-hours").value
    rate_input = document.querySelector("#hourly-rate").value
    result = document.querySelector("#rental-result")

    try:
        hours = float(hours_input)
        rate = float(rate_input)
        if not isfinite(hours) or not isfinite(rate) or hours <= 0 or rate <= 0:
            raise ValueError
    except (TypeError, ValueError):
        result.innerText = (
            "Enter a number of hours and an hourly rate greater than zero."
        )
        result.className = "result-box result-error"
        return

    total = hours * rate
    result.innerText = (
        f"{hours:g} hour(s) × {peso(rate)} per hour = estimated total "
        f"{peso(total)}. This is an estimate, not an official business price."
    )
    result.className = "result-box result-success"


# The @when decorators above connect each Python function to a browser event:
# changing the dropdown updates the rate, and clicking either button calculates
# an estimate. PyScript calls the matching function when that event occurs.

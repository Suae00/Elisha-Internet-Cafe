Elisha Internet Cafe

A responsive, single-page student project for Elisha Internet Cafe, a family-run computer shop in Barangay Duljo Fatima, Cebu City. It introduces the business and its services and demonstrates Event-Driven Programming with two Python-powered estimates.

 Technologies

- HTML for page structure and accessible calculator controls
- CSS for responsive styling and the workstation illustration
- Python with PyScript for printing and computer rental calculations
- PyScript 2026.7.3 loaded from the official `pyscript.net` CDN

There is no backend, database, login, or contact form. The project does not collect or submit visitor information.

Run in Replit

Open this artifact in Replit and use the existing preview workflow to serve the website. If running it locally, start any static web server from this folder (for example, `python -m http.server 8000`) and open the local server URL in a browser. The page needs an internet connection to load PyScript and the hosted fonts.

Test the calculators

1. In Printing cost, switch between Black-and-white and Colored. The displayed sample rate changes to ₱3 or ₱5 per page.
2. Enter a positive whole number of pages and choose Calculate Total. The result includes the selected type, quantity, sample rate, and estimated total in Philippine pesos.
3. Try a blank, zero, negative, or non-whole page quantity to see the helpful validation message.
4. In Computer rental, enter hours and an hourly rate greater than zero, then choose Calculate Rental Cost. The estimate is hours multiplied by the rate.
5. Try blank, zero, or negative rental values to see the validation message.

Printing rates are unconfirmed sample rates drawn from competitor prices in the research paper. They are not represented as Elisha Internet Cafe's actual prices; confirm actual prices with the owner. The rental rate is entered by the visitor because the actual rate was not provided, and the result is only an estimate.

Event-Driven Programming

An event is an action such as a click or a selection change. At the bottom of `main.py`, Python registers event listeners for the printing-type selection and both calculator buttons. PyScript calls `update_print_rate`, `calculate_print_total`, or `calculate_rental_cost` when the corresponding event happens. Those functions read the HTML inputs, validate their values, calculate in Python, and update the page's result text.

Updating sample prices

In `main.py`, edit the `PRINT_RATES` dictionary (`bw` and `color`) to change the calculator's demonstration rates. Also update the visible sample-rate and disclaimer copy in `index.html` so the explanation remains consistent. The displayed rates must remain clearly identified as unconfirmed samples unless the business owner confirms actual prices.

Project note

This is a student project for Event-Driven Programming and Business Analytics. Survey percentages in Research Highlights describe the group's survey of 34 respondents and may not represent all customers. The mission wording is presented as a proposed mission for the website, not an official statement.

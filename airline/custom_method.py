import frappe

def set_full_name(doc, method):
    """
    Set the full name before saving the document.
    """
    if doc.firstname and doc.lastname:
        doc.fullname = f"{doc.firstname} {doc.lastname}"
    else:
        doc.fullname = doc.firstname or doc.lastname


def calculate_total_amount(doc, method):
    """
    Calculate the total amount before saving the document.
    """
    total_add_ons = sum([d.amount for d in doc.add_ons])
    doc.total_amount = doc.flight_price + total_add_ons

def validate_status_before_submit(doc, method):
    """
    Prevent submission of the Airplane Ticket document if the status is not 'Boarded'.
    """
    if doc.status != 'Boarded':
        frappe.throw(_("Cannot submit the Airplane Ticket document unless the status is 'Boarded'."))

def assign_seat(doc):
    """
    Logic to assign a seat to a passenger.
    This example simply assigns the first available seat.
    """
    # Placeholder logic for seat assignment; replace with your actual logic
    available_seat = get_next_available_seat(doc.airplane_flight)
    return available_seat

def get_next_available_seat(flight_name):
    """
    Example logic to get the next available seat.
    Replace this with your actual seat assignment logic.
    """
    # Placeholder for demonstration; in practice, query your database for the next available seat
    seats = ['1A', '1B', '2A', '2B']
    for seat in seats:
        if not frappe.db.exists('Airplane Ticket', {'seat': seat, 'airplane_flight': flight_name}):
            return seat
    return None

"""
Inventory Management System
Rungta International Skills University - PS No. 14
Python 3 | Lists, Dictionaries, Functions, CRUD

Run: python inventory_management.py
"""

inventory = []
next_item_number = 101
LOW_STOCK_LIMIT = 5


def generate_item_id():
    """Return the next unique ID (I101, I102, ...)."""
    global next_item_number
    item_id = f"I{next_item_number}"
    next_item_number += 1
    return item_id


def read_quantity(prompt="Quantity: "):
    """Read a non-negative whole-number quantity; return None if invalid."""
    raw = input(prompt).strip()
    try:
        # Reject decimal values and strings such as '3.0'.
        value = int(raw)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid quantity. Quantity must be a non-negative whole number.")
        return None


def read_price(prompt="Price: "):
    """Read a non-negative price; return None if invalid."""
    raw = input(prompt).strip()
    try:
        value = float(raw)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid price. Price must be a non-negative number.")
        return None


def find_item_by_id(item_id):
    """Return the matching item dictionary, or None."""
    for item in inventory:
        if item["id"].lower() == item_id.strip().lower():
            return item
    return None


def print_table(items):
    """Display item dictionaries in a neat table."""
    if not items:
        print("No items found.")
        return

    print("-" * 62)
    print(f"{'ID':<8} {'Name':<20} {'Quantity':>10} {'Price':>10} {'Stock Value':>12}")
    print("-" * 62)
    for item in items:
        value = item["quantity"] * item["price"]
        print(f"{item['id']:<8} {item['name']:<20} {item['quantity']:>10} "
              f"{item['price']:>10.2f} {value:>12.2f}")
    print("-" * 62)


def add_item():
    """Create and append a new item after validating its values."""
    name = input("Name: ").strip()
    if not name:
        print("Invalid name. Name cannot be empty. Item not added.")
        return

    quantity = read_quantity()
    if quantity is None:
        print("Item not added.")
        return

    price = read_price()
    if price is None:
        print("Item not added.")
        return

    item = {
        "id": generate_item_id(),
        "name": name,
        "quantity": quantity,
        "price": price
    }
    inventory.append(item)
    print(f"Item added. ID: {item['id']}")
    print(f"{item['id']} | {item['name']} | Qty: {item['quantity']} | Price: {item['price']:g}")
    if item["quantity"] < LOW_STOCK_LIMIT:
        print(f"Low stock alert: {item['name']} ({item['quantity']})")


def view_items():
    """Display all inventory items."""
    print_table(inventory)


def update_item():
    """Update an existing item after validating all supplied changes."""
    item_id = input("Enter item ID to update: ").strip()
    item = find_item_by_id(item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    print("Press Enter to keep the current value.")
    new_name = input(f"Name [{item['name']}]: ").strip()
    raw_quantity = input(f"Quantity [{item['quantity']}]: ").strip()
    raw_price = input(f"Price [{item['price']:g}]: ").strip()

    # Validate first so a bad value cannot leave a partly updated record.
    new_quantity = item["quantity"]
    new_price = item["price"]
    if raw_quantity:
        try:
            new_quantity = int(raw_quantity)
            if new_quantity < 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity. Quantity must be a non-negative whole number.")
            print("Update cancelled; no changes saved.")
            return
    if raw_price:
        try:
            new_price = float(raw_price)
            if new_price < 0:
                raise ValueError
        except ValueError:
            print("Invalid price. Price must be a non-negative number.")
            print("Update cancelled; no changes saved.")
            return

    if new_name:
        item["name"] = new_name
    item["quantity"] = new_quantity
    item["price"] = new_price
    print(f"Item {item['id']} updated.")
    if item["quantity"] < LOW_STOCK_LIMIT:
        print(f"Low stock alert: {item['name']} ({item['quantity']})")


def search_item():
    """Search for an item by its ID or name."""
    term = input("Enter item ID or name to search: ").strip().lower()
    matches = [
        item for item in inventory
        if term == item["id"].lower() or term in item["name"].lower()
    ]
    print_table(matches)


def delete_item():
    """Delete an item by ID."""
    item_id = input("Enter item ID to delete: ").strip()
    item = find_item_by_id(item_id)
    if item is None:
        print(f"Item ID {item_id} not found.")
        return

    inventory.remove(item)
    print(f"Item '{item['name']}' deleted. Items left: {len(inventory)}")


def total_stock_value():
    """Calculate and display each item's value and the overall value."""
    if not inventory:
        print("Total stock value: 0.00")
        return

    total = 0.0
    for item in inventory:
        value = item["quantity"] * item["price"]
        print(f"{item['name']}: {value:g}")
        total += value
    print(f"Total stock value: {total:g}")


def low_stock_report():
    """List items whose quantity is below 5."""
    low_items = [item for item in inventory if item["quantity"] < LOW_STOCK_LIMIT]
    if not low_items:
        print("No low-stock items.")
        return

    print("Low stock (below 5):")
    for item in low_items:
        print(f"{item['id']} | {item['name']} | Qty: {item['quantity']}")


def display_menu():
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add item")
    print("2. View items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Total stock value")
    print("6. Low-stock report")
    print("7. Search item")
    print("8. Exit")


def main():
    """Run the menu repeatedly until the user chooses Exit."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            total_stock_value()
        elif choice == "6":
            low_stock_report()
        elif choice == "7":
            search_item()
        elif choice == "8":
            print("Thank you for using Inventory Management System.")
            break
        else:
            print("Invalid menu option. Please choose from 1 to 8.")


if __name__ == "__main__":
    main()

import json

# Load data from cloud database
def load_database(filename='database.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save data to cloud database
def save_database(data, filename='database.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Check if new data is duplicate
def is_duplicate(new_entry, database):
    for entry in database:
        if entry["email"] == new_entry["email"]:
            return True
    return False

# Append only if unique
def add_data(new_entry):
    db = load_database()
    if is_duplicate(new_entry, db):
        print("❌ Duplicate entry found. Data not added.")
    else:
        new_entry["id"] = len(db) + 1
        db.append(new_entry)
        save_database(db)
        print("✅ Unique data added successfully.")

# Example usage
if __name__ == "__main__":
    # New data input
    new_user = {
        "name": "Charlie",
        "email": "charlie@example.com"
    }

    add_data(new_user)

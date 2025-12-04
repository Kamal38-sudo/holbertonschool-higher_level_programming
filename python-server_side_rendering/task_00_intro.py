import os
import sys

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Replace placeholders with values or "N/A" if missing
        filled_template = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Generate output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, "w", encoding="utf-8") as f:
                f.write(filled_template)
            print(f"[copy_files] File created: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Read template from file
    template_file = "template.txt"
    if not os.path.exists(template_file):
        print(f"Template file '{template_file}' not found.")
        sys.exit(1)

    with open(template_file, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Example attendee data
    attendees = [
        {"name": "Alice", "event_title": "Python Workshop", "event_date": "2025-12-10", "event_location": "New York"},
        {"name": "Bob", "event_title": "Python Workshop", "event_date": "2025-12-10"},  # missing event_location
        {"name": "Charlie"}  # missing most fields
    ]

    # Generate invitations
    generate_invitations(template_content, attendees)

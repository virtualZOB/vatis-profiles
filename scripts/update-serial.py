import json
import glob
import os
from datetime import datetime

json_files = glob.glob(os.path.join("../", "**", "*.json"), recursive=False)
current_date = str(datetime.now().strftime('%Y%m%d'))


for json_file in json_files:
    for json_file in json_files:
        with open(json_file, 'r') as file:
            #Parse JSON
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {json_file}: {e}")

        # Set initial release to 0
        release_number = 0
        # Grab file's current serial
        serial_value = str(data["updateSerial"])
        
        # If the YYYYMMDD matches today, grab the last two digits and increment
        if serial_value[:8] == current_date:
            last_two_digits = int(serial_value[-2:])
            last_two_digits =+ 1

            # If more than 99 updates in a day on this file, we need to bomb out loudly
            if last_two_digits > 99:
                print(f"Update count exceedes 99, unable to continue!")
                exit(1)


        # Pad the release number to 2 digits and combine with date, convert to int for JSON
        formatted_release_number = str(f"{release_number:02d}")
        release_serial_str = current_date + formatted_release_number
        release_serial_int = int(release_serial_str)

        data["updateSerial"] = release_serial_int

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)


#!/bin/bash

# Run the data loading script
python ./scripts/load_data.py

# Run the export script to generate a CSV
python export_db_to_csv.py


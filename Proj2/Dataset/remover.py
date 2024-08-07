############################################################################
import csv


def clean_name(name):
    """
    Remove unwanted characters from the name.
    """
    # Remove quotes and commas from the name
    cleaned_name = name.replace('"', '').replace(',', '')
    return cleaned_name


def clean_csv_file(input_csv, output_csv):
    """
    Read a CSV file, clean the Name column, and write the cleaned data to a new CSV file.
    """
    with open(input_csv, 'r', newline='', encoding='utf-8') as infile, \
         open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
       
        # Create CSV reader and writer objects
        csvreader = csv.reader(infile)
        csvwriter = csv.writer(outfile)
       
        # Read and write the header
        header = next(csvreader)
        csvwriter.writerow(header)
       
        # Process each row
        for row in csvreader:
            # Clean the Name column (assuming Name is the second column in the CSV)
            name_index = header.index("Name")
            row[name_index] = clean_name(row[name_index])
           
            # Write the cleaned row to the output CSV
            csvwriter.writerow(row)


    print(f"Data has been cleaned and written to {output_csv}")


# Usage example
input_csv = 'scraped_data.csv'
output_csv = 'cleaned_data.csv'
clean_csv_file(input_csv, output_csv)

def read_this_file():
    try:
# step 1: read this file

        with open("sales_data.txt", 'r') as file:

            sales_data = file.readlines()

# step 2: total sales for each product

        revenue_dict = {}

        for line in sales_data:

            try:

                product_name, quantity_sold, price_per_unit = line.strip().split(',')

                quantity_sold = int(quantity_sold.strip())

                price_per_unit = int(price_per_unit.strip())


                if product_name in revenue_dict:

                    revenue_dict[product_name] += quantity_sold * price_per_unit

                else:

                    revenue_dict[product_name] = quantity_sold * price_per_unit

            except ValueError:

                print(f"Error processing line: {line.strip()}")

# step 3: Create a new file

        with open("sales_summary.txt", 'w') as summary_file:

            for product_name, total_revenue in revenue_dict.items():
                summary_file.write(f"{product_name}: {total_revenue}\n")
                print(f"{product_name}: {total_revenue}")

        print("Sales summary has been written to sales_summary.txt")


    except FileNotFoundError:

        print("Error: sales_data.txt file not found.")

    except Exception as e:

        print(f"An error occurred: {e}")

read_this_file()






        # with open('sales_data.txt', 'r') as file:
        #     for line in file:
        #         sales_data = line
        #         print(sales_data)












# read_this_file()

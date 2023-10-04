# Use the given array of product objects below, each with their name, price, 
# and quantity sold. Additionally, you are given a tax rate as a percentage. 
# Write a function called calculateTotalSalesWithTax that takes in an array of 
# product objects, along with the tax rate, and returns the total sales amount including tax.


from functools import reduce



products = [
    {"name": "Apple", "price": 0.5, "quantity": 10},
    {"name": "Banana", "price": 0.3, "quantity": 20},
    {"name": "Orange", "price": 0.6, "quantity": 15},
]


def main() -> None:
    print(
        calculate_total_sales_with_tax(
                [
                    {"name": "Apple", "price": 0.5, "quantity": 10},
                    {"name": "Banana", "price": 0.3, "quantity": 20},
                    {"name": "Orange", "price": 0.6, "quantity": 15},
                ],
                8
        )
    )
    

def calculate_total_sales_with_tax(products, tax) -> int:
    
    sales: list[float] = list(map(lambda product: product["price"] * product["quantity"], products))

    total_sales: int = int(reduce(lambda total, product: total + product, sales))

    total_sales_with_tax: int = total_sales + ((total_sales * tax) / 100)

    return total_sales_with_tax



if __name__ == "__main__":
    main()
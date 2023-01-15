class CoockingError(Exception):
    def __str__(self):
        return f"З такою кількістю продуктів приготувати їжу не можливо "
def check_material(amount_of_products, limit_value):
    if amount_of_products>limit_value:
        return "недостатньо продуктів"
    else:
        raise CoockingError(amount_of_products)

material=11
check_material(material, 100)
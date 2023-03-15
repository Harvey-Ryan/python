class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True

    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)

skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Cole Haan", "Wing-tip", 199.99)



# Skater shoes go on sale by 20% reduced price
#skater_shoe.price = (1 - 0.2) * skater_shoe.price
skater_shoe.on_sale_by_percent(0.2)
print(skater_shoe.price)
# Dress shoe 10% reduction
#dress_shoe.price = dress_shoe.price * (1 - .1)
dress_shoe.on_sale_by_percent(0.5)
print(dress_shoe.price)

# Skater shoe additional 10% off
#skater_shoe.price = (1 - 0.1) * skater_shoe.price
print(skater_shoe.price)
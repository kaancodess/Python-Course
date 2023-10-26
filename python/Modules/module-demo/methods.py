import db as db

def add_product(product_name, product_price):
    db.products.append({
        "product_id": len(db.products) + 1,
        "product_name": product_name,
        "price": product_price
    })

def update_product(product_id, product_name, product_price):
    for product in db.products:
        if(product["product_id"] == product_id):
            product["product_name"] = product_name,
            product["price"] = product_price,
            break

def get_products():
    for product in db.products:
        print(product)
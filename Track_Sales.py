stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print("Hit jans sale target: ", target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print("Jeans in stock: ", in_stock)

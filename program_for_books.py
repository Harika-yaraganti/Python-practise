book_price=24.95
total_books=(book_price*60)/100
shipping_cost_for_first_copy=3
additional_copy=0.75
b=59*0.75
c=(shipping_cost_for_first_copy+b)
print("total books price={}".format(books*60+c))

class Values:

    bun_name = 'Космическая булка'
    bun_price = 1234
    bun_prices = 1234, 1, 0, 5678748

    ingredient_name = 'Космический острый'
    ingredient_price = 200
    ingredient_type = 'соус'


    expected_receipt = "(==== Космическая булка ====)\n" \
                       "= соус Космический острый =\n" \
                       "= соус Космический острый =\n" \
                       "(==== Космическая булка ====)\n" \
                       "\n" \
                       "Price: 2868"
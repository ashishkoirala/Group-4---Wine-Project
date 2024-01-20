from . import models

def add_currencies_to_db(currencies: list) -> None:
    for currency in currencies:
        iso = currency[1]
        long_name = currency[0]

        c = models.Currency.objects.filter(iso=iso).first()
        if c is None:
            c = models.Currency(
                iso=currency[1],
                long_name=currency[0],
            )
        else:
            c.iso = iso
            c.long_name = long_name

        c.save()

def get_wines(selected_sweetness, selected_vintage, selected_body, selected_pairing, selected_quantity):
    wines = models.Wine.objects.filter(
        wine_sweetness=selected_sweetness,
        current_vintage=selected_vintage,
        wine_body=selected_body,
        food_match=selected_pairing,
        quantity=selected_quantity,
    )
    list_length = min(len(wines), 3)
    recommended = []
    for wine in wines[0:list_length]:
        wine_info = {"name": wine, "link": wine.product_link, "price": wine.price}
        recommended.append(wine_info)
    return recommended


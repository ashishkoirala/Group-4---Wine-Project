from . import models

def get_wines(selected_sweetness, selected_vintage, selected_body, selected_pairing, selected_quantity, selected_alcohol_volume):
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
        # delete this if statement if you don't want to check alcohol volume
        if (is_alcohol_volume_in_range(selected_alcohol_volume, wine)):
            wine_info = {"name": wine, "link": wine.product_link, "price": wine.price, "alcohol_content": wine.alcohol_volume}
            recommended.append(wine_info)
    return recommended

# calculates if alcohol volume is in range
def is_alcohol_volume_in_range(selected_alcohol_volume, wine):
    alcohol_volume_str = wine.alcohol_volume[:-1] # remove the % character from the string
    try:
        alcohol_volume_number = float(alcohol_volume_str) # convert string "14" to int 14
        print(alcohol_volume_number)
    except ValueError:
        print(f"Cannot convert '{alcohol_volume_str}' to an integer.")
        return False
    if selected_alcohol_volume == "0-8%":
        return 0 <= alcohol_volume_number <= 8
    elif selected_alcohol_volume == "9-15%":
        return 9 <= alcohol_volume_number <= 15
    else:
        return alcohol_volume_number > 15

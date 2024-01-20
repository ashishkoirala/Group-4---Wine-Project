from django import forms


class WinePreferenceForm(forms.Form):

    VINTAGE_CHOICES = [
        ('vintage', 'Vintage'),
        ('non_vintage', 'Non Vintage'),
    ]

    ALCOHOL_CONTENT_CHOICES = [
        ('<8', 'Less than 8%'),
        ('8-15', 'Between 8% and 15%'),
        ('>15', 'Above 15%'),
        ('various', 'Various')
    ]

    SWEETNESS_CHOICES = [
        ('dry', 'Dry'),
        ('semi_sweet', 'Semi Sweet'),
        ('sweet', 'Sweet'),
    ]

    BODY_CHOICES = [
        ('medium_bodied', 'Medium Bodied'),
        ('light_bodied', 'Light Bodied'),
        ('full_bodied', 'Full Bodied'),
    ]

    FOOD_CHOICES = [
        ('seafood', 'Seafood'),
        ('beef', 'Beef'),
        ('game', 'Game'),
        ('antipasto', 'Antipasto'),
        ('chicken', 'Chicken'),
        ('cheese', 'Cheese'),
        ('lamb', 'Lamb'),
        # Add more food choices here if necessary
    ]

    vintage = forms.ChoiceField(choices=VINTAGE_CHOICES, label="Vintage or Non-Vintage")
    alcohol_content = forms.ChoiceField(choices=ALCOHOL_CONTENT_CHOICES, label="Alcohol Content")
    sweetness = forms.ChoiceField(choices=SWEETNESS_CHOICES, label="Wine Sweetness")
    body = forms.ChoiceField(choices=BODY_CHOICES, label="Wine Body")
    food = forms.MultipleChoiceField(choices=FOOD_CHOICES, widget=forms.CheckboxSelectMultiple, label="Food Pairing", required=False)

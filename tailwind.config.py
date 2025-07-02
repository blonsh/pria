from django_tailwind.config import tailwind_app_config

tailwind_app_config = {
    'theme': {
        'extend': {
            'colors': {
                'primary': '#6A0DAD',  # Morado principal
                'text': '#000000',     # Negro para texto
            },
            'fontFamily': {
                'montserrat': ['"Montserrat"', 'sans-serif'],
                'open-sans': ['"Open Sans"', 'sans-serif'],
            },
        },
    },
    'plugins': [],
}

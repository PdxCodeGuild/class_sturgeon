Using Django 3.2 because 4.0 is coming out next month (December 2021) and I want this to still work.
I'm using imageField to handle pictures, so: python -m pip install Pillow
Goto Settings and down at the bottom add STATICFILES_DIRS = [BASE_DIR / 'static']
Goto Settings and add to templates:  BASE_DIR / 'templates'
post.body|linebreaksbr is used for a blogbpost to allow <br> or enter between linebreaksbr
pip install django-autoslug    to use autoslug
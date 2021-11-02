from django.urls import path

from . views import index, createshorturl, urlcreated, url_link, delete_url, delete_all

app_name="short"
urlpatterns = [
    path('', index, name="index"),
    path('createshorturl', createshorturl, name="createshorturl"),
    path("list", urlcreated, name="urlcreated"),
    path("this_url_can_be_changed_at_will_thanks_to_the_href_in_the_urls_py_page_line_21/<str:for_the_function_in_views_from_urls>", url_link, name="reference_me_in_urls_html"),
    path('delete_item/<pk>', delete_url, name='delete_url'),
    path('delete_all/', delete_all, name='delete_all'),
]
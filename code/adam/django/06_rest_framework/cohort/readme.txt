The one-liner "path('api-auth/', include('rest_framework.urls'))," in the project file (cohort) url page
    enables the login-logout button on the top-right of the Django Rest Framework page to work. This way
    you can create more users that have varying levels of permission (also, only admin can log in until
    you put this line in). The line works because we installed the rest_framework

In apis permissions, we put is_staff which superusers automatically are a part of. Staff is a box that 
    can be clicked to add already created users to. 

I followed this tutorial to help set up the page: https://learndjango.com/tutorials/django-rest-framework-tutorial-todo-api



The following was added to the settings page: 
    'students',
    'rest_framework',
    'apis',
    'django_filters',
    ]

    REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
        ],

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        ],
    }
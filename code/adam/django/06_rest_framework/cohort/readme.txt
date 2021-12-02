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


Instructor Merrit made a template by adding a template section by:
    Adding template format to with base home on the project URL page
    Adding BASE_DIR on the templates section of the settings
    creating a home.html page with a vue and an axios script tag, then adding script under them
    put {% csrf_token %} in the body, but above the app so it doesn't interfere with it
    in the creation method include the let crsf_token line he has (in the methods of the app)
    Make the x-csrfttoken line in the header a string 'X-CsrfToken' because vue doesn't like "-"
    Created a new view in the APIs to find current user so that title/post input can be left only by logged-in permission
    
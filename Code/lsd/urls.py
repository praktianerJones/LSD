#SPDX-License-Identifier: BSD-3-Clause
'''
urls.py

(C) Copyright 2020 Friedrich Luetze GmbH, S. Strobel, S. Hentges, J. Luelsdorf <lsd@luetze.de>

'''
from django.urls import path
from lsd import views

# CAUTION!
# string/staticString/ has to be defined before any occurence
# of string/<str:variableName>/ otherwise
# staticString would be interpreted as <str:variableName>

urlpatterns = [
    path(''                                        , views.home                  , name='lsd-home'               ),
    path('about'                                   , views.about                 , name='lsd-about'              ),
]

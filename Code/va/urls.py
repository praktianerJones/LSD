from django.urls import path
from . import views

urlpatterns = [
    path(''                                     , views.va                    , name='lsd-va'                 ),
    path('latest'                               , views.va_details_latest     , name='lsd-va-latest'          ),
    path('latest/doc'                           , views.va_details_latest_doc , name='lsd-va-latest-doc'      ),
    path('latest/sw'                            , views.va_details_latest_sw  , name='lsd-va-latest-sw'       ),
    path('nightly'                              , views.va_details_nightly    , name='lsd-va-nightly'         ),
    path('nightly/doc'                          , views.va_details_nightly_doc, name='lsd-va-nightly-doc'     ),
    path('nightly/sw'                           , views.va_details_nightly_sw , name='lsd-va-nightly-sw'      ),
    path('<path:branch_type>'                    , views.va_branch             , name='lsd-va-branch-type'     ),
    path('<str:branch_type>/<str:branch_name>'  , views.va_branch_name        , name='lsd-va-branch-type-name'),
]
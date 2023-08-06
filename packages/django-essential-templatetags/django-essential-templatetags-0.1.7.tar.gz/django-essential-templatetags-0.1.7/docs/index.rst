..
   Created : 2019-02-01

   @author: Koral Hassan

   django-essential-templatetags documentation master file,

========================
django-essential-templatetags
========================

Essential templatetags for Django.

Installation
------------

Install with pip::

    pip install django-essential-templatetags

Then declare the app in your settings.py ::

    INSTALLED_APPS = [
    ...
        'essential_templatetags',
    ]

To use the templatetags, add in your template::

    {% load essential_templatetags_extra %}

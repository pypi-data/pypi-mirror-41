===========================
Django "excontrib" Comments
===========================

.. image:: https://img.shields.io/pypi/v/maykin-django-contrib-comments.svg
   :target: https://pypi.org/project/maykin-django-contrib-comments

.. image:: https://img.shields.io/travis/maykinmedia/django-contrib-comments.svg
    :target: http://travis-ci.org/maykinmedia/django-contrib-comments

Django used to include a comments framework; since Django 1.6 it's been
separated to a separate project. This is that project.

This framework can be used to attach comments to any model, so you can use it
for comments on blog entries, photos, book chapters, or anything else.

This is a fork of the official django maintained package. The only difference
is that the object_pk field is actually an IntegerField instead of a TextField
for performance reasons.

For details, `consult the documentation`__.

__ https://django-contrib-comments.readthedocs.io/

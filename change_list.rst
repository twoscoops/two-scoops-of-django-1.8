Two Scoops of Django 1.8 Change List
=====================================

**Warning: This is a work in progress and may not match the current status of Two Scoops of Django 1.8.**

* Various grammar mistakes have been corrected

* Removed references to django.views.defaults.shortcut and django.conf.urls.shortcut

* Chapter: Setup

  * Added virtalenvwrapper-win for windows

* Chapter: Project Layout

  * Cookiecutter-django for default project layout
 
  * Use config for root config directory of project
  
  * Added Kevin Xu's fork of Two Scoops Project project.
 
* Chapter: Database

  * Removed South mentions
  
* Chapter: PostgresSQL (NEW)

 * Postgres-specific fields and widgets, validators, hstore support (in progress)

* Chapter: Function- and Class-Based Views

  *  Warned against use of dotted paths in URL definitions
 
* Chapter: Forms

  * django.forms.Field.has_changed() instead of django.forms.Field._has_changed()
  
  * Added example of using forms to validate incoming non-Web data
 
* Chapter: Templates

  * Mention use of Jinja2

* Chapter: Admin

 * @admin.register decorator

* Chapter: Security

  * Fix borked security link

* Chapter: debugging (NEW)

  * Context processor for debugging (thanks @simonw)
  
  * feature flags (again thanks @simonw)
  
  * PDB/IPDB

* Chapter: Deployment

  * Really, really don't use mod_python
  
* Chapter: Continuous Integration

  * Added AppVeyor

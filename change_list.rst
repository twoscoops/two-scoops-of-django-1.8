Two Scoops of Django 1.8 Change List
=====================================

**Warning: This is a work in progress and may not match the current status of Two Scoops of Django 1.8.**

* Various grammar mistakes have been corrected

* Removed references to django.views.defaults.shortcut and django.conf.urls.shortcut

* Chapter: Coding Style

  * JS style guides
  
  * JS style checker packages
  
  * HTML/CSS style guides
  
  * CSS style checker packages

* Chapter: The Ultimate Django Environment Setup

  * Added virtalenvwrapper-win for windows
  
  * Merged in the chapter on Identical Environments

* Chapter: How to Lay Out Django Projects

  * Cookiecutter-django for default project layout
 
  * Use config for root config directory of project
  
  * Added Kevin Xu's fork of Two Scoops Project project.
 
* Chapter: Database

  * Removed South mentions
  
  * Added Postgres fields
  
  * Break out queries and database interactions into their own chapter
  
* Chapter (New): Queries and the Database

  * Added database functions
  * Added try/except issues and exceptions to use.

* Chapter: Function- and Class-Based Views

  *  Warned against use of dotted paths in URL definitions

* Chapter (new): Form Fundamentals

  * Moved 'more forms' to be the basics of things to do with forms
  
  * Now explicitly instructing to use forms for all incoming data
  
  * Added mention of ModelForms for non-web data
  
  * Added mention fields without pre-made widgets

* Chapter: Forms and Class-Based Views

  * django.forms.Field.has_changed() instead of django.forms.Field._has_changed()
  
* Chapter: Templates

  * Mention use of Jinja2

* Chapter: Django and Jinja2

  * Using default filters in Jinja2
  
  * Replacing the need for context_processors with middleware.
  
  * Address CSRF usage.
  
  * The static nature of the Jinja2 Environment class.
  
* Chapter: Rest API

  * Added 410 methods
  
  * Mention Service-Oriented Architecture
  
  * Promoting your API
  
  * Create SDKs for API integrators

* Chapter: Admin

  * @admin.register decorator
  
  * Corrected our advice for __str__ or __unicode__.
  
* Chapter: Third-Party Packages

  * Pointed at Audrey's project release checklist
  
  * Advocate use of cookiecutter for jumpstarting projects
  
  * Suggested appveyor for getting Windows users of projects

* Chapter: Security

  * Fix borked security link
  
* Chapter: Testing

 * Tricks for using Request Factory
 
 *  Quick intro to using Mock

* Chapter: debugging (NEW)

  * Context processor for debugging (thanks @simonw)
  
  * feature flags (again thanks @simonw)
  
  * PDB/IPDB

* Chapter: Deployment

  * Added high level instructions for starting from scratch

  * Really, really don't use mod_python

  * Removed suggested practices for Salt and Ansible. They are out of scope for this book and the content changes too quickly.
  
* Chapter: Identical Environments

  * Merged into the The Ultimate Django Environment Setup chapter
  
* Chapter: Continuous Integration

  * Added AppVeyor

# Two Scoops of Django 1.8 Change List

http://twoscoopspress.com/products/two-scoops-of-django-1-8

## Two Scoops of Django 1.8 Change List Update #5 (final)

* Chapter: Security
  * Much better definition of zero-day attack, plus easy-to-understand examples. Thanks to @ludw (#80).
  * Removed link to `code.google.com/p/browsersec/wiki/Main` as google code is going away and the document was the foundation for [The Tangled Web](http://amzn.to/1hXAAyx), which is also linked on the same page.
* Chapter: Continuous Integration
  * Clearer explanation of CI workflow item 2, thanks to @bogdal (#79)
* Chapter: Debugging
  * Added IPDB and PDB packages
  * Added emphasis about removing email addresses in Mirroring Production section, thanks to @ludw (#81).
* Appendix: Packages
  * Added django-test-plus
* Appendix: Additional Resources
  * Added new Python tutorial
  * Added cdrf.co
* Grammar and typo fixes
* Formatting corrections

## Two Scoops of Django 1.8 Change List Update #4

* Chapter: Coding Style
  * Changed the bullets in `Consider the Django Coding Style Guidelines` into subsections so they could be expanded up with code examples.
* Chapter: Environment Setup
  * Moved `Fixtures Are Not a Magic Solution` subsection downwards in the chapter to make more sense
  * Changed some spacing to improve readability
* Chapter: Optimal Django Setup
  * Reworked the 3-tier project layout sections
  * Changed named of `Using a Cookiecutter Template to Generate Our Layout` to `Going Beyond startproject`
  * Explained the reasoning behind and the use of `Cookiecutter` and why we stopped updating django-twoscoops-project
  * Clarified `PYTHONPATH` box and using `django-admin.py` instead of `manage.py`
* Chapter: Fundamentals of App Design
  * Reference the utilities chapter from the listing of `utils.py`
* Chapter: Queries
  * Pointed text at correct code example, thanks to @NPann (#77)
* Chapter: Class- and Function-Based Views
  * Added section on avoiding usie of `locals()` as views context, thanks to @michaeljohnbarr (#78)
* Chapter: Best Practices for CBVs
  * Fixed `get_object_or_404`, thanks to @bogdal (#65)
* Chapter: Common Patterns for Forms
  * Pointed text at correct code example, thanks to @NPann (#77)
  * Addressed `forms.ValidationError` argument for `code` in a tip box, thanks to @arnaudlimbourg and @mjtamlyn  (#63) 
* Chapter: Security
  * Added reference to `Appendix G: Security Settings Reference`
* Chapter: Utilities
  * Added section on creating `utils.py`
* Appendix G: Security Settings Reference
  * Added section on Cross Site Request Forgery protection
  * Added mention of secure settings for email
* Changed `helper` module term to `utility` as that is more in line with CS best practices
* Grammar and tyoo fixes
* Link cleanup
* Formatting corrections

## Two Scoops of Django 1.8 Change List Update #3

* Chapter: Model Best Practices
  * Clarified text in figure 6.1, thanks to @gkeller2 (#71)
  * Fixed table 6.3 formatting, thanks to @gkeller2 (#72)
* Chapter: Best Practices for Class-Based Views
  * Indexed the slug field used in queries, thanks to @bogdal (#65)
* Chapter: Form Fundamentals
  * Added `Form.add_error` thanks to @michaeljohnbarr (#64)
  * Added links to the other new and nifty form methods, thanks to @michaeljohnbarr (#70)
* Chapter: REST API
  * Clarified some of the definitions
  * Expanded on the REST API architecture section
  * Added www.cdrf.co because it is awesome. (#73)
  * Added `serializer_class` in DRF sample, thanks to @tomchristie
* Chapter: Asynchronous Task Queues
  * Removed unnecessary column headers from table 25.2, thanks to @jliendo (#68)
  * Removed section on passing in kwargs.
* Chapter: Security
  * Fixed Bad URL to @alex's blog, thanks to @jpadilla (#62)
  * Added UUID to obfuscate primary keys, thanks to @kevinxu and @michaeljohnbarr (#1)
  * Corrected CSRF internal reference to forms chapter, thanks to @kelseyq (#69)
* Chapter: Debugging
  * Fixed ALLOWED_HOSTS. Again. Thanks to @nbensa (#67)
* Appendix G: Security Settings
  * Corrected DEBUG settings, thanks to @phinnaeus (#66)
* Grammar/Spelling, thanks to @cdjk, @patpatpatpatpat, @cpsimpson
* Many small but important formatting changes!

## Two Scoops of Django 1.8 Change List Update #2

* Chapter: Queries and the Database Layer
  * Corrected code example 7.1 thanks to @schinkelg (#56)
* Chapter: Form Fundamentals
  * Added section 11.4 - adding form instance attributes, thanks to @halfnibble and @lambacck (#10).
  * In example 11.5 Changed `# flavors/models.py` to `# flavors/views.py`, thanks to @ksketo (#55)
  * Fixed two links to CSRF docs thanks to @ksketo (#54)
* Chapter: Templates
  * Removed mention of style guide in the context of 404/500 pages, thanks to @ssarj (#58)
* Chapter: Third-Party Packages
  * Fixed broken link to @alex's blog (HTTPS all the things!), thanks to @jpadilla (#62)
* Chapter: Testing
  * Added subsection on using fancier test methods (#34)
* Chapter: Bottlenecks
  * Added mention of `prefetch_related`
* Chapter: Asynchronous Task Queues (NEW), suggested by @abhaga and many others (#36)
  * Is a task queue needed?
  * Choosing task queue software
  * best practices for task queues
  * resources
* Chapter: Continuous Integration
  * Mention code coverage (codecov.io) as a service
* Chapter: Debugging
  * Added subsection on debugging file uploads (#31)
  * In subsection on ALLOWED_HOSTS switched specification of DEBUG=True to DEBUG is False, thanks to @nbensa (#52)
* Appendix A: Packages 
  * Added django-watson, django-reversions, django-background-tasks, flower, and more
* Grammar/Spelling, thanks to @belak, @timbb07, @afuna, @zuhairp, @KTamayo, @cdjk

## Two Scoops of Django 1.8 Change List Update #1

* Chapter: Project Layout
  * Fixed URL to cookiecutters, thanks to @MihailRussu (#47)
* Chapter: Building REST APIs
  * In warning box about simple API lacking permissions, linked to relevant section in DRF documentation.
* Chapter: Tradeoffs Replacing Core Components
  * Added mention of CAP theorem to the fad table, thanks to @vartec
* Chapter: User Model
  * Added `verbose_name` argument to `PositiveIntegerField`.
* Chapter: Third-Party Packages
  * For the purpose of clarity, switched from OSI to choosealicense.com for selecting licenses, thanks to @vartec
* Chapter: Testing
  * Added subsection 22.3.7 on *Testing for Failure*.
  * added section 22.10 for alternatives to `unittest`
    * pytest and pytest-django
    * nose and django-nose
* Chapter: Security
  * Added warning box that static media is not protected by ``SecurityMiddleware``.
  * Added PasswordInput variant suggestion for payment information entered in public venues.
* Chapter: Ask Questions
  * Removed broken link to the defunct planetdjango.org, thanks to @jeanbaptistelab (#46)
* Appendix G: Security Settings Reference (NEW)
  * ALLOWED_HOSTS
  * CSRF_COOKIE_SECURE
  * DEBUG
  * MIDDLEWARE_CLASSES
  * SECRET_KEY
  * SECURE_PROXY_SSL_HEADER
  * SECURE_SSL_HOST
  * SESSION_COOKIE_SECURE
  * SESSION_SERIALIZER
* PDF TOC navbar now have chapter/section numbers, suggested by @gkeller2 (#41)
* Grammar/Spelling, thanks to @PatCurry and @gkeller2 

## Two Scoops of Django 1.8 Early Release Change List

* General:
  * Bumped up version to Django 1.8 everywhere applicable
  * Various grammar mistakes have been corrected
  * Removed references to django.views.defaults.shortcut and django.conf.urls.shortcut
  * Moved lists of tables/figures to the back
  * Longer chapter, section, subsection and box titles now break more aesthetically on their pages.
* Introduction
  * Added clarity to section on Fat Models, Thin Views, Helper functions, and stupid templates
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
* Chapter: Django apps
  * Explained conventions for naming modules
* Chapter: Models
  * Removed South mentions
  * Added content for django.db.migrations
  * Added Postgres fields
  * Recommended against use of generic relations. Truth: Great for the implementor, never ends well for the maintainer. :(
  * Lazy Evaluation!
  * Mentioned _meta
  * Discussed Fat models, how to make them and how to avoid the god class anti-pattern
  * Broke out queries and database interactions into their own chapter
* Chapter: Queries and the Database (NEW)
  * Added database functions
  * Added try/except issues and exceptions to use.
* Chapter: Function- and Class-Based Views
  *  Warned against use of dotted paths in URL definitions
* Chapter: Form Fundamentals (NEW)
  * Moved 'more forms' to be the basics of things to do with forms
  * Now explicitly instructing to use forms for all incoming data
  * Added mention of ModelForms for non-web data
  * Added mention fields without pre-made widgets
  * Moved some material from security chapter to this chapter
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
  * Rate limiting APIs
  * Promoting your API
  * Create SDKs for API integrators
  * Some material on Service Oriented Architecture
* Consuming REST APIs (our kinda JavaScript chapter)
  * Remind the reader that JavaScripty stuff changes too fast.
  * Mention react
  * Switch from Grunt to Gulp
* Chapter: Admin
  * @admin.register decorator
  * Corrected our advice for __str__ or __unicode__.
* Chapter: Third-Party Packages
  * Pointed at Audrey's project release checklist
  * Advocate use of cookiecutter for jumpstarting projects
  * Suggested appveyor for getting Windows users of projects
* Chapter: Testing
  * Tricks for using Request Factory. Like example of request middleware having a session attached.
  * Quick intro to using Mock
  * Described integration tests
* Chapter: Documentation
  * Pandoc for converting long README.md to long README.rst
* Chapter: Bottleneckes
  * Added Silk profiling project
  * Recommended Lincoln Loop's High Performance Django
* Chapter: Security
  * Fix borked security link
  * Additional HSTS warnings
  * More warnings for Session cookies.
  * Mentioned Two-Factor Auth
  * Moved some content to forms chapter
* Chapter: Third Party Packages
  * Refactored how we describe broad version requirements
* Chapter: Utilities
  * Mentioned deprecation and danger of using remove_tags
  * Added awesome-slugify
* Chapter: Deployment
  * Added high level instructions for starting from scratch
  * Really, really don't use mod_python
  * Removed suggested practices for Salt and Ansible. They are out of scope for this book and the content changes too quickly.
* Chapter: Identical Environments
  * Merged into the The Ultimate Django Environment Setup chapter
* Chapter: Continuous Integration
  * Added AppVeyor
* Chapter: Debugging (new)
  * PDB/IPDB
  * Django-debug-toolbar: Just in case it isn't being used yet
  * Reminder about annoying ALLOWED_HOSTS in deployments
  * Common CBV error debugging trick
  * Context processor for debugging (thanks @simonw)
  * feature flags (again thanks @simonw)
* Appendix: Resources
  * Added new stuff
  * Removed stuff that is out of date

Section Header
==============

**emphasis (bold/strong)**

*italics*

Simple link: http://django.2scoops.org
Fancier Link: `Two Scoops of Django`_

.. _Two Scoops of Django: https://django.2scoops.org

Subsection Header
-----------------

#) An enumerated list item

#) Second item

* First bullet

* Second bullet

  * Indented Bullet

  * Note carriage return and indents

Literal code block::

    def like():
        print("I like Ice Cream")

    for i in range(10):
        like()

Python colored code block (requires pygments):

code-block:: python

    # You need to "pip install pygments" to make this work.

    for i in range(10):
        like()

JavaScript colored code block:

code-block:: javascript

    console.log("Don't use alert()");

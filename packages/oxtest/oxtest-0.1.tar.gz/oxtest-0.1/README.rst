Introduction
============

Tools to help create dockerized tests in python.

Tips and Tricks
===============

PhantomJS
---------

PhantomJS is a great selenium driver. There are a few things you may
want to keep in mind:

1. Use
   ``service_args=['--ignore-ssl-errors=true', '--ssl-protocol=any']``
   when creating the driver (e.g.,
   ``driver =  webdriver.PhantomJS(service_args=...)``). This is helpful
   if you are doing tests and do not have proper SSL certificates
   installed.
2. Do something like ``driver.set_page_load_timeout(300)`` if you have
   pages which take a while.
3. Do something like ``driver.maximize_window()`` to make sure the
   window is big enough to "see" the page.
4. Make sure you have at least version 2 or things will be broken.

   -  Installing can be a pain and you may have to do it manually (e.g.,
      see `this
      gist <https://gist.github.com/telbiyski/ec56a92d7114b8631c906c18064ce620>`__).

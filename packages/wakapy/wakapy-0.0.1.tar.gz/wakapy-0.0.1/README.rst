====================
Introduction
====================

Wakapy is a python library aiming for Python 3.6+ versions whose purpose
is to provide easy data manipulation to the developer.

.. note:: 1. This project is not related to `WakaTime <https://wakatime.com/>`_ or its developer team in any way.
          2. This project revolves around the json file that you can download from your **Wakatime account**


Wakapy basically loads the **big** json file containing all of your data provided for free by WakaTime and
group every piece of data in convenient classes. The Wakatime json file is big, a 161 days file, where only 121 days actually
contain relevant data is roughly 75k long (in my case).

Wakapy features:
----------------
1. **Extensive data class containerization**
(Every bit of data from the json file is accessible with the library).

2. **Extra functionalities** added to ease
the data manipulation.

3. **Date slicing**, in other words, you can get the data from a chosen  range,
similar to the Wakatime *paid features*

4. Some nice **charts** out of the box for the people who just want to
get a quick insight of the data without putting too much effort
on it



Quick example:
--------------
Code: ::

    from wakapy import User

    user = User('/home/surister/data.json')
    chart = user.pie_chart('lan')
    # lan = languages. See the different options here.
    chart.show()
    # Shows the chart.
    chart.save('/home/surister/mychart.png')
    # Saves the chart to the desired filepath.


This would output:

.. image:: /docs/source/_static/example1.png

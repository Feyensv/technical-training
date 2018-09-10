# Odoo 12.0 - Technical Training
================================
# Views

## Requirements

* [01. Models, Fields and Relations](https://github.com/odoo/technical-training/tree/12.0-01-models/)
* [02. Computed Fields, Onchange and Constraints](https://github.com/odoo/technical-training/tree/12.0-02-fields/)


## Problem 1: Display Course and Session (OpenAcademy)

We have designed two models Course and Session, we have defined some fields on
them but when we install the module, nothing changes in the Odoo user interface.
It's time to change that.

We will have several courses. This means we need to show a list of all courses,
and a list of all sessions. The user should see the details of each course and
each session in a separate form.

Of course, those features should be available directly once the module is
installed.

- **Technical Hint**: Explore the developer mode. Check for tree views and form
  views. Check for window actions and menu items.

#### Extra Task

* Add a nice icon for the top menu of the Openacademy application in the app switcher.
* Show the percentage of taken seats as a progressbar.



## Resources

### Reference

* [Activate Debug Mode](https://www.odoo.com/documentation/12.0/howtos/web.html#a-simple-module)
* [Data Files](http://www.odoo.com/documentation/12.0/reference/data.html)
* [Menu Items](http://www.odoo.com/documentation/12.0/reference/data.html#menuitem)
* [Action](http://www.odoo.com/documentation/12.0/reference/actions.html)
* [Views](http://www.odoo.com/documentation/12.0/reference/views.html)
* [Fields](http://www.odoo.com/documentation/12.0/reference/orm.html#basic-fields)
* [Online Tutorial](http://www.odoo.com/documentation/12.0/howtos/backend.html#basic-views)
* [Domains](https://www.odoo.com/documentation/12.0/reference/orm.html#domains)

### Code Samples

* [Views](https://github.com/odoo/odoo/blob/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/product/views/product_views.xml)
* [Menu Item](https://github.com/odoo/odoo/blob/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/account/views/account_menuitem.xml)
* [Example of a fancy module description](https://github.com/odoo/odoo/tree/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/account/static/description)
* [CRM tree view ordered](https://github.com/odoo/odoo/blob/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/crm/views/crm_lead_views.xml#L540)
* [Attrs](https://github.com/odoo/odoo/blob/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/hr_recruitment/views/hr_recruitment_views.xml#L412)
* [Use of Options in Views](https://github.com/odoo/odoo/blob/76c443eda331b75bf5dfa7ec22b8eb22e1084343/addons/hr_recruitment/views/hr_recruitment_views.xml#L102)
* [Display float as time](https://github.com/odoo/odoo/blame/fe42986ee2f886527d6cebc702903d039b15f509/addons/calendar/views/calendar_views.xml#L113)

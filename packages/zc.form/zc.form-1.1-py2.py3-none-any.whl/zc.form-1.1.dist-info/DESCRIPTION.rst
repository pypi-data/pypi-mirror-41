The zc.form package is a possibly temporary appendage used to hold extra
browser widgets and alternative approaches to code found in the
zope.formlib package.  Most or all of the code is created by Zope
Corporation and is intended for eventual folding into the main Zope 3
release.


.. contents::

=======
Changes
=======

1.1 (2019-02-11)
----------------

- Fix ZCML configuration issue if the ``[mruwidget]`` extra was not installed.


1.0 (2019-01-11)
----------------

Features
++++++++

- Claim support for Python 3.5, 3.6, 3.7, PyPy and PyPy3.

Bugfixes
++++++++

- Fix a ``NameError`` in ``BaseVocabularyDisplay.render()``.

- Actually pass a ``missing_value`` set on the ``Combination`` field to the
  containing fields.

Caveats
+++++++

- Installation of ``MruSourceInputWidget`` and ``TimeZoneWidget`` requires the
  ``[mruwidget]`` extra to break dependency on ``zc.resourcelibrary`` for
  projects which do not need it.


0.5 (2016-08-02)
----------------

- Bind fields that are contained in a ``zc.form.field.Combination`` to fix the
  ``context`` of those fields.


0.4 (2016-01-12)
----------------

- Get rid of the `zope.app.pagetemplate` dependency.


0.3 (2014-04-23)
----------------

- Remove requirement, that ``zc.form.field.Combination`` needs at least
  two subfields.


0.2 (2011-09-24)
----------------

- Got rid of ``zope.app.form`` dependency by requiring at least
  ``zope.formlib`` 4.0.

- Got rid of ``zope.app.component`` dependency by requiring at least
  ``zope.component`` 3.8.

- Depending on ``zope.catalog`` instead of ``zope.app.catalog``.

- Depending on ``zope.security`` instead of ``zope.app.security``.

- Depending on ``zope.app.wsgi`` >=3.7 instead of ``zope.app.testing`` for
  test setup.

- Depending on ``zope.browserpage`` and ``zope.container`` instead of
  ``zope.app.publisher``.

- Got rid of the following dependencies:

  - ``zope.app.basicskin``
  - ``zope.app.securitypolicy``
  - ``zope.app.zapi``
  - ``zope.app.zcmlfiles``

- Fixed tests to run with ``zope.schema`` >= 3.6.

- Made package fit to run on ZTK 1.1.

- Moved test dependencies to `test` extra.

- Using Python's ``doctest`` module instead of deprecated
  ``zope.testing.doctest``.


0.1
---

- Exception views are now unicode aware. They used to break on translated
  content.

- Added use_default_for_not_selected to Union field to use default
  value even if sub field is not selected.


===================
 CombinationWidget
===================

The combinationwidget collects two or more subfields to provide a convenient
way to specify a sequence of values.

Rendering the widget returns a table with the subfields::

    >>> from zc.form.browser.combinationwidget import (
    ...     CombinationWidget, CombinationDisplayWidget, default_template)
    >>> from zope import component, interface
    >>> component.provideAdapter(default_template, name='default')
    >>> from zc.form.field import Combination, OrderedCombinationConstraint
    >>> from zope.schema import Int
    >>> from zope.schema.interfaces import IInt
    >>> from zope.publisher.interfaces.browser import IBrowserRequest
    >>> from zope.formlib.interfaces import IInputWidget
    >>> from zope.formlib.textwidgets import IntWidget
    >>> component.provideAdapter(
    ...     IntWidget, (IInt, IBrowserRequest), IInputWidget)
    >>> from zope import interface
    >>> class IDemo(interface.Interface):
    ...     acceptable_count = Combination(
    ...         (Int(title=u'Minimum', required=True, min=0),
    ...          Int(title=u'Maximum', required=False)),
    ...         title=u'Acceptable Count',
    ...         required=False,
    ...         constraints=(OrderedCombinationConstraint(),))
    ...
    >>> from zope.publisher.browser import TestRequest
    >>> request = TestRequest()
    >>> widget = CombinationWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.loadValueFromRequest() # None
    >>> print(widget())
    <input type='hidden' name='field.acceptable_count-marker' value='x' />
    <table class="combinationFieldWidget">
      <tr>
        <td class="label">
          <label for="field.acceptable_count.combination_00">
            <span class="required">*</span><span>Minimum</span>
          </label>
        </td>
        <td class="field">
          <div class="widget"><input class="textType"
            id="field.acceptable_count.combination_00"
            name="field.acceptable_count.combination_00" size="10" type="text"
            value=""  />
          </div>
        </td>
      </tr>
      <tr>
        <td class="label">
          <label for="field.acceptable_count.combination_01">
            <span>Maximum</span>
          </label>
        </td>
        <td class="field">
          <div class="widget"><input class="textType"
            id="field.acceptable_count.combination_01"
            name="field.acceptable_count.combination_01" size="10" type="text"
            value=""  />
          </div>
        </td>
      </tr>
    </table>

Setting the appropriate values in the Request lets the widget correctly read
the specified value::

    >>> request.form['field.acceptable_count-marker'] = 'x'
    >>> request.form['field.acceptable_count.combination_00'] = '10'
    >>> request.form['field.acceptable_count.combination_01'] = ''
    >>> widget = CombinationWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.getInputValue()
    (10, None)
    >>> print(widget())
    <...
    ...<input class="textType" id="field.acceptable_count.combination_00"
              name="field.acceptable_count.combination_00" size="10" type="text"
              value="10" />...
    ...<input class="textType" id="field.acceptable_count.combination_01"
              name="field.acceptable_count.combination_01" size="10" type="text"
              value="" />...


The field is fine with empty values, because it is not required::

    >>> request.form['field.acceptable_count-marker'] = 'x'
    >>> request.form['field.acceptable_count.combination_00'] = ''
    >>> request.form['field.acceptable_count.combination_01'] = ''
    >>> widget = CombinationWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.getInputValue() # None
    >>> print(widget())
    <...
    ...<input class="textType" id="field.acceptable_count.combination_00"
              name="field.acceptable_count.combination_00" size="10" type="text"
              value="" />...
    ...<input class="textType" id="field.acceptable_count.combination_01"
              name="field.acceptable_count.combination_01" size="10" type="text"
              value="" />...
    >>> bool(widget.error())
    False
    >>> bool(widget.widgets[0].error())
    False

If the optional value is filled in and the required one is not, though, there
are errors::

    >>> request.form['field.acceptable_count-marker'] = 'x'
    >>> request.form['field.acceptable_count.combination_00'] = ''
    >>> request.form['field.acceptable_count.combination_01'] = '10'
    >>> widget = CombinationWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.getInputValue()
    Traceback (most recent call last):
    WidgetInputError: ('acceptable_count', u'Acceptable Count',
    WidgetInputError('combination_00', u'Minimum',
    RequiredMissing('combination_00')))
    >>> import zope.formlib.interfaces
    >>> import zope.publisher.interfaces.browser
    >>> @interface.implementer(zope.formlib.interfaces.IWidgetInputErrorView)
    ... @component.adapter(zope.formlib.interfaces.WidgetInputError,
    ...     zope.publisher.interfaces.browser.IBrowserRequest)
    ... class SnippetView(object):
    ...
    ...     def __init__(self, context, request):
    ...         self.context = context
    ...         self.request = request
    ...     def snippet(self):
    ...         return self.context.doc()
    ...
    >>> component.provideAdapter(SnippetView)
    >>> print(widget())
    <...
    ...<input class="textType" id="field.acceptable_count.combination_00"
              name="field.acceptable_count.combination_00" size="10"
              type="text" value="" />...
    ...Required input is missing...
    ...<input class="textType" id="field.acceptable_count.combination_01"
              name="field.acceptable_count.combination_01" size="10"
              type="text" value="10" />...
    >>> print(widget.error())
    Required input is missing.
    >>> print(widget.widgets[0].error())
    Required input is missing.

Similarly, if the field's constraints are not met, the widget shows errors::

    >>> request.form['field.acceptable_count-marker'] = 'x'
    >>> request.form['field.acceptable_count.combination_00'] = '20'
    >>> request.form['field.acceptable_count.combination_01'] = '10'
    >>> widget = CombinationWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.getInputValue()
    Traceback (most recent call last):
    WidgetInputError: ('acceptable_count', u'Acceptable Count',
    MessageValidationError(u'${minimum} ...
    >>> print(widget())
    <...
    ...input class="textType" id="field.acceptable_count.combination_00"
              name="field.acceptable_count.combination_00" size="10"
              type="text" value="20" />...
    ...<input class="textType" id="field.acceptable_count.combination_01"
              name="field.acceptable_count.combination_01" size="10"
              type="text" value="10" />...
    >>> print(widget.error())
    ${minimum} must be less than or equal to ${maximum}.


There's also a display version of the widget::

    >>> request = TestRequest()
    >>> from zope.formlib.widget import DisplayWidget
    >>> from zope.formlib.interfaces import IDisplayWidget
    >>> component.provideAdapter(
    ...     DisplayWidget, (IInt, IBrowserRequest), IDisplayWidget)
    >>> widget = CombinationDisplayWidget(IDemo['acceptable_count'], request)
    >>> widget.setPrefix('field')
    >>> widget.setRenderedValue(('10', '2'))
    >>> print(widget())
    <input type='hidden' name='field.acceptable_count-marker' value='x' />
        <table class="combinationFieldWidget">
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_00">
                      <span>Minimum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">10
                </div>
              </td>
          </tr>
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_01">
                      <span>Maximum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">2
                </div>
              </td>
          </tr>
        </table>

In case of a wrong amount of parameters, the missing_value is used::

    >>> field = IDemo['acceptable_count']
    >>> field.missing_value=('23', '42')
    >>> widget = CombinationDisplayWidget(field, request)
    >>> widget.setPrefix('field')
    >>> widget.setRenderedValue(('10', '2', '3'))
    >>> print(widget())
    <input type='hidden' name='field.acceptable_count-marker' value='x' />
        <table class="combinationFieldWidget">
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_00">
                      <span>Minimum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">23
                </div>
              </td>
          </tr>
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_01">
                      <span>Maximum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">42
                </div>
              </td>
          </tr>
        </table>

In case the parameter is not a sequence, the missing_value is used::

    >>> widget = CombinationDisplayWidget(field, request)
    >>> widget.setPrefix('field')
    >>> widget.setRenderedValue(10)
    >>> print(widget())
    <input type='hidden' name='field.acceptable_count-marker' value='x' />
        <table class="combinationFieldWidget">
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_00">
                      <span>Minimum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">23
                </div>
              </td>
          </tr>
          <tr>
                  <td class="label">
                    <label for="field.acceptable_count.combination_01">
                      <span>Maximum</span>
                    </label>
                  </td>
              <td class="field">
                <div class="widget">42
                </div>
              </td>
          </tr>
        </table>

The order of label and field are inverted in case of boolean::

    >>> request = TestRequest()
    >>> from zope.schema import Bool
    >>> from zope.schema.interfaces import IBool
    >>> from zope.formlib.boolwidgets import CheckBoxWidget
    >>> from zope.formlib.widget import DisplayWidget
    >>> from zope.formlib.interfaces import IDisplayWidget
    >>> component.provideAdapter(
    ...     CheckBoxWidget, (IBool, IBrowserRequest), IInputWidget)
    >>> class IBoolDemo(interface.Interface):
    ...     choices = Combination(
    ...         (Bool(title=u'first'),
    ...          Bool(title=u'second')),
    ...         title=u'Choices',
    ...         required=False,)

    >>> widget = CombinationWidget(IBoolDemo['choices'], request)
    >>> widget.setPrefix('field')
    >>> print(widget())
    <input type='hidden' name='field.choices-marker' value='x' />
        <table class="combinationFieldWidget">
          <tr>
                <td></td>
              <td class="field">
                <div class="widget"><input class="hiddenType" id="field.choices.combination_00.used" name="field.choices.combination_00.used" type="hidden" value="" /> <input class="checkboxType" id="field.choices.combination_00" name="field.choices.combination_00" type="checkbox" value="on"  />
                  <span>first</span>
                </div>
              </td>
          </tr>
          <tr>
                <td></td>
              <td class="field">
                <div class="widget"><input class="hiddenType" id="field.choices.combination_01.used" name="field.choices.combination_01.used" type="hidden" value="" /> <input class="checkboxType" id="field.choices.combination_01" name="field.choices.combination_01" type="checkbox" value="on"  />
                  <span>second</span>
                </div>
              </td>
          </tr>
        </table>



========================================
 Most Recently Used (MRU) Source Widget
========================================

The MRU widget keeps track of the last few values selected (on a per-principal
basis) and allows quickly selecting from that list instead of using a query
interface.

We can see the widget in action by using a custom form.  Let's define a schema
for the form that uses a source::

    >>> import zope.interface
    >>> import zope.schema

    >>> class IDemo(zope.interface.Interface):
    ...
    ...     color = zope.schema.Choice(
    ...         title=u"Color",
    ...         description=u"My favorite color",
    ...         source=AvailableColors,
    ...         )

And then a class that implements the interface::

    >>> @zope.interface.implementer(IDemo)
    ... class Demo(object):
    ...
    ...     color = None

We'll need a form that uses this schema::

    >>> import zope.formlib.form

    >>> class DemoInput(zope.formlib.form.EditForm):
    ...     actions = ()
    ...     form_fields = zope.formlib.form.fields(IDemo)

By rendering the form we can see that there are no MRU items to choose from
(because this principal has never visited this form before) and the query
interface is displayed::

    >>> import zope.publisher.browser
    >>> import zope.security.interfaces
    >>> import zope.security.management
    >>> import zope.component.hooks

    >>> @zope.interface.implementer(zope.security.interfaces.IPrincipal)
    ... class DummyPrincipal(object):
    ...
    ...     id = "someuser"
    ...     title = "Some User's Name"
    ...     description = "A User"

Note that we need to use the special resourcelibrary request.  We're
hacking together the TestRequest and the resourcelibrary request here; when we
switch to TestBrowser we can remove this oddity.

    >>> import zc.resourcelibrary.publication
    >>> class TestRequest(zope.publisher.browser.TestRequest,
    ...                   zc.resourcelibrary.publication.Request):
    ...     def _createResponse(self):
    ...         return zc.resourcelibrary.publication.Request._createResponse(
    ...             self)
    ...

    >>> request = TestRequest()
    >>> principal = DummyPrincipal()
    >>> request.setPrincipal(principal)
    >>> zope.security.management.newInteraction(request)

    >>> oldsite = zope.component.hooks.getSite()
    >>> zope.component.hooks.setSite(getRootFolder())

Now we can use an instance of our demo object to see that the form
pulls the possible values from the vocabulary we've defined above::

    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <div class="queries"...>
    <div class="query"...>
      <div class="queryinput"...>
        <query view for colors>
      </div> <!-- queryinput -->
    </div> <!-- query -->
    </div> <!-- queries -->
    ...

Note that the select box of MRU values isn't in the output, because the user
has never selected a value before::

    >>> '<select name="form.color">' not in form()
    True

Now, we can select one of the values::

    >>> zope.security.management.endInteraction()

    >>> request = TestRequest()
    >>> request.form = {
    ...     'form.color.query.selection': 'red_token',
    ...     'form.color.query.apply': 'Apply',
    ...     'form.color.displayed': '',
    ...     }
    >>> request.setPrincipal(principal)

    >>> zope.security.management.newInteraction(request)

Process the request and the list of MRU values is in the form::

    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="red_token" selected="selected">Red</option>
    </select>
    ...

And the query view is hidden because we have an MRU list::

    >>> print(form())
    <...
    <input type="hidden" name="form.color.queries.visible" ... value="no">
    ...

If we select another value...::

    >>> request = TestRequest()
    >>> request.form = {
    ...     'form.color.query.selection': 'green_token',
    ...     'form.color.query.apply': 'Apply',
    ...     'form.color.displayed': '',
    ...     }
    >>> request.setPrincipal(principal)

...and process the request, the list of MRU values includes the new one, at
the top, and it is selected::

    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="green_token" selected="selected">Green</option>
      <option value="red_token">Red</option>
    </select>
    ...

If we request a value not in the source everything stays the same, but nothing
is selected::

    >>> request = TestRequest()
    >>> request.form = {
    ...     'form.color.query.selection': 'blue_token',
    ...     'form.color.query.apply': 'Apply',
    ...     'form.color.displayed': '',
    ...     }
    >>> request.setPrincipal(principal)
    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="green_token">Green</option>
      <option value="red_token">Red</option>
    </select>
    ...

We can make the query visible::

    >>> request = TestRequest()
    >>> request.form = {
    ...     'form.color.query.selection': 'red_token',
    ...     'form.color.query.apply': 'Apply',
    ...     'form.color.queries.visible': 'yes',
    ...     'form.color.query.search': 'yes',
    ...     'form.color.query.searchstring': 'red',
    ...     'form.color.displayed': '',
    ...     }
    >>> request.setPrincipal(principal)
    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="red_token" selected="selected">Red</option>
      <option value="green_token">Green</option>
    </select>
    ...
    <select name="form.color.query.selection">
    <option value="red_token">Red</option>
    </select>
    <input type="submit" name="form.color.query.apply" value="Apply" />
    ...

It is not shown if the query is not applied::

    >>> request = TestRequest()
    >>> request.form = {
    ...     'form.color.query.selection': 'red_token',
    ...     'form.color.queries.visible': 'yes',
    ...     'form.color.query.search': 'yes',
    ...     'form.color.query.searchstring': 'red',
    ...     'form.color.displayed': '',
    ...     }
    >>> request.setPrincipal(principal)
    >>> form = DemoInput(Demo(), request)
    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="red_token">Red</option>
      <option value="green_token">Green</option>
    </select>
    ...
    <select name="form.color.query.selection">
    <option value="red_token">Red</option>
    </select>
    <input type="submit" name="form.color.query.apply" value="Apply" />
    ...

Tokens in the annotation of the principal are ignored if they are not in the
source::

    >>> from zope.annotation.interfaces import IAnnotations
    >>> annotations = IAnnotations(principal)
    >>> annotation = annotations.get('zc.form.browser.mruwidget')
    >>> tokens = annotation.get('form.color')
    >>> tokens.append('black_token')
    >>> tokens
    ['red_token', 'green_token', 'black_token']

    >>> print(form())
    <...
    <select name="form.color" id="form.color">
      <option value="red_token">Red</option>
      <option value="green_token">Green</option>
    </select>
    ...
    <select name="form.color.query.selection">
    <option value="red_token">Red</option>
    </select>
    <input type="submit" name="form.color.query.apply" value="Apply" />
    ...


Clean up a bit::

    >>> zope.security.management.endInteraction()
    >>> zope.component.hooks.setSite(oldsite)



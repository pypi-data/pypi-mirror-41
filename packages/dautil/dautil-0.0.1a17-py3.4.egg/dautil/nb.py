""" IPython/Jupyter notebook widgets and utilities. """
from IPython.display import display
from IPython.display import Math
from IPython.html import widgets
from dautil import collect
from dautil import conf
from dautil import ts
from dautil import log_api
import matplotlib as mpl
from matplotlib.colors import rgb2hex
import pprint
from matplotlib.colors import ColorConverter


def create_month_widget(month, *args, **kwargs):
    """ Creates a dropdown wiget with short month names
    as labels.

    :param: month: The month to select by default.

    :returns: The configured month widget.
    """
    return widgets.Dropdown(options=ts.short_months(),
                            selected_label=month, *args, **kwargs)



class WidgetFactory():
    def __init__(self, rcw):
        self.rc_widget = rcw

    # TODO allow ‘rgbcmykw’
    # TODO allow standard names like 'aqua'
    def color_chooser(self, property):
        """ Creates a box with widgets related to choosing a color.

        :param: property: A color related key in matplotlib.rcParams.

        :returns: A box with widgets.
        """
        cc = ColorConverter()
        rgb = cc.to_rgb(mpl.rcParams[property])
        logger = log_api.env_logger()
        logger.debug('{0} {1}'.format(property, rgb))

        r = widgets.FloatSlider(min=0, max=1, value=rgb[0], description='Red')
        r.border_color = 'red'

        g = widgets.FloatSlider(min=0, max=1, value=rgb[1],
                                description='Green')
        g.border_color = 'green'

        b = widgets.FloatSlider(min=0, max=1, value=rgb[2], description='Blue')
        b.border_color = 'blue'

        h = widgets.widget_string.HTML(property)
        # TODO put this in a func
        hex = rgb2hex((rgb[0], rgb[1], rgb[2]))
        h.value = '<p style="background-color: {0};">{0}</p>'.format(hex)

        def update(name, value):
            hex = rgb2hex((r.value, g.value, b.value))
            h.value = '<p style="background-color: {0};">{0}</p>'.format(hex)
            self.rc_widget.process(property, hex)

        r.on_trait_change(update, 'value')
        g.on_trait_change(update, 'value')
        b.on_trait_change(update, 'value')

        box = widgets.VBox(children=(r, g, b, h))
        box.border_style = 'dotted'
        box.description = property

        return box


# TODO mix DIY widgets with WidgetFactory calls
class RcWidget():
    """ This widget configures the
    matplotlib.rcParams global settings. """
    def __init__(self, context=None):
        self.context = context
        self.factory = WidgetFactory(self)

        if self.context:
            rc = self.context.read_rc()

            if rc:
                mpl.rcParams.update(rc)

        self.old = mpl.rcParams.copy()

        tab = widgets.Tab(children=[self.axes_page(), self.figure_page(),
                                    self.font_page(), self.grid_page(),
                                    self.lines_page()])
        tab.set_title(0, 'Axes')
        tab.set_title(1, 'Figure')
        tab.set_title(2, 'Font')
        tab.set_title(3, 'Grid')
        tab.set_title(4, 'Lines')
        display(tab)

        self.updates_text = widgets.HTML()
        display(self.updates_text)

        self.params_text = widgets.HTML()
        display(self.params_text)

        self.show_params = widgets.widget_button.Button()
        self.show_params.description = 'Show rcParams'
        self.show_params.on_click(self.print_params)
        display(self.show_params)

    def print_params(self, button_instance):
        """ Prints the current matplotlib.rcParams in a textarea.

        :param: button_instance: The button to click on.
        """
        html = '<textarea rows="5" cols="50" readonly>{}</textarea>'
        self.params_text.value = html.format(pprint.pformat(mpl.rcParams))

    def process(self, param, value):
        """ Processes changes to the GUI and updates matplotlib.rcParams.

        :param: param: A key in the matplotlib.rcParams dictionary.
        :param: value: A value in the matplotlib.rcParams dictionary.
        """
        logger = log_api.env_logger()
        logger.debug('name={0}, value={1}'.format(param, value))
        self.params_text.value = ''
        mpl.rcParams[param] = value
        updates = collect.dict_updates(self.old, mpl.rcParams)

        if self.context:
            self.context.update_rc(updates)

        self.updates_text.value = ('<p>mpl.RcParams updates {}</p>'.
                                   format(updates))

    def axes_page(self):
        """ Creates a tab page for the matplotlib.rcParams
        keys which start with axes."""
        box = widgets.Accordion()
        linewidth = create_linewidth_slider('axes.linewidth')

        edgecolor = self.factory.color_chooser('axes.edgecolor')
        titlesize = create_size_slider('axes.titlesize')

        box.children = [edgecolor, linewidth, titlesize]
        box.set_title(0, edgecolor.description)
        box.set_title(1, linewidth.description)
        box.set_title(2, titlesize.description)

        def update_axes_linewidth(name, value):
            self.process(linewidth.description, value)

        def update_titlesize(name, value):
            self.process(titlesize.description, value)

        linewidth.on_trait_change(update_axes_linewidth, 'value')
        titlesize.on_trait_change(update_titlesize, 'value')

        return box

    def font_page(self):
        """ Creates a tab page for the matplotlib.rcParams
        keys which start with font."""
        box = widgets.Accordion()
        size = create_size_slider('font.size')
        box.children = [size]

        def update_font_size(name, value):
            self.process(size.description, value)

        size.on_trait_change(update_font_size, 'value')

        return box

    def figure_page(self):
        """ Creates a tab page for the matplotlib.rcParams
        keys which start with figure."""
        box = widgets.VBox()
        box.description = 'figure.figsize'
        height = widgets.FloatSlider(min=0, max=16,
                                     value=mpl.rcParams[box.description][0],
                                     description='Height')
        width = widgets.FloatSlider(
            min=0, max=12, value=mpl.rcParams[box.description][1],
            description='Width')
        box.children = [height, width]

        def update_fig_size(name, value):
            self.process(box.description, (height.value, width.value))

        height.on_trait_change(update_fig_size, 'value')
        width.on_trait_change(update_fig_size, 'value')

        return box

    def grid_page(self):
        """ Creates a tab page for the matplotlib.rcParams
        keys which start with grid."""
        logger = log_api.env_logger()
        logger.debug('Created grid page')
        linewidth = create_linewidth_slider('grid.linewidth')

        color = self.factory.color_chooser('grid.color')
        box = widgets.Accordion(children=[linewidth, color])
        box.set_title(0, linewidth.description)
        box.set_title(1, color.description)

        def update_linewidth(name, value):
            self.process(linewidth.description, value)

        linewidth.on_trait_change(update_linewidth, 'value')

        return box

    def lines_page(self):
        """ Creates a tab page for the matplotlib.rcParams
        keys which start with lines."""
        linewidth = create_linewidth_slider('lines.linewidth')
        box = widgets.Accordion(children=[linewidth])
        box.set_title(0, linewidth.description)

        def update_linewidth(name, value):
            self.process(linewidth.description, value)

        linewidth.on_trait_change(update_linewidth, 'value')

        return box


def create_linewidth_slider(desc, *args, **kwargs):
    """ Creates a slider for linewidth-type settings
    in matplotlib.rcParams.

    :param: desc: The description label of the widget.

    :returns: The configured slider.
    """
    from_rc = mpl.rcParams[desc]

    val = 0

    # TODO deal with strings
    if not isinstance(from_rc, str):
        val = from_rc

    return widgets.IntSlider(min=0, max=9, value=val,
                             description=desc, *args, **kwargs)


def create_size_slider(desc, *args, **kwargs):
    """ Creates a slider for size-type settings
    in matplotlib.rcParams.

    :param: desc: The description label of the widget.

    :returns: The configured slider.
    """
    from_rc = mpl.rcParams[desc]

    val = 0

    # TODO deal with strings
    if not isinstance(from_rc, str):
        val = from_rc

    return widgets.FloatSlider(min=0, value=val,
                               description=desc, *args, **kwargs)


class LatexRenderer():
    """ Utiliity class which helps number and render Latex
    in a IPython/Jupyter notebook. """
    def __init__(self, chapter=None, start=1, context=None):
        self.chapter = chapter
        self.curr = start
        self.numbers = []
        self.context = context

        if self.context:
            from_context = self.context.read_latex()

            if from_context:
                log_api.Printer().print(from_context)
                eqn_list = list(from_context.values())
                assert not start in collect.flatten(eqn_list), from_context

    # DIY numbering because IPython doesn't
    # support numbering
    def number_equation(self):
        """ Creates a Latex string relating
        to the numbering of equations.

        :returns: A Later string with the correct equation number.
        """
        number = '('

        if self.chapter:
            number += str(self.chapter) + '.'

        number += str(self.curr) + ')\hspace{1cm}'

        return number

    def render(self, equation):
        """ Renders an equation.

        :param: equation: A string containing the equation.
        """
        number = self.number_equation()
        self.numbers.append(self.curr)
        logger = log_api.env_logger()

        if self.context:
            logger.debug(self.numbers)
            self.context.update_latex(self.numbers)

        display(Math(r'%s' % (number + equation)))
        self.curr += 1


# TODO store key/id information in sql lite db in CONF_DIR
# with key mnemonic, creation time etc
class Context():
    """ A mediator for the storing and retrieving
    of configuration settings. """
    def __init__(self, fname):
        self.fname = fname
        self.labels = fname + '.labels'
        self.latex = fname + '.latex'

    def read_rc(self):
        """ Reads the current configuration
        settings related to matplotlib.rcParams,
        which are used by RcWidget.

        :returns: The current configuration settings or
        an empty dict.
        """
        config = conf.read_rc()

        if config:
            config = config.get(self.fname, {})

        return config

    def update_rc(self, updates):
        """ Updates the configuration settings related to
        matplotlib.rcParams used by RcWidget.

        :param: updates: Changes to the configuration.
        """
        conf.update_rc(self.fname, updates)

    def read_labels(self):
        """ Reads the current configuration settings related
        to the matplotlib.rcParams used by LabelWidget.

        :returns: The current configuration settings\
        or None if no settings are found.
        """
        config = conf.read_rc()

        if config:
            config = config.get(self.labels, None)

        return config

    def update_labels(self, updates):
        """ Updates the configuration settings related to
        matplotlib.rcParams used by LabelWidget.

        :param: updates: Changes to the configuration.
        """
        conf.update_rc(self.labels, updates)

    def read_latex(self):
        """ Reads the current configuration settings related
        to the LatexRenderer.

        :returns: The current configuration settings\
        or None if no settings are found.
        """
        config = conf.read_rc()

        if config:
             keys = collect.filter_dict_keys(lambda x: x.endswith('.latex'),
                                             config)
             config = collect.dict_from_keys(config, keys)
             config.pop(self.latex, None)

        return config

    def update_latex(self, updates):
        """ Updates the configuration settings related to
        LatexRenderer.

        :param: updates: Changes to the configuration.
        """
        conf.update_rc(self.latex, updates)


class LabelWidget():
    """ A widget you can use to easily fill
    in strings for titles, xlabels and ylabels
    of matplotlib subplots. """
    def __init__(self, nrows, ncols, context):
        assert not context is None, 'Define context'
        self.context = context
        self.labels = collect.GridList(nrows, ncols, {})
        self.read_old_labels()

        for i in range(nrows):
            children = []

            for j in range(ncols):
                labels_box = self.create_mpl_labels_box(i, j,
                                                        self.labels.grid[i][j])
                children.append(labels_box)

            display(widgets.HBox(children=children))
            display(widgets.HTML('<br/>'))

    def read_old_labels(self):
        """ Reads the labels from a configuration file. """
        old = self.context.read_labels()

        if old:
            self.labels.fill(old)

    def update(self, name, value, row, col):
        """ Updates an internal data structure and
        related configuration file.

        :param: name: title, xlabel, legend or ylabel.
        :param: value: A string representing a label.
        If needed use curly braces as used by the Python
        format() string method.
        """
        self.labels.update(row, col, {name: value})
        self.context.update_labels(self.labels.grid)

    def create_mpl_labels_box(self, row, col, old):
        """ Creates a box with the widgets for a single
        subplot (cell).

        :param: row: The row number of the subplot.
        :param: col: The column number of the subplot.
        :param: old: The setting for this subplot from a configuration file.

        :returns: The box with widgets.
        """
        box = widgets.VBox()
        box.border_color = 'red'
        coord = ' [{0}][{1}]'.format(row, col)
        title = widgets.widget_string.Text(old.get('title', ''),
                                           description='title' + coord)
        xlabel = widgets.widget_string.Text(old.get('xlabel', ''),
                                            description='xlabel' + coord)
        ylabel = widgets.widget_string.Text(old.get('ylabel', ''),
                                            description='ylabel' + coord)
        legend = widgets.Dropdown(options=['No Legend', 'loc=best',
                                           'loc=upper right',
                                           'loc=upper left'],
                                  selected_label=old.get('legend',
                                                         'No Legend'))
        box.children = [title, xlabel, ylabel, legend]

        def update_title(name, value):
            self.update('title', value, row, col)

        title.on_trait_change(update_title, 'value')

        def update_xlabel(name, value):
            self.update('xlabel', value, row, col)

        xlabel.on_trait_change(update_xlabel, 'value')

        def update_ylabel(name, value):
            self.update('ylabel', value, row, col)

        ylabel.on_trait_change(update_ylabel, 'value')

        def update_legend(name, value):
            self.update('legend', value, row, col)

        legend.on_trait_change(update_legend, 'value')

        return box

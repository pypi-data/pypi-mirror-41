""" This module contains plotting utilities. """
from itertools import cycle
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt
import numpy as np
from dautil import collect


def plot_polyfit(ax, x, y, degree=1):
    """ Plots a polynomial fit.

    :param: ax: A matplotlib SubplotAxes object.
    :param: x: An array of 'x' values.
    :param: y: An array of 'y' values.
    :param: degree: The polynomial degree.
    """
    poly = np.polyfit(x, y, degree)

    ax.plot(x, np.polyval(poly, x), label='Fit')


def scatter_with_bar(ax, bar_label, *args, **kwargs):
    """ Creates a matplotlib scatter plot with a colorbar.

    :param: ax: A matplotlib SubplotAxes.
    :param: bar_label: The label of the colorbar.
    """
    sc = ax.scatter(*args, **kwargs)
    plt.colorbar(sc, ax=ax, label=bar_label)


def sample_cmap(name='Reds', start=0.1, end=0.9, ncolors=9):
    """ Samples a matplotlib color map
    using a linearly spaced range.

    :param: name: Name of the color map.
    :param: start: Start of the linear range.
    :param: end: End of the linear range.
    :param: ncolors: The number of colors in the range.

    :returns: A sample of the color map.
    """
    cmap = plt.cm.get_cmap(name)

    return cmap(np.linspace(start, end, ncolors))


def sample_hex_cmap(name='Reds', start=0.1, end=0.9, ncolors=9):
    """ Samples a matplotlib color map
    using a linearly spaced range and
    return hex values for the colors.

    :param: name: Name of the color map.
    :param: start: Start of the linear range.
    :param: end: End of the linear range.
    :param: ncolors: The number of colors in the range.

    :returns: A list of hex values from a sample of the color map.
    """
    cmap = sample_cmap(name, start, end, ncolors)

    return [rgb2hex(c) for c in cmap]


def embellish(axes, legends=None):
    """ Adds grid and legends to matplotlib plots.

    :param: axes: Axes as returned by the plt.subplots() function.
    :param: legends: A list of indices of subplots, which need a legend.
    """
    for i, ax in enumerate(axes):
        ax.grid(True)

        if legends is None:
            ax.legend(loc='best')
        elif i in legends:
            ax.legend(loc='best')


def hide_axes(axes):
    """ Hides the x-axis and y-axis of
    matplotlib plots.

    :param: axes: Axes as returned by the plt.subplots() function.
    """
    flat_axes = axes

    if len(axes) > 0:
        flat_axes = axes.ravel()

    for ax in flat_axes:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)


class Cycler():
    """ Utility class, which cycle through values of
    plotting related lists. """
    def __init__(self, styles=["-", "--", "-.", ":"], lw=[1, 2]):
        self.STYLES = cycle(styles)
        self.LW = cycle(lw)
        self.colors = cycle(sample_hex_cmap(name='hot'))

    def style(self):
        """ Cycles through a list of line styles. """
        return next(self.STYLES)

    def lw(self):
        """ Cycles through a list of linewidth values. """
        return next(self.LW)

    def color(self):
        """ Cycles through a list of colors. """
        return next(self.colors)


class CyclePlotter():
    """ A plotter which cycles through different linestyle
    and linewidth values. """
    def __init__(self, ax):
        self.ax = ax
        self.cycler = Cycler()

    def plot(self, x, y, *args, **kwargs):
        """ A facade for the matplotlib plot() method.

        :param: x: Array of 'x' values for the plot.
        :param: y: Array of 'y' values for the plot.
        """
        self.ax.plot(x, y, self.cycler.style(),
                     lw=self.cycler.lw(), *args, **kwargs)


class Subplotter():
    """ A utility to help with subplotting. """
    def __init__(self, nrows=1, ncols=1, context=None):
        self.context = context
        self.old = None
        self.index = -1

        if context:
            self.old = self.context.read_labels()

            if self.old:
                self.old = collect.flatten(self.old)

        # TODO turn off squeeze
        self.fig, self.axes = plt.subplots(nrows, ncols)

        if nrows > 1 and ncols > 1:
            self.axes = collect.flatten(self.axes)

        if nrows == 1 and ncols == 1:
            self.ax = self.axes
            self.index = 0
        else:
            self.ax_iter = iter(self.axes)
            self.next_ax()

    def next_ax(self):
        """ Advance to next subplot.

        :returns: The current subplot after advancing.
        """
        self.index += 1

        self.ax = next(self.ax_iter)

        return self.ax

    def get_string(self, old, key, params):
        """ Gets a string used to label x-axis,
        y-axis or title of a subplot.

        :param: old: Configuration setting from a file.
        :param: key: title, xlabel, legend or ylabel.
        :param: params: Extra params provided for the
        Python string format() method. We expect the
        appropriate use of curly braces.

        :returns: A (formatted) string for the x-axis,
        y-axis, legend or title of a subplot.
        """
        astr = old.get(key, '')

        if params:
            if isinstance(params, str):
                astr = astr.format(params)
            else:
                astr = astr.format(*params)

        return astr

    def label(self, advance=False, title_params=None,
              xlabel_params=None, ylabel_params=None):
        """ Labels the subplot.

        :param: advance: Boolean indicating whether to move \
            to the next subplot.
        :param: title_params: Optional title parameters.
        :param: xlabel_params: Optional xlabel parameters.
        :param: ylabel_params: Optional ylabel parameters.
        """
        if advance:
            self.next_ax()

        # Cowardly refusing to continue
        if self.old is None:
            return

        old = self.old[self.index]

        title = self.get_string(old, 'title', title_params)

        if title:
            self.ax.set_title(title)

        xlabel = self.get_string(old, 'xlabel', xlabel_params)

        if xlabel:
            self.ax.set_xlabel(xlabel)

        ylabel = self.get_string(old, 'ylabel', ylabel_params)

        if ylabel:
            self.ax.set_ylabel(ylabel)

        legend = self.get_string(old, 'legend', None)

        if legend.startswith('loc='):
            self.ax.legend(loc=legend.replace('loc=', ''))

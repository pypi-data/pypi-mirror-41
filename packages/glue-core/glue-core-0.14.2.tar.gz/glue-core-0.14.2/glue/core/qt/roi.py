from __future__ import absolute_import, division, print_function

import numpy as np

from qtpy.QtCore import Qt
from qtpy import QtCore, QtGui

from glue.core import roi as _roi
from glue.utils.qt import mpl_to_qt_color


class QtROI(object):

    """
    A mixin class used to override the drawing methods used by
    the MPL ROIs in core.roi. Paints to the Widget directly,
    avoiding calls that redraw the entire matplotlib plot.

    This permits smoother ROI selection for dense plots
    that take long to render
    """

    def setup_patch(self):
        pass

    def _draw(self):
        pass

    def _sync_patch(self):
        self.canvas.roi_callback = self._paint_check
        try:
            self.canvas.update()  # QT repaint without MPL redraw
        except RuntimeError:
            # In some cases the above can raise a "wrapped C/C++ object of
            # type ... has been deleted" error, in which case we can just
            # ignore and carry on.
            pass

    @property
    def canvas(self):
        return self._axes.figure.canvas

    def _paint_check(self, canvas):
        # check if the ROI should be rendered
        # called within the Qt paint loop
        if not (self._roi.defined() and self._mid_selection):
            return
        self.paint(canvas)

    def paint(self, canvas):
        x, y = self._roi.to_polygon()
        self.draw_polygon(canvas, x, y)

    def draw_polygon(self, canvas, x, y):
        x, y = self._transform(x, y)
        poly = QtGui.QPolygon()
        points = [QtCore.QPoint(xx, yy) for xx, yy in zip(x, y)]
        for p in points:
            poly.append(p)

        p = self.get_painter(canvas)
        p.drawPolygon(poly)
        p.end()

    def _transform(self, x, y):
        """ Convert points from MPL data coords to Qt Widget coords"""
        t = self._axes.transData

        xy = np.column_stack((x, y))
        pts = t.transform(xy)

        # Matplotlib 2.x with PyQt5 on a retina display has a bug which means
        # that the coordinates returned by transData are twice as large as they
        # should be. Since we don't know when/if this bug will be fixed, we
        # check whether the coordinates of the top right corner are outside
        # the canvas.
        xmax = self._axes.get_xlim()[1]
        ymax = self._axes.get_ylim()[1]
        xd, yd = t.transform((xmax, ymax))
        if xd > self.canvas.width() or yd > self.canvas.height():
            ratio = self.canvas.devicePixelRatio()
            pts /= ratio

        pts[:, 1] = self.canvas.height() - pts[:, 1]
        return pts[:, 0], pts[:, 1]

    def get_painter(self, canvas):
        p = QtGui.QPainter(canvas)
        facecolor = mpl_to_qt_color(self.plot_opts['facecolor'],
                                    self.plot_opts['alpha'])
        edgecolor = mpl_to_qt_color(self.plot_opts['edgecolor'],
                                    self.plot_opts['alpha'])

        pen = QtGui.QPen(edgecolor)
        pen.setWidth(self.plot_opts.get('edgewidth', 0))
        p.setPen(pen)

        p.setBrush(QtGui.QBrush(facecolor))

        return p


class QtPathROI(QtROI, _roi.MplPathROI):

    def get_painter(self, canvas):
        p = super(QtPathROI, self).get_painter(canvas)
        p.setBrush(Qt.NoBrush)
        p.setRenderHint(p.HighQualityAntialiasing)
        return p

    def draw_polygon(self, canvas, x, y):
        x, y = self._transform(x, y)
        poly = QtGui.QPolygon()
        points = [QtCore.QPoint(xx, yy) for xx, yy in zip(x, y)]
        for p in points:
            poly.append(p)

        p = self.get_painter(canvas)
        p.drawPolyline(poly)
        p.end()


class QtRectangularROI(QtROI, _roi.MplRectangularROI):

    def __init__(self, axes):
        _roi.MplRectangularROI.__init__(self, axes)


class QtPolygonalROI(QtROI, _roi.MplPolygonalROI):

    def __init__(self, axes, roi=None):
        _roi.MplPolygonalROI.__init__(self, axes, roi=roi)


class QtXRangeROI(QtROI, _roi.MplXRangeROI):

    def __init__(self, axes):
        _roi.MplXRangeROI.__init__(self, axes)

    def paint(self, canvas):
        x = self._roi.range()
        xy = self._axes.transAxes.transform([(0, 0), (1.0, 1.0)])
        xy = self._axes.transData.inverted().transform(xy)
        y = xy[:, 1]
        self.draw_polygon(canvas, [x[0], x[1], x[1], x[0]],
                          [y[0], y[0], y[1], y[1]])


class QtYRangeROI(QtROI, _roi.MplYRangeROI):

    def __init__(self, axes):
        _roi.MplYRangeROI.__init__(self, axes)

    def paint(self, canvas):
        y = self._roi.range()
        xy = self._axes.transAxes.transform([(0, 0.0), (1.0, 1.0)])
        xy = self._axes.transData.inverted().transform(xy)
        x = xy[:, 0]
        self.draw_polygon(canvas, [x[0], x[1], x[1], x[0]],
                          [y[0], y[0], y[1], y[1]])


class QtCircularROI(QtROI, _roi.MplCircularROI):

    def __init__(self, axes):
        _roi.MplCircularROI.__init__(self, axes)

    def paint(self, canvas):

        xy = list(map(int, self._roi.get_center()))
        radius = int(self._roi.get_radius())

        # Matplotlib 2.x with PyQt5 on a retina display has a bug which means
        # that the coordinates returned by transData are twice as large as they
        # should be. Since we don't know when/if this bug will be fixed, we
        # check whether the coordinates of the top right corner are outside
        # the canvas.
        xmax = self._axes.get_xlim()[1]
        ymax = self._axes.get_ylim()[1]
        xd, yd = self._axes.transData.transform((xmax, ymax))
        if xd > self.canvas.width() or yd > self.canvas.height():
            ratio = self.canvas.devicePixelRatio()
            xy[0] /= ratio
            xy[1] /= ratio
            radius /= ratio

        center = QtCore.QPoint(xy[0], canvas.height() - xy[1])

        p = self.get_painter(canvas)
        p.drawEllipse(center, radius, radius)
        p.end()

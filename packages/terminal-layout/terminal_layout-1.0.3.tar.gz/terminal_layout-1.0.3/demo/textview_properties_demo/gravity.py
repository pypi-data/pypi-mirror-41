# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from terminal_layout import *

ctl = LayoutCtl.quick(TableLayout,
                      [
                          [TextView('', 'gravity = left', width=25, gravity=Gravity.left, back=Back.cyan)],
                          [TextView('', 'gravity = center', width=25, gravity=Gravity.center, back=Back.green)],
                          [TextView('', 'gravity = right', width=25, gravity=Gravity.right, back=Back.magenta)],
                      ])

ctl.get_layout().width = 50

ctl.draw()

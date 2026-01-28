from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class redorchid(ColorScheme):
    progress_bar_color = 196  # bright red

    def use(self, context):
        fg, bg, attr = default_colors

        rose    = 227
        crimson = 202
        orchid  = 202
        accent  = 196
        maroon  = 124

        fg = rose
        bg = default
        attr = normal

        if context.directory:
            fg = crimson
            attr |= bold

        if context.file:
            fg = rose

        if context.executable:
            fg = accent
            attr |= bold

        if context.link:
            fg = orchid
            attr |= bold

        if context.image:
            fg = orchid

        if context.selected:
            fg = black
            bg = orchid
            attr |= bold

        if context.marked:
            fg = black
            bg = accent
            attr |= bold

        if context.bad:
            fg = accent
            attr |= bold | reverse

        if context.border:
            fg = 196
            bg = default

        if context.in_statusbar:
            fg = rose
            bg = default
            attr |= bold

        if context.title:
            fg = accent
            attr |= bold

        return fg, bg, attr

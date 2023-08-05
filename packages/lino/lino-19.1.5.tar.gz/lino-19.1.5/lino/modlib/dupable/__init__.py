# Copyright 2017 Rumma & Ko Ltd
# License: BSD (see file COPYING for details)

"""

.. autosummary::
   :toctree:

   mixins
   models


"""

from lino import ad, _


class Plugin(ad.Plugin):

    verbose_name = _("Dupe control")

    needs_plugins = ['lino.modlib.gfks']

    def setup_explorer_menu(self, site, user_type, main):
        mg = site.plugins.system
        m = main.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('dupable.PhoneticWords')
        

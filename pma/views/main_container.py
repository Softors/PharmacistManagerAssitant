from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

from pma.views.drugs.drugs_tab import DrugsTabItem
from pma.views.substances.substances_tab import SubstancesTabItem
from pma.views.usages.usages_tab import UsagesTabItem
from pma.views.wards.wards_tab import WardsTabItem


class MainContainer(TabbedPanel):
    def __init__(self, **kwargs):
        super(MainContainer, self).__init__(**kwargs)
        wards_tab_item = WardsTabItem()
        self.add_widget(wards_tab_item)
        self.add_widget(SubstancesTabItem())
        self.add_widget(DrugsTabItem())
        self.add_widget(UsagesTabItem())
        self.set_def_tab(wards_tab_item)

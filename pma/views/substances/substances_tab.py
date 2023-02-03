from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanelItem

from pma.views.tab_content import TabContent


class SubstancesTabContent(TabContent):
    def __init__(self, **kwargs):
        super(SubstancesTabContent, self).__init__(**kwargs)
        self.add_widget(Button(text='Substances Header', size_hint=(0.25, 0.1)))  # placeholder
        self.add_widget(Button(text='Substances Content', size_hint=(0.25, 0.1)))  # placeholder
        self.add_widget(FloatLayout())  # placeholder


class SubstancesTabItem(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(SubstancesTabItem, self).__init__(**kwargs)
        self.text = 'Substances'
        self.add_widget(SubstancesTabContent())

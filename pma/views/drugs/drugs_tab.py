from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanelItem

from pma.views.tab_content import TabContent


class DrugsTabContent(TabContent):
    def __init__(self, **kwargs):
        super(DrugsTabContent, self).__init__(**kwargs)
        self.add_widget(Button(text='Drugs Header', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(Button(text='Drugs Content', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(FloatLayout())  # placeholder


class DrugsTabItem(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(DrugsTabItem, self).__init__(**kwargs)
        self.text = 'Drugs'
        self.add_widget(DrugsTabContent())

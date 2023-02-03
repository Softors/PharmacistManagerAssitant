from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.tabbedpanel import TabbedPanelItem

from pma.views.tab_content import TabContent


class WardsTabContent(TabContent):
    def __init__(self, **kwargs):
        super(WardsTabContent, self).__init__(**kwargs)
        self.add_widget(Button(text='Wards Header', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(Button(text='Wards Content', size_hint=(0.2, 0.1)))  # placeholder
        self.add_widget(FloatLayout())  # placeholder


class WardsTabItem(TabbedPanelItem):
    def __init__(self, **kwargs):
        super(WardsTabItem, self).__init__(**kwargs)
        self.text = 'Wards'
        self.add_widget(WardsTabContent())

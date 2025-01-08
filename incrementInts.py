import sublime
import sublime_plugin
import re

class IncrementMauiRowNumbersCommand(sublime_plugin.TextCommand):
    """
    Command to increment the Grid Row number like 
    Grid.Row="1"-> Grid.Row="2"
    """
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region)
                incremented = re.sub(
                    r'Grid\.Row\s*=\s*"(\d+)"',
                    lambda m: f'Grid.Row="{int(m.group(1)) + 1}"',
                    text
                )
                self.view.replace(edit, region, incremented)


class IncrementMauiColumnNumbersCommand(sublime_plugin.TextCommand):
    """
    Command to increment the Grid Column number like 
    Grid.Column="1"-> Grid.Column="2"
    """
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                text = self.view.substr(region)
                incremented = re.sub(
                    r'Grid\.Column\s*=\s*"(\d+)"',
                    lambda m: f'Grid.Column="{int(m.group(1)) + 1}"',
                    text
                )
                self.view.replace(edit, region, incremented)


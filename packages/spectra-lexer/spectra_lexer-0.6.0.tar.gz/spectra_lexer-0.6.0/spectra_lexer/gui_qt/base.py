""" Base module for the GUI Qt package. """

from spectra_lexer import Composite
from spectra_lexer.gui_qt.board import GUIQtBoardDisplay
from spectra_lexer.gui_qt.config import GUIQtConfig
from spectra_lexer.gui_qt.main_window import MainWindow
from spectra_lexer.gui_qt.menu import GUIQtMenu
from spectra_lexer.gui_qt.search import GUIQtSearch
from spectra_lexer.gui_qt.text import GUIQtTextDisplay
from spectra_lexer.gui_qt.window import GUIQtWindow


class GUIQt(Composite):
    """ Top-level component of the GUI Qt package. Central constructor/container for all other Qt-based components. """

    ROLE = "gui"
    # Subcomponents of the GUI with their widget sections. Some components may use the same section.
    # The window shouldn't be shown until everything else is set up, so create the window controller last.
    COMPONENTS = {GUIQtMenu:         "menu",
                  GUIQtSearch:       "search",
                  GUIQtTextDisplay:  "text",
                  GUIQtBoardDisplay: "board",
                  GUIQtConfig:       "window",
                  GUIQtWindow:       "window"}

    window: MainWindow  # Main window must be publicly accessible for the Plover plugin.

    def __init__(self):
        """ Create the main window and assemble all child components with their required widgets. """
        self.window = MainWindow()
        cmp_args = self.window.partition()
        super().__init__([cmp_args[w] for w in self.COMPONENTS.values()])

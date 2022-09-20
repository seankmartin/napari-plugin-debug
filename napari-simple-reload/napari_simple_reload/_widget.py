# napari_simple_reload/_widget.py
from magicgui import magic_factory
from qtpy.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit
import logging
import sys
from napari.utils.notifications import notification_manager, Notification, NotificationSeverity, show_console_notification

my_plugin_logger = logging.getLogger("napari_simple_reload")
stdout_handler = logging.StreamHandler(sys.stderr)
stdout_handler.setFormatter(
    logging.Formatter(
        fmt="%(levelname)s: %(asctime)s %(message)s",
        datefmt="%d/%m/%Y %I:%M:%S %p"
    )
)
my_plugin_logger.addHandler(stdout_handler)
my_plugin_logger.setLevel(logging.WARNING)

def show_debug(message: str):
    """
    Show a debug message in the notification manager.
    """
    notification_ = Notification(message, severity=NotificationSeverity.DEBUG)
    # This goes to the console only ->
    show_console_notification(notification_)
    # This goes to the console and the napari GUI ->
    notification_manager.dispatch(notification_)
    # You can control what level of these messages is shown via napari preferences

def example(input_string: str) -> str:
    output_string = f"You entered {input_string}!" if input_string else "Please enter something in the text box."
    show_debug(f"The input string was (napari): {input_string}")
    my_plugin_logger.debug(f"The input string was (logging): {input_string}")
    print(output_string)
    return output_string

@magic_factory
def example_factory(input_string: str) -> str:
    return example(input_string)

class ExampleQWidget(QWidget):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Run")
        btn.clicked.connect(self._on_click)
        text_box = QLineEdit()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(text_box)
        self.layout().addWidget(btn)

    def _on_click(self):
        example(self.layout().itemAt(0).widget().text())
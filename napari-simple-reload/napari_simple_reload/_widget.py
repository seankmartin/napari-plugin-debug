# napari_simple_reload/_widget.py
from magicgui import magic_factory
from qtpy.QtWidgets import QVBoxLayout, QPushButton, QWidget, QLineEdit

def example(input_string: str) -> str:
    output_string = f"You entered {input_string}!"
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
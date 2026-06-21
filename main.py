from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
import fitz
import fitz
import os

from plyer import filechooser

Window.clearcolor = (1, 1, 1, 1)


class SelectScreen(Screen):

    def open_pdf(self):
        filechooser.open_file(
            on_selection=self.handle_selection,
            filters=["*.pdf"]
        )

    def handle_selection(self, selection):
        if selection:
            app = App.get_running_app()
            app.pdf_path = selection[0]

            viewer = self.manager.get_screen("viewer")
            viewer.load_pdf()

            self.manager.current = "viewer"


# class ViewerScreen(Screen):

#     def load_pdf(self):

#         app = App.get_running_app()

#         doc = fitz.open(app.pdf_path)

#         page = doc[0]

#         pix = page.get_pixmap(
#             matrix=fitz.Matrix(3, 3)
#         )

#         import os
#         import tempfile

#         temp_dir = tempfile.gettempdir()
#         img_path = os.path.join(temp_dir, "current_page.png")

#         # если старый файл есть, удаляем
#         if os.path.exists(img_path):
#             try:
#                 os.remove(img_path)
#             except:
#                 pass

#         pix.save(img_path)

#         self.ids.pdf_image.source = img_path
#         self.ids.pdf_image.reload()

class ViewerScreen(Screen):

    def load_pdf(self):

        app = App.get_running_app()

        pdf_path = app.pdf_path

        os.makedirs("cache", exist_ok=True)

        image_path = "cache/page.png"

        doc = fitz.open(pdf_path)

        page = doc[0]

        mat = fitz.Matrix(4, 4)

        pix = page.get_pixmap(matrix=mat)

        if os.path.exists(image_path):
            try:
                os.remove(image_path)
            except:
                pass

        pix.save(image_path)

        self.ids.pdf_image.source = image_path
        self.ids.pdf_image.reload()

class PdfApp(App):

    pdf_path = ""

    def build(self):
        Window.bind(on_keyboard=self.android_back)

        sm = ScreenManager()
        sm.add_widget(SelectScreen(name="select"))
        sm.add_widget(ViewerScreen(name="viewer"))

        return sm

    def android_back(self, window, key, *args):

        # кнопка BACK
        if key == 27:

            sm = self.root

            if sm.current == "viewer":
                sm.current = "select"
                return True

        return False


PdfApp().run()
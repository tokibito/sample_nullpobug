# coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        self.button_test = gtk.Button('test')
        self.button_test.connect('clicked', self.on_button_test_clicked)

        self.window.add(self.button_test)
        self.window.connect('delete-event', self.on_delete_event)

    def on_delete_event(self, window, event, data=None):
        """ウィンドウ閉じる
        """
        gtk.main_quit()
        return False

    def on_button_test_clicked(self, widget, data=None):
        """ボタンクリック
        """
        self.messagebox(u'こんにちはPyGTK!')

    def messagebox(self, text):
        dialog = gtk.MessageDialog(
            self.window,
            gtk.DIALOG_MODAL,
            gtk.MESSAGE_INFO,
            gtk.BUTTONS_OK,
            text,
        )
        dialog.run()
        dialog.destroy()

    def main(self):
        # 画面を表示してメインループに入る
        self.window.show_all()
        gtk.main()


if __name__ == '__main__':
    app = MyApp()
    app.main()

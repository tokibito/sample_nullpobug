# coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        # テキストボックス
        self.entry = gtk.Entry()

        # OKボタン
        self.button_ok = gtk.Button('OK')
        self.button_ok.connect('clicked', self.on_button_ok_clicked)

        # レイアウト用ボックス
        self.vbox = gtk.VBox()
        self.vbox.add(self.entry)
        self.vbox.add(self.button_ok)

        self.window.add(self.vbox)
        self.window.connect('delete-event', self.on_delete_event)

    def on_delete_event(self, window, event, data=None):
        """ウィンドウ閉じる
        """
        gtk.main_quit()
        return False

    def on_button_ok_clicked(self, widget, data=None):
        """ボタンクリック
        """
        self.messagebox(u'入力内容は %s です。' % self.entry.get_text())

    def messagebox(self, text):
        """メッセージボックス
        """
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

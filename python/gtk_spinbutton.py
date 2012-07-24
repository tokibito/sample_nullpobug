# coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk
import gobject


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        # スピンボタン
        self.spinbutton = gtk.SpinButton()
        self.spinbutton.set_range(-10, 20)  # 値の範囲を-10〜20に設定
        self.spinbutton.set_increments(1, 10)  # インクリメント量の設定,通常:1,中ボタン:10
        self.spinbutton.set_value(5)  # 値を5に設定

        # OKボタン
        self.button_ok = gtk.Button('OK')
        self.button_ok.connect('clicked', self.on_button_ok_clicked)

        # レイアウト用ボックス
        self.vbox = gtk.VBox()
        self.vbox.add(self.spinbutton)
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
        self.messagebox(u'値は %d です。' % self.get_spinbutton_value())

    def get_spinbutton_value(self):
        """スピンボタンの値を返す
        """
        return self.spinbutton.get_value_as_int()

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

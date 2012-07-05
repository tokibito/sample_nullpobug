# coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk
import gobject


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        # ラジオボタン
        self.radiobutton1 = gtk.RadioButton(None, u'アイテム1')
        self.radiobutton2 = gtk.RadioButton(self.radiobutton1, u'アイテム2')
        self.radiobutton3 = gtk.RadioButton(self.radiobutton2, u'アイテム3')

        # ラジオボタンを囲む枠
        self.frame = gtk.Frame()
        # 枠内に横並び
        self.hbox = gtk.HBox(spacing=5)
        # ラジオボタンをボックスに追加
        self.hbox.add(self.radiobutton1)
        self.hbox.add(self.radiobutton2)
        self.hbox.add(self.radiobutton3)
        self.frame.add(self.hbox)

        # OKボタン
        self.button_ok = gtk.Button('OK')
        self.button_ok.connect('clicked', self.on_button_ok_clicked)

        # レイアウト用ボックス
        self.vbox = gtk.VBox()
        self.vbox.pack_start(self.frame, False, False, 10)
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
        self.messagebox(u'選択した内容は %s です。' % self.get_radiobutton_text())

    def get_radiobutton_text(self):
        """選択中のラジオボタンのテキストを返す
        """
        for radiobutton in self.radiobutton1.get_group():
            if radiobutton.get_active():
                return radiobutton.get_label()

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

# coding: utf-8
import pygtk
pygtk.require('2.0')
import gtk
import gobject


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        # コンボボックス用ListStore(文字列のカラム1列)
        self.liststore = gtk.ListStore(gobject.TYPE_STRING)
        for i in range(5):
            self.liststore.append([u"アイテム%d" % i])
        # コンボボックス用テキストレンダラを用意
        cell = gtk.CellRendererText()
        # コンボボックス
        self.combobox = gtk.ComboBox(self.liststore)
        self.combobox.pack_start(cell, True)
        self.combobox.add_attribute(cell, 'text', 0)
        # 3つめのアイテムを選択状態にする
        self.combobox.set_active(2)

        # OKボタン
        self.button_ok = gtk.Button('OK')
        self.button_ok.connect('clicked', self.on_button_ok_clicked)

        # レイアウト用ボックス
        self.vbox = gtk.VBox()
        self.vbox.add(self.combobox)
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
        self.messagebox(u'選択した内容は %s です。' % self.combobox.get_active_text())

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

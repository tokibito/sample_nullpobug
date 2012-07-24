# coding: utf-8
import os
import pygtk
pygtk.require('2.0')
import gtk


class FileReference(object):
    def __init__(self, parent_window=None):
        # 親ウィンドウ
        self.parent_window = parent_window
        # テキストボックス
        self.entry = gtk.Entry()
        # 参照ボタン
        self.button = gtk.Button("...")
        self.button.connect('clicked', self.on_button_click)
        # ダイアログ
        self.dialog = gtk.FileChooserDialog(u"Select file", self.parent_window,
            buttons=(
                gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        self.dialog.set_default_response(gtk.RESPONSE_OK)
        self.filefilter = gtk.FileFilter()
        self.filefilter.set_name(u"テキストファイル")
        self.filefilter.add_pattern("*.txt")
        self.dialog.add_filter(self.filefilter)

        # レイアウト用ボックス
        self.hbox = gtk.HBox()
        self.hbox.add(self.entry)
        self.hbox.add(self.button)

    def browse(self):
        """ファイル選択ダイアログを開く
        """
        # 現在のパスが有効であればダイアログに設定
        current = self.get_filename()
        if os.path.exists(current):
            self.dialog.set_filename(current)
        # ダイアログを開く
        response = self.dialog.run()
        # OKなら更新
        if response == gtk.RESPONSE_OK:
            filename = self.dialog.get_filename()
            self.set_filename(filename)
        self.dialog.hide()

    def get_filename(self):
        """ファイルパスを返す
        """
        return self.entry.get_text()

    def set_filename(self, filename):
        """ファイルパスを更新
        """
        self.entry.set_text(filename)

    def on_button_click(self, widget):
        """ボタンクリック時イベント
        """
        self.browse()


class MyApp(object):
    def __init__(self):
        self.window = gtk.Window()

        # FileReferenceのリスト
        self.filereferences = []
        for i in range(3):
            self.filereferences.append(FileReference(self.window))

        # OKボタン
        self.button_ok = gtk.Button('OK')
        self.button_ok.connect('clicked', self.on_button_ok_clicked)

        # レイアウト用ボックス
        self.vbox = gtk.VBox()
        for obj in self.filereferences:
            self.vbox.add(obj.hbox)
        self.vbox.add(self.button_ok)

        self.window.add(self.vbox)
        self.window.connect('delete-event', self.on_delete_event)

    def on_delete_event(self, window, event):
        """ウィンドウ閉じる
        """
        gtk.main_quit()
        return False

    def on_button_ok_clicked(self, widget):
        """ボタンクリック
        """
        filenames = '\n'.join(obj.get_filename() for obj in self.filereferences)
        self.messagebox(u'入力内容は\n%s\nです。' % filenames)

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

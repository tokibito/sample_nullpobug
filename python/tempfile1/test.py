# coding: utf-8
import os
import tempfile
import shutil
import unittest


class RenameFileTest(unittest.TestCase):
    u"""ファイル名の変更のテスト
    """

    def setUp(self):
        # 一時ディレクトリを作成
        self.temp_dir = tempfile.mkdtemp()
        # テスト用のファイルを作成
        self.test_src = os.path.join(self.temp_dir, 'test')
        open(self.test_src, 'w').close()
        self.test_dst = os.path.join(self.temp_dir, 'moved')

    def tearDown(self):
        # 一時ディレクトリを削除
        shutil.rmtree(self.temp_dir)

    def test_rename(self):
        u"ファイル名を変更する"
        os.rename(self.test_src, self.test_dst)
        # 変更後のファイルが存在すること
        self.assertTrue(os.path.exists(self.test_dst))
        # 変更前のファイルが存在しないこと
        self.assertFalse(os.path.exists(self.test_src))

if __name__ == '__main__':
    unittest.main()

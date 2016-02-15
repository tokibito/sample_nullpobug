from unittest import TestCase, mock


class SayHelloTest(TestCase):
    """say_hello関数のテスト
    """
    def _get_target(self):
        from main import say_hello as target
        return target

    def _callFUT(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_somebody(self):
        """somebody引数が使われていることを確認するテスト
        """
        with mock.patch('main.say', return_value=0) as patcher:
            result = self._callFUT("Spam")
            self.assertEqual(result, 0, "正常な終了コードになること")
            # somebody引数が使われたメッセージを指定して
            # say関数を実行していること
            patcher.assert_called_with("Hello, Spam!")

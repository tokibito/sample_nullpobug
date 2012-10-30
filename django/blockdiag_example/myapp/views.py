# coding: utf-8
from django.views.generic import TemplateView

test_text = """
restructuredtextフィルタでblockdiagを使う
=========================================

restructuredtextフィルタでblockdiagディレクティブを使っています。

.. blockdiag::

   {
     A -> B -> ほげ;
          B -> ふが;
   }

テスト
======

ほげふが
"""


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'test_text': test_text}

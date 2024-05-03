from django import forms


def create_form(form_schema_dict):
    """
    動的にフォームを作成する

    :form_schema_dict: フォームのスキーマを定義した辞書
    :return: フォームクラス

    例:
    form_class = create_form({
        "name": {"max_length": 100},
        "email": {"max_length": 100},
    })
    """
    form_schema = {}
    for field_name, options in form_schema_dict.items():
        form_schema[field_name] = forms.CharField(label=field_name, **options)
    return type("DynamicForm", (forms.Form,), form_schema)

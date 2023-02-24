from django import template
from django.template.base import TemplateSyntaxError
from django.template.defaulttags import AutoEscapeControlNode

register = template.Library()

@register.tag
def autoescape2(parser, token):
    """
    Force autoescape behavior for this block.
    """
    # token.split_contents() isn't useful here because this tag doesn't accept
    # variable as arguments.
    args = token.contents.split()
    if len(args) != 2:
        raise TemplateSyntaxError("'autoescape' tag requires exactly one argument.")
    arg = args[1]
    if arg not in ("on", "off"):
        raise TemplateSyntaxError("'autoescape' argument should be 'on' or 'off'")
    nodelist = parser.parse(("endautoescape2",))
    parser.delete_first_token()
    return AutoEscapeControlNode2((arg == "on"), nodelist)

class AutoEscapeControlNode2(AutoEscapeControlNode):
    """Implement the actions of the autoescape tag."""

    def render(self, context):
        output = super().render(context)
        # outputを変える
        return output.replace("===FOO===", "BAR")

from django.template import Node, Library, TemplateSyntaxError, Variable

register = Library()

class DisplayItemNode(Node):
    def __init__(self, item_var):
        self.item_var = Variable(item_var)

    def render(self, context):
        item = self.item_var.resolve(context)
        return item.display(context)

@register.tag
def displayitem(parser, token):
    bits = token.split_contents()
    if len(bits) != 2:
        raise TemplateSyntaxError("%r takes one argument." % bits[0])
    return DisplayItemNode(bits[1])

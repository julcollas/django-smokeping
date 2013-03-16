from django import template

register = template.Library()

class RepeatNode(template.Node):
    def __init__(self, nodelist, count):
        self.nodelist = nodelist
        self.count = template.Variable(count)
    
    def render(self, context):
        output = self.nodelist.render(context)
        return output * int(self.count.resolve(context) + 1)


def repeat(parser, token):
    """
    Repeats the containing text a certain number of times.
    
    Requires a single argument, an integer, to indicate the number of times to
    repeat the enclosing content.
    
    Example::
    
        {% repeat 3 %}foo{% endrepeat %}
    
    Yields::
    
        foofoofoo
    """
    bits = token.split_contents()
    
    if len(bits) != 2:
        raise template.TemplateSyntaxError('%r tag requires 1 argument.' % bits[0])
    
    count = bits[1]
    nodelist = parser.parse(('endrepeat',))
    parser.delete_first_token()
    return RepeatNode(nodelist, count)


repeat = register.tag(repeat)


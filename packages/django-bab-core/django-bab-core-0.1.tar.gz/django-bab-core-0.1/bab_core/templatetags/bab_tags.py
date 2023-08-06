from django import template

from django import VERSION as DJANGO_VERSION
from django import template
from django.conf import settings
from django.utils.encoding import escape_uri_path
from django.urls import reverse


register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, viewnames, css_class=None, strict=None, *args, **kwargs):
    """
    Renders the given CSS class if the request path matches the path of the view.
    :param context: The context where the tag was called. Used to access the request object.
    :param viewnames: The name of the view or views separated by || (include namespaces if any).
    :param css_class: The CSS class to render.
    :param strict: If True, the tag will perform an exact match with the request path.
    :return:
    """
    if css_class is None:
        css_class = getattr(settings, 'ACTIVE_LINK_CSS_CLASS', 'active')

    if strict is None:
        strict = getattr(settings, 'ACTIVE_LINK_STRICT', False)

    request = context.get('request')
    if request is None:
        # Can't work without the request object.
        return ''
    active = False
    views = viewnames.split('||')
    for viewname in views:
        path = reverse(viewname.strip(), args=args, kwargs=kwargs)
        request_path = escape_uri_path(request.path)
        if strict:
            active = request_path == path
        else:
            active = request_path.find(path) == 0
        if active:
            break

    if active:
        return css_class

    return ''

@register.inclusion_tag('widgets/carousel.html')
def carousel(objects, html_id):
    return {
        'objects': objects,
        'html_id': html_id
    }



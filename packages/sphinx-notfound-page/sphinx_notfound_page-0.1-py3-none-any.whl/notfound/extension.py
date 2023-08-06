# -*- coding: utf-8 -*-

from sphinx.errors import ExtensionError


class BaseURIError(ExtensionError):
    pass


# https://www.sphinx-doc.org/en/stable/extdev/appapi.html#event-html-collect-pages
def html_collect_pages(app):
    """
    Create a ``404.html`` page.

    Uses ``notfound_template`` as a template to be rendered with
    ``notfound_context`` for its context.

    .. note::

       The most important key from the context is ``body``.
    """
    return [(
        app.config.notfound_pagename,
        app.config.notfound_context,
        app.config.notfound_template,
    )]


def finalize_media(app, pagename, templatename, context, doctree):
    """ Point media files at our media server. """

    # https://github.com/sphinx-doc/sphinx/blob/7138d03ba033e384f1e7740f639849ba5f2cc71d/sphinx/builders/html.py#L1054-L1065
    def pathto(otheruri, resource=False, baseuri=None):
        """
        Hack pathto to display absolute URL's.

        Instead of calling ``relative_url`` function, we call
        ``app.builder.get_target_uri`` to get the absolut URL.

        .. note::

            If ``otheruri`` is a external ``resource`` it does not modify it.
        """
        if resource and '://' in otheruri:
            # allow non-local resources given by scheme
            return otheruri
        elif not resource:
            otheruri = app.builder.get_target_uri(otheruri)

        if baseuri is None:
            baseuri = '/{language}/{version}/'.format(
                language=app.config.notfound_default_language,
                version=app.config.notfound_default_version,
            )

        if not baseuri.startswith('/'):
            raise BaseURIError('"baseuri" must be absolute')

        if otheruri and not otheruri.startswith('/'):
            otheruri = '/' + otheruri

        if otheruri:
            if baseuri.endswith('/'):
                baseuri = baseuri[:-1]
            otheruri = baseuri + otheruri

        uri = otheruri or '#'
        return uri

    # Apply our custom manipulation to 404.html page only
    if pagename == app.config.notfound_pagename:
        # Override the ``pathto`` helper function from the context to use a custom ones
        # https://www.sphinx-doc.org/en/master/templating.html#pathto
        context['pathto'] = pathto


def setup(app):
    default_context = {
        # TODO: improve the default ``body``
        'body': '<h1>Page not found</h1>\n\nThanks for trying.',
    }

    # https://github.com/sphinx-doc/sphinx/blob/master/sphinx/themes/basic/page.html
    app.add_config_value('notfound_template', 'page.html', 'html')
    app.add_config_value('notfound_context', default_context, 'html')
    app.add_config_value('notfound_pagename', '404', 'html')

    # TODO: get these values from Project's settings
    app.add_config_value('notfound_default_language', 'en', 'html')
    app.add_config_value('notfound_default_version', 'latest', 'html')

    app.connect('html-collect-pages', html_collect_pages)
    app.connect('html-page-context', finalize_media)

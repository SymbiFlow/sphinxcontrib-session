#!/usr/bin/python3
# coding: utf-8

import logging
import os
import re

from shutil import copyfile

from docutils import nodes
from docutils.parsers import rst

from sphinx.errors import ExtensionError
from sphinx.directives.code import CodeBlock

import pygments
from pygments import token
from pygments.token import Token
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter


logger = logging.getLogger(__name__)


# --------------------------

def rewrite_match(m):
    klass, content, extra_whitespace = m.groups()
    #content = html.escape(content)
    #extra_whitespace = html.escape(extra_whitespace)
    return '<span class="{}" data-content="{}{}"></span>'.format(
        klass, content, extra_whitespace)


SPAN_REGEX = {}


def rewrite_span(s, t):
    if t not in SPAN_REGEX:
        klass = token.STANDARD_TYPES[t]

        SPAN_REGEX[t] = re.compile('<span class="({})">([^<]*)</span>(\\s+)'.format(klass), re.DOTALL)

    regex = SPAN_REGEX[t]
    return regex.sub(rewrite_match, s)

# --------------------------

SESSION_TYPES = {
    'BashLexer':        'shell-session',
    'BatchLexer':       'doscon',
    'PowerShellLexer':  'ps1con',
    'TcshLexer':        'tcshcon',
    'Python2Lexer':     'pycon',
    'PythonLexer':      'pycon',
    'RdLexer':          'rconsole',
    'SLexer':           'rconsole',
    'PostgresLexer':    'psql',
    'RubyLexer':        'rbconn',
}

def session_lexer(lexer):
    lexer_name = lexer.__class__.__name__

    if 'Session' in lexer_name:
        return lexer
    if 'Console' in lexer_name:
        return lexer

    if lexer_name in SESSION_TYPES:
        return get_lexer_by_name(SESSION_TYPES[lexer_name])
    else:
        print(lexer, lexer_name, "not found in SESSION_TYPES")

    return None

def get_lexer(self, source, lang, opts=None, force=False, location=None):
    lexer = XXXX.get_lexer(self, source, lang, opts, force, location)

    lexer = session_lexer(lexer_orig)
    if lexer is None:
        logger.warning("""\
Session contents should be a XXXSession lexer like `console`, `doscon` or \
`ps1con`. Got instead '{}'.""".format(lexer_orig), location=location)
        return
    return lexer

# --------------------------

class SessionDirective(CodeBlock):

    def run(self):
        n = session()
        n.contains = CodeBlock.run(self)
        return [n]


class session(nodes.Element): pass

# --------------------------

def visit_session_html(self, node):

    if not hasattr(node, 'contains'):
        logger.warning("Warning no contents found on {}".format(node))
        return
    data_node = node.contains[0]

    if data_node.rawsource != data_node.astext():
        # most probably a parsed-literal block -- don't highlight
        return super().visit_literal_block(date_node)

    lang = data_node.get('language', 'default')
    linenos = data_node.get('linenos', False)
    highlight_args = data_node.get('highlight_args', {})
    highlight_args['force'] = data_node.get('force', False)
    if lang is self.builder.config.highlight_language:
        # only pass highlighter options for original language
        opts = self.builder.config.highlight_options
    else:
        opts = {}

    highlighted = self.highlighter.highlight_block(
        data_node.rawsource, lang, opts=opts, linenos=linenos,
        location=(self.builder.current_docname, data_node.line),
        **highlight_args
    )

    o = highlighted
    for t in [Token.Generic.Prompt, Token.Generic.Output]:
        o = rewrite_span(o, t)

    starttag = self.starttag(
        node, 'div', suffix='', CLASS='highlight-%s notranslate' % lang)
    self.body.append(starttag + o + '</div>\n')
    raise nodes.SkipNode

def depart_session_html(self, node):
    return

# --------------------------

def _is_html(app):
    return app.builder.name in ('html', 'readthedocs')


def add_stylesheet(app):
    app.add_stylesheet('session.css')


def copy_stylesheet(app, exception):
    if not _is_html(app) or exception:
        return

    source = os.path.abspath(os.path.dirname(__file__))
    dest = os.path.join(app.builder.outdir, '_static', 'session.css')
    copyfile(os.path.join(source, "session.css"), dest)

# --------------------------

def setup(app):
    app.connect('builder-inited', add_stylesheet)
    app.connect('build-finished', copy_stylesheet)
    app.add_directive('session', SessionDirective)
    app.add_node(session, html=(visit_session_html, depart_session_html))

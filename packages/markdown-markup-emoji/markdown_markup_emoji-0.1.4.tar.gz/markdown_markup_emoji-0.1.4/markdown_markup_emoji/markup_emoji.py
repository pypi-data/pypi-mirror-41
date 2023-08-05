#!/usr/bin/python3
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 sts=4 tw=78 et:
# -----------------------------------------------------------------------------
"""
Markup Emoji Extension for Python-Markdown

Python-Markdown extension for markup of Emoji in the markdown document.
"""
import markdown

INSIDE_ELEMENTS = (
    'p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'li', 'a', 'th', 'td', 'dt', 'dd'
)
RANGE_EMOJI = (
    ('\u2700', '\u27bf'),           # Dingbats
    ('\U0001f650', '\U0001f67f'),   # Ornamental Dingbats
    ('\U0001f600', '\U0001f64f'),   # Emoticons
    ('\u2600', '\u26ff'),           # Miscellaneous Symbols
    ('\U0001f300', '\U0001f5ff'),   # Miscellaneous Symbols and Pictographs
    ('\U0001f900', '\U0001f9ff'),   # Supplemental Symbols and Pictographs
    ('\U0001f680', '\U0001f6ff'),   # Transport and Map Symbols
    ('\u200d', '\u200d'),           # ZERO WIDTH JOINER
    ('\ufe0e', '\ufe0f'),           # VARIATION SELECTOR-15/16
)


class MarkupEmojiExtension(markdown.Extension):
    """Markup Emoji Extension for Python-Markdown."""

    def extendMarkdown(self, md, md_globals=None):
        # Register instance with a priority.
        md.treeprocessors.register(
            MarkupEmojiTreeProcessor(md), 'markup_emoji', 4)


class MarkupEmojiTreeProcessor(markdown.treeprocessors.Treeprocessor):
    """Markup Emoji Extension Processor."""

    def run(self, root):
        def _check_range(char, c_range):
            for start, end in c_range:
                # if len(start) >= 2:     # Not supported unicode RANGE
                #     exit
                if start <= char <= end:
                    return True
            return False

        def _split_emoji(text):
            prev_emoji = curr_emoji = False
            words = []
            result_text = None
            for char in text:
                curr_emoji = _check_range(char, RANGE_EMOJI)
                if prev_emoji == curr_emoji:
                    result_text = (result_text or '') + char
                else:
                    words.append(result_text)
                    result_text = char
                    prev_emoji = curr_emoji
            words.append(result_text)
            if curr_emoji:
                words.append(None)
            # return list of string: ['ascii', ('CJK', 'ascii'), ...]
            return(words)

        def _et_copy(src):
            new = markdown.util.etree.Element(src.tag)
            new.text = src.text
            new.tail = src.tail
            if hasattr(src, 'attrib'):
                for key, value in src.attrib:
                    new.set(key, value)
            return new

        def _et_emoji(text, tail):
            new = markdown.util.etree.Element('span')
            new.text = text
            new.tail = tail
            new.set('class', 'emoji')
            return new

        def _tree_copy(n, src, parent):
            new = _et_copy(src)
            parent.append(new)
            for n, e in enumerate(src):
                _tree_copy(n, e, new)

            if src.text and src.tag in INSIDE_ELEMENTS:
                words = _split_emoji(src.text)
                new.text = words.pop(0)
                while len(words) > 1:
                    tail = words.pop()
                    text = words.pop()
                    emoji = _et_emoji(text, tail)
                    new.insert(0, emoji)
            if src.tail:
                words = _split_emoji(src.tail)
                new.tail = words.pop(0)
                while len(words) > 1:
                    tail = words.pop()
                    text = words.pop()
                    emoji = _et_emoji(text, tail)
                    parent.insert(n + 1, emoji)

        parent = _et_copy(root)
        for n, e in enumerate(root):
            _tree_copy(n, e, parent)
        return(parent)


def makeExtension(**kwargs):    # pragma: no cover
    return MarkupEmojiExtension(**kwargs)

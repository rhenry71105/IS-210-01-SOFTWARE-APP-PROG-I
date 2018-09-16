# -*- coding: utf-8 -*-

from landslide import macro
import os
import re
import unittest
import codecs
import base64

from landslide.generator import Generator
from landslide.parser import Parser


DATA_DIR = os.path.join(os.path.dirname(__file__), 'test-data')

if (not os.path.exists(DATA_DIR)):
    raise IOError('Test data not found, cannot run tests')


class BaseTestCase(unittest.TestCase):
    def logtest(self, message, type='notice'):
        if type == 'warning':
            raise WarningMessage(message)
        elif type == 'error':
            raise ErrorMessage(message)


class GeneratorTest(BaseTestCase):
    def test___init__(self):
        self.assertRaises(IOError, Generator, None)
        self.assertRaises(IOError, Generator, 'foo.md')

    def test_add_user_assets(self):
        base_dir = os.path.join(DATA_DIR, 'test.md')
        g = Generator(base_dir, logger=self.logtest)
        g.add_user_css(os.path.join(DATA_DIR, 'test.css'))
        self.assertEqual(g.user_css[0]['contents'], '* {color: red;}')

    def test_get_toc(self):
        base_dir = os.path.join(DATA_DIR, 'test.md')
        g = Generator(base_dir, logger=self.logtest)
        g.add_toc_entry('Section 1', 1, 1)
        g.add_toc_entry('Section 1.1', 2, 2)
        g.add_toc_entry('Section 1.2', 2, 3)
        g.add_toc_entry('Section 2', 1, 4)
        g.add_toc_entry('Section 2.1', 2, 5)
        g.add_toc_entry('Section 3', 1, 6)
        toc = g.toc
        self.assertEqual(len(toc), 3)
        self.assertEqual(toc[0]['title'], 'Section 1')
        self.assertEqual(len(toc[0]['sub']), 2)
        self.assertEqual(toc[0]['sub'][1]['title'], 'Section 1.2')
        self.assertEqual(toc[1]['title'], 'Section 2')
        self.assertEqual(len(toc[1]['sub']), 1)
        self.assertEqual(toc[2]['title'], 'Section 3')
        self.assertEqual(len(toc[2]['sub']), 0)

    def test_get_slide_vars(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        svars = g.get_slide_vars("<h1>heading</h1>\n<p>foo</p>\n<p>bar</p>\n")
        self.assertEqual(svars['title'], 'heading')
        self.assertEqual(svars['level'], 1)
        self.assertEqual(svars['header'], '<h1>heading</h1>')
        self.assertEqual(svars['content'], '<p>foo</p>\n<p>bar</p>')
        self.assertEqual(svars['source'], {})
        self.assertEqual(svars['classes'], [])

    def test_unicode(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        g.execute()
        s = g.render()
        self.assertTrue(s.find('<pre>') != 1)
        self.assertEqual(len(re.findall('<pre><span', s)), 0)

    def test_inputencoding(self):
        path = os.path.join(DATA_DIR, 'encoding.rst')
        g = Generator(path, encoding='koi8_r')
        content = g.render()

        # check that the string is utf_8
        self.assertTrue(re.findall(u'русский', content, flags=re.UNICODE))
        g.execute()
        with codecs.open(g.destination_file, encoding='utf_8') as file_object:
            file_contents = file_object.read()
        # check that the file was properly encoded in utf_8
        self.assertTrue(re.findall(u'русский', file_contents,
            flags=re.UNICODE))

    def test_get_template_vars(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        svars = g.get_template_vars([{'title': "slide1", 'level': 1},
                                     {'title': "slide2", 'level': 1},
                                     {'title': None, 'level': 1},
        ])
        self.assertEqual(svars['head_title'], 'slide1')

    def test_process_macros(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        # Notes
        r = g.process_macros('<p>foo</p>\n<p>.notes: bar</p>\n<p>baz</p>')
        self.assertEqual(r[0].find('<p class="notes">bar</p>'), 11)
        self.assertEqual(r[1], [u'has_notes'])
        # FXs
        content = '<p>foo</p>\n<p>.fx: blah blob</p>\n<p>baz</p>'
        r = g.process_macros(content)
        self.assertEqual(r[0], '<p>foo</p>\n<p>baz</p>')
        self.assertEqual(r[1][0], 'blah')
        self.assertEqual(r[1][1], 'blob')

    def test_register_macro(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))

        class SampleMacro(macro.Macro):
            pass

        g.register_macro(SampleMacro)
        self.assertTrue(SampleMacro in g.macros)

        def plop(foo):
            pass

        self.assertRaises(TypeError, g.register_macro, plop)

    def test_presenter_notes(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        svars = g.get_slide_vars("<h1>heading</h1>\n<p>foo</p>\n"
                                 "<h1>Presenter Notes</h1>\n<p>bar</p>\n")
        self.assertEqual(svars['presenter_notes'], "<p>bar</p>")

        # Check that presenter notes work even if the slide has no heading.
        # For example, if it is only an image:

        g = Generator(os.path.join(DATA_DIR, 'test.md'))
        svars = g.get_slide_vars("<p>foo</p>\n"
                                 "<h1>Presenter Notes</h1>\n<p>bar</p>\n")

    def test_skip_presenter_notes(self):
        g = Generator(os.path.join(DATA_DIR, 'test.md'),
                presenter_notes=False)
        svars = g.get_slide_vars("<h1>heading</h1>\n<p>foo</p>\n"
                                 "<h1>Presenter Notes</h1>\n<p>bar</p>\n")
        self.assertEqual(svars['presenter_notes'], None)



class FixImagePathsMacroTest(BaseTestCase):
    def test_process(self):
        base_dir = os.path.join(DATA_DIR, 'test.md')
        m = macro.FixImagePathsMacro(self.logtest, False)
        content, classes = m.process('<img src="img.png"/>', base_dir)
        self.assertTrue(re.match(r'<img src="file://.*?/img.png" */>',
                                 content))


class FxMacroTest(BaseTestCase):
    def test_process(self):
        m = macro.FxMacro(self.logtest)
        content = '<p>foo</p>\n<p>.fx: blah blob</p>\n<p>baz</p>'
        r = m.process(content)
        self.assertEqual(r[0], '<p>foo</p>\n<p>baz</p>')
        self.assertEqual(r[1][0], 'blah')
        self.assertEqual(r[1][1], 'blob')


class NotesMacroTest(BaseTestCase):
    def test_process(self):
        m = macro.NotesMacro(self.logtest)
        r = m.process('<p>foo</p>\n<p>.notes: bar</p>\n<p>baz</p>')
        self.assertEqual(r[0].find('<p class="notes">bar</p>'), 11)
        self.assertEqual(r[1], [u'has_notes'])


class ParserTest(BaseTestCase):
    def test___init__(self):
        self.assertEqual(Parser('.md').format, 'markdown')
        self.assertEqual(Parser('.markdown').format, 'markdown')
        self.assertEqual(Parser('.rst').format, 'restructuredtext')
        self.assertRaises(NotImplementedError, Parser, '.txt')


class WarningMessage(Exception):
    pass

class ErrorMessage(Exception):
    pass

if __name__ == '__main__':
    unittest.main()

# coding:utf-8
from base import TestBase
import sublime
import sys

class TestIndent(TestBase):
    """Test of attributes 'indent'"""

    # for debug
    # def tearDown(self):
    #     pass

    indent_text = \
"""

<!-- MarkdownTOC {0} -->

<!-- /MarkdownTOC -->

# foo
## bar
### buz
#### qux
"""
    # TODO: This test cannot be passed when tab(\t) is convert to space by sublime's other feature
    # def test_indent_default(self):
    #     """Default indent is 1tab"""
    #     toc_txt = self.commonSetup(self.indent_text.format('depth=0'))
    #     self.assert_In('- foo', toc_txt)
    #     self.assert_In('\t- bar', toc_txt)
    #     self.assert_In('\t\t- buz', toc_txt)
    #     self.assert_In('\t\t\t- qux', toc_txt)

    def test_indent_2spaces(self):
        toc_txt = self.commonSetup(self.indent_text.format('depth=0 indent="  "'))
        self.assert_In('- foo', toc_txt)
        self.assert_In('  - bar', toc_txt)
        self.assert_In('    - buz', toc_txt)
        self.assert_In('      - qux', toc_txt)

    def test_indent_4spaces(self):
        toc_txt = self.commonSetup(self.indent_text.format('depth=0 indent="    "'))
        self.assert_In('- foo', toc_txt)
        self.assert_In('    - bar', toc_txt)
        self.assert_In('        - buz', toc_txt)
        self.assert_In('            - qux', toc_txt)

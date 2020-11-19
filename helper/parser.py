# This file was generated from parser.peg
# See http://canopy.jcoglan.com/ for documentation.

from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements):
        self.text = text
        self.offset = offset
        self.elements = elements

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.tag_pairs = elements[0]
        self.gcomment = elements[2]
        self.movetext = elements[3]
        self.score = elements[4]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.dlm = elements[9]
        self.key = elements[2]
        self.value = elements[5]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.move_number = elements[0]
        self.dlm = elements[19]
        self.white = elements[3]
        self.san = elements[3]
        self.wnags = elements[6]
        self.wcomment = elements[8]
        self.wvars = elements[10]
        self.black = elements[12]
        self.bnags = elements[14]
        self.bcomment = elements[16]
        self.bvars = elements[18]
        self.mcomment = elements[20]


class TreeNode4(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode4, self).__init__(text, offset, elements)
        self.file = elements[3]
        self.rank = elements[4]
        self.dlm = elements[2]


class TreeNode5(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode5, self).__init__(text, offset, elements)
        self.file = elements[7]
        self.rank = elements[8]
        self.dlm = elements[4]


class TreeNode6(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode6, self).__init__(text, offset, elements)
        self.file = elements[5]
        self.rank = elements[6]
        self.dlm = elements[2]


class TreeNode7(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode7, self).__init__(text, offset, elements)
        self.piece = elements[6]
        self.file = elements[9]
        self.rank = elements[10]
        self.dlm = elements[5]


class TreeNode8(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode8, self).__init__(text, offset, elements)
        self.piece = elements[0]
        self.file = elements[8]
        self.rank = elements[9]
        self.dlm = elements[5]


class TreeNode9(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode9, self).__init__(text, offset, elements)
        self.file = elements[8]
        self.rank = elements[9]
        self.dlm = elements[4]
        self.piece = elements[5]


class TreeNode10(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode10, self).__init__(text, offset, elements)
        self.file = elements[0]
        self.takes = elements[1]
        self.square = elements[2]


class TreeNode11(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode11, self).__init__(text, offset, elements)
        self.piece = elements[0]
        self.square = elements[3]


class TreeNode12(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode12, self).__init__(text, offset, elements)
        self.piece = elements[0]
        self.square = elements[2]


class TreeNode13(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode13, self).__init__(text, offset, elements)
        self.piece = elements[0]
        self.file = elements[1]
        self.square = elements[3]


class TreeNode14(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode14, self).__init__(text, offset, elements)
        self.piece = elements[0]
        self.rank = elements[1]
        self.square = elements[3]


class TreeNode15(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode15, self).__init__(text, offset, elements)
        self.file = elements[0]
        self.rank = elements[1]


class TreeNode16(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode16, self).__init__(text, offset, elements)
        self.dlm = elements[2]


class TreeNode17(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode17, self).__init__(text, offset, elements)
        self.dlm = elements[4]
        self.movetext = elements[2]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    REGEX_1 = re.compile('^[\\n]')
    REGEX_2 = re.compile('^[\\s]')
    REGEX_3 = re.compile('^[A-Za-z0-9_]')
    REGEX_4 = re.compile('^[^\\"]')
    REGEX_5 = re.compile('^[0-9]')
    REGEX_6 = re.compile('^[KQRNBP]')
    REGEX_7 = re.compile('^[a-h]')
    REGEX_8 = re.compile('^[1-8]')
    REGEX_9 = re.compile('^[KQRNB]')
    REGEX_10 = re.compile('^[+#]')
    REGEX_11 = re.compile('^[^\\}]')
    REGEX_12 = re.compile('^[0-9]')
    REGEX_13 = re.compile('^[\\s+]')

    def _read_game(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['game'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_tag_pairs()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            index2 = self._offset
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_1.search(chunk0):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[\\n]')
            if address2 is FAILURE:
                address2 = TreeNode(self._input[index2:index2], index2, [])
                self._offset = index2
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index3 = self._offset
                address3 = self._read_comment()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index3:index3], index3, [])
                    self._offset = index3
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_movetext()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        index4 = self._offset
                        address5 = self._read_score()
                        if address5 is FAILURE:
                            address5 = TreeNode(self._input[index4:index4], index4, [])
                            self._offset = index4
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            remaining0, index5, elements1, address7 = 0, self._offset, [], True
                            while address7 is not FAILURE:
                                chunk1, max1 = None, self._offset + 1
                                if max1 <= self._input_size:
                                    chunk1 = self._input[self._offset:max1]
                                if chunk1 is not None and Grammar.REGEX_2.search(chunk1):
                                    address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address7 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('[\\s]')
                                if address7 is not FAILURE:
                                    elements1.append(address7)
                                    remaining0 -= 1
                            if remaining0 <= 0:
                                address6 = TreeNode(self._input[index5:self._offset], index5, elements1)
                                self._offset = self._offset
                            else:
                                address6 = FAILURE
                            if address6 is not FAILURE:
                                elements0.append(address6)
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_game(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['game'][index0] = (address0, self._offset)
        return address0

    def _read_tag_pairs(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['tag_pairs'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_tag_pair()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.make_tag_pairs(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['tag_pairs'][index0] = (address0, self._offset)
        return address0

    def _read_tag_pair(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['tag_pair'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '[':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"["')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_dlm()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_key()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_dlm()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        chunk1, max1 = None, self._offset + 1
                        if max1 <= self._input_size:
                            chunk1 = self._input[self._offset:max1]
                        if chunk1 == '"':
                            address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                            self._offset = self._offset + 1
                        else:
                            address5 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('"\\""')
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_value()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                chunk2, max2 = None, self._offset + 1
                                if max2 <= self._input_size:
                                    chunk2 = self._input[self._offset:max2]
                                if chunk2 == '"':
                                    address7 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                    self._offset = self._offset + 1
                                else:
                                    address7 = FAILURE
                                    if self._offset > self._failure:
                                        self._failure = self._offset
                                        self._expected = []
                                    if self._offset == self._failure:
                                        self._expected.append('"\\""')
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read_dlm()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        chunk3, max3 = None, self._offset + 1
                                        if max3 <= self._input_size:
                                            chunk3 = self._input[self._offset:max3]
                                        if chunk3 == ']':
                                            address9 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                                            self._offset = self._offset + 1
                                        else:
                                            address9 = FAILURE
                                            if self._offset > self._failure:
                                                self._failure = self._offset
                                                self._expected = []
                                            if self._offset == self._failure:
                                                self._expected.append('"]"')
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
                                            address10 = FAILURE
                                            address10 = self._read_dlm()
                                            if address10 is not FAILURE:
                                                elements0.append(address10)
                                            else:
                                                elements0 = None
                                                self._offset = index1
                                        else:
                                            elements0 = None
                                            self._offset = index1
                                    else:
                                        elements0 = None
                                        self._offset = index1
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_tag_pair(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['tag_pair'][index0] = (address0, self._offset)
        return address0

    def _read_key(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['key'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_3.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[A-Za-z0-9_]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['key'][index0] = (address0, self._offset)
        return address0

    def _read_value(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['value'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_4.search(chunk0):
                address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address1 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[^\\"]')
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['value'][index0] = (address0, self._offset)
        return address0

    def _read_movetext(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['movetext'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_move()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.make_movetext(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['movetext'][index0] = (address0, self._offset)
        return address0

    def _read_move(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['move'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_move_number()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_dlm()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_dlm()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_san()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_dlm()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                            address6 = FAILURE
                            address6 = self._read_dlm()
                            if address6 is not FAILURE:
                                elements0.append(address6)
                                address7 = FAILURE
                                index2 = self._offset
                                address7 = self._read_nags()
                                if address7 is FAILURE:
                                    address7 = TreeNode(self._input[index2:index2], index2, [])
                                    self._offset = index2
                                if address7 is not FAILURE:
                                    elements0.append(address7)
                                    address8 = FAILURE
                                    address8 = self._read_dlm()
                                    if address8 is not FAILURE:
                                        elements0.append(address8)
                                        address9 = FAILURE
                                        index3 = self._offset
                                        address9 = self._read_comment()
                                        if address9 is FAILURE:
                                            address9 = TreeNode(self._input[index3:index3], index3, [])
                                            self._offset = index3
                                        if address9 is not FAILURE:
                                            elements0.append(address9)
                                            address10 = FAILURE
                                            address10 = self._read_dlm()
                                            if address10 is not FAILURE:
                                                elements0.append(address10)
                                                address11 = FAILURE
                                                index4 = self._offset
                                                address11 = self._read_variations()
                                                if address11 is FAILURE:
                                                    address11 = TreeNode(self._input[index4:index4], index4, [])
                                                    self._offset = index4
                                                if address11 is not FAILURE:
                                                    elements0.append(address11)
                                                    address12 = FAILURE
                                                    address12 = self._read_dlm()
                                                    if address12 is not FAILURE:
                                                        elements0.append(address12)
                                                        address13 = FAILURE
                                                        index5 = self._offset
                                                        address13 = self._read_san()
                                                        if address13 is FAILURE:
                                                            address13 = TreeNode(self._input[index5:index5], index5, [])
                                                            self._offset = index5
                                                        if address13 is not FAILURE:
                                                            elements0.append(address13)
                                                            address14 = FAILURE
                                                            address14 = self._read_dlm()
                                                            if address14 is not FAILURE:
                                                                elements0.append(address14)
                                                                address15 = FAILURE
                                                                index6 = self._offset
                                                                address15 = self._read_nags()
                                                                if address15 is FAILURE:
                                                                    address15 = TreeNode(self._input[index6:index6], index6, [])
                                                                    self._offset = index6
                                                                if address15 is not FAILURE:
                                                                    elements0.append(address15)
                                                                    address16 = FAILURE
                                                                    address16 = self._read_dlm()
                                                                    if address16 is not FAILURE:
                                                                        elements0.append(address16)
                                                                        address17 = FAILURE
                                                                        index7 = self._offset
                                                                        address17 = self._read_comment()
                                                                        if address17 is FAILURE:
                                                                            address17 = TreeNode(self._input[index7:index7], index7, [])
                                                                            self._offset = index7
                                                                        if address17 is not FAILURE:
                                                                            elements0.append(address17)
                                                                            address18 = FAILURE
                                                                            address18 = self._read_dlm()
                                                                            if address18 is not FAILURE:
                                                                                elements0.append(address18)
                                                                                address19 = FAILURE
                                                                                index8 = self._offset
                                                                                address19 = self._read_variations()
                                                                                if address19 is FAILURE:
                                                                                    address19 = TreeNode(self._input[index8:index8], index8, [])
                                                                                    self._offset = index8
                                                                                if address19 is not FAILURE:
                                                                                    elements0.append(address19)
                                                                                    address20 = FAILURE
                                                                                    address20 = self._read_dlm()
                                                                                    if address20 is not FAILURE:
                                                                                        elements0.append(address20)
                                                                                        address21 = FAILURE
                                                                                        index9 = self._offset
                                                                                        address21 = self._read_comment()
                                                                                        if address21 is FAILURE:
                                                                                            address21 = TreeNode(self._input[index9:index9], index9, [])
                                                                                            self._offset = index9
                                                                                        if address21 is not FAILURE:
                                                                                            elements0.append(address21)
                                                                                        else:
                                                                                            elements0 = None
                                                                                            self._offset = index1
                                                                                    else:
                                                                                        elements0 = None
                                                                                        self._offset = index1
                                                                                else:
                                                                                    elements0 = None
                                                                                    self._offset = index1
                                                                            else:
                                                                                elements0 = None
                                                                                self._offset = index1
                                                                        else:
                                                                            elements0 = None
                                                                            self._offset = index1
                                                                    else:
                                                                        elements0 = None
                                                                        self._offset = index1
                                                                else:
                                                                    elements0 = None
                                                                    self._offset = index1
                                                            else:
                                                                elements0 = None
                                                                self._offset = index1
                                                        else:
                                                            elements0 = None
                                                            self._offset = index1
                                                    else:
                                                        elements0 = None
                                                        self._offset = index1
                                                else:
                                                    elements0 = None
                                                    self._offset = index1
                                            else:
                                                elements0 = None
                                                self._offset = index1
                                        else:
                                            elements0 = None
                                            self._offset = index1
                                    else:
                                        elements0 = None
                                        self._offset = index1
                                else:
                                    elements0 = None
                                    self._offset = index1
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode3(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['move'][index0] = (address0, self._offset)
        return address0

    def _read_move_number(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['move_number'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 1, self._offset, [], True
        while address2 is not FAILURE:
            chunk0, max0 = None, self._offset + 1
            if max0 <= self._input_size:
                chunk0 = self._input[self._offset:max0]
            if chunk0 is not None and Grammar.REGEX_5.search(chunk0):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[0-9]')
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '.':
                address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"."')
            if address3 is not FAILURE:
                elements0.append(address3)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['move_number'][index0] = (address0, self._offset)
        return address0

    def _read_san(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['san'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        index2 = self._offset
        index3, elements1 = self._offset, []
        address2 = FAILURE
        address2 = self._read_file()
        if address2 is not FAILURE:
            elements1.append(address2)
            address3 = FAILURE
            address3 = self._read_rank()
            if address3 is not FAILURE:
                elements1.append(address3)
                address4 = FAILURE
                address4 = self._read_dlm()
                if address4 is not FAILURE:
                    elements1.append(address4)
                    address5 = FAILURE
                    address5 = self._read_file()
                    if address5 is not FAILURE:
                        elements1.append(address5)
                        address6 = FAILURE
                        address6 = self._read_rank()
                        if address6 is not FAILURE:
                            elements1.append(address6)
                        else:
                            elements1 = None
                            self._offset = index3
                    else:
                        elements1 = None
                        self._offset = index3
                else:
                    elements1 = None
                    self._offset = index3
            else:
                elements1 = None
                self._offset = index3
        else:
            elements1 = None
            self._offset = index3
        if elements1 is None:
            address1 = FAILURE
        else:
            address1 = TreeNode4(self._input[index3:self._offset], index3, elements1)
            self._offset = self._offset
        if address1 is FAILURE:
            self._offset = index2
            index4, elements2 = self._offset, []
            address7 = FAILURE
            address7 = self._read_file()
            if address7 is not FAILURE:
                elements2.append(address7)
                address8 = FAILURE
                address8 = self._read_rank()
                if address8 is not FAILURE:
                    elements2.append(address8)
                    address9 = FAILURE
                    address9 = self._read_file()
                    if address9 is not FAILURE:
                        elements2.append(address9)
                        address10 = FAILURE
                        address10 = self._read_rank()
                        if address10 is not FAILURE:
                            elements2.append(address10)
                            address11 = FAILURE
                            address11 = self._read_dlm()
                            if address11 is not FAILURE:
                                elements2.append(address11)
                                address12 = FAILURE
                                address12 = self._read_file()
                                if address12 is not FAILURE:
                                    elements2.append(address12)
                                    address13 = FAILURE
                                    address13 = self._read_rank()
                                    if address13 is not FAILURE:
                                        elements2.append(address13)
                                        address14 = FAILURE
                                        address14 = self._read_file()
                                        if address14 is not FAILURE:
                                            elements2.append(address14)
                                            address15 = FAILURE
                                            address15 = self._read_rank()
                                            if address15 is not FAILURE:
                                                elements2.append(address15)
                                            else:
                                                elements2 = None
                                                self._offset = index4
                                        else:
                                            elements2 = None
                                            self._offset = index4
                                    else:
                                        elements2 = None
                                        self._offset = index4
                                else:
                                    elements2 = None
                                    self._offset = index4
                            else:
                                elements2 = None
                                self._offset = index4
                        else:
                            elements2 = None
                            self._offset = index4
                    else:
                        elements2 = None
                        self._offset = index4
                else:
                    elements2 = None
                    self._offset = index4
            else:
                elements2 = None
                self._offset = index4
            if elements2 is None:
                address1 = FAILURE
            else:
                address1 = TreeNode5(self._input[index4:self._offset], index4, elements2)
                self._offset = self._offset
            if address1 is FAILURE:
                self._offset = index2
                index5, elements3 = self._offset, []
                address16 = FAILURE
                address16 = self._read_file()
                if address16 is not FAILURE:
                    elements3.append(address16)
                    address17 = FAILURE
                    address17 = self._read_rank()
                    if address17 is not FAILURE:
                        elements3.append(address17)
                        address18 = FAILURE
                        address18 = self._read_dlm()
                        if address18 is not FAILURE:
                            elements3.append(address18)
                            address19 = FAILURE
                            address19 = self._read_file()
                            if address19 is not FAILURE:
                                elements3.append(address19)
                                address20 = FAILURE
                                address20 = self._read_rank()
                                if address20 is not FAILURE:
                                    elements3.append(address20)
                                    address21 = FAILURE
                                    address21 = self._read_file()
                                    if address21 is not FAILURE:
                                        elements3.append(address21)
                                        address22 = FAILURE
                                        address22 = self._read_rank()
                                        if address22 is not FAILURE:
                                            elements3.append(address22)
                                        else:
                                            elements3 = None
                                            self._offset = index5
                                    else:
                                        elements3 = None
                                        self._offset = index5
                                else:
                                    elements3 = None
                                    self._offset = index5
                            else:
                                elements3 = None
                                self._offset = index5
                        else:
                            elements3 = None
                            self._offset = index5
                    else:
                        elements3 = None
                        self._offset = index5
                else:
                    elements3 = None
                    self._offset = index5
                if elements3 is None:
                    address1 = FAILURE
                else:
                    address1 = TreeNode6(self._input[index5:self._offset], index5, elements3)
                    self._offset = self._offset
                if address1 is FAILURE:
                    self._offset = index2
                    index6, elements4 = self._offset, []
                    address23 = FAILURE
                    address23 = self._read_piece()
                    if address23 is not FAILURE:
                        elements4.append(address23)
                        address24 = FAILURE
                        address24 = self._read_file()
                        if address24 is not FAILURE:
                            elements4.append(address24)
                            address25 = FAILURE
                            address25 = self._read_rank()
                            if address25 is not FAILURE:
                                elements4.append(address25)
                                address26 = FAILURE
                                address26 = self._read_file()
                                if address26 is not FAILURE:
                                    elements4.append(address26)
                                    address27 = FAILURE
                                    address27 = self._read_rank()
                                    if address27 is not FAILURE:
                                        elements4.append(address27)
                                        address28 = FAILURE
                                        address28 = self._read_dlm()
                                        if address28 is not FAILURE:
                                            elements4.append(address28)
                                            address29 = FAILURE
                                            address29 = self._read_piece()
                                            if address29 is not FAILURE:
                                                elements4.append(address29)
                                                address30 = FAILURE
                                                address30 = self._read_file()
                                                if address30 is not FAILURE:
                                                    elements4.append(address30)
                                                    address31 = FAILURE
                                                    address31 = self._read_rank()
                                                    if address31 is not FAILURE:
                                                        elements4.append(address31)
                                                        address32 = FAILURE
                                                        address32 = self._read_file()
                                                        if address32 is not FAILURE:
                                                            elements4.append(address32)
                                                            address33 = FAILURE
                                                            address33 = self._read_rank()
                                                            if address33 is not FAILURE:
                                                                elements4.append(address33)
                                                            else:
                                                                elements4 = None
                                                                self._offset = index6
                                                        else:
                                                            elements4 = None
                                                            self._offset = index6
                                                    else:
                                                        elements4 = None
                                                        self._offset = index6
                                                else:
                                                    elements4 = None
                                                    self._offset = index6
                                            else:
                                                elements4 = None
                                                self._offset = index6
                                        else:
                                            elements4 = None
                                            self._offset = index6
                                    else:
                                        elements4 = None
                                        self._offset = index6
                                else:
                                    elements4 = None
                                    self._offset = index6
                            else:
                                elements4 = None
                                self._offset = index6
                        else:
                            elements4 = None
                            self._offset = index6
                    else:
                        elements4 = None
                        self._offset = index6
                    if elements4 is None:
                        address1 = FAILURE
                    else:
                        address1 = TreeNode7(self._input[index6:self._offset], index6, elements4)
                        self._offset = self._offset
                    if address1 is FAILURE:
                        self._offset = index2
                        index7, elements5 = self._offset, []
                        address34 = FAILURE
                        address34 = self._read_piece()
                        if address34 is not FAILURE:
                            elements5.append(address34)
                            address35 = FAILURE
                            address35 = self._read_file()
                            if address35 is not FAILURE:
                                elements5.append(address35)
                                address36 = FAILURE
                                address36 = self._read_rank()
                                if address36 is not FAILURE:
                                    elements5.append(address36)
                                    address37 = FAILURE
                                    address37 = self._read_file()
                                    if address37 is not FAILURE:
                                        elements5.append(address37)
                                        address38 = FAILURE
                                        address38 = self._read_rank()
                                        if address38 is not FAILURE:
                                            elements5.append(address38)
                                            address39 = FAILURE
                                            address39 = self._read_dlm()
                                            if address39 is not FAILURE:
                                                elements5.append(address39)
                                                address40 = FAILURE
                                                address40 = self._read_file()
                                                if address40 is not FAILURE:
                                                    elements5.append(address40)
                                                    address41 = FAILURE
                                                    address41 = self._read_rank()
                                                    if address41 is not FAILURE:
                                                        elements5.append(address41)
                                                        address42 = FAILURE
                                                        address42 = self._read_file()
                                                        if address42 is not FAILURE:
                                                            elements5.append(address42)
                                                            address43 = FAILURE
                                                            address43 = self._read_rank()
                                                            if address43 is not FAILURE:
                                                                elements5.append(address43)
                                                            else:
                                                                elements5 = None
                                                                self._offset = index7
                                                        else:
                                                            elements5 = None
                                                            self._offset = index7
                                                    else:
                                                        elements5 = None
                                                        self._offset = index7
                                                else:
                                                    elements5 = None
                                                    self._offset = index7
                                            else:
                                                elements5 = None
                                                self._offset = index7
                                        else:
                                            elements5 = None
                                            self._offset = index7
                                    else:
                                        elements5 = None
                                        self._offset = index7
                                else:
                                    elements5 = None
                                    self._offset = index7
                            else:
                                elements5 = None
                                self._offset = index7
                        else:
                            elements5 = None
                            self._offset = index7
                        if elements5 is None:
                            address1 = FAILURE
                        else:
                            address1 = TreeNode8(self._input[index7:self._offset], index7, elements5)
                            self._offset = self._offset
                        if address1 is FAILURE:
                            self._offset = index2
                            index8, elements6 = self._offset, []
                            address44 = FAILURE
                            address44 = self._read_file()
                            if address44 is not FAILURE:
                                elements6.append(address44)
                                address45 = FAILURE
                                address45 = self._read_rank()
                                if address45 is not FAILURE:
                                    elements6.append(address45)
                                    address46 = FAILURE
                                    address46 = self._read_file()
                                    if address46 is not FAILURE:
                                        elements6.append(address46)
                                        address47 = FAILURE
                                        address47 = self._read_rank()
                                        if address47 is not FAILURE:
                                            elements6.append(address47)
                                            address48 = FAILURE
                                            address48 = self._read_dlm()
                                            if address48 is not FAILURE:
                                                elements6.append(address48)
                                                address49 = FAILURE
                                                address49 = self._read_piece()
                                                if address49 is not FAILURE:
                                                    elements6.append(address49)
                                                    address50 = FAILURE
                                                    address50 = self._read_file()
                                                    if address50 is not FAILURE:
                                                        elements6.append(address50)
                                                        address51 = FAILURE
                                                        address51 = self._read_rank()
                                                        if address51 is not FAILURE:
                                                            elements6.append(address51)
                                                            address52 = FAILURE
                                                            address52 = self._read_file()
                                                            if address52 is not FAILURE:
                                                                elements6.append(address52)
                                                                address53 = FAILURE
                                                                address53 = self._read_rank()
                                                                if address53 is not FAILURE:
                                                                    elements6.append(address53)
                                                                else:
                                                                    elements6 = None
                                                                    self._offset = index8
                                                            else:
                                                                elements6 = None
                                                                self._offset = index8
                                                        else:
                                                            elements6 = None
                                                            self._offset = index8
                                                    else:
                                                        elements6 = None
                                                        self._offset = index8
                                                else:
                                                    elements6 = None
                                                    self._offset = index8
                                            else:
                                                elements6 = None
                                                self._offset = index8
                                        else:
                                            elements6 = None
                                            self._offset = index8
                                    else:
                                        elements6 = None
                                        self._offset = index8
                                else:
                                    elements6 = None
                                    self._offset = index8
                            else:
                                elements6 = None
                                self._offset = index8
                            if elements6 is None:
                                address1 = FAILURE
                            else:
                                address1 = TreeNode9(self._input[index8:self._offset], index8, elements6)
                                self._offset = self._offset
                            if address1 is FAILURE:
                                self._offset = index2
                                address1 = self._read_square()
                                if address1 is FAILURE:
                                    self._offset = index2
                                    address1 = self._read_san_psq()
                                    if address1 is FAILURE:
                                        self._offset = index2
                                        index9, elements7 = self._offset, []
                                        address54 = FAILURE
                                        address54 = self._read_file()
                                        if address54 is not FAILURE:
                                            elements7.append(address54)
                                            address55 = FAILURE
                                            address55 = self._read_takes()
                                            if address55 is not FAILURE:
                                                elements7.append(address55)
                                                address56 = FAILURE
                                                address56 = self._read_square()
                                                if address56 is not FAILURE:
                                                    elements7.append(address56)
                                                else:
                                                    elements7 = None
                                                    self._offset = index9
                                            else:
                                                elements7 = None
                                                self._offset = index9
                                        else:
                                            elements7 = None
                                            self._offset = index9
                                        if elements7 is None:
                                            address1 = FAILURE
                                        else:
                                            address1 = TreeNode10(self._input[index9:self._offset], index9, elements7)
                                            self._offset = self._offset
                                        if address1 is FAILURE:
                                            self._offset = index2
                                            address1 = self._read_castle()
                                            if address1 is FAILURE:
                                                self._offset = index2
                                                address1 = self._read_blacks_move()
                                                if address1 is FAILURE:
                                                    self._offset = index2
        if address1 is not FAILURE:
            elements0.append(address1)
            address57 = FAILURE
            index10 = self._offset
            address57 = self._read_promotes()
            if address57 is FAILURE:
                address57 = TreeNode(self._input[index10:index10], index10, [])
                self._offset = index10
            if address57 is not FAILURE:
                elements0.append(address57)
                address58 = FAILURE
                index11 = self._offset
                address58 = self._read_check()
                if address58 is FAILURE:
                    address58 = TreeNode(self._input[index11:index11], index11, [])
                    self._offset = index11
                if address58 is not FAILURE:
                    elements0.append(address58)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['san'][index0] = (address0, self._offset)
        return address0

    def _read_san_psq(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['san_psq'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        index2, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_piece()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_square()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                index3 = self._offset
                address3 = self._read_takes()
                if address3 is FAILURE:
                    address3 = TreeNode(self._input[index3:index3], index3, [])
                    self._offset = index3
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    address4 = self._read_square()
                    if address4 is not FAILURE:
                        elements0.append(address4)
                    else:
                        elements0 = None
                        self._offset = index2
                else:
                    elements0 = None
                    self._offset = index2
            else:
                elements0 = None
                self._offset = index2
        else:
            elements0 = None
            self._offset = index2
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode11(self._input[index2:self._offset], index2, elements0)
            self._offset = self._offset
        if address0 is FAILURE:
            self._offset = index1
            index4, elements1 = self._offset, []
            address5 = FAILURE
            address5 = self._read_piece()
            if address5 is not FAILURE:
                elements1.append(address5)
                address6 = FAILURE
                index5 = self._offset
                address6 = self._read_takes()
                if address6 is FAILURE:
                    address6 = TreeNode(self._input[index5:index5], index5, [])
                    self._offset = index5
                if address6 is not FAILURE:
                    elements1.append(address6)
                    address7 = FAILURE
                    address7 = self._read_square()
                    if address7 is not FAILURE:
                        elements1.append(address7)
                    else:
                        elements1 = None
                        self._offset = index4
                else:
                    elements1 = None
                    self._offset = index4
            else:
                elements1 = None
                self._offset = index4
            if elements1 is None:
                address0 = FAILURE
            else:
                address0 = TreeNode12(self._input[index4:self._offset], index4, elements1)
                self._offset = self._offset
            if address0 is FAILURE:
                self._offset = index1
                index6, elements2 = self._offset, []
                address8 = FAILURE
                address8 = self._read_piece()
                if address8 is not FAILURE:
                    elements2.append(address8)
                    address9 = FAILURE
                    address9 = self._read_file()
                    if address9 is not FAILURE:
                        elements2.append(address9)
                        address10 = FAILURE
                        index7 = self._offset
                        address10 = self._read_takes()
                        if address10 is FAILURE:
                            address10 = TreeNode(self._input[index7:index7], index7, [])
                            self._offset = index7
                        if address10 is not FAILURE:
                            elements2.append(address10)
                            address11 = FAILURE
                            address11 = self._read_square()
                            if address11 is not FAILURE:
                                elements2.append(address11)
                            else:
                                elements2 = None
                                self._offset = index6
                        else:
                            elements2 = None
                            self._offset = index6
                    else:
                        elements2 = None
                        self._offset = index6
                else:
                    elements2 = None
                    self._offset = index6
                if elements2 is None:
                    address0 = FAILURE
                else:
                    address0 = TreeNode13(self._input[index6:self._offset], index6, elements2)
                    self._offset = self._offset
                if address0 is FAILURE:
                    self._offset = index1
                    index8, elements3 = self._offset, []
                    address12 = FAILURE
                    address12 = self._read_piece()
                    if address12 is not FAILURE:
                        elements3.append(address12)
                        address13 = FAILURE
                        address13 = self._read_rank()
                        if address13 is not FAILURE:
                            elements3.append(address13)
                            address14 = FAILURE
                            index9 = self._offset
                            address14 = self._read_takes()
                            if address14 is FAILURE:
                                address14 = TreeNode(self._input[index9:index9], index9, [])
                                self._offset = index9
                            if address14 is not FAILURE:
                                elements3.append(address14)
                                address15 = FAILURE
                                address15 = self._read_square()
                                if address15 is not FAILURE:
                                    elements3.append(address15)
                                else:
                                    elements3 = None
                                    self._offset = index8
                            else:
                                elements3 = None
                                self._offset = index8
                        else:
                            elements3 = None
                            self._offset = index8
                    else:
                        elements3 = None
                        self._offset = index8
                    if elements3 is None:
                        address0 = FAILURE
                    else:
                        address0 = TreeNode14(self._input[index8:self._offset], index8, elements3)
                        self._offset = self._offset
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['san_psq'][index0] = (address0, self._offset)
        return address0

    def _read_piece(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['piece'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_6.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[KQRNBP]')
        self._cache['piece'][index0] = (address0, self._offset)
        return address0

    def _read_disam(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['disam'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_square()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_file()
            if address0 is FAILURE:
                self._offset = index1
                address0 = self._read_rank()
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['disam'][index0] = (address0, self._offset)
        return address0

    def _read_odisam(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['odisam'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        address0 = self._read_square()
        if address0 is FAILURE:
            self._offset = index1
            address0 = self._read_disam()
            if address0 is FAILURE:
                self._offset = index1
        self._cache['odisam'][index0] = (address0, self._offset)
        return address0

    def _read_takes(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['takes'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'x':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"x"')
        self._cache['takes'][index0] = (address0, self._offset)
        return address0

    def _read_square(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['square'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        address1 = self._read_file()
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_rank()
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode15(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['square'][index0] = (address0, self._offset)
        return address0

    def _read_file(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['file'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_7.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[a-h]')
        self._cache['file'][index0] = (address0, self._offset)
        return address0

    def _read_rank(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['rank'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_8.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[1-8]')
        self._cache['rank'][index0] = (address0, self._offset)
        return address0

    def _read_promotes(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['promotes'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '=':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"="')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            chunk1, max1 = None, self._offset + 1
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 is not None and Grammar.REGEX_9.search(chunk1):
                address2 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                self._offset = self._offset + 1
            else:
                address2 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('[KQRNB]')
            if address2 is not FAILURE:
                elements0.append(address2)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['promotes'][index0] = (address0, self._offset)
        return address0

    def _read_check(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['check'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_10.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[+#]')
        self._cache['check'][index0] = (address0, self._offset)
        return address0

    def _read_castle(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['castle'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 5
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == 'O-O-O':
            address0 = TreeNode(self._input[self._offset:self._offset + 5], self._offset, [])
            self._offset = self._offset + 5
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"O-O-O"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 3
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == 'O-O':
                address0 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                self._offset = self._offset + 3
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"O-O"')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 4
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == 'e1g1':
                    address0 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                    self._offset = self._offset + 4
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"e1g1"')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 4
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == 'e8g8':
                        address0 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                        self._offset = self._offset + 4
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('"e8g8"')
                    if address0 is FAILURE:
                        self._offset = index1
                        chunk4, max4 = None, self._offset + 4
                        if max4 <= self._input_size:
                            chunk4 = self._input[self._offset:max4]
                        if chunk4 == 'e1c1':
                            address0 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                            self._offset = self._offset + 4
                        else:
                            address0 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('"e1c1"')
                        if address0 is FAILURE:
                            self._offset = index1
                            chunk5, max5 = None, self._offset + 4
                            if max5 <= self._input_size:
                                chunk5 = self._input[self._offset:max5]
                            if chunk5 == 'e8c8':
                                address0 = TreeNode(self._input[self._offset:self._offset + 4], self._offset, [])
                                self._offset = self._offset + 4
                            else:
                                address0 = FAILURE
                                if self._offset > self._failure:
                                    self._failure = self._offset
                                    self._expected = []
                                if self._offset == self._failure:
                                    self._expected.append('"e8c8"')
                            if address0 is FAILURE:
                                self._offset = index1
        self._cache['castle'][index0] = (address0, self._offset)
        return address0

    def _read_comment(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['comment'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '{':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"{"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_11.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[^\\}]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                chunk2, max2 = None, self._offset + 1
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '}':
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"}"')
                if address4 is not FAILURE:
                    elements0.append(address4)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['comment'][index0] = (address0, self._offset)
        return address0

    def _read_blacks_move(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['blacks_move'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 2
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '..':
            address0 = TreeNode(self._input[self._offset:self._offset + 2], self._offset, [])
            self._offset = self._offset + 2
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('".."')
        self._cache['blacks_move'][index0] = (address0, self._offset)
        return address0

    def _read_cblacks_move(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['cblacks_move'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '...':
            address0 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
            self._offset = self._offset + 3
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"..."')
        self._cache['cblacks_move'][index0] = (address0, self._offset)
        return address0

    def _read_nags(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['nags'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_nag()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['nags'][index0] = (address0, self._offset)
        return address0

    def _read_nag(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['nag'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '$':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"$"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 1, self._offset, [], True
            while address3 is not FAILURE:
                chunk1, max1 = None, self._offset + 1
                if max1 <= self._input_size:
                    chunk1 = self._input[self._offset:max1]
                if chunk1 is not None and Grammar.REGEX_12.search(chunk1):
                    address3 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                    self._offset = self._offset + 1
                else:
                    address3 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('[0-9]')
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address4 = FAILURE
                address4 = self._read_dlm()
                if address4 is not FAILURE:
                    elements0.append(address4)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode16(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['nag'][index0] = (address0, self._offset)
        return address0

    def _read_variations(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['variations'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_variation()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = self._actions.make_variations(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['variations'][index0] = (address0, self._offset)
        return address0

    def _read_variation(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['variation'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '(':
            address1 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"("')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            address2 = self._read_dlm()
            if address2 is not FAILURE:
                elements0.append(address2)
                address3 = FAILURE
                address3 = self._read_movetext()
                if address3 is not FAILURE:
                    elements0.append(address3)
                    address4 = FAILURE
                    chunk1, max1 = None, self._offset + 1
                    if max1 <= self._input_size:
                        chunk1 = self._input[self._offset:max1]
                    if chunk1 == ')':
                        address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address4 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('")"')
                    if address4 is not FAILURE:
                        elements0.append(address4)
                        address5 = FAILURE
                        address5 = self._read_dlm()
                        if address5 is not FAILURE:
                            elements0.append(address5)
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = self._actions.make_variation(self._input, index1, self._offset, elements0)
            self._offset = self._offset
        self._cache['variation'][index0] = (address0, self._offset)
        return address0

    def _read_score(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['score'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 3
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 == '1-0':
            address0 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
            self._offset = self._offset + 3
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"1-0"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1, max1 = None, self._offset + 3
            if max1 <= self._input_size:
                chunk1 = self._input[self._offset:max1]
            if chunk1 == '0-1':
                address0 = TreeNode(self._input[self._offset:self._offset + 3], self._offset, [])
                self._offset = self._offset + 3
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"0-1"')
            if address0 is FAILURE:
                self._offset = index1
                chunk2, max2 = None, self._offset + 7
                if max2 <= self._input_size:
                    chunk2 = self._input[self._offset:max2]
                if chunk2 == '1/2-1/2':
                    address0 = TreeNode(self._input[self._offset:self._offset + 7], self._offset, [])
                    self._offset = self._offset + 7
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"1/2-1/2"')
                if address0 is FAILURE:
                    self._offset = index1
                    chunk3, max3 = None, self._offset + 1
                    if max3 <= self._input_size:
                        chunk3 = self._input[self._offset:max3]
                    if chunk3 == '*':
                        address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
                        self._offset = self._offset + 1
                    else:
                        address0 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('"*"')
                    if address0 is FAILURE:
                        self._offset = index1
        self._cache['score'][index0] = (address0, self._offset)
        return address0

    def _read_dlm(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['dlm'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0, max0 = None, self._offset + 1
        if max0 <= self._input_size:
            chunk0 = self._input[self._offset:max0]
        if chunk0 is not None and Grammar.REGEX_13.search(chunk0):
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset, [])
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('[\\s+]')
        if address0 is FAILURE:
            address0 = TreeNode(self._input[index1:index1], index1, [])
            self._offset = index1
        self._cache['dlm'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_game()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()

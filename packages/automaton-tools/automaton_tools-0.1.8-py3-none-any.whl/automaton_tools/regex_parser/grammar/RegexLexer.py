# Generated from C:/Users/xiaochent/Downloads/automaton_tools-master/automaton_tools/regex_parser/grammar\Regex.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\5\23S\n\23\3\24\3\24\3")
        buf.write("\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26\3\2\4\6\2\"\61<B]b}\u0080\r\2C\\aac|\u00c2\u00d8")
        buf.write("\u00da\u00f8\u00fa\u2001\u3042\u3191\u3302\u3381\u3402")
        buf.write("\u3d2f\u4e02\ua001\uf902\ufb01\2Y\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2\t\61\3\2")
        buf.write("\2\2\13\63\3\2\2\2\r\65\3\2\2\2\17\67\3\2\2\2\219\3\2")
        buf.write("\2\2\23;\3\2\2\2\25=\3\2\2\2\27?\3\2\2\2\31A\3\2\2\2\33")
        buf.write("C\3\2\2\2\35F\3\2\2\2\37H\3\2\2\2!J\3\2\2\2#L\3\2\2\2")
        buf.write("%N\3\2\2\2\'T\3\2\2\2)V\3\2\2\2+,\7,\2\2,\4\3\2\2\2-.")
        buf.write("\7-\2\2.\6\3\2\2\2/\60\7}\2\2\60\b\3\2\2\2\61\62\7.\2")
        buf.write("\2\62\n\3\2\2\2\63\64\7\177\2\2\64\f\3\2\2\2\65\66\7A")
        buf.write("\2\2\66\16\3\2\2\2\678\7~\2\28\20\3\2\2\29:\7*\2\2:\22")
        buf.write("\3\2\2\2;<\7+\2\2<\24\3\2\2\2=>\7\60\2\2>\26\3\2\2\2?")
        buf.write("@\7&\2\2@\30\3\2\2\2AB\7`\2\2B\32\3\2\2\2CD\7]\2\2DE\7")
        buf.write("`\2\2E\34\3\2\2\2FG\7_\2\2G\36\3\2\2\2HI\7]\2\2I \3\2")
        buf.write("\2\2JK\7/\2\2K\"\3\2\2\2LM\4\62;\2M$\3\2\2\2NR\7^\2\2")
        buf.write("OS\5\'\24\2PS\5)\25\2QS\5#\22\2RO\3\2\2\2RP\3\2\2\2RQ")
        buf.write("\3\2\2\2S&\3\2\2\2TU\t\2\2\2U(\3\2\2\2VW\t\3\2\2W*\3\2")
        buf.write("\2\2\4\2R\2")
        return buf.getvalue()


class RegexLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    Digit = 17
    EscapedChar = 18
    Punctuation = 19
    Letter = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'+'", "'{'", "','", "'}'", "'?'", "'|'", "'('", "')'", 
            "'.'", "'$'", "'^'", "'[^'", "']'", "'['", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "Digit", "EscapedChar", "Punctuation", "Letter" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "Digit", "EscapedChar", "Punctuation", 
                  "Letter" ]

    grammarFileName = "Regex.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



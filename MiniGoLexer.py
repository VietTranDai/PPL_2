# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


#2213951
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u020b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\7\66\u0154\n\66\f\66\16\66\u0157\13\66\3\67\3\67")
        buf.write("\3\67\38\38\58\u015e\n8\39\39\79\u0162\n9\f9\169\u0165")
        buf.write("\139\39\39\3:\3:\7:\u016b\n:\f:\16:\u016e\13:\3:\3:\5")
        buf.write(":\u0172\n:\3:\5:\u0175\n:\3:\3:\3;\3;\7;\u017b\n;\f;\16")
        buf.write(";\u017e\13;\3;\3;\3;\3;\3<\3<\7<\u0186\n<\f<\16<\u0189")
        buf.write("\13<\3<\5<\u018c\n<\3=\3=\3=\3=\6=\u0192\n=\r=\16=\u0193")
        buf.write("\3=\3=\3=\3=\6=\u019a\n=\r=\16=\u019b\5=\u019e\n=\3>\3")
        buf.write(">\3>\3>\6>\u01a4\n>\r>\16>\u01a5\3>\3>\3>\3>\6>\u01ac")
        buf.write("\n>\r>\16>\u01ad\5>\u01b0\n>\3?\3?\3?\3?\6?\u01b6\n?\r")
        buf.write("?\16?\u01b7\3?\3?\3?\3?\6?\u01be\n?\r?\16?\u01bf\5?\u01c2")
        buf.write("\n?\3@\3@\3@\3@\5@\u01c8\n@\3A\6A\u01cb\nA\rA\16A\u01cc")
        buf.write("\3A\3A\7A\u01d1\nA\fA\16A\u01d4\13A\3A\3A\5A\u01d8\nA")
        buf.write("\3A\6A\u01db\nA\rA\16A\u01dc\5A\u01df\nA\3B\3B\3B\3B\7")
        buf.write("B\u01e5\nB\fB\16B\u01e8\13B\3B\3B\3C\3C\3C\3C\3C\7C\u01f1")
        buf.write("\nC\fC\16C\u01f4\13C\3C\3C\3C\3C\3C\3D\5D\u01fc\nD\3D")
        buf.write("\3D\3D\3D\3E\6E\u0203\nE\rE\16E\u0204\3E\3E\3F\3F\3F\3")
        buf.write("\u01f2\2G\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m\2o\2q8s9u:w\2y\2{\2}\2\177;\u0081<\u0083=\u0085>")
        buf.write("\u0087?\u0089@\u008bA\3\2\17\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\7\2$$^^ppttvv\6\2\f\f\17\17$$^^\3\2\63;\3\2\62;\3\2")
        buf.write("\62\63\3\2\629\5\2\62;CHch\4\2GGgg\4\2--//\4\2\f\f\16")
        buf.write("\17\5\2\13\13\16\17\"\"\2\u0223\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2\177\3\2\2")
        buf.write("\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\3\u008d\3\2\2")
        buf.write("\2\5\u0092\3\2\2\2\7\u0096\3\2\2\2\t\u009c\3\2\2\2\13")
        buf.write("\u009f\3\2\2\2\r\u00a4\3\2\2\2\17\u00a8\3\2\2\2\21\u00af")
        buf.write("\3\2\2\2\23\u00b4\3\2\2\2\25\u00b9\3\2\2\2\27\u00c0\3")
        buf.write("\2\2\2\31\u00ca\3\2\2\2\33\u00d1\3\2\2\2\35\u00d5\3\2")
        buf.write("\2\2\37\u00db\3\2\2\2!\u00e3\3\2\2\2#\u00ec\3\2\2\2%\u00f2")
        buf.write("\3\2\2\2\'\u00f8\3\2\2\2)\u00fd\3\2\2\2+\u0103\3\2\2\2")
        buf.write("-\u0107\3\2\2\2/\u0109\3\2\2\2\61\u010b\3\2\2\2\63\u010d")
        buf.write("\3\2\2\2\65\u010f\3\2\2\2\67\u0111\3\2\2\29\u0114\3\2")
        buf.write("\2\2;\u0117\3\2\2\2=\u011a\3\2\2\2?\u011d\3\2\2\2A\u011f")
        buf.write("\3\2\2\2C\u0121\3\2\2\2E\u0124\3\2\2\2G\u0127\3\2\2\2")
        buf.write("I\u0129\3\2\2\2K\u012b\3\2\2\2M\u012e\3\2\2\2O\u0131\3")
        buf.write("\2\2\2Q\u0134\3\2\2\2S\u0137\3\2\2\2U\u013a\3\2\2\2W\u013d")
        buf.write("\3\2\2\2Y\u013f\3\2\2\2[\u0141\3\2\2\2]\u0143\3\2\2\2")
        buf.write("_\u0145\3\2\2\2a\u0147\3\2\2\2c\u0149\3\2\2\2e\u014b\3")
        buf.write("\2\2\2g\u014d\3\2\2\2i\u014f\3\2\2\2k\u0151\3\2\2\2m\u0158")
        buf.write("\3\2\2\2o\u015d\3\2\2\2q\u015f\3\2\2\2s\u0168\3\2\2\2")
        buf.write("u\u0178\3\2\2\2w\u018b\3\2\2\2y\u019d\3\2\2\2{\u01af\3")
        buf.write("\2\2\2}\u01c1\3\2\2\2\177\u01c7\3\2\2\2\u0081\u01ca\3")
        buf.write("\2\2\2\u0083\u01e0\3\2\2\2\u0085\u01eb\3\2\2\2\u0087\u01fb")
        buf.write("\3\2\2\2\u0089\u0202\3\2\2\2\u008b\u0208\3\2\2\2\u008d")
        buf.write("\u008e\7o\2\2\u008e\u008f\7c\2\2\u008f\u0090\7k\2\2\u0090")
        buf.write("\u0091\7p\2\2\u0091\4\3\2\2\2\u0092\u0093\7x\2\2\u0093")
        buf.write("\u0094\7c\2\2\u0094\u0095\7t\2\2\u0095\6\3\2\2\2\u0096")
        buf.write("\u0097\7e\2\2\u0097\u0098\7q\2\2\u0098\u0099\7p\2\2\u0099")
        buf.write("\u009a\7u\2\2\u009a\u009b\7v\2\2\u009b\b\3\2\2\2\u009c")
        buf.write("\u009d\7k\2\2\u009d\u009e\7h\2\2\u009e\n\3\2\2\2\u009f")
        buf.write("\u00a0\7g\2\2\u00a0\u00a1\7n\2\2\u00a1\u00a2\7u\2\2\u00a2")
        buf.write("\u00a3\7g\2\2\u00a3\f\3\2\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\u00a6\7q\2\2\u00a6\u00a7\7t\2\2\u00a7\16\3\2\2\2\u00a8")
        buf.write("\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7v\2\2\u00ab")
        buf.write("\u00ac\7w\2\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7p\2\2\u00ae")
        buf.write("\20\3\2\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7w\2\2\u00b1")
        buf.write("\u00b2\7p\2\2\u00b2\u00b3\7e\2\2\u00b3\22\3\2\2\2\u00b4")
        buf.write("\u00b5\7v\2\2\u00b5\u00b6\7{\2\2\u00b6\u00b7\7r\2\2\u00b7")
        buf.write("\u00b8\7g\2\2\u00b8\24\3\2\2\2\u00b9\u00ba\7u\2\2\u00ba")
        buf.write("\u00bb\7v\2\2\u00bb\u00bc\7t\2\2\u00bc\u00bd\7w\2\2\u00bd")
        buf.write("\u00be\7e\2\2\u00be\u00bf\7v\2\2\u00bf\26\3\2\2\2\u00c0")
        buf.write("\u00c1\7k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7h\2\2\u00c6")
        buf.write("\u00c7\7c\2\2\u00c7\u00c8\7e\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\30\3\2\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7v\2\2\u00cc")
        buf.write("\u00cd\7t\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf\7p\2\2\u00cf")
        buf.write("\u00d0\7i\2\2\u00d0\32\3\2\2\2\u00d1\u00d2\7k\2\2\u00d2")
        buf.write("\u00d3\7p\2\2\u00d3\u00d4\7v\2\2\u00d4\34\3\2\2\2\u00d5")
        buf.write("\u00d6\7h\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7q\2\2\u00d8")
        buf.write("\u00d9\7c\2\2\u00d9\u00da\7v\2\2\u00da\36\3\2\2\2\u00db")
        buf.write("\u00dc\7d\2\2\u00dc\u00dd\7q\2\2\u00dd\u00de\7q\2\2\u00de")
        buf.write("\u00df\7n\2\2\u00df\u00e0\7g\2\2\u00e0\u00e1\7c\2\2\u00e1")
        buf.write("\u00e2\7p\2\2\u00e2 \3\2\2\2\u00e3\u00e4\7e\2\2\u00e4")
        buf.write("\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7\7v\2\2\u00e7")
        buf.write("\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7w\2\2\u00ea")
        buf.write("\u00eb\7g\2\2\u00eb\"\3\2\2\2\u00ec\u00ed\7d\2\2\u00ed")
        buf.write("\u00ee\7t\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0")
        buf.write("\u00f1\7m\2\2\u00f1$\3\2\2\2\u00f2\u00f3\7t\2\2\u00f3")
        buf.write("\u00f4\7c\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6\7i\2\2\u00f6")
        buf.write("\u00f7\7g\2\2\u00f7&\3\2\2\2\u00f8\u00f9\7v\2\2\u00f9")
        buf.write("\u00fa\7t\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("(\3\2\2\2\u00fd\u00fe\7h\2\2\u00fe\u00ff\7c\2\2\u00ff")
        buf.write("\u0100\7n\2\2\u0100\u0101\7u\2\2\u0101\u0102\7g\2\2\u0102")
        buf.write("*\3\2\2\2\u0103\u0104\7p\2\2\u0104\u0105\7k\2\2\u0105")
        buf.write("\u0106\7n\2\2\u0106,\3\2\2\2\u0107\u0108\7-\2\2\u0108")
        buf.write(".\3\2\2\2\u0109\u010a\7/\2\2\u010a\60\3\2\2\2\u010b\u010c")
        buf.write("\7,\2\2\u010c\62\3\2\2\2\u010d\u010e\7\61\2\2\u010e\64")
        buf.write("\3\2\2\2\u010f\u0110\7\'\2\2\u0110\66\3\2\2\2\u0111\u0112")
        buf.write("\7(\2\2\u0112\u0113\7(\2\2\u01138\3\2\2\2\u0114\u0115")
        buf.write("\7~\2\2\u0115\u0116\7~\2\2\u0116:\3\2\2\2\u0117\u0118")
        buf.write("\7?\2\2\u0118\u0119\7?\2\2\u0119<\3\2\2\2\u011a\u011b")
        buf.write("\7#\2\2\u011b\u011c\7?\2\2\u011c>\3\2\2\2\u011d\u011e")
        buf.write("\7>\2\2\u011e@\3\2\2\2\u011f\u0120\7@\2\2\u0120B\3\2\2")
        buf.write("\2\u0121\u0122\7>\2\2\u0122\u0123\7?\2\2\u0123D\3\2\2")
        buf.write("\2\u0124\u0125\7@\2\2\u0125\u0126\7?\2\2\u0126F\3\2\2")
        buf.write("\2\u0127\u0128\7#\2\2\u0128H\3\2\2\2\u0129\u012a\7?\2")
        buf.write("\2\u012aJ\3\2\2\2\u012b\u012c\7-\2\2\u012c\u012d\7?\2")
        buf.write("\2\u012dL\3\2\2\2\u012e\u012f\7/\2\2\u012f\u0130\7?\2")
        buf.write("\2\u0130N\3\2\2\2\u0131\u0132\7,\2\2\u0132\u0133\7?\2")
        buf.write("\2\u0133P\3\2\2\2\u0134\u0135\7\61\2\2\u0135\u0136\7?")
        buf.write("\2\2\u0136R\3\2\2\2\u0137\u0138\7\'\2\2\u0138\u0139\7")
        buf.write("?\2\2\u0139T\3\2\2\2\u013a\u013b\7<\2\2\u013b\u013c\7")
        buf.write("?\2\2\u013cV\3\2\2\2\u013d\u013e\7]\2\2\u013eX\3\2\2\2")
        buf.write("\u013f\u0140\7_\2\2\u0140Z\3\2\2\2\u0141\u0142\7}\2\2")
        buf.write("\u0142\\\3\2\2\2\u0143\u0144\7\177\2\2\u0144^\3\2\2\2")
        buf.write("\u0145\u0146\7*\2\2\u0146`\3\2\2\2\u0147\u0148\7+\2\2")
        buf.write("\u0148b\3\2\2\2\u0149\u014a\7.\2\2\u014ad\3\2\2\2\u014b")
        buf.write("\u014c\7=\2\2\u014cf\3\2\2\2\u014d\u014e\7<\2\2\u014e")
        buf.write("h\3\2\2\2\u014f\u0150\7\60\2\2\u0150j\3\2\2\2\u0151\u0155")
        buf.write("\t\2\2\2\u0152\u0154\t\3\2\2\u0153\u0152\3\2\2\2\u0154")
        buf.write("\u0157\3\2\2\2\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2")
        buf.write("\u0156l\3\2\2\2\u0157\u0155\3\2\2\2\u0158\u0159\7^\2\2")
        buf.write("\u0159\u015a\t\4\2\2\u015an\3\2\2\2\u015b\u015e\n\5\2")
        buf.write("\2\u015c\u015e\5m\67\2\u015d\u015b\3\2\2\2\u015d\u015c")
        buf.write("\3\2\2\2\u015ep\3\2\2\2\u015f\u0163\7$\2\2\u0160\u0162")
        buf.write("\5o8\2\u0161\u0160\3\2\2\2\u0162\u0165\3\2\2\2\u0163\u0161")
        buf.write("\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0166\3\2\2\2\u0165")
        buf.write("\u0163\3\2\2\2\u0166\u0167\7$\2\2\u0167r\3\2\2\2\u0168")
        buf.write("\u016c\7$\2\2\u0169\u016b\5o8\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u0174\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0175\7")
        buf.write("\2\2\3\u0170\u0172\7\17\2\2\u0171\u0170\3\2\2\2\u0171")
        buf.write("\u0172\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0175\7\f\2\2")
        buf.write("\u0174\u016f\3\2\2\2\u0174\u0171\3\2\2\2\u0175\u0176\3")
        buf.write("\2\2\2\u0176\u0177\b:\2\2\u0177t\3\2\2\2\u0178\u017c\7")
        buf.write("$\2\2\u0179\u017b\5o8\2\u017a\u0179\3\2\2\2\u017b\u017e")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017f\3\2\2\2\u017e\u017c\3\2\2\2\u017f\u0180\7^\2\2")
        buf.write("\u0180\u0181\n\4\2\2\u0181\u0182\b;\3\2\u0182v\3\2\2\2")
        buf.write("\u0183\u0187\t\6\2\2\u0184\u0186\t\7\2\2\u0185\u0184\3")
        buf.write("\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0188")
        buf.write("\3\2\2\2\u0188\u018c\3\2\2\2\u0189\u0187\3\2\2\2\u018a")
        buf.write("\u018c\7\62\2\2\u018b\u0183\3\2\2\2\u018b\u018a\3\2\2")
        buf.write("\2\u018cx\3\2\2\2\u018d\u018e\7\62\2\2\u018e\u018f\7d")
        buf.write("\2\2\u018f\u0191\3\2\2\2\u0190\u0192\t\b\2\2\u0191\u0190")
        buf.write("\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0191\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194\u019e\3\2\2\2\u0195\u0196\7\62\2")
        buf.write("\2\u0196\u0197\7D\2\2\u0197\u0199\3\2\2\2\u0198\u019a")
        buf.write("\t\b\2\2\u0199\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b")
        buf.write("\u0199\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019e\3\2\2\2")
        buf.write("\u019d\u018d\3\2\2\2\u019d\u0195\3\2\2\2\u019ez\3\2\2")
        buf.write("\2\u019f\u01a0\7\62\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a3")
        buf.write("\3\2\2\2\u01a2\u01a4\t\t\2\2\u01a3\u01a2\3\2\2\2\u01a4")
        buf.write("\u01a5\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01b0\3\2\2\2\u01a7\u01a8\7\62\2\2\u01a8\u01a9")
        buf.write("\7Q\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01ac\t\t\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2")
        buf.write("\u01ad\u01ae\3\2\2\2\u01ae\u01b0\3\2\2\2\u01af\u019f\3")
        buf.write("\2\2\2\u01af\u01a7\3\2\2\2\u01b0|\3\2\2\2\u01b1\u01b2")
        buf.write("\7\62\2\2\u01b2\u01b3\7z\2\2\u01b3\u01b5\3\2\2\2\u01b4")
        buf.write("\u01b6\t\n\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01c2\3")
        buf.write("\2\2\2\u01b9\u01ba\7\62\2\2\u01ba\u01bb\7Z\2\2\u01bb\u01bd")
        buf.write("\3\2\2\2\u01bc\u01be\t\n\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2")
        buf.write("\u01c0\u01c2\3\2\2\2\u01c1\u01b1\3\2\2\2\u01c1\u01b9\3")
        buf.write("\2\2\2\u01c2~\3\2\2\2\u01c3\u01c8\5y=\2\u01c4\u01c8\5")
        buf.write("{>\2\u01c5\u01c8\5}?\2\u01c6\u01c8\5w<\2\u01c7\u01c3\3")
        buf.write("\2\2\2\u01c7\u01c4\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c6")
        buf.write("\3\2\2\2\u01c8\u0080\3\2\2\2\u01c9\u01cb\t\7\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d2\7")
        buf.write("\60\2\2\u01cf\u01d1\t\7\2\2\u01d0\u01cf\3\2\2\2\u01d1")
        buf.write("\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01de\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d7\t")
        buf.write("\13\2\2\u01d6\u01d8\t\f\2\2\u01d7\u01d6\3\2\2\2\u01d7")
        buf.write("\u01d8\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01db\t\7\2\2")
        buf.write("\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01d5")
        buf.write("\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u0082\3\2\2\2\u01e0")
        buf.write("\u01e1\7\61\2\2\u01e1\u01e2\7\61\2\2\u01e2\u01e6\3\2\2")
        buf.write("\2\u01e3\u01e5\n\r\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01ea\bB\4\2")
        buf.write("\u01ea\u0084\3\2\2\2\u01eb\u01ec\7\61\2\2\u01ec\u01ed")
        buf.write("\7,\2\2\u01ed\u01f2\3\2\2\2\u01ee\u01f1\5\u0085C\2\u01ef")
        buf.write("\u01f1\13\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2")
        buf.write("\2\u01f1\u01f4\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5")
        buf.write("\u01f6\7,\2\2\u01f6\u01f7\7\61\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\bC\4\2\u01f9\u0086\3\2\2\2\u01fa\u01fc\7")
        buf.write("\17\2\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u01fe\7\f\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u0200\bD\5\2\u0200\u0088\3\2\2\2\u0201\u0203\t")
        buf.write("\16\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0207\bE\4\2\u0207\u008a\3\2\2\2\u0208\u0209\13")
        buf.write("\2\2\2\u0209\u020a\bF\6\2\u020a\u008c\3\2\2\2 \2\u0155")
        buf.write("\u015d\u0163\u016c\u0171\u0174\u017c\u0187\u018b\u0193")
        buf.write("\u019b\u019d\u01a5\u01ad\u01af\u01b7\u01bf\u01c1\u01c7")
        buf.write("\u01cc\u01d2\u01d7\u01dc\u01de\u01e6\u01f0\u01f2\u01fb")
        buf.write("\u0204\7\3:\2\3;\3\b\2\2\3D\4\3F\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    VAR = 2
    CONST = 3
    IF = 4
    ELSE = 5
    FOR = 6
    RETURN = 7
    FUNCTION = 8
    TYPE = 9
    STRUCT = 10
    INTERFACE = 11
    STRING_TYPE = 12
    INT_TYPE = 13
    FLOAT_TYPE = 14
    BOOLEAN_TYPE = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    TRUE = 19
    FALSE = 20
    NIL = 21
    ADD = 22
    SUB = 23
    MUL = 24
    DIV = 25
    MOD = 26
    AND = 27
    OR = 28
    EQ = 29
    NOT_EQ = 30
    LT = 31
    GT = 32
    LTE = 33
    GTE = 34
    NEGATION = 35
    ASSIGN = 36
    ADDASSIGN = 37
    SUBASSIGN = 38
    MULASSIGN = 39
    DIVASSIGN = 40
    MODASSIGN = 41
    ASSIGN_COLON = 42
    LBRACK = 43
    RBRACK = 44
    LBRACE = 45
    RBRACE = 46
    LPAREN = 47
    RPAREN = 48
    COMMA = 49
    SEMI_COLON = 50
    COLON = 51
    DOT = 52
    IDENTIFIER = 53
    STRINGLIT = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    INT = 57
    FLOAT = 58
    SINGLE_LINE_COMMENT = 59
    MULTI_LINE_COMMENT = 60
    NL = 61
    WS = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'var'", "'const'", "'if'", "'else'", "'for'", "'return'", 
            "'func'", "'type'", "'struct'", "'interface'", "'string'", "'int'", 
            "'float'", "'boolean'", "'continue'", "'break'", "'range'", 
            "'true'", "'false'", "'nil'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'!'", "'='", "'+='", "'-='", "'*='", "'/='", "'%='", "':='", 
            "'['", "']'", "'{'", "'}'", "'('", "')'", "','", "';'", "':'", 
            "'.'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "CONST", "IF", "ELSE", "FOR", "RETURN", "FUNCTION", "TYPE", 
            "STRUCT", "INTERFACE", "STRING_TYPE", "INT_TYPE", "FLOAT_TYPE", 
            "BOOLEAN_TYPE", "CONTINUE", "BREAK", "RANGE", "TRUE", "FALSE", 
            "NIL", "ADD", "SUB", "MUL", "DIV", "MOD", "AND", "OR", "EQ", 
            "NOT_EQ", "LT", "GT", "LTE", "GTE", "NEGATION", "ASSIGN", "ADDASSIGN", 
            "SUBASSIGN", "MULASSIGN", "DIVASSIGN", "MODASSIGN", "ASSIGN_COLON", 
            "LBRACK", "RBRACK", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
            "COMMA", "SEMI_COLON", "COLON", "DOT", "IDENTIFIER", "STRINGLIT", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "INT", "FLOAT", "SINGLE_LINE_COMMENT", 
            "MULTI_LINE_COMMENT", "NL", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "VAR", "CONST", "IF", "ELSE", "FOR", "RETURN", 
                  "FUNCTION", "TYPE", "STRUCT", "INTERFACE", "STRING_TYPE", 
                  "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "CONTINUE", 
                  "BREAK", "RANGE", "TRUE", "FALSE", "NIL", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "AND", "OR", "EQ", "NOT_EQ", "LT", 
                  "GT", "LTE", "GTE", "NEGATION", "ASSIGN", "ADDASSIGN", 
                  "SUBASSIGN", "MULASSIGN", "DIVASSIGN", "MODASSIGN", "ASSIGN_COLON", 
                  "LBRACK", "RBRACK", "LBRACE", "RBRACE", "LPAREN", "RPAREN", 
                  "COMMA", "SEMI_COLON", "COLON", "DOT", "IDENTIFIER", "ESC", 
                  "VALID_CHAR", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "DEC_INT", "BIN_INT", "OCT_INT", "HEX_INT", "INT", "FLOAT", 
                  "SINGLE_LINE_COMMENT", "MULTI_LINE_COMMENT", "NL", "WS", 
                  "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
        self.previousTokenType = None  # Khởi tạo biến ghi nhớ token trước

    def emit(self):
        tk = self.type
        self.previousTokenType = tk
        if tk == self.UNCLOSE_STRING:
            result = super().emit()
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        else:
            return super().emit()


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[56] = self.UNCLOSE_STRING_action 
            actions[57] = self.ILLEGAL_ESCAPE_action 
            actions[66] = self.NL_action 
            actions[68] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                      text = self.text;
                      if text.endswith("\r\n"):
                          text = text[:-2];
                      elif text.endswith("\n"):
                          text = text[:-1];
                      raise UncloseString(text);
                  
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                      text = self.text;
                      raise IllegalEscape(text);
                  
     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    if self.previousTokenType in [
                        type(self).IDENTIFIER, type(self).TRUE, type(self).FALSE, type(self).NIL,
                        type(self).INT, type(self).FLOAT, type(self).STRINGLIT,
                        type(self).RETURN, type(self).CONTINUE, type(self).BREAK,
                        type(self).RBRACE, type(self).RBRACK, type(self).RPAREN,
                        type(self).STRING_TYPE, type(self).INT_TYPE, type(self).FLOAT_TYPE, type(self).BOOLEAN_TYPE
                    ]:
                        self.type = type(self).SEMI_COLON;
                        self.text = ';';
                        return self.emit();
                    else:
                        self.skip();
                
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text); 
     



# Generated from /Users/aleksandrrudakov/dev/zmei/generator/zmei_generator/parser/gen/grammar/ZmeiLangParser.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u00a1")
        buf.write("\u09b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0")
        buf.write("\4\u00f1\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4")
        buf.write("\t\u00f4\4\u00f5\t\u00f5\4\u00f6\t\u00f6\4\u00f7\t\u00f7")
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\4\u00fb")
        buf.write("\t\u00fb\4\u00fc\t\u00fc\4\u00fd\t\u00fd\4\u00fe\t\u00fe")
        buf.write("\4\u00ff\t\u00ff\4\u0100\t\u0100\4\u0101\t\u0101\4\u0102")
        buf.write("\t\u0102\4\u0103\t\u0103\4\u0104\t\u0104\4\u0105\t\u0105")
        buf.write("\4\u0106\t\u0106\4\u0107\t\u0107\4\u0108\t\u0108\4\u0109")
        buf.write("\t\u0109\4\u010a\t\u010a\4\u010b\t\u010b\4\u010c\t\u010c")
        buf.write("\4\u010d\t\u010d\4\u010e\t\u010e\4\u010f\t\u010f\4\u0110")
        buf.write("\t\u0110\4\u0111\t\u0111\4\u0112\t\u0112\4\u0113\t\u0113")
        buf.write("\4\u0114\t\u0114\4\u0115\t\u0115\4\u0116\t\u0116\3\2\7")
        buf.write("\2\u022e\n\2\f\2\16\2\u0231\13\2\3\2\7\2\u0234\n\2\f\2")
        buf.write("\16\2\u0237\13\2\3\2\7\2\u023a\n\2\f\2\16\2\u023d\13\2")
        buf.write("\3\2\5\2\u0240\n\2\3\2\6\2\u0243\n\2\r\2\16\2\u0244\5")
        buf.write("\2\u0247\n\2\3\2\7\2\u024a\n\2\f\2\16\2\u024d\13\2\3\2")
        buf.write("\5\2\u0250\n\2\3\2\6\2\u0253\n\2\r\2\16\2\u0254\5\2\u0257")
        buf.write("\n\2\3\2\7\2\u025a\n\2\f\2\16\2\u025d\13\2\3\2\3\2\3\3")
        buf.write("\6\3\u0262\n\3\r\3\16\3\u0263\3\4\6\4\u0267\n\4\r\4\16")
        buf.write("\4\u0268\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u0271\n\7\3\7\3\7")
        buf.write("\3\7\6\7\u0276\n\7\r\7\16\7\u0277\3\b\5\b\u027b\n\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\7\t\u0282\n\t\f\t\16\t\u0285\13\t\3")
        buf.write("\n\3\n\3\n\5\n\u028a\n\n\3\n\5\n\u028d\n\n\3\13\3\13\3")
        buf.write("\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\7\17\u029a\n\17")
        buf.write("\f\17\16\17\u029d\13\17\3\20\3\20\3\20\3\20\5\20\u02a3")
        buf.write("\n\20\3\20\3\20\3\21\5\21\u02a8\n\21\3\21\3\21\3\21\3")
        buf.write("\21\7\21\u02ae\n\21\f\21\16\21\u02b1\13\21\3\21\3\21\3")
        buf.write("\21\5\21\u02b6\n\21\3\21\7\21\u02b9\n\21\f\21\16\21\u02bc")
        buf.write("\13\21\5\21\u02be\n\21\3\22\5\22\u02c1\n\22\3\22\3\22")
        buf.write("\5\22\u02c5\n\22\3\23\3\23\3\23\3\23\3\24\3\24\5\24\u02cd")
        buf.write("\n\24\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u02df\n\27\3\30\3")
        buf.write("\30\3\30\3\30\3\30\5\30\u02e6\n\30\3\31\3\31\3\32\3\32")
        buf.write("\3\32\5\32\u02ed\n\32\3\33\3\33\3\33\5\33\u02f2\n\33\3")
        buf.write("\34\3\34\3\34\5\34\u02f7\n\34\3\35\3\35\3\35\5\35\u02fc")
        buf.write("\n\35\3\36\3\36\3\36\7\36\u0301\n\36\f\36\16\36\u0304")
        buf.write("\13\36\3\36\5\36\u0307\n\36\3\36\7\36\u030a\n\36\f\36")
        buf.write("\16\36\u030d\13\36\3\36\6\36\u0310\n\36\r\36\16\36\u0311")
        buf.write("\3\36\7\36\u0315\n\36\f\36\16\36\u0318\13\36\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3 \7 \u0321\n \f \16 \u0324\13 \3 \5")
        buf.write(" \u0327\n \3 \7 \u032a\n \f \16 \u032d\13 \3 \3 \5 \u0331")
        buf.write("\n \7 \u0333\n \f \16 \u0336\13 \3 \7 \u0339\n \f \16")
        buf.write(" \u033c\13 \3 \3 \3!\3!\3!\7!\u0343\n!\f!\16!\u0346\13")
        buf.write("!\3!\3!\3!\7!\u034b\n!\f!\16!\u034e\13!\5!\u0350\n!\3")
        buf.write("!\7!\u0353\n!\f!\16!\u0356\13!\3!\3!\3\"\7\"\u035b\n\"")
        buf.write("\f\"\16\"\u035e\13\"\3\"\3\"\3\"\7\"\u0363\n\"\f\"\16")
        buf.write("\"\u0366\13\"\3\"\3\"\5\"\u036a\n\"\7\"\u036c\n\"\f\"")
        buf.write("\16\"\u036f\13\"\3\"\7\"\u0372\n\"\f\"\16\"\u0375\13\"")
        buf.write("\3\"\5\"\u0378\n\"\3#\3#\3$\3$\7$\u037e\n$\f$\16$\u0381")
        buf.write("\13$\3$\3$\7$\u0385\n$\f$\16$\u0388\13$\3$\3$\3$\7$\u038d")
        buf.write("\n$\f$\16$\u0390\13$\3$\3$\3$\7$\u0395\n$\f$\16$\u0398")
        buf.write("\13$\3$\3$\5$\u039c\n$\7$\u039e\n$\f$\16$\u03a1\13$\5")
        buf.write("$\u03a3\n$\3$\7$\u03a6\n$\f$\16$\u03a9\13$\3$\3$\7$\u03ad")
        buf.write("\n$\f$\16$\u03b0\13$\3%\3%\3%\3&\3&\3&\3&\6&\u03b9\n&")
        buf.write("\r&\16&\u03ba\3\'\3\'\3\'\3\'\6\'\u03c1\n\'\r\'\16\'\u03c2")
        buf.write("\3(\3(\3(\3(\6(\u03c9\n(\r(\16(\u03ca\3)\7)\u03ce\n)\f")
        buf.write(")\16)\u03d1\13)\3)\3)\3)\3)\3*\3*\3+\3+\3+\3+\5+\u03dd")
        buf.write("\n+\3,\3,\3,\3,\3-\3-\3.\3.\3.\3.\3.\3.\3.\5.\u03ec\n")
        buf.write(".\3.\3.\3/\3/\3\60\3\60\3\60\5\60\u03f5\n\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\62\3\62\3\62\7\62\u03ff\n\62\f\62\16")
        buf.write("\62\u0402\13\62\3\63\3\63\5\63\u0406\n\63\3\63\7\63\u0409")
        buf.write("\n\63\f\63\16\63\u040c\13\63\3\63\7\63\u040f\n\63\f\63")
        buf.write("\16\63\u0412\13\63\3\63\7\63\u0415\n\63\f\63\16\63\u0418")
        buf.write("\13\63\3\63\7\63\u041b\n\63\f\63\16\63\u041e\13\63\3\63")
        buf.write("\7\63\u0421\n\63\f\63\16\63\u0424\13\63\3\64\3\64\3\64")
        buf.write("\6\64\u0429\n\64\r\64\16\64\u042a\3\64\5\64\u042e\n\64")
        buf.write("\3\65\3\65\5\65\u0432\n\65\3\65\3\65\5\65\u0436\n\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\3\66\3\66\6\66\u043f\n\66\r\66")
        buf.write("\16\66\u0440\3\67\3\67\3\67\3\67\5\67\u0447\n\67\38\3")
        buf.write("8\38\58\u044c\n8\39\39\39\39\39\59\u0453\n9\3:\3:\3;\7")
        buf.write(";\u0458\n;\f;\16;\u045b\13;\3;\3;\5;\u045f\n;\3;\5;\u0462")
        buf.write("\n;\3;\5;\u0465\n;\3;\6;\u0468\n;\r;\16;\u0469\3;\5;\u046d")
        buf.write("\n;\3<\3<\5<\u0471\n<\3<\3<\3<\5<\u0476\n<\3<\3<\3<\5")
        buf.write("<\u047b\n<\3=\3=\3>\5>\u0480\n>\3>\3>\3?\3?\3?\3@\3@\3")
        buf.write("A\3A\3A\3B\3B\3C\3C\3D\6D\u0491\nD\rD\16D\u0492\3D\3D")
        buf.write("\5D\u0497\nD\3E\3E\3E\3F\3F\3F\3G\3G\3H\3H\3I\3I\3I\3")
        buf.write("I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\5I\u04b5\n")
        buf.write("I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3")
        buf.write("R\3S\3S\3T\3T\3U\3U\3V\3V\3V\3V\3V\5V\u04d4\nV\3V\3V\5")
        buf.write("V\u04d8\nV\3W\3W\3X\3X\3X\3X\3X\7X\u04e1\nX\fX\16X\u04e4")
        buf.write("\13X\3Y\5Y\u04e7\nY\3Y\3Y\3Z\3Z\3Z\5Z\u04ee\nZ\3[\3[\3")
        buf.write("[\3\\\3\\\3\\\3\\\3\\\5\\\u04f8\n\\\3]\3]\3]\3]\3]\7]")
        buf.write("\u04ff\n]\f]\16]\u0502\13]\3^\5^\u0505\n^\3^\3^\3_\3_")
        buf.write("\3_\5_\u050c\n_\3`\3`\3`\3a\3a\3a\3a\3a\3b\3b\3b\7b\u0519")
        buf.write("\nb\fb\16b\u051c\13b\3c\3c\3d\3d\3d\3d\3d\5d\u0525\nd")
        buf.write("\3e\3e\3f\3f\3f\3f\3f\5f\u052e\nf\3g\3g\3h\3h\3h\7h\u0535")
        buf.write("\nh\fh\16h\u0538\13h\3i\3i\3i\3i\3j\3j\3k\3k\3k\3l\7l")
        buf.write("\u0544\nl\fl\16l\u0547\13l\3m\3m\3m\3n\3n\3n\5n\u054f")
        buf.write("\nn\3n\3n\5n\u0553\nn\3n\5n\u0556\nn\3n\3n\3o\3o\3p\3")
        buf.write("p\3q\3q\3r\3r\3s\3s\3s\3s\3t\3t\3t\3t\3t\3t\3t\3t\3t\3")
        buf.write("t\3t\3t\3t\3t\3t\5t\u0575\nt\3u\3u\3u\3u\3u\3u\3u\3u\3")
        buf.write("u\3u\3u\3u\3u\3u\7u\u0585\nu\fu\16u\u0588\13u\3u\7u\u058b")
        buf.write("\nu\fu\16u\u058e\13u\3u\5u\u0591\nu\3u\7u\u0594\nu\fu")
        buf.write("\16u\u0597\13u\3v\3v\3v\7v\u059c\nv\fv\16v\u059f\13v\3")
        buf.write("v\3v\3v\7v\u05a4\nv\fv\16v\u05a7\13v\3v\7v\u05aa\nv\f")
        buf.write("v\16v\u05ad\13v\3w\3w\3w\3w\3w\7w\u05b4\nw\fw\16w\u05b7")
        buf.write("\13w\3x\3x\3y\3y\3z\3z\3z\3z\3z\7z\u05c2\nz\fz\16z\u05c5")
        buf.write("\13z\3{\3{\3{\3{\3{\3{\3{\7{\u05ce\n{\f{\16{\u05d1\13")
        buf.write("{\3{\5{\u05d4\n{\3|\3|\3}\3}\3}\3}\3~\3~\3\177\3\177\3")
        buf.write("\177\3\177\3\u0080\3\u0080\3\u0080\3\u0080\3\u0081\3\u0081")
        buf.write("\3\u0081\3\u0081\3\u0081\7\u0081\u05eb\n\u0081\f\u0081")
        buf.write("\16\u0081\u05ee\13\u0081\3\u0082\3\u0082\5\u0082\u05f2")
        buf.write("\n\u0082\3\u0082\3\u0082\3\u0082\3\u0082\3\u0083\3\u0083")
        buf.write("\3\u0084\3\u0084\3\u0085\3\u0085\3\u0085\3\u0085\7\u0085")
        buf.write("\u0600\n\u0085\f\u0085\16\u0085\u0603\13\u0085\3\u0086")
        buf.write("\3\u0086\3\u0086\3\u0086\7\u0086\u0609\n\u0086\f\u0086")
        buf.write("\16\u0086\u060c\13\u0086\3\u0087\3\u0087\3\u0087\3\u0087")
        buf.write("\7\u0087\u0612\n\u0087\f\u0087\16\u0087\u0615\13\u0087")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0088\7\u0088\u061b\n\u0088")
        buf.write("\f\u0088\16\u0088\u061e\13\u0088\3\u0089\3\u0089\3\u0089")
        buf.write("\3\u0089\7\u0089\u0624\n\u0089\f\u0089\16\u0089\u0627")
        buf.write("\13\u0089\3\u008a\3\u008a\3\u008a\3\u008a\7\u008a\u062d")
        buf.write("\n\u008a\f\u008a\16\u008a\u0630\13\u008a\3\u008b\3\u008b")
        buf.write("\3\u008b\3\u008b\3\u008b\3\u008b\7\u008b\u0638\n\u008b")
        buf.write("\f\u008b\16\u008b\u063b\13\u008b\5\u008b\u063d\n\u008b")
        buf.write("\3\u008b\3\u008b\5\u008b\u0641\n\u008b\3\u008c\3\u008c")
        buf.write("\3\u008d\3\u008d\3\u008e\3\u008e\3\u008e\5\u008e\u064a")
        buf.write("\n\u008e\3\u008e\3\u008e\3\u008e\3\u008e\5\u008e\u0650")
        buf.write("\n\u008e\3\u008f\3\u008f\3\u008f\3\u008f\7\u008f\u0656")
        buf.write("\n\u008f\f\u008f\16\u008f\u0659\13\u008f\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\7\u0090\u0667\n\u0090\f\u0090")
        buf.write("\16\u0090\u066a\13\u0090\3\u0091\3\u0091\3\u0092\3\u0092")
        buf.write("\3\u0092\3\u0092\7\u0092\u0672\n\u0092\f\u0092\16\u0092")
        buf.write("\u0675\13\u0092\3\u0093\3\u0093\3\u0093\7\u0093\u067a")
        buf.write("\n\u0093\f\u0093\16\u0093\u067d\13\u0093\3\u0094\3\u0094")
        buf.write("\5\u0094\u0681\n\u0094\3\u0094\3\u0094\7\u0094\u0685\n")
        buf.write("\u0094\f\u0094\16\u0094\u0688\13\u0094\3\u0095\3\u0095")
        buf.write("\5\u0095\u068c\n\u0095\3\u0095\3\u0095\7\u0095\u0690\n")
        buf.write("\u0095\f\u0095\16\u0095\u0693\13\u0095\3\u0096\3\u0096")
        buf.write("\5\u0096\u0697\n\u0096\3\u0096\3\u0096\7\u0096\u069b\n")
        buf.write("\u0096\f\u0096\16\u0096\u069e\13\u0096\3\u0097\3\u0097")
        buf.write("\3\u0097\3\u0097\7\u0097\u06a4\n\u0097\f\u0097\16\u0097")
        buf.write("\u06a7\13\u0097\3\u0098\3\u0098\3\u0098\3\u0098\7\u0098")
        buf.write("\u06ad\n\u0098\f\u0098\16\u0098\u06b0\13\u0098\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\5\u0099\u06b6\n\u0099\3\u0099")
        buf.write("\7\u0099\u06b9\n\u0099\f\u0099\16\u0099\u06bc\13\u0099")
        buf.write("\3\u009a\3\u009a\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\7\u009b\u06c5\n\u009b\f\u009b\16\u009b\u06c8\13\u009b")
        buf.write("\3\u009b\3\u009b\3\u009c\3\u009c\3\u009c\3\u009c\5\u009c")
        buf.write("\u06d0\n\u009c\3\u009d\3\u009d\3\u009e\3\u009e\3\u009f")
        buf.write("\3\u009f\3\u00a0\3\u00a0\3\u00a0\3\u00a0\7\u00a0\u06dc")
        buf.write("\n\u00a0\f\u00a0\16\u00a0\u06df\13\u00a0\3\u00a1\3\u00a1")
        buf.write("\3\u00a1\3\u00a1\5\u00a1\u06e5\n\u00a1\3\u00a2\3\u00a2")
        buf.write("\3\u00a3\3\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write("\6\u00a4\u06f0\n\u00a4\r\u00a4\16\u00a4\u06f1\3\u00a5")
        buf.write("\3\u00a5\3\u00a5\3\u00a5\3\u00a5\3\u00a6\3\u00a6\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a8\3\u00a8\3\u00a8")
        buf.write("\7\u00a8\u0703\n\u00a8\f\u00a8\16\u00a8\u0706\13\u00a8")
        buf.write("\3\u00a9\3\u00a9\3\u00a9\3\u00aa\3\u00aa\3\u00aa\3\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\3\u00ab\5\u00ab\u0713\n\u00ab")
        buf.write("\3\u00ac\3\u00ac\3\u00ad\3\u00ad\3\u00ad\3\u00ad\3\u00ad")
        buf.write("\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00af\3\u00af")
        buf.write("\3\u00b0\3\u00b0\3\u00b0\3\u00b1\3\u00b1\3\u00b1\3\u00b2")
        buf.write("\3\u00b2\3\u00b2\3\u00b3\3\u00b3\3\u00b3\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\3\u00b4\3\u00b5\3\u00b5\3\u00b6\3\u00b6")
        buf.write("\7\u00b6\u0738\n\u00b6\f\u00b6\16\u00b6\u073b\13\u00b6")
        buf.write("\3\u00b6\3\u00b6\7\u00b6\u073f\n\u00b6\f\u00b6\16\u00b6")
        buf.write("\u0742\13\u00b6\3\u00b7\3\u00b7\5\u00b7\u0746\n\u00b7")
        buf.write("\3\u00b7\3\u00b7\5\u00b7\u074a\n\u00b7\3\u00b7\3\u00b7")
        buf.write("\5\u00b7\u074e\n\u00b7\3\u00b7\3\u00b7\5\u00b7\u0752\n")
        buf.write("\u00b7\5\u00b7\u0754\n\u00b7\3\u00b7\3\u00b7\5\u00b7\u0758")
        buf.write("\n\u00b7\3\u00b8\3\u00b8\3\u00b8\5\u00b8\u075d\n\u00b8")
        buf.write("\3\u00b8\3\u00b8\3\u00b8\3\u00b8\3\u00b9\3\u00b9\3\u00b9")
        buf.write("\3\u00ba\3\u00ba\3\u00bb\3\u00bb\5\u00bb\u076a\n\u00bb")
        buf.write("\3\u00bc\3\u00bc\3\u00bc\7\u00bc\u076f\n\u00bc\f\u00bc")
        buf.write("\16\u00bc\u0772\13\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\3\u00bd\6\u00bd\u0779\n\u00bd\r\u00bd\16\u00bd\u077a")
        buf.write("\3\u00be\5\u00be\u077e\n\u00be\3\u00be\3\u00be\3\u00bf")
        buf.write("\3\u00bf\3\u00bf\6\u00bf\u0785\n\u00bf\r\u00bf\16\u00bf")
        buf.write("\u0786\3\u00c0\3\u00c0\3\u00c0\3\u00c0\3\u00c1\3\u00c1")
        buf.write("\5\u00c1\u078f\n\u00c1\3\u00c2\3\u00c2\3\u00c2\6\u00c2")
        buf.write("\u0794\n\u00c2\r\u00c2\16\u00c2\u0795\3\u00c2\5\u00c2")
        buf.write("\u0799\n\u00c2\5\u00c2\u079b\n\u00c2\3\u00c3\3\u00c3\3")
        buf.write("\u00c4\7\u00c4\u07a0\n\u00c4\f\u00c4\16\u00c4\u07a3\13")
        buf.write("\u00c4\3\u00c4\7\u00c4\u07a6\n\u00c4\f\u00c4\16\u00c4")
        buf.write("\u07a9\13\u00c4\3\u00c4\5\u00c4\u07ac\n\u00c4\3\u00c4")
        buf.write("\7\u00c4\u07af\n\u00c4\f\u00c4\16\u00c4\u07b2\13\u00c4")
        buf.write("\3\u00c4\7\u00c4\u07b5\n\u00c4\f\u00c4\16\u00c4\u07b8")
        buf.write("\13\u00c4\3\u00c5\3\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6")
        buf.write("\6\u00c6\u07c0\n\u00c6\r\u00c6\16\u00c6\u07c1\3\u00c6")
        buf.write("\5\u00c6\u07c5\n\u00c6\3\u00c7\3\u00c7\3\u00c8\3\u00c8")
        buf.write("\3\u00c9\3\u00c9\3\u00c9\5\u00c9\u07ce\n\u00c9\3\u00c9")
        buf.write("\3\u00c9\5\u00c9\u07d2\n\u00c9\3\u00c9\6\u00c9\u07d5\n")
        buf.write("\u00c9\r\u00c9\16\u00c9\u07d6\3\u00c9\5\u00c9\u07da\n")
        buf.write("\u00c9\3\u00ca\3\u00ca\3\u00cb\3\u00cb\3\u00cb\7\u00cb")
        buf.write("\u07e1\n\u00cb\f\u00cb\16\u00cb\u07e4\13\u00cb\3\u00cc")
        buf.write("\5\u00cc\u07e7\n\u00cc\3\u00cc\3\u00cc\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd\3\u00cd")
        buf.write("\3\u00cd\5\u00cd\u07fc\n\u00cd\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\6\u00ce\u0802\n\u00ce\r\u00ce\16\u00ce\u0803")
        buf.write("\3\u00ce\3\u00ce\3\u00cf\3\u00cf\5\u00cf\u080a\n\u00cf")
        buf.write("\3\u00cf\5\u00cf\u080d\n\u00cf\3\u00cf\5\u00cf\u0810\n")
        buf.write("\u00cf\3\u00cf\5\u00cf\u0813\n\u00cf\3\u00d0\3\u00d0\5")
        buf.write("\u00d0\u0817\n\u00d0\3\u00d1\3\u00d1\3\u00d2\3\u00d2\3")
        buf.write("\u00d2\3\u00d2\3\u00d2\3\u00d2\7\u00d2\u0821\n\u00d2\f")
        buf.write("\u00d2\16\u00d2\u0824\13\u00d2\5\u00d2\u0826\n\u00d2\3")
        buf.write("\u00d3\3\u00d3\3\u00d4\3\u00d4\3\u00d4\5\u00d4\u082d\n")
        buf.write("\u00d4\3\u00d5\3\u00d5\3\u00d6\3\u00d6\3\u00d7\3\u00d7")
        buf.write("\3\u00d7\5\u00d7\u0836\n\u00d7\3\u00d7\3\u00d7\3\u00d8")
        buf.write("\3\u00d8\3\u00d9\3\u00d9\3\u00d9\5\u00d9\u083f\n\u00d9")
        buf.write("\3\u00d9\3\u00d9\3\u00da\3\u00da\3\u00db\3\u00db\3\u00db")
        buf.write("\3\u00dc\3\u00dc\3\u00dc\3\u00dd\3\u00dd\5\u00dd\u084d")
        buf.write("\n\u00dd\3\u00dd\3\u00dd\7\u00dd\u0851\n\u00dd\f\u00dd")
        buf.write("\16\u00dd\u0854\13\u00dd\3\u00dd\3\u00dd\5\u00dd\u0858")
        buf.write("\n\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd")
        buf.write("\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd\3\u00dd")
        buf.write("\3\u00dd\3\u00dd\7\u00dd\u0869\n\u00dd\f\u00dd\16\u00dd")
        buf.write("\u086c\13\u00dd\3\u00dd\7\u00dd\u086f\n\u00dd\f\u00dd")
        buf.write("\16\u00dd\u0872\13\u00dd\3\u00dd\3\u00dd\5\u00dd\u0876")
        buf.write("\n\u00dd\3\u00dd\7\u00dd\u0879\n\u00dd\f\u00dd\16\u00dd")
        buf.write("\u087c\13\u00dd\3\u00dd\7\u00dd\u087f\n\u00dd\f\u00dd")
        buf.write("\16\u00dd\u0882\13\u00dd\3\u00dd\7\u00dd\u0885\n\u00dd")
        buf.write("\f\u00dd\16\u00dd\u0888\13\u00dd\3\u00dd\3\u00dd\3\u00de")
        buf.write("\3\u00de\7\u00de\u088e\n\u00de\f\u00de\16\u00de\u0891")
        buf.write("\13\u00de\3\u00de\3\u00de\7\u00de\u0895\n\u00de\f\u00de")
        buf.write("\16\u00de\u0898\13\u00de\3\u00de\3\u00de\7\u00de\u089c")
        buf.write("\n\u00de\f\u00de\16\u00de\u089f\13\u00de\3\u00de\3\u00de")
        buf.write("\7\u00de\u08a3\n\u00de\f\u00de\16\u00de\u08a6\13\u00de")
        buf.write("\3\u00df\3\u00df\3\u00e0\3\u00e0\3\u00e0\3\u00e0\5\u00e0")
        buf.write("\u08ae\n\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e1")
        buf.write("\3\u00e1\3\u00e2\3\u00e2\3\u00e2\3\u00e2\5\u00e2\u08ba")
        buf.write("\n\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e2\3\u00e3\3\u00e3")
        buf.write("\3\u00e4\3\u00e4\5\u00e4\u08c4\n\u00e4\3\u00e5\3\u00e5")
        buf.write("\3\u00e6\3\u00e6\3\u00e6\3\u00e6\3\u00e7\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e8\3\u00e8\3\u00e9\3\u00e9\3\u00e9\3\u00e9")
        buf.write("\3\u00ea\3\u00ea\3\u00eb\3\u00eb\3\u00eb\3\u00eb\3\u00ec")
        buf.write("\3\u00ec\3\u00ec\3\u00ec\5\u00ec\u08e0\n\u00ec\3\u00ed")
        buf.write("\3\u00ed\3\u00ed\3\u00ed\5\u00ed\u08e6\n\u00ed\3\u00ee")
        buf.write("\3\u00ee\3\u00ee\3\u00ee\3\u00ef\3\u00ef\3\u00ef\3\u00ef")
        buf.write("\3\u00f0\3\u00f0\3\u00f0\3\u00f0\3\u00f1\3\u00f1\3\u00f1")
        buf.write("\7\u00f1\u08f7\n\u00f1\f\u00f1\16\u00f1\u08fa\13\u00f1")
        buf.write("\3\u00f2\3\u00f2\3\u00f3\3\u00f3\3\u00f3\3\u00f3\3\u00f4")
        buf.write("\3\u00f4\3\u00f4\3\u00f4\3\u00f5\3\u00f5\3\u00f6\3\u00f6")
        buf.write("\3\u00f6\3\u00f6\3\u00f7\3\u00f7\3\u00f8\3\u00f8\3\u00f8")
        buf.write("\7\u00f8\u0911\n\u00f8\f\u00f8\16\u00f8\u0914\13\u00f8")
        buf.write("\3\u00f9\3\u00f9\5\u00f9\u0918\n\u00f9\3\u00fa\3\u00fa")
        buf.write("\5\u00fa\u091c\n\u00fa\3\u00fa\5\u00fa\u091f\n\u00fa\3")
        buf.write("\u00fb\3\u00fb\3\u00fc\3\u00fc\3\u00fc\3\u00fc\3\u00fd")
        buf.write("\3\u00fd\3\u00fd\7\u00fd\u092a\n\u00fd\f\u00fd\16\u00fd")
        buf.write("\u092d\13\u00fd\3\u00fe\3\u00fe\3\u00ff\3\u00ff\5\u00ff")
        buf.write("\u0933\n\u00ff\3\u00ff\5\u00ff\u0936\n\u00ff\3\u0100\3")
        buf.write("\u0100\5\u0100\u093a\n\u0100\3\u0101\3\u0101\5\u0101\u093e")
        buf.write("\n\u0101\3\u0102\3\u0102\3\u0102\3\u0103\3\u0103\3\u0103")
        buf.write("\3\u0104\3\u0104\3\u0104\3\u0105\3\u0105\3\u0105\3\u0105")
        buf.write("\3\u0105\7\u0105\u094e\n\u0105\f\u0105\16\u0105\u0951")
        buf.write("\13\u0105\3\u0105\6\u0105\u0954\n\u0105\r\u0105\16\u0105")
        buf.write("\u0955\3\u0105\7\u0105\u0959\n\u0105\f\u0105\16\u0105")
        buf.write("\u095c\13\u0105\3\u0105\3\u0105\3\u0106\3\u0106\3\u0107")
        buf.write("\5\u0107\u0963\n\u0107\3\u0107\7\u0107\u0966\n\u0107\f")
        buf.write("\u0107\16\u0107\u0969\13\u0107\3\u0107\5\u0107\u096c\n")
        buf.write("\u0107\3\u0107\3\u0107\3\u0107\5\u0107\u0971\n\u0107\3")
        buf.write("\u0107\7\u0107\u0974\n\u0107\f\u0107\16\u0107\u0977\13")
        buf.write("\u0107\3\u0108\3\u0108\3\u0108\5\u0108\u097c\n\u0108\3")
        buf.write("\u0109\3\u0109\3\u010a\3\u010a\3\u010a\3\u010a\7\u010a")
        buf.write("\u0984\n\u010a\f\u010a\16\u010a\u0987\13\u010a\3\u010a")
        buf.write("\3\u010a\3\u010b\3\u010b\3\u010b\3\u010b\3\u010c\3\u010c")
        buf.write("\3\u010d\3\u010d\3\u010d\5\u010d\u0994\n\u010d\3\u010e")
        buf.write("\3\u010e\3\u010f\3\u010f\3\u010f\3\u010f\3\u010f\3\u0110")
        buf.write("\3\u0110\3\u0110\5\u0110\u09a0\n\u0110\3\u0110\3\u0110")
        buf.write("\3\u0111\3\u0111\3\u0111\5\u0111\u09a7\n\u0111\3\u0112")
        buf.write("\3\u0112\3\u0112\3\u0113\3\u0113\3\u0114\3\u0114\5\u0114")
        buf.write("\u09b0\n\u0114\3\u0115\3\u0115\3\u0115\3\u0115\3\u0115")
        buf.write("\3\u0116\3\u0116\3\u0116\2\2\u0117\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac")
        buf.write("\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be")
        buf.write("\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0")
        buf.write("\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2")
        buf.write("\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4")
        buf.write("\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106")
        buf.write("\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118")
        buf.write("\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a")
        buf.write("\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c")
        buf.write("\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e")
        buf.write("\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160")
        buf.write("\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172")
        buf.write("\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184")
        buf.write("\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196")
        buf.write("\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4\u01a6\u01a8")
        buf.write("\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6\u01b8\u01ba")
        buf.write("\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca\u01cc")
        buf.write("\u01ce\u01d0\u01d2\u01d4\u01d6\u01d8\u01da\u01dc\u01de")
        buf.write("\u01e0\u01e2\u01e4\u01e6\u01e8\u01ea\u01ec\u01ee\u01f0")
        buf.write("\u01f2\u01f4\u01f6\u01f8\u01fa\u01fc\u01fe\u0200\u0202")
        buf.write("\u0204\u0206\u0208\u020a\u020c\u020e\u0210\u0212\u0214")
        buf.write("\u0216\u0218\u021a\u021c\u021e\u0220\u0222\u0224\u0226")
        buf.write("\u0228\u022a\2\23\4\2,wyy\3\2\u0092\u0093\4\2\u008b\u008b")
        buf.write("\u0090\u0090\3\2\u0092\u0092\3\2\u0099\u009a\3\2\u008b")
        buf.write("\u0090\4\2zz\u0084\u0084\5\288::==\3\2BD\4\2\u008e\u008e")
        buf.write("\u0090\u0090\3\2`b\3\2,.\4\2\u0086\u0086\u0090\u0090\4")
        buf.write("\2\u0088\u0088\u008c\u008c\3\2\r\17\3\2WY\4\2WZnn\2\u0a18")
        buf.write("\2\u022f\3\2\2\2\4\u0261\3\2\2\2\6\u0266\3\2\2\2\b\u026a")
        buf.write("\3\2\2\2\n\u026c\3\2\2\2\f\u0270\3\2\2\2\16\u027a\3\2")
        buf.write("\2\2\20\u027e\3\2\2\2\22\u028c\3\2\2\2\24\u028e\3\2\2")
        buf.write("\2\26\u0290\3\2\2\2\30\u0292\3\2\2\2\32\u0294\3\2\2\2")
        buf.write("\34\u0296\3\2\2\2\36\u029e\3\2\2\2 \u02bd\3\2\2\2\"\u02c0")
        buf.write("\3\2\2\2$\u02c6\3\2\2\2&\u02cc\3\2\2\2(\u02ce\3\2\2\2")
        buf.write("*\u02d2\3\2\2\2,\u02de\3\2\2\2.\u02e0\3\2\2\2\60\u02e7")
        buf.write("\3\2\2\2\62\u02e9\3\2\2\2\64\u02ee\3\2\2\2\66\u02f3\3")
        buf.write("\2\2\28\u02f8\3\2\2\2:\u02fd\3\2\2\2<\u031b\3\2\2\2>\u031d")
        buf.write("\3\2\2\2@\u033f\3\2\2\2B\u035c\3\2\2\2D\u0379\3\2\2\2")
        buf.write("F\u037b\3\2\2\2H\u03b1\3\2\2\2J\u03b8\3\2\2\2L\u03c0\3")
        buf.write("\2\2\2N\u03c8\3\2\2\2P\u03cf\3\2\2\2R\u03d6\3\2\2\2T\u03dc")
        buf.write("\3\2\2\2V\u03de\3\2\2\2X\u03e2\3\2\2\2Z\u03e4\3\2\2\2")
        buf.write("\\\u03ef\3\2\2\2^\u03f4\3\2\2\2`\u03f6\3\2\2\2b\u03fb")
        buf.write("\3\2\2\2d\u0403\3\2\2\2f\u0425\3\2\2\2h\u042f\3\2\2\2")
        buf.write("j\u043a\3\2\2\2l\u0442\3\2\2\2n\u044b\3\2\2\2p\u044d\3")
        buf.write("\2\2\2r\u0454\3\2\2\2t\u0459\3\2\2\2v\u047a\3\2\2\2x\u047c")
        buf.write("\3\2\2\2z\u047f\3\2\2\2|\u0483\3\2\2\2~\u0486\3\2\2\2")
        buf.write("\u0080\u0488\3\2\2\2\u0082\u048b\3\2\2\2\u0084\u048d\3")
        buf.write("\2\2\2\u0086\u0496\3\2\2\2\u0088\u0498\3\2\2\2\u008a\u049b")
        buf.write("\3\2\2\2\u008c\u049e\3\2\2\2\u008e\u04a0\3\2\2\2\u0090")
        buf.write("\u04b4\3\2\2\2\u0092\u04b6\3\2\2\2\u0094\u04b8\3\2\2\2")
        buf.write("\u0096\u04ba\3\2\2\2\u0098\u04bc\3\2\2\2\u009a\u04be\3")
        buf.write("\2\2\2\u009c\u04c0\3\2\2\2\u009e\u04c2\3\2\2\2\u00a0\u04c4")
        buf.write("\3\2\2\2\u00a2\u04c6\3\2\2\2\u00a4\u04c8\3\2\2\2\u00a6")
        buf.write("\u04ca\3\2\2\2\u00a8\u04cc\3\2\2\2\u00aa\u04ce\3\2\2\2")
        buf.write("\u00ac\u04d9\3\2\2\2\u00ae\u04db\3\2\2\2\u00b0\u04e6\3")
        buf.write("\2\2\2\u00b2\u04ed\3\2\2\2\u00b4\u04ef\3\2\2\2\u00b6\u04f2")
        buf.write("\3\2\2\2\u00b8\u04f9\3\2\2\2\u00ba\u0504\3\2\2\2\u00bc")
        buf.write("\u050b\3\2\2\2\u00be\u050d\3\2\2\2\u00c0\u0510\3\2\2\2")
        buf.write("\u00c2\u0515\3\2\2\2\u00c4\u051d\3\2\2\2\u00c6\u051f\3")
        buf.write("\2\2\2\u00c8\u0526\3\2\2\2\u00ca\u0528\3\2\2\2\u00cc\u052f")
        buf.write("\3\2\2\2\u00ce\u0531\3\2\2\2\u00d0\u0539\3\2\2\2\u00d2")
        buf.write("\u053d\3\2\2\2\u00d4\u053f\3\2\2\2\u00d6\u0545\3\2\2\2")
        buf.write("\u00d8\u0548\3\2\2\2\u00da\u054b\3\2\2\2\u00dc\u0559\3")
        buf.write("\2\2\2\u00de\u055b\3\2\2\2\u00e0\u055d\3\2\2\2\u00e2\u055f")
        buf.write("\3\2\2\2\u00e4\u0561\3\2\2\2\u00e6\u0574\3\2\2\2\u00e8")
        buf.write("\u0576\3\2\2\2\u00ea\u0598\3\2\2\2\u00ec\u05ae\3\2\2\2")
        buf.write("\u00ee\u05b8\3\2\2\2\u00f0\u05ba\3\2\2\2\u00f2\u05bc\3")
        buf.write("\2\2\2\u00f4\u05c6\3\2\2\2\u00f6\u05d5\3\2\2\2\u00f8\u05d7")
        buf.write("\3\2\2\2\u00fa\u05db\3\2\2\2\u00fc\u05dd\3\2\2\2\u00fe")
        buf.write("\u05e1\3\2\2\2\u0100\u05e5\3\2\2\2\u0102\u05ef\3\2\2\2")
        buf.write("\u0104\u05f7\3\2\2\2\u0106\u05f9\3\2\2\2\u0108\u05fb\3")
        buf.write("\2\2\2\u010a\u0604\3\2\2\2\u010c\u060d\3\2\2\2\u010e\u0616")
        buf.write("\3\2\2\2\u0110\u061f\3\2\2\2\u0112\u0628\3\2\2\2\u0114")
        buf.write("\u0631\3\2\2\2\u0116\u0642\3\2\2\2\u0118\u0644\3\2\2\2")
        buf.write("\u011a\u0646\3\2\2\2\u011c\u0651\3\2\2\2\u011e\u0668\3")
        buf.write("\2\2\2\u0120\u066b\3\2\2\2\u0122\u066d\3\2\2\2\u0124\u0676")
        buf.write("\3\2\2\2\u0126\u067e\3\2\2\2\u0128\u0689\3\2\2\2\u012a")
        buf.write("\u0694\3\2\2\2\u012c\u069f\3\2\2\2\u012e\u06a8\3\2\2\2")
        buf.write("\u0130\u06b1\3\2\2\2\u0132\u06bd\3\2\2\2\u0134\u06bf\3")
        buf.write("\2\2\2\u0136\u06cb\3\2\2\2\u0138\u06d1\3\2\2\2\u013a\u06d3")
        buf.write("\3\2\2\2\u013c\u06d5\3\2\2\2\u013e\u06d7\3\2\2\2\u0140")
        buf.write("\u06e0\3\2\2\2\u0142\u06e6\3\2\2\2\u0144\u06e8\3\2\2\2")
        buf.write("\u0146\u06ea\3\2\2\2\u0148\u06f3\3\2\2\2\u014a\u06f8\3")
        buf.write("\2\2\2\u014c\u06fa\3\2\2\2\u014e\u06ff\3\2\2\2\u0150\u0707")
        buf.write("\3\2\2\2\u0152\u070a\3\2\2\2\u0154\u070d\3\2\2\2\u0156")
        buf.write("\u0714\3\2\2\2\u0158\u0716\3\2\2\2\u015a\u071b\3\2\2\2")
        buf.write("\u015c\u0720\3\2\2\2\u015e\u0722\3\2\2\2\u0160\u0725\3")
        buf.write("\2\2\2\u0162\u0728\3\2\2\2\u0164\u072b\3\2\2\2\u0166\u072e")
        buf.write("\3\2\2\2\u0168\u0733\3\2\2\2\u016a\u0735\3\2\2\2\u016c")
        buf.write("\u0743\3\2\2\2\u016e\u075c\3\2\2\2\u0170\u0762\3\2\2\2")
        buf.write("\u0172\u0765\3\2\2\2\u0174\u0769\3\2\2\2\u0176\u076b\3")
        buf.write("\2\2\2\u0178\u0778\3\2\2\2\u017a\u077d\3\2\2\2\u017c\u0784")
        buf.write("\3\2\2\2\u017e\u0788\3\2\2\2\u0180\u078e\3\2\2\2\u0182")
        buf.write("\u079a\3\2\2\2\u0184\u079c\3\2\2\2\u0186\u07a1\3\2\2\2")
        buf.write("\u0188\u07b9\3\2\2\2\u018a\u07bb\3\2\2\2\u018c\u07c6\3")
        buf.write("\2\2\2\u018e\u07c8\3\2\2\2\u0190\u07ca\3\2\2\2\u0192\u07db")
        buf.write("\3\2\2\2\u0194\u07dd\3\2\2\2\u0196\u07e6\3\2\2\2\u0198")
        buf.write("\u07fb\3\2\2\2\u019a\u07fd\3\2\2\2\u019c\u0807\3\2\2\2")
        buf.write("\u019e\u0816\3\2\2\2\u01a0\u0818\3\2\2\2\u01a2\u081a\3")
        buf.write("\2\2\2\u01a4\u0827\3\2\2\2\u01a6\u0829\3\2\2\2\u01a8\u082e")
        buf.write("\3\2\2\2\u01aa\u0830\3\2\2\2\u01ac\u0832\3\2\2\2\u01ae")
        buf.write("\u0839\3\2\2\2\u01b0\u083b\3\2\2\2\u01b2\u0842\3\2\2\2")
        buf.write("\u01b4\u0844\3\2\2\2\u01b6\u0847\3\2\2\2\u01b8\u084c\3")
        buf.write("\2\2\2\u01ba\u088b\3\2\2\2\u01bc\u08a7\3\2\2\2\u01be\u08ad")
        buf.write("\3\2\2\2\u01c0\u08b3\3\2\2\2\u01c2\u08b9\3\2\2\2\u01c4")
        buf.write("\u08bf\3\2\2\2\u01c6\u08c3\3\2\2\2\u01c8\u08c5\3\2\2\2")
        buf.write("\u01ca\u08c7\3\2\2\2\u01cc\u08cb\3\2\2\2\u01ce\u08cf\3")
        buf.write("\2\2\2\u01d0\u08d1\3\2\2\2\u01d2\u08d5\3\2\2\2\u01d4\u08d7")
        buf.write("\3\2\2\2\u01d6\u08db\3\2\2\2\u01d8\u08e1\3\2\2\2\u01da")
        buf.write("\u08e7\3\2\2\2\u01dc\u08eb\3\2\2\2\u01de\u08ef\3\2\2\2")
        buf.write("\u01e0\u08f3\3\2\2\2\u01e2\u08fb\3\2\2\2\u01e4\u08fd\3")
        buf.write("\2\2\2\u01e6\u0901\3\2\2\2\u01e8\u0905\3\2\2\2\u01ea\u0907")
        buf.write("\3\2\2\2\u01ec\u090b\3\2\2\2\u01ee\u090d\3\2\2\2\u01f0")
        buf.write("\u0915\3\2\2\2\u01f2\u091e\3\2\2\2\u01f4\u0920\3\2\2\2")
        buf.write("\u01f6\u0922\3\2\2\2\u01f8\u0926\3\2\2\2\u01fa\u092e\3")
        buf.write("\2\2\2\u01fc\u0935\3\2\2\2\u01fe\u0937\3\2\2\2\u0200\u093b")
        buf.write("\3\2\2\2\u0202\u093f\3\2\2\2\u0204\u0942\3\2\2\2\u0206")
        buf.write("\u0945\3\2\2\2\u0208\u0948\3\2\2\2\u020a\u095f\3\2\2\2")
        buf.write("\u020c\u0962\3\2\2\2\u020e\u0978\3\2\2\2\u0210\u097d\3")
        buf.write("\2\2\2\u0212\u097f\3\2\2\2\u0214\u098a\3\2\2\2\u0216\u098e")
        buf.write("\3\2\2\2\u0218\u0993\3\2\2\2\u021a\u0995\3\2\2\2\u021c")
        buf.write("\u0997\3\2\2\2\u021e\u099f\3\2\2\2\u0220\u09a6\3\2\2\2")
        buf.write("\u0222\u09a8\3\2\2\2\u0224\u09ab\3\2\2\2\u0226\u09ad\3")
        buf.write("\2\2\2\u0228\u09b1\3\2\2\2\u022a\u09b6\3\2\2\2\u022c\u022e")
        buf.write("\7x\2\2\u022d\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f")
        buf.write("\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0235\3\2\2\2")
        buf.write("\u0231\u022f\3\2\2\2\u0232\u0234\5,\27\2\u0233\u0232\3")
        buf.write("\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236")
        buf.write("\3\2\2\2\u0236\u023b\3\2\2\2\u0237\u0235\3\2\2\2\u0238")
        buf.write("\u023a\7x\2\2\u0239\u0238\3\2\2\2\u023a\u023d\3\2\2\2")
        buf.write("\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u0246\3")
        buf.write("\2\2\2\u023d\u023b\3\2\2\2\u023e\u0240\5\4\3\2\u023f\u023e")
        buf.write("\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0242\3\2\2\2\u0241")
        buf.write("\u0243\5\u016a\u00b6\2\u0242\u0241\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245")
        buf.write("\u0247\3\2\2\2\u0246\u023f\3\2\2\2\u0246\u0247\3\2\2\2")
        buf.write("\u0247\u024b\3\2\2\2\u0248\u024a\7x\2\2\u0249\u0248\3")
        buf.write("\2\2\2\u024a\u024d\3\2\2\2\u024b\u0249\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u0256\3\2\2\2\u024d\u024b\3\2\2\2\u024e")
        buf.write("\u0250\5\6\4\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2")
        buf.write("\u0250\u0252\3\2\2\2\u0251\u0253\5d\63\2\u0252\u0251\3")
        buf.write("\2\2\2\u0253\u0254\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255")
        buf.write("\3\2\2\2\u0255\u0257\3\2\2\2\u0256\u024f\3\2\2\2\u0256")
        buf.write("\u0257\3\2\2\2\u0257\u025b\3\2\2\2\u0258\u025a\7x\2\2")
        buf.write("\u0259\u0258\3\2\2\2\u025a\u025d\3\2\2\2\u025b\u0259\3")
        buf.write("\2\2\2\u025b\u025c\3\2\2\2\u025c\u025e\3\2\2\2\u025d\u025b")
        buf.write("\3\2\2\2\u025e\u025f\7\2\2\3\u025f\3\3\2\2\2\u0260\u0262")
        buf.write("\5\b\5\2\u0261\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263")
        buf.write("\u0261\3\2\2\2\u0263\u0264\3\2\2\2\u0264\5\3\2\2\2\u0265")
        buf.write("\u0267\5\n\6\2\u0266\u0265\3\2\2\2\u0267\u0268\3\2\2\2")
        buf.write("\u0268\u0266\3\2\2\2\u0268\u0269\3\2\2\2\u0269\7\3\2\2")
        buf.write("\2\u026a\u026b\5\f\7\2\u026b\t\3\2\2\2\u026c\u026d\5\f")
        buf.write("\7\2\u026d\13\3\2\2\2\u026e\u026f\7\\\2\2\u026f\u0271")
        buf.write("\5\16\b\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("\u0272\3\2\2\2\u0272\u0273\7t\2\2\u0273\u0275\5\20\t\2")
        buf.write("\u0274\u0276\7x\2\2\u0275\u0274\3\2\2\2\u0276\u0277\3")
        buf.write("\2\2\2\u0277\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278\r")
        buf.write("\3\2\2\2\u0279\u027b\7\u0088\2\2\u027a\u0279\3\2\2\2\u027a")
        buf.write("\u027b\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027d\5\34\17")
        buf.write("\2\u027d\17\3\2\2\2\u027e\u0283\5\22\n\2\u027f\u0280\7")
        buf.write("\u0087\2\2\u0280\u0282\5\22\n\2\u0281\u027f\3\2\2\2\u0282")
        buf.write("\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284\3\2\2\2")
        buf.write("\u0284\21\3\2\2\2\u0285\u0283\3\2\2\2\u0286\u0289\5\24")
        buf.write("\13\2\u0287\u0288\7u\2\2\u0288\u028a\5\26\f\2\u0289\u0287")
        buf.write("\3\2\2\2\u0289\u028a\3\2\2\2\u028a\u028d\3\2\2\2\u028b")
        buf.write("\u028d\5\30\r\2\u028c\u0286\3\2\2\2\u028c\u028b\3\2\2")
        buf.write("\2\u028d\23\3\2\2\2\u028e\u028f\5\34\17\2\u028f\25\3\2")
        buf.write("\2\2\u0290\u0291\5\32\16\2\u0291\27\3\2\2\2\u0292\u0293")
        buf.write("\7\u008f\2\2\u0293\31\3\2\2\2\u0294\u0295\t\2\2\2\u0295")
        buf.write("\33\3\2\2\2\u0296\u029b\5\32\16\2\u0297\u0298\7\u0088")
        buf.write("\2\2\u0298\u029a\5\32\16\2\u0299\u0297\3\2\2\2\u029a\u029d")
        buf.write("\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029c\3\2\2\2\u029c")
        buf.write("\35\3\2\2\2\u029d\u029b\3\2\2\2\u029e\u02a2\7\u0089\2")
        buf.write("\2\u029f\u02a0\5\32\16\2\u02a0\u02a1\7\u0088\2\2\u02a1")
        buf.write("\u02a3\3\2\2\2\u02a2\u029f\3\2\2\2\u02a2\u02a3\3\2\2\2")
        buf.write("\u02a3\u02a4\3\2\2\2\u02a4\u02a5\5\32\16\2\u02a5\37\3")
        buf.write("\2\2\2\u02a6\u02a8\7\u0088\2\2\u02a7\u02a6\3\2\2\2\u02a7")
        buf.write("\u02a8\3\2\2\2\u02a8\u02a9\3\2\2\2\u02a9\u02af\7\u008f")
        buf.write("\2\2\u02aa\u02ab\7\u0087\2\2\u02ab\u02ac\7\177\2\2\u02ac")
        buf.write("\u02ae\5\"\22\2\u02ad\u02aa\3\2\2\2\u02ae\u02b1\3\2\2")
        buf.write("\2\u02af\u02ad\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02be")
        buf.write("\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02ba\5\32\16\2\u02b3")
        buf.write("\u02b5\7\u0087\2\2\u02b4\u02b6\7\177\2\2\u02b5\u02b4\3")
        buf.write("\2\2\2\u02b5\u02b6\3\2\2\2\u02b6\u02b7\3\2\2\2\u02b7\u02b9")
        buf.write("\5\"\22\2\u02b8\u02b3\3\2\2\2\u02b9\u02bc\3\2\2\2\u02ba")
        buf.write("\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02be\3\2\2\2")
        buf.write("\u02bc\u02ba\3\2\2\2\u02bd\u02a7\3\2\2\2\u02bd\u02b2\3")
        buf.write("\2\2\2\u02be!\3\2\2\2\u02bf\u02c1\7\u008f\2\2\u02c0\u02bf")
        buf.write("\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2\3\2\2\2\u02c2")
        buf.write("\u02c4\5\32\16\2\u02c3\u02c5\7\u008f\2\2\u02c4\u02c3\3")
        buf.write("\2\2\2\u02c4\u02c5\3\2\2\2\u02c5#\3\2\2\2\u02c6\u02c7")
        buf.write("\7\u0082\2\2\u02c7\u02c8\7v\2\2\u02c8\u02c9\7\u0083\2")
        buf.write("\2\u02c9%\3\2\2\2\u02ca\u02cd\5*\26\2\u02cb\u02cd\5(\25")
        buf.write("\2\u02cc\u02ca\3\2\2\2\u02cc\u02cb\3\2\2\2\u02cd\'\3\2")
        buf.write("\2\2\u02ce\u02cf\7\u0099\2\2\u02cf\u02d0\7\u009d\2\2\u02d0")
        buf.write("\u02d1\7x\2\2\u02d1)\3\2\2\2\u02d2\u02d3\7\u009b\2\2\u02d3")
        buf.write("+\3\2\2\2\u02d4\u02df\5.\30\2\u02d5\u02df\5\62\32\2\u02d6")
        buf.write("\u02df\5\64\33\2\u02d7\u02df\5\66\34\2\u02d8\u02df\58")
        buf.write("\35\2\u02d9\u02df\5:\36\2\u02da\u02df\5V,\2\u02db\u02df")
        buf.write("\5Z.\2\u02dc\u02df\5`\61\2\u02dd\u02df\7x\2\2\u02de\u02d4")
        buf.write("\3\2\2\2\u02de\u02d5\3\2\2\2\u02de\u02d6\3\2\2\2\u02de")
        buf.write("\u02d7\3\2\2\2\u02de\u02d8\3\2\2\2\u02de\u02d9\3\2\2\2")
        buf.write("\u02de\u02da\3\2\2\2\u02de\u02db\3\2\2\2\u02de\u02dc\3")
        buf.write("\2\2\2\u02de\u02dd\3\2\2\2\u02df-\3\2\2\2\u02e0\u02e5")
        buf.write("\7\4\2\2\u02e1\u02e2\7\u0080\2\2\u02e2\u02e3\5\60\31\2")
        buf.write("\u02e3\u02e4\7\u0081\2\2\u02e4\u02e6\3\2\2\2\u02e5\u02e1")
        buf.write("\3\2\2\2\u02e5\u02e6\3\2\2\2\u02e6/\3\2\2\2\u02e7\u02e8")
        buf.write("\t\3\2\2\u02e8\61\3\2\2\2\u02e9\u02ec\7\5\2\2\u02ea\u02eb")
        buf.write("\7\u0080\2\2\u02eb\u02ed\7\u0081\2\2\u02ec\u02ea\3\2\2")
        buf.write("\2\u02ec\u02ed\3\2\2\2\u02ed\63\3\2\2\2\u02ee\u02f1\7")
        buf.write("\7\2\2\u02ef\u02f0\7\u0080\2\2\u02f0\u02f2\7\u0081\2\2")
        buf.write("\u02f1\u02ef\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2\65\3\2")
        buf.write("\2\2\u02f3\u02f6\7\b\2\2\u02f4\u02f5\7\u0080\2\2\u02f5")
        buf.write("\u02f7\7\u0081\2\2\u02f6\u02f4\3\2\2\2\u02f6\u02f7\3\2")
        buf.write("\2\2\u02f7\67\3\2\2\2\u02f8\u02fb\7\13\2\2\u02f9\u02fa")
        buf.write("\7\u0080\2\2\u02fa\u02fc\7\u0081\2\2\u02fb\u02f9\3\2\2")
        buf.write("\2\u02fb\u02fc\3\2\2\2\u02fc9\3\2\2\2\u02fd\u02fe\7\f")
        buf.write("\2\2\u02fe\u0302\7\u0080\2\2\u02ff\u0301\7x\2\2\u0300")
        buf.write("\u02ff\3\2\2\2\u0301\u0304\3\2\2\2\u0302\u0300\3\2\2\2")
        buf.write("\u0302\u0303\3\2\2\2\u0303\u0306\3\2\2\2\u0304\u0302\3")
        buf.write("\2\2\2\u0305\u0307\5<\37\2\u0306\u0305\3\2\2\2\u0306\u0307")
        buf.write("\3\2\2\2\u0307\u030b\3\2\2\2\u0308\u030a\7x\2\2\u0309")
        buf.write("\u0308\3\2\2\2\u030a\u030d\3\2\2\2\u030b\u0309\3\2\2\2")
        buf.write("\u030b\u030c\3\2\2\2\u030c\u030f\3\2\2\2\u030d\u030b\3")
        buf.write("\2\2\2\u030e\u0310\5F$\2\u030f\u030e\3\2\2\2\u0310\u0311")
        buf.write("\3\2\2\2\u0311\u030f\3\2\2\2\u0311\u0312\3\2\2\2\u0312")
        buf.write("\u0316\3\2\2\2\u0313\u0315\7x\2\2\u0314\u0313\3\2\2\2")
        buf.write("\u0315\u0318\3\2\2\2\u0316\u0314\3\2\2\2\u0316\u0317\3")
        buf.write("\2\2\2\u0317\u0319\3\2\2\2\u0318\u0316\3\2\2\2\u0319\u031a")
        buf.write("\7\u0081\2\2\u031a;\3\2\2\2\u031b\u031c\5> \2\u031c=\3")
        buf.write("\2\2\2\u031d\u031e\7J\2\2\u031e\u0322\7\u0080\2\2\u031f")
        buf.write("\u0321\7x\2\2\u0320\u031f\3\2\2\2\u0321\u0324\3\2\2\2")
        buf.write("\u0322\u0320\3\2\2\2\u0322\u0323\3\2\2\2\u0323\u0326\3")
        buf.write("\2\2\2\u0324\u0322\3\2\2\2\u0325\u0327\5@!\2\u0326\u0325")
        buf.write("\3\2\2\2\u0326\u0327\3\2\2\2\u0327\u032b\3\2\2\2\u0328")
        buf.write("\u032a\7x\2\2\u0329\u0328\3\2\2\2\u032a\u032d\3\2\2\2")
        buf.write("\u032b\u0329\3\2\2\2\u032b\u032c\3\2\2\2\u032c\u0334\3")
        buf.write("\2\2\2\u032d\u032b\3\2\2\2\u032e\u0330\5P)\2\u032f\u0331")
        buf.write("\7\u0087\2\2\u0330\u032f\3\2\2\2\u0330\u0331\3\2\2\2\u0331")
        buf.write("\u0333\3\2\2\2\u0332\u032e\3\2\2\2\u0333\u0336\3\2\2\2")
        buf.write("\u0334\u0332\3\2\2\2\u0334\u0335\3\2\2\2\u0335\u033a\3")
        buf.write("\2\2\2\u0336\u0334\3\2\2\2\u0337\u0339\7x\2\2\u0338\u0337")
        buf.write("\3\2\2\2\u0339\u033c\3\2\2\2\u033a\u0338\3\2\2\2\u033a")
        buf.write("\u033b\3\2\2\2\u033b\u033d\3\2\2\2\u033c\u033a\3\2\2\2")
        buf.write("\u033d\u033e\7\u0081\2\2\u033e?\3\2\2\2\u033f\u0340\7")
        buf.write("I\2\2\u0340\u0344\7\u0080\2\2\u0341\u0343\7x\2\2\u0342")
        buf.write("\u0341\3\2\2\2\u0343\u0346\3\2\2\2\u0344\u0342\3\2\2\2")
        buf.write("\u0344\u0345\3\2\2\2\u0345\u034f\3\2\2\2\u0346\u0344\3")
        buf.write("\2\2\2\u0347\u034c\5B\"\2\u0348\u0349\7\u0087\2\2\u0349")
        buf.write("\u034b\5B\"\2\u034a\u0348\3\2\2\2\u034b\u034e\3\2\2\2")
        buf.write("\u034c\u034a\3\2\2\2\u034c\u034d\3\2\2\2\u034d\u0350\3")
        buf.write("\2\2\2\u034e\u034c\3\2\2\2\u034f\u0347\3\2\2\2\u034f\u0350")
        buf.write("\3\2\2\2\u0350\u0354\3\2\2\2\u0351\u0353\7x\2\2\u0352")
        buf.write("\u0351\3\2\2\2\u0353\u0356\3\2\2\2\u0354\u0352\3\2\2\2")
        buf.write("\u0354\u0355\3\2\2\2\u0355\u0357\3\2\2\2\u0356\u0354\3")
        buf.write("\2\2\2\u0357\u0358\7\u0081\2\2\u0358A\3\2\2\2\u0359\u035b")
        buf.write("\7x\2\2\u035a\u0359\3\2\2\2\u035b\u035e\3\2\2\2\u035c")
        buf.write("\u035a\3\2\2\2\u035c\u035d\3\2\2\2\u035d\u035f\3\2\2\2")
        buf.write("\u035e\u035c\3\2\2\2\u035f\u0377\5D#\2\u0360\u0364\7\u0080")
        buf.write("\2\2\u0361\u0363\7x\2\2\u0362\u0361\3\2\2\2\u0363\u0366")
        buf.write("\3\2\2\2\u0364\u0362\3\2\2\2\u0364\u0365\3\2\2\2\u0365")
        buf.write("\u036d\3\2\2\2\u0366\u0364\3\2\2\2\u0367\u0369\5P)\2\u0368")
        buf.write("\u036a\7\u0087\2\2\u0369\u0368\3\2\2\2\u0369\u036a\3\2")
        buf.write("\2\2\u036a\u036c\3\2\2\2\u036b\u0367\3\2\2\2\u036c\u036f")
        buf.write("\3\2\2\2\u036d\u036b\3\2\2\2\u036d\u036e\3\2\2\2\u036e")
        buf.write("\u0373\3\2\2\2\u036f\u036d\3\2\2\2\u0370\u0372\7x\2\2")
        buf.write("\u0371\u0370\3\2\2\2\u0372\u0375\3\2\2\2\u0373\u0371\3")
        buf.write("\2\2\2\u0373\u0374\3\2\2\2\u0374\u0376\3\2\2\2\u0375\u0373")
        buf.write("\3\2\2\2\u0376\u0378\7\u0081\2\2\u0377\u0360\3\2\2\2\u0377")
        buf.write("\u0378\3\2\2\2\u0378C\3\2\2\2\u0379\u037a\5\32\16\2\u037a")
        buf.write("E\3\2\2\2\u037b\u037f\5J&\2\u037c\u037e\7x\2\2\u037d\u037c")
        buf.write("\3\2\2\2\u037e\u0381\3\2\2\2\u037f\u037d\3\2\2\2\u037f")
        buf.write("\u0380\3\2\2\2\u0380\u0382\3\2\2\2\u0381\u037f\3\2\2\2")
        buf.write("\u0382\u0386\5H%\2\u0383\u0385\7x\2\2\u0384\u0383\3\2")
        buf.write("\2\2\u0385\u0388\3\2\2\2\u0386\u0384\3\2\2\2\u0386\u0387")
        buf.write("\3\2\2\2\u0387\u0389\3\2\2\2\u0388\u0386\3\2\2\2\u0389")
        buf.write("\u038a\5L\'\2\u038a\u038e\7\u0080\2\2\u038b\u038d\7x\2")
        buf.write("\2\u038c\u038b\3\2\2\2\u038d\u0390\3\2\2\2\u038e\u038c")
        buf.write("\3\2\2\2\u038e\u038f\3\2\2\2\u038f\u0391\3\2\2\2\u0390")
        buf.write("\u038e\3\2\2\2\u0391\u03a2\5N(\2\u0392\u0396\7~\2\2\u0393")
        buf.write("\u0395\7x\2\2\u0394\u0393\3\2\2\2\u0395\u0398\3\2\2\2")
        buf.write("\u0396\u0394\3\2\2\2\u0396\u0397\3\2\2\2\u0397\u039f\3")
        buf.write("\2\2\2\u0398\u0396\3\2\2\2\u0399\u039b\5P)\2\u039a\u039c")
        buf.write("\7\u0087\2\2\u039b\u039a\3\2\2\2\u039b\u039c\3\2\2\2\u039c")
        buf.write("\u039e\3\2\2\2\u039d\u0399\3\2\2\2\u039e\u03a1\3\2\2\2")
        buf.write("\u039f\u039d\3\2\2\2\u039f\u03a0\3\2\2\2\u03a0\u03a3\3")
        buf.write("\2\2\2\u03a1\u039f\3\2\2\2\u03a2\u0392\3\2\2\2\u03a2\u03a3")
        buf.write("\3\2\2\2\u03a3\u03a7\3\2\2\2\u03a4\u03a6\7x\2\2\u03a5")
        buf.write("\u03a4\3\2\2\2\u03a6\u03a9\3\2\2\2\u03a7\u03a5\3\2\2\2")
        buf.write("\u03a7\u03a8\3\2\2\2\u03a8\u03aa\3\2\2\2\u03a9\u03a7\3")
        buf.write("\2\2\2\u03aa\u03ae\7\u0081\2\2\u03ab\u03ad\7x\2\2\u03ac")
        buf.write("\u03ab\3\2\2\2\u03ad\u03b0\3\2\2\2\u03ae\u03ac\3\2\2\2")
        buf.write("\u03ae\u03af\3\2\2\2\u03afG\3\2\2\2\u03b0\u03ae\3\2\2")
        buf.write("\2\u03b1\u03b2\t\4\2\2\u03b2\u03b3\7}\2\2\u03b3I\3\2\2")
        buf.write("\2\u03b4\u03b9\5\32\16\2\u03b5\u03b9\7\u0086\2\2\u03b6")
        buf.write("\u03b9\7\u008f\2\2\u03b7\u03b9\7\u008a\2\2\u03b8\u03b4")
        buf.write("\3\2\2\2\u03b8\u03b5\3\2\2\2\u03b8\u03b6\3\2\2\2\u03b8")
        buf.write("\u03b7\3\2\2\2\u03b9\u03ba\3\2\2\2\u03ba\u03b8\3\2\2\2")
        buf.write("\u03ba\u03bb\3\2\2\2\u03bbK\3\2\2\2\u03bc\u03c1\5\32\16")
        buf.write("\2\u03bd\u03c1\7\u0086\2\2\u03be\u03c1\7\u008a\2\2\u03bf")
        buf.write("\u03c1\7\u008f\2\2\u03c0\u03bc\3\2\2\2\u03c0\u03bd\3\2")
        buf.write("\2\2\u03c0\u03be\3\2\2\2\u03c0\u03bf\3\2\2\2\u03c1\u03c2")
        buf.write("\3\2\2\2\u03c2\u03c0\3\2\2\2\u03c2\u03c3\3\2\2\2\u03c3")
        buf.write("M\3\2\2\2\u03c4\u03c9\5\32\16\2\u03c5\u03c9\7\u0086\2")
        buf.write("\2\u03c6\u03c9\7\u008f\2\2\u03c7\u03c9\7\u0088\2\2\u03c8")
        buf.write("\u03c4\3\2\2\2\u03c8\u03c5\3\2\2\2\u03c8\u03c6\3\2\2\2")
        buf.write("\u03c8\u03c7\3\2\2\2\u03c9\u03ca\3\2\2\2\u03ca\u03c8\3")
        buf.write("\2\2\2\u03ca\u03cb\3\2\2\2\u03cbO\3\2\2\2\u03cc\u03ce")
        buf.write("\7x\2\2\u03cd\u03cc\3\2\2\2\u03ce\u03d1\3\2\2\2\u03cf")
        buf.write("\u03cd\3\2\2\2\u03cf\u03d0\3\2\2\2\u03d0\u03d2\3\2\2\2")
        buf.write("\u03d1\u03cf\3\2\2\2\u03d2\u03d3\5R*\2\u03d3\u03d4\7\u008b")
        buf.write("\2\2\u03d4\u03d5\5T+\2\u03d5Q\3\2\2\2\u03d6\u03d7\5\32")
        buf.write("\16\2\u03d7S\3\2\2\2\u03d8\u03dd\7\u0092\2\2\u03d9\u03dd")
        buf.write("\7\u0093\2\2\u03da\u03dd\7z\2\2\u03db\u03dd\5\32\16\2")
        buf.write("\u03dc\u03d8\3\2\2\2\u03dc\u03d9\3\2\2\2\u03dc\u03da\3")
        buf.write("\2\2\2\u03dc\u03db\3\2\2\2\u03ddU\3\2\2\2\u03de\u03df")
        buf.write("\7\22\2\2\u03df\u03e0\5X-\2\u03e0\u03e1\5&\24\2\u03e1")
        buf.write("W\3\2\2\2\u03e2\u03e3\t\5\2\2\u03e3Y\3\2\2\2\u03e4\u03e5")
        buf.write("\7\20\2\2\u03e5\u03e6\7\u0080\2\2\u03e6\u03eb\5^\60\2")
        buf.write("\u03e7\u03e8\7\u0087\2\2\u03e8\u03e9\7G\2\2\u03e9\u03ea")
        buf.write("\7\u008b\2\2\u03ea\u03ec\5\\/\2\u03eb\u03e7\3\2\2\2\u03eb")
        buf.write("\u03ec\3\2\2\2\u03ec\u03ed\3\2\2\2\u03ed\u03ee\7\u0081")
        buf.write("\2\2\u03ee[\3\2\2\2\u03ef\u03f0\7w\2\2\u03f0]\3\2\2\2")
        buf.write("\u03f1\u03f5\5\32\16\2\u03f2\u03f5\7\u0092\2\2\u03f3\u03f5")
        buf.write("\7\u0093\2\2\u03f4\u03f1\3\2\2\2\u03f4\u03f2\3\2\2\2\u03f4")
        buf.write("\u03f3\3\2\2\2\u03f5_\3\2\2\2\u03f6\u03f7\7+\2\2\u03f7")
        buf.write("\u03f8\7\u0080\2\2\u03f8\u03f9\5b\62\2\u03f9\u03fa\7\u0081")
        buf.write("\2\2\u03faa\3\2\2\2\u03fb\u0400\7y\2\2\u03fc\u03fd\7\u0087")
        buf.write("\2\2\u03fd\u03ff\7y\2\2\u03fe\u03fc\3\2\2\2\u03ff\u0402")
        buf.write("\3\2\2\2\u0400\u03fe\3\2\2\2\u0400\u0401\3\2\2\2\u0401")
        buf.write("c\3\2\2\2\u0402\u0400\3\2\2\2\u0403\u0405\5h\65\2\u0404")
        buf.write("\u0406\5f\64\2\u0405\u0404\3\2\2\2\u0405\u0406\3\2\2\2")
        buf.write("\u0406\u040a\3\2\2\2\u0407\u0409\7x\2\2\u0408\u0407\3")
        buf.write("\2\2\2\u0409\u040c\3\2\2\2\u040a\u0408\3\2\2\2\u040a\u040b")
        buf.write("\3\2\2\2\u040b\u0410\3\2\2\2\u040c\u040a\3\2\2\2\u040d")
        buf.write("\u040f\5t;\2\u040e\u040d\3\2\2\2\u040f\u0412\3\2\2\2\u0410")
        buf.write("\u040e\3\2\2\2\u0410\u0411\3\2\2\2\u0411\u0416\3\2\2\2")
        buf.write("\u0412\u0410\3\2\2\2\u0413\u0415\7x\2\2\u0414\u0413\3")
        buf.write("\2\2\2\u0415\u0418\3\2\2\2\u0416\u0414\3\2\2\2\u0416\u0417")
        buf.write("\3\2\2\2\u0417\u041c\3\2\2\2\u0418\u0416\3\2\2\2\u0419")
        buf.write("\u041b\5\u00e6t\2\u041a\u0419\3\2\2\2\u041b\u041e\3\2")
        buf.write("\2\2\u041c\u041a\3\2\2\2\u041c\u041d\3\2\2\2\u041d\u0422")
        buf.write("\3\2\2\2\u041e\u041c\3\2\2\2\u041f\u0421\7x\2\2\u0420")
        buf.write("\u041f\3\2\2\2\u0421\u0424\3\2\2\2\u0422\u0420\3\2\2\2")
        buf.write("\u0422\u0423\3\2\2\2\u0423e\3\2\2\2\u0424\u0422\3\2\2")
        buf.write("\2\u0425\u0426\7\u008b\2\2\u0426\u042d\t\3\2\2\u0427\u0429")
        buf.write("\7x\2\2\u0428\u0427\3\2\2\2\u0429\u042a\3\2\2\2\u042a")
        buf.write("\u0428\3\2\2\2\u042a\u042b\3\2\2\2\u042b\u042e\3\2\2\2")
        buf.write("\u042c\u042e\7\2\2\3\u042d\u0428\3\2\2\2\u042d\u042c\3")
        buf.write("\2\2\2\u042eg\3\2\2\2\u042f\u0431\7\u0089\2\2\u0430\u0432")
        buf.write("\5p9\2\u0431\u0430\3\2\2\2\u0431\u0432\3\2\2\2\u0432\u0433")
        buf.write("\3\2\2\2\u0433\u0435\5r:\2\u0434\u0436\5l\67\2\u0435\u0434")
        buf.write("\3\2\2\2\u0435\u0436\3\2\2\2\u0436\u0437\3\2\2\2\u0437")
        buf.write("\u0438\5j\66\2\u0438\u0439\7x\2\2\u0439i\3\2\2\2\u043a")
        buf.write("\u043b\7x\2\2\u043b\u043c\7\u0086\2\2\u043c\u043e\7\u0086")
        buf.write("\2\2\u043d\u043f\7\u0086\2\2\u043e\u043d\3\2\2\2\u043f")
        buf.write("\u0440\3\2\2\2\u0440\u043e\3\2\2\2\u0440\u0441\3\2\2\2")
        buf.write("\u0441k\3\2\2\2\u0442\u0443\7~\2\2\u0443\u0446\5n8\2\u0444")
        buf.write("\u0445\7\u008a\2\2\u0445\u0447\5n8\2\u0446\u0444\3\2\2")
        buf.write("\2\u0446\u0447\3\2\2\2\u0447m\3\2\2\2\u0448\u044c\5\32")
        buf.write("\16\2\u0449\u044c\7\u0092\2\2\u044a\u044c\7\u0093\2\2")
        buf.write("\u044b\u0448\3\2\2\2\u044b\u0449\3\2\2\2\u044b\u044a\3")
        buf.write("\2\2\2\u044co\3\2\2\2\u044d\u0452\5\32\16\2\u044e\u044f")
        buf.write("\7\u0086\2\2\u044f\u0453\7}\2\2\u0450\u0451\7\u0090\2")
        buf.write("\2\u0451\u0453\7}\2\2\u0452\u044e\3\2\2\2\u0452\u0450")
        buf.write("\3\2\2\2\u0453q\3\2\2\2\u0454\u0455\5\32\16\2\u0455s\3")
        buf.write("\2\2\2\u0456\u0458\5\u008eH\2\u0457\u0456\3\2\2\2\u0458")
        buf.write("\u045b\3\2\2\2\u0459\u0457\3\2\2\2\u0459\u045a\3\2\2\2")
        buf.write("\u045a\u045c\3\2\2\2\u045b\u0459\3\2\2\2\u045c\u045e\5")
        buf.write("\u008cG\2\u045d\u045f\5v<\2\u045e\u045d\3\2\2\2\u045e")
        buf.write("\u045f\3\2\2\2\u045f\u0461\3\2\2\2\u0460\u0462\5\u008a")
        buf.write("F\2\u0461\u0460\3\2\2\2\u0461\u0462\3\2\2\2\u0462\u0464")
        buf.write("\3\2\2\2\u0463\u0465\5\u0088E\2\u0464\u0463\3\2\2\2\u0464")
        buf.write("\u0465\3\2\2\2\u0465\u046c\3\2\2\2\u0466\u0468\7x\2\2")
        buf.write("\u0467\u0466\3\2\2\2\u0468\u0469\3\2\2\2\u0469\u0467\3")
        buf.write("\2\2\2\u0469\u046a\3\2\2\2\u046a\u046d\3\2\2\2\u046b\u046d")
        buf.write("\7\2\2\3\u046c\u0467\3\2\2\2\u046c\u046b\3\2\2\2\u046d")
        buf.write("u\3\2\2\2\u046e\u0470\7~\2\2\u046f\u0471\5x=\2\u0470\u046f")
        buf.write("\3\2\2\2\u0470\u0471\3\2\2\2\u0471\u047b\3\2\2\2\u0472")
        buf.write("\u0473\7~\2\2\u0473\u0475\5\u0090I\2\u0474\u0476\5z>\2")
        buf.write("\u0475\u0474\3\2\2\2\u0475\u0476\3\2\2\2\u0476\u047b\3")
        buf.write("\2\2\2\u0477\u0478\7~\2\2\u0478\u047b\5~@\2\u0479\u047b")
        buf.write("\5\u0080A\2\u047a\u046e\3\2\2\2\u047a\u0472\3\2\2\2\u047a")
        buf.write("\u0477\3\2\2\2\u047a\u0479\3\2\2\2\u047bw\3\2\2\2\u047c")
        buf.write("\u047d\5*\26\2\u047dy\3\2\2\2\u047e\u0480\5|?\2\u047f")
        buf.write("\u047e\3\2\2\2\u047f\u0480\3\2\2\2\u0480\u0481\3\2\2\2")
        buf.write("\u0481\u0482\5*\26\2\u0482{\3\2\2\2\u0483\u0484\7\u0088")
        buf.write("\2\2\u0484\u0485\7\u0088\2\2\u0485}\3\2\2\2\u0486\u0487")
        buf.write("\5\32\16\2\u0487\177\3\2\2\2\u0488\u0489\5\u0082B\2\u0489")
        buf.write("\u048a\5\u0084C\2\u048a\u0081\3\2\2\2\u048b\u048c\t\6")
        buf.write("\2\2\u048c\u0083\3\2\2\2\u048d\u048e\7\u009d\2\2\u048e")
        buf.write("\u0085\3\2\2\2\u048f\u0491\5\32\16\2\u0490\u048f\3\2\2")
        buf.write("\2\u0491\u0492\3\2\2\2\u0492\u0490\3\2\2\2\u0492\u0493")
        buf.write("\3\2\2\2\u0493\u0497\3\2\2\2\u0494\u0497\7\u0092\2\2\u0495")
        buf.write("\u0497\7\u0093\2\2\u0496\u0490\3\2\2\2\u0496\u0494\3\2")
        buf.write("\2\2\u0496\u0495\3\2\2\2\u0497\u0087\3\2\2\2\u0498\u0499")
        buf.write("\7\u0084\2\2\u0499\u049a\5\u0086D\2\u049a\u0089\3\2\2")
        buf.write("\2\u049b\u049c\7\u008a\2\2\u049c\u049d\5\u0086D\2\u049d")
        buf.write("\u008b\3\2\2\2\u049e\u049f\5\32\16\2\u049f\u008d\3\2\2")
        buf.write("\2\u04a0\u04a1\t\7\2\2\u04a1\u008f\3\2\2\2\u04a2\u04b5")
        buf.write("\5\u0092J\2\u04a3\u04b5\5\u0096L\2\u04a4\u04b5\5\u0094")
        buf.write("K\2\u04a5\u04b5\5\u0098M\2\u04a6\u04b5\5\u009aN\2\u04a7")
        buf.write("\u04b5\5\u009cO\2\u04a8\u04b5\5\u009eP\2\u04a9\u04b5\5")
        buf.write("\u00a0Q\2\u04aa\u04b5\5\u00a2R\2\u04ab\u04b5\5\u00aaV")
        buf.write("\2\u04ac\u04b5\5\u00b6\\\2\u04ad\u04b5\5\u00c0a\2\u04ae")
        buf.write("\u04b5\5\u00c6d\2\u04af\u04b5\5\u00dan\2\u04b0\u04b5\5")
        buf.write("\u00caf\2\u04b1\u04b5\5\u00a4S\2\u04b2\u04b5\5\u00a6T")
        buf.write("\2\u04b3\u04b5\5\u00a8U\2\u04b4\u04a2\3\2\2\2\u04b4\u04a3")
        buf.write("\3\2\2\2\u04b4\u04a4\3\2\2\2\u04b4\u04a5\3\2\2\2\u04b4")
        buf.write("\u04a6\3\2\2\2\u04b4\u04a7\3\2\2\2\u04b4\u04a8\3\2\2\2")
        buf.write("\u04b4\u04a9\3\2\2\2\u04b4\u04aa\3\2\2\2\u04b4\u04ab\3")
        buf.write("\2\2\2\u04b4\u04ac\3\2\2\2\u04b4\u04ad\3\2\2\2\u04b4\u04ae")
        buf.write("\3\2\2\2\u04b4\u04af\3\2\2\2\u04b4\u04b0\3\2\2\2\u04b4")
        buf.write("\u04b1\3\2\2\2\u04b4\u04b2\3\2\2\2\u04b4\u04b3\3\2\2\2")
        buf.write("\u04b5\u0091\3\2\2\2\u04b6\u04b7\7/\2\2\u04b7\u0093\3")
        buf.write("\2\2\2\u04b8\u04b9\7\60\2\2\u04b9\u0095\3\2\2\2\u04ba")
        buf.write("\u04bb\7\61\2\2\u04bb\u0097\3\2\2\2\u04bc\u04bd\7\62\2")
        buf.write("\2\u04bd\u0099\3\2\2\2\u04be\u04bf\7\63\2\2\u04bf\u009b")
        buf.write("\3\2\2\2\u04c0\u04c1\7\64\2\2\u04c1\u009d\3\2\2\2\u04c2")
        buf.write("\u04c3\7\65\2\2\u04c3\u009f\3\2\2\2\u04c4\u04c5\7\66\2")
        buf.write("\2\u04c5\u00a1\3\2\2\2\u04c6\u04c7\7\67\2\2\u04c7\u00a3")
        buf.write("\3\2\2\2\u04c8\u04c9\79\2\2\u04c9\u00a5\3\2\2\2\u04ca")
        buf.write("\u04cb\7;\2\2\u04cb\u00a7\3\2\2\2\u04cc\u04cd\7<\2\2\u04cd")
        buf.write("\u00a9\3\2\2\2\u04ce\u04d7\7>\2\2\u04cf\u04d0\7\u0080")
        buf.write("\2\2\u04d0\u04d3\5\u00acW\2\u04d1\u04d2\7\u0087\2\2\u04d2")
        buf.write("\u04d4\5\u00aeX\2\u04d3\u04d1\3\2\2\2\u04d3\u04d4\3\2")
        buf.write("\2\2\u04d4\u04d5\3\2\2\2\u04d5\u04d6\7\u0081\2\2\u04d6")
        buf.write("\u04d8\3\2\2\2\u04d7\u04cf\3\2\2\2\u04d7\u04d8\3\2\2\2")
        buf.write("\u04d8\u00ab\3\2\2\2\u04d9\u04da\t\b\2\2\u04da\u00ad\3")
        buf.write("\2\2\2\u04db\u04dc\7E\2\2\u04dc\u04dd\7\u008b\2\2\u04dd")
        buf.write("\u04e2\5\u00b0Y\2\u04de\u04df\7\u0087\2\2\u04df\u04e1")
        buf.write("\5\u00b0Y\2\u04e0\u04de\3\2\2\2\u04e1\u04e4\3\2\2\2\u04e2")
        buf.write("\u04e0\3\2\2\2\u04e2\u04e3\3\2\2\2\u04e3\u00af\3\2\2\2")
        buf.write("\u04e4\u04e2\3\2\2\2\u04e5\u04e7\5\u00b4[\2\u04e6\u04e5")
        buf.write("\3\2\2\2\u04e6\u04e7\3\2\2\2\u04e7\u04e8\3\2\2\2\u04e8")
        buf.write("\u04e9\5\u00b2Z\2\u04e9\u00b1\3\2\2\2\u04ea\u04ee\5\32")
        buf.write("\16\2\u04eb\u04ee\7\u0092\2\2\u04ec\u04ee\7\u0093\2\2")
        buf.write("\u04ed\u04ea\3\2\2\2\u04ed\u04eb\3\2\2\2\u04ed\u04ec\3")
        buf.write("\2\2\2\u04ee\u00b3\3\2\2\2\u04ef\u04f0\5\32\16\2\u04f0")
        buf.write("\u04f1\7~\2\2\u04f1\u00b5\3\2\2\2\u04f2\u04f7\7?\2\2\u04f3")
        buf.write("\u04f4\7\u0080\2\2\u04f4\u04f5\5\u00b8]\2\u04f5\u04f6")
        buf.write("\7\u0081\2\2\u04f6\u04f8\3\2\2\2\u04f7\u04f3\3\2\2\2\u04f7")
        buf.write("\u04f8\3\2\2\2\u04f8\u00b7\3\2\2\2\u04f9\u04fa\7E\2\2")
        buf.write("\u04fa\u04fb\7\u008b\2\2\u04fb\u0500\5\u00ba^\2\u04fc")
        buf.write("\u04fd\7\u0087\2\2\u04fd\u04ff\5\u00ba^\2\u04fe\u04fc")
        buf.write("\3\2\2\2\u04ff\u0502\3\2\2\2\u0500\u04fe\3\2\2\2\u0500")
        buf.write("\u0501\3\2\2\2\u0501\u00b9\3\2\2\2\u0502\u0500\3\2\2\2")
        buf.write("\u0503\u0505\5\u00be`\2\u0504\u0503\3\2\2\2\u0504\u0505")
        buf.write("\3\2\2\2\u0505\u0506\3\2\2\2\u0506\u0507\5\u00bc_\2\u0507")
        buf.write("\u00bb\3\2\2\2\u0508\u050c\5\32\16\2\u0509\u050c\7\u0092")
        buf.write("\2\2\u050a\u050c\7\u0093\2\2\u050b\u0508\3\2\2\2\u050b")
        buf.write("\u0509\3\2\2\2\u050b\u050a\3\2\2\2\u050c\u00bd\3\2\2\2")
        buf.write("\u050d\u050e\7z\2\2\u050e\u050f\7~\2\2\u050f\u00bf\3\2")
        buf.write("\2\2\u0510\u0511\7@\2\2\u0511\u0512\7\u0080\2\2\u0512")
        buf.write("\u0513\5\u00c2b\2\u0513\u0514\7\u0081\2\2\u0514\u00c1")
        buf.write("\3\2\2\2\u0515\u051a\5\u00c4c\2\u0516\u0517\7\u0087\2")
        buf.write("\2\u0517\u0519\5\u00c4c\2\u0518\u0516\3\2\2\2\u0519\u051c")
        buf.write("\3\2\2\2\u051a\u0518\3\2\2\2\u051a\u051b\3\2\2\2\u051b")
        buf.write("\u00c3\3\2\2\2\u051c\u051a\3\2\2\2\u051d\u051e\5\32\16")
        buf.write("\2\u051e\u00c5\3\2\2\2\u051f\u0524\7A\2\2\u0520\u0521")
        buf.write("\7\u0080\2\2\u0521\u0522\5\u00c8e\2\u0522\u0523\7\u0081")
        buf.write("\2\2\u0523\u0525\3\2\2\2\u0524\u0520\3\2\2\2\u0524\u0525")
        buf.write("\3\2\2\2\u0525\u00c7\3\2\2\2\u0526\u0527\7w\2\2\u0527")
        buf.write("\u00c9\3\2\2\2\u0528\u052d\5\u00ccg\2\u0529\u052a\7\u0080")
        buf.write("\2\2\u052a\u052b\5\u00ceh\2\u052b\u052c\7\u0081\2\2\u052c")
        buf.write("\u052e\3\2\2\2\u052d\u0529\3\2\2\2\u052d\u052e\3\2\2\2")
        buf.write("\u052e\u00cb\3\2\2\2\u052f\u0530\t\t\2\2\u0530\u00cd\3")
        buf.write("\2\2\2\u0531\u0536\5\u00d0i\2\u0532\u0533\7\u0087\2\2")
        buf.write("\u0533\u0535\5\u00d0i\2\u0534\u0532\3\2\2\2\u0535\u0538")
        buf.write("\3\2\2\2\u0536\u0534\3\2\2\2\u0536\u0537\3\2\2\2\u0537")
        buf.write("\u00cf\3\2\2\2\u0538\u0536\3\2\2\2\u0539\u053a\5\u00d4")
        buf.write("k\2\u053a\u053b\5\u00d2j\2\u053b\u053c\5\u00d6l\2\u053c")
        buf.write("\u00d1\3\2\2\2\u053d\u053e\7{\2\2\u053e\u00d3\3\2\2\2")
        buf.write("\u053f\u0540\5\32\16\2\u0540\u0541\7\u008b\2\2\u0541\u00d5")
        buf.write("\3\2\2\2\u0542\u0544\5\u00d8m\2\u0543\u0542\3\2\2\2\u0544")
        buf.write("\u0547\3\2\2\2\u0545\u0543\3\2\2\2\u0545\u0546\3\2\2\2")
        buf.write("\u0546\u00d7\3\2\2\2\u0547\u0545\3\2\2\2\u0548\u0549\7")
        buf.write("\u0091\2\2\u0549\u054a\5\32\16\2\u054a\u00d9\3\2\2\2\u054b")
        buf.write("\u054c\5\u00dco\2\u054c\u054e\7\u0080\2\2\u054d\u054f")
        buf.write("\5\u00dep\2\u054e\u054d\3\2\2\2\u054e\u054f\3\2\2\2\u054f")
        buf.write("\u0552\3\2\2\2\u0550\u0553\5\u00e0q\2\u0551\u0553\5\u00e2")
        buf.write("r\2\u0552\u0550\3\2\2\2\u0552\u0551\3\2\2\2\u0553\u0555")
        buf.write("\3\2\2\2\u0554\u0556\5\u00e4s\2\u0555\u0554\3\2\2\2\u0555")
        buf.write("\u0556\3\2\2\2\u0556\u0557\3\2\2\2\u0557\u0558\7\u0081")
        buf.write("\2\2\u0558\u00db\3\2\2\2\u0559\u055a\t\n\2\2\u055a\u00dd")
        buf.write("\3\2\2\2\u055b\u055c\t\13\2\2\u055c\u00df\3\2\2\2\u055d")
        buf.write("\u055e\5\36\20\2\u055e\u00e1\3\2\2\2\u055f\u0560\5\34")
        buf.write("\17\2\u0560\u00e3\3\2\2\2\u0561\u0562\7\u0086\2\2\u0562")
        buf.write("\u0563\7}\2\2\u0563\u0564\5\32\16\2\u0564\u00e5\3\2\2")
        buf.write("\2\u0565\u0575\5\u00e8u\2\u0566\u0575\5\u0114\u008b\2")
        buf.write("\u0567\u0575\5\u011a\u008e\2\u0568\u0575\5\u014c\u00a7")
        buf.write("\2\u0569\u0575\5\u0150\u00a9\2\u056a\u0575\5\u0152\u00aa")
        buf.write("\2\u056b\u0575\5\u0154\u00ab\2\u056c\u0575\5\u0158\u00ad")
        buf.write("\2\u056d\u0575\5\u015a\u00ae\2\u056e\u0575\5\u015e\u00b0")
        buf.write("\2\u056f\u0575\5\u0160\u00b1\2\u0570\u0575\5\u0162\u00b2")
        buf.write("\2\u0571\u0575\5\u0164\u00b3\2\u0572\u0575\5\u0166\u00b4")
        buf.write("\2\u0573\u0575\7x\2\2\u0574\u0565\3\2\2\2\u0574\u0566")
        buf.write("\3\2\2\2\u0574\u0567\3\2\2\2\u0574\u0568\3\2\2\2\u0574")
        buf.write("\u0569\3\2\2\2\u0574\u056a\3\2\2\2\u0574\u056b\3\2\2\2")
        buf.write("\u0574\u056c\3\2\2\2\u0574\u056d\3\2\2\2\u0574\u056e\3")
        buf.write("\2\2\2\u0574\u056f\3\2\2\2\u0574\u0570\3\2\2\2\u0574\u0571")
        buf.write("\3\2\2\2\u0574\u0572\3\2\2\2\u0574\u0573\3\2\2\2\u0575")
        buf.write("\u00e7\3\2\2\2\u0576\u0590\7\3\2\2\u0577\u0586\7\u0080")
        buf.write("\2\2\u0578\u0585\5\u0108\u0085\2\u0579\u0585\5\u010a\u0086")
        buf.write("\2\u057a\u0585\5\u010c\u0087\2\u057b\u0585\5\u010e\u0088")
        buf.write("\2\u057c\u0585\5\u0110\u0089\2\u057d\u0585\5\u0112\u008a")
        buf.write("\2\u057e\u0585\5\u0100\u0081\2\u057f\u0585\5\u00f2z\2")
        buf.write("\u0580\u0585\5\u00ecw\2\u0581\u0585\5\u00eav\2\u0582\u0585")
        buf.write("\7x\2\2\u0583\u0585\7\u0087\2\2\u0584\u0578\3\2\2\2\u0584")
        buf.write("\u0579\3\2\2\2\u0584\u057a\3\2\2\2\u0584\u057b\3\2\2\2")
        buf.write("\u0584\u057c\3\2\2\2\u0584\u057d\3\2\2\2\u0584\u057e\3")
        buf.write("\2\2\2\u0584\u057f\3\2\2\2\u0584\u0580\3\2\2\2\u0584\u0581")
        buf.write("\3\2\2\2\u0584\u0582\3\2\2\2\u0584\u0583\3\2\2\2\u0585")
        buf.write("\u0588\3\2\2\2\u0586\u0584\3\2\2\2\u0586\u0587\3\2\2\2")
        buf.write("\u0587\u058c\3\2\2\2\u0588\u0586\3\2\2\2\u0589\u058b\7")
        buf.write("x\2\2\u058a\u0589\3\2\2\2\u058b\u058e\3\2\2\2\u058c\u058a")
        buf.write("\3\2\2\2\u058c\u058d\3\2\2\2\u058d\u058f\3\2\2\2\u058e")
        buf.write("\u058c\3\2\2\2\u058f\u0591\7\u0081\2\2\u0590\u0577\3\2")
        buf.write("\2\2\u0590\u0591\3\2\2\2\u0591\u0595\3\2\2\2\u0592\u0594")
        buf.write("\7x\2\2\u0593\u0592\3\2\2\2\u0594\u0597\3\2\2\2\u0595")
        buf.write("\u0593\3\2\2\2\u0595\u0596\3\2\2\2\u0596\u00e9\3\2\2\2")
        buf.write("\u0597\u0595\3\2\2\2\u0598\u0599\7_\2\2\u0599\u059d\7")
        buf.write("~\2\2\u059a\u059c\7x\2\2\u059b\u059a\3\2\2\2\u059c\u059f")
        buf.write("\3\2\2\2\u059d\u059b\3\2\2\2\u059d\u059e\3\2\2\2\u059e")
        buf.write("\u05a0\3\2\2\2\u059f\u059d\3\2\2\2\u05a0\u05ab\5\u00f0")
        buf.write("y\2\u05a1\u05a5\7\u0087\2\2\u05a2\u05a4\7x\2\2\u05a3\u05a2")
        buf.write("\3\2\2\2\u05a4\u05a7\3\2\2\2\u05a5\u05a3\3\2\2\2\u05a5")
        buf.write("\u05a6\3\2\2\2\u05a6\u05a8\3\2\2\2\u05a7\u05a5\3\2\2\2")
        buf.write("\u05a8\u05aa\5\u00f0y\2\u05a9\u05a1\3\2\2\2\u05aa\u05ad")
        buf.write("\3\2\2\2\u05ab\u05a9\3\2\2\2\u05ab\u05ac\3\2\2\2\u05ac")
        buf.write("\u00eb\3\2\2\2\u05ad\u05ab\3\2\2\2\u05ae\u05af\7^\2\2")
        buf.write("\u05af\u05b0\7~\2\2\u05b0\u05b5\5\u00eex\2\u05b1\u05b2")
        buf.write("\7\u0087\2\2\u05b2\u05b4\5\u00eex\2\u05b3\u05b1\3\2\2")
        buf.write("\2\u05b4\u05b7\3\2\2\2\u05b5\u05b3\3\2\2\2\u05b5\u05b6")
        buf.write("\3\2\2\2\u05b6\u00ed\3\2\2\2\u05b7\u05b5\3\2\2\2\u05b8")
        buf.write("\u05b9\t\3\2\2\u05b9\u00ef\3\2\2\2\u05ba\u05bb\t\3\2\2")
        buf.write("\u05bb\u00f1\3\2\2\2\u05bc\u05bd\7c\2\2\u05bd\u05be\7")
        buf.write("~\2\2\u05be\u05c3\5\u00f4{\2\u05bf\u05c0\7\u0087\2\2\u05c0")
        buf.write("\u05c2\5\u00f4{\2\u05c1\u05bf\3\2\2\2\u05c2\u05c5\3\2")
        buf.write("\2\2\u05c3\u05c1\3\2\2\2\u05c3\u05c4\3\2\2\2\u05c4\u00f3")
        buf.write("\3\2\2\2\u05c5\u05c3\3\2\2\2\u05c6\u05d3\5\u00f6|\2\u05c7")
        buf.write("\u05cf\7\u0080\2\2\u05c8\u05ce\5\u00f8}\2\u05c9\u05ce")
        buf.write("\5\u00fc\177\2\u05ca\u05ce\5\u00fe\u0080\2\u05cb\u05ce")
        buf.write("\7x\2\2\u05cc\u05ce\7\u0087\2\2\u05cd\u05c8\3\2\2\2\u05cd")
        buf.write("\u05c9\3\2\2\2\u05cd\u05ca\3\2\2\2\u05cd\u05cb\3\2\2\2")
        buf.write("\u05cd\u05cc\3\2\2\2\u05ce\u05d1\3\2\2\2\u05cf\u05cd\3")
        buf.write("\2\2\2\u05cf\u05d0\3\2\2\2\u05d0\u05d2\3\2\2\2\u05d1\u05cf")
        buf.write("\3\2\2\2\u05d2\u05d4\7\u0081\2\2\u05d3\u05c7\3\2\2\2\u05d3")
        buf.write("\u05d4\3\2\2\2\u05d4\u00f5\3\2\2\2\u05d5\u05d6\5\32\16")
        buf.write("\2\u05d6\u00f7\3\2\2\2\u05d7\u05d8\7d\2\2\u05d8\u05d9")
        buf.write("\7~\2\2\u05d9\u05da\5\u00fa~\2\u05da\u00f9\3\2\2\2\u05db")
        buf.write("\u05dc\t\f\2\2\u05dc\u00fb\3\2\2\2\u05dd\u05de\7l\2\2")
        buf.write("\u05de\u05df\7~\2\2\u05df\u05e0\7z\2\2\u05e0\u00fd\3\2")
        buf.write("\2\2\u05e1\u05e2\7s\2\2\u05e2\u05e3\7~\2\2\u05e3\u05e4")
        buf.write("\5 \21\2\u05e4\u00ff\3\2\2\2\u05e5\u05e6\7m\2\2\u05e6")
        buf.write("\u05e7\7~\2\2\u05e7\u05ec\5\u0102\u0082\2\u05e8\u05e9")
        buf.write("\7\u0087\2\2\u05e9\u05eb\5\u0102\u0082\2\u05ea\u05e8\3")
        buf.write("\2\2\2\u05eb\u05ee\3\2\2\2\u05ec\u05ea\3\2\2\2\u05ec\u05ed")
        buf.write("\3\2\2\2\u05ed\u0101\3\2\2\2\u05ee\u05ec\3\2\2\2\u05ef")
        buf.write("\u05f1\5\u0104\u0083\2\u05f0\u05f2\5\u0106\u0084\2\u05f1")
        buf.write("\u05f0\3\2\2\2\u05f1\u05f2\3\2\2\2\u05f2\u05f3\3\2\2\2")
        buf.write("\u05f3\u05f4\7\u0080\2\2\u05f4\u05f5\5 \21\2\u05f5\u05f6")
        buf.write("\7\u0081\2\2\u05f6\u0103\3\2\2\2\u05f7\u05f8\5\32\16\2")
        buf.write("\u05f8\u0105\3\2\2\2\u05f9\u05fa\t\3\2\2\u05fa\u0107\3")
        buf.write("\2\2\2\u05fb\u05fc\7n\2\2\u05fc\u05fd\7~\2\2\u05fd\u0601")
        buf.write("\5 \21\2\u05fe\u0600\7x\2\2\u05ff\u05fe\3\2\2\2\u0600")
        buf.write("\u0603\3\2\2\2\u0601\u05ff\3\2\2\2\u0601\u0602\3\2\2\2")
        buf.write("\u0602\u0109\3\2\2\2\u0603\u0601\3\2\2\2\u0604\u0605\7")
        buf.write("o\2\2\u0605\u0606\7~\2\2\u0606\u060a\5 \21\2\u0607\u0609")
        buf.write("\7x\2\2\u0608\u0607\3\2\2\2\u0609\u060c\3\2\2\2\u060a")
        buf.write("\u0608\3\2\2\2\u060a\u060b\3\2\2\2\u060b\u010b\3\2\2\2")
        buf.write("\u060c\u060a\3\2\2\2\u060d\u060e\7p\2\2\u060e\u060f\7")
        buf.write("~\2\2\u060f\u0613\5 \21\2\u0610\u0612\7x\2\2\u0611\u0610")
        buf.write("\3\2\2\2\u0612\u0615\3\2\2\2\u0613\u0611\3\2\2\2\u0613")
        buf.write("\u0614\3\2\2\2\u0614\u010d\3\2\2\2\u0615\u0613\3\2\2\2")
        buf.write("\u0616\u0617\7q\2\2\u0617\u0618\7~\2\2\u0618\u061c\5 ")
        buf.write("\21\2\u0619\u061b\7x\2\2\u061a\u0619\3\2\2\2\u061b\u061e")
        buf.write("\3\2\2\2\u061c\u061a\3\2\2\2\u061c\u061d\3\2\2\2\u061d")
        buf.write("\u010f\3\2\2\2\u061e\u061c\3\2\2\2\u061f\u0620\7r\2\2")
        buf.write("\u0620\u0621\7~\2\2\u0621\u0625\5 \21\2\u0622\u0624\7")
        buf.write("x\2\2\u0623\u0622\3\2\2\2\u0624\u0627\3\2\2\2\u0625\u0623")
        buf.write("\3\2\2\2\u0625\u0626\3\2\2\2\u0626\u0111\3\2\2\2\u0627")
        buf.write("\u0625\3\2\2\2\u0628\u0629\7s\2\2\u0629\u062a\7~\2\2\u062a")
        buf.write("\u062e\5 \21\2\u062b\u062d\7x\2\2\u062c\u062b\3\2\2\2")
        buf.write("\u062d\u0630\3\2\2\2\u062e\u062c\3\2\2\2\u062e\u062f\3")
        buf.write("\2\2\2\u062f\u0113\3\2\2\2\u0630\u062e\3\2\2\2\u0631\u0640")
        buf.write("\7\t\2\2\u0632\u063c\7\u0080\2\2\u0633\u063d\5\u0116\u008c")
        buf.write("\2\u0634\u0639\5\u0118\u008d\2\u0635\u0636\7\u0087\2\2")
        buf.write("\u0636\u0638\5\u0118\u008d\2\u0637\u0635\3\2\2\2\u0638")
        buf.write("\u063b\3\2\2\2\u0639\u0637\3\2\2\2\u0639\u063a\3\2\2\2")
        buf.write("\u063a\u063d\3\2\2\2\u063b\u0639\3\2\2\2\u063c\u0633\3")
        buf.write("\2\2\2\u063c\u0634\3\2\2\2\u063d\u063e\3\2\2\2\u063e\u063f")
        buf.write("\7\u0081\2\2\u063f\u0641\3\2\2\2\u0640\u0632\3\2\2\2\u0640")
        buf.write("\u0641\3\2\2\2\u0641\u0115\3\2\2\2\u0642\u0643\7\u008f")
        buf.write("\2\2\u0643\u0117\3\2\2\2\u0644\u0645\5\32\16\2\u0645\u0119")
        buf.write("\3\2\2\2\u0646\u0649\7\n\2\2\u0647\u0648\7\u0088\2\2\u0648")
        buf.write("\u064a\5\u0120\u0091\2\u0649\u0647\3\2\2\2\u0649\u064a")
        buf.write("\3\2\2\2\u064a\u064f\3\2\2\2\u064b\u064c\7\u0080\2\2\u064c")
        buf.write("\u064d\5\u011c\u008f\2\u064d\u064e\7\u0081\2\2\u064e\u0650")
        buf.write("\3\2\2\2\u064f\u064b\3\2\2\2\u064f\u0650\3\2\2\2\u0650")
        buf.write("\u011b\3\2\2\2\u0651\u0657\5\u011e\u0090\2\u0652\u0656")
        buf.write("\5\u0146\u00a4\2\u0653\u0656\7x\2\2\u0654\u0656\7\u0087")
        buf.write("\2\2\u0655\u0652\3\2\2\2\u0655\u0653\3\2\2\2\u0655\u0654")
        buf.write("\3\2\2\2\u0656\u0659\3\2\2\2\u0657\u0655\3\2\2\2\u0657")
        buf.write("\u0658\3\2\2\2\u0658\u011d\3\2\2\2\u0659\u0657\3\2\2\2")
        buf.write("\u065a\u0667\5\u0130\u0099\2\u065b\u0667\5\u0122\u0092")
        buf.write("\2\u065c\u0667\5\u0134\u009b\2\u065d\u0667\5\u0124\u0093")
        buf.write("\2\u065e\u0667\5\u0126\u0094\2\u065f\u0667\5\u0128\u0095")
        buf.write("\2\u0660\u0667\5\u012a\u0096\2\u0661\u0667\5\u012c\u0097")
        buf.write("\2\u0662\u0667\5\u012e\u0098\2\u0663\u0667\5\u013e\u00a0")
        buf.write("\2\u0664\u0667\7x\2\2\u0665\u0667\7\u0087\2\2\u0666\u065a")
        buf.write("\3\2\2\2\u0666\u065b\3\2\2\2\u0666\u065c\3\2\2\2\u0666")
        buf.write("\u065d\3\2\2\2\u0666\u065e\3\2\2\2\u0666\u065f\3\2\2\2")
        buf.write("\u0666\u0660\3\2\2\2\u0666\u0661\3\2\2\2\u0666\u0662\3")
        buf.write("\2\2\2\u0666\u0663\3\2\2\2\u0666\u0664\3\2\2\2\u0666\u0665")
        buf.write("\3\2\2\2\u0667\u066a\3\2\2\2\u0668\u0666\3\2\2\2\u0668")
        buf.write("\u0669\3\2\2\2\u0669\u011f\3\2\2\2\u066a\u0668\3\2\2\2")
        buf.write("\u066b\u066c\5\32\16\2\u066c\u0121\3\2\2\2\u066d\u066e")
        buf.write("\7k\2\2\u066e\u066f\7~\2\2\u066f\u0673\7w\2\2\u0670\u0672")
        buf.write("\7x\2\2\u0671\u0670\3\2\2\2\u0672\u0675\3\2\2\2\u0673")
        buf.write("\u0671\3\2\2\2\u0673\u0674\3\2\2\2\u0674\u0123\3\2\2\2")
        buf.write("\u0675\u0673\3\2\2\2\u0676\u0677\7h\2\2\u0677\u067b\5")
        buf.write("&\24\2\u0678\u067a\7x\2\2\u0679\u0678\3\2\2\2\u067a\u067d")
        buf.write("\3\2\2\2\u067b\u0679\3\2\2\2\u067b\u067c\3\2\2\2\u067c")
        buf.write("\u0125\3\2\2\2\u067d\u067b\3\2\2\2\u067e\u0680\7g\2\2")
        buf.write("\u067f\u0681\7~\2\2\u0680\u067f\3\2\2\2\u0680\u0681\3")
        buf.write("\2\2\2\u0681\u0682\3\2\2\2\u0682\u0686\5&\24\2\u0683\u0685")
        buf.write("\7x\2\2\u0684\u0683\3\2\2\2\u0685\u0688\3\2\2\2\u0686")
        buf.write("\u0684\3\2\2\2\u0686\u0687\3\2\2\2\u0687\u0127\3\2\2\2")
        buf.write("\u0688\u0686\3\2\2\2\u0689\u068b\7M\2\2\u068a\u068c\7")
        buf.write("~\2\2\u068b\u068a\3\2\2\2\u068b\u068c\3\2\2\2\u068c\u068d")
        buf.write("\3\2\2\2\u068d\u0691\5&\24\2\u068e\u0690\7x\2\2\u068f")
        buf.write("\u068e\3\2\2\2\u0690\u0693\3\2\2\2\u0691\u068f\3\2\2\2")
        buf.write("\u0691\u0692\3\2\2\2\u0692\u0129\3\2\2\2\u0693\u0691\3")
        buf.write("\2\2\2\u0694\u0696\7L\2\2\u0695\u0697\7~\2\2\u0696\u0695")
        buf.write("\3\2\2\2\u0696\u0697\3\2\2\2\u0697\u0698\3\2\2\2\u0698")
        buf.write("\u069c\5&\24\2\u0699\u069b\7x\2\2\u069a\u0699\3\2\2\2")
        buf.write("\u069b\u069e\3\2\2\2\u069c\u069a\3\2\2\2\u069c\u069d\3")
        buf.write("\2\2\2\u069d\u012b\3\2\2\2\u069e\u069c\3\2\2\2\u069f\u06a0")
        buf.write("\7o\2\2\u06a0\u06a1\7~\2\2\u06a1\u06a5\5 \21\2\u06a2\u06a4")
        buf.write("\7x\2\2\u06a3\u06a2\3\2\2\2\u06a4\u06a7\3\2\2\2\u06a5")
        buf.write("\u06a3\3\2\2\2\u06a5\u06a6\3\2\2\2\u06a6\u012d\3\2\2\2")
        buf.write("\u06a7\u06a5\3\2\2\2\u06a8\u06a9\7e\2\2\u06a9\u06aa\7")
        buf.write("~\2\2\u06aa\u06ae\5\32\16\2\u06ab\u06ad\7x\2\2\u06ac\u06ab")
        buf.write("\3\2\2\2\u06ad\u06b0\3\2\2\2\u06ae\u06ac\3\2\2\2\u06ae")
        buf.write("\u06af\3\2\2\2\u06af\u012f\3\2\2\2\u06b0\u06ae\3\2\2\2")
        buf.write("\u06b1\u06b2\7s\2\2\u06b2\u06b3\7~\2\2\u06b3\u06b5\5 ")
        buf.write("\21\2\u06b4\u06b6\5\u0132\u009a\2\u06b5\u06b4\3\2\2\2")
        buf.write("\u06b5\u06b6\3\2\2\2\u06b6\u06ba\3\2\2\2\u06b7\u06b9\7")
        buf.write("x\2\2\u06b8\u06b7\3\2\2\2\u06b9\u06bc\3\2\2\2\u06ba\u06b8")
        buf.write("\3\2\2\2\u06ba\u06bb\3\2\2\2\u06bb\u0131\3\2\2\2\u06bc")
        buf.write("\u06ba\3\2\2\2\u06bd\u06be\5$\23\2\u06be\u0133\3\2\2\2")
        buf.write("\u06bf\u06c0\7i\2\2\u06c0\u06c1\7\u0080\2\2\u06c1\u06c6")
        buf.write("\5\u0136\u009c\2\u06c2\u06c3\7\u0087\2\2\u06c3\u06c5\5")
        buf.write("\u0136\u009c\2\u06c4\u06c2\3\2\2\2\u06c5\u06c8\3\2\2\2")
        buf.write("\u06c6\u06c4\3\2\2\2\u06c6\u06c7\3\2\2\2\u06c7\u06c9\3")
        buf.write("\2\2\2\u06c8\u06c6\3\2\2\2\u06c9\u06ca\7\u0081\2\2\u06ca")
        buf.write("\u0135\3\2\2\2\u06cb\u06cf\5\u0138\u009d\2\u06cc\u06cd")
        buf.write("\7~\2\2\u06cd\u06d0\5\u013a\u009e\2\u06ce\u06d0\5\u013c")
        buf.write("\u009f\2\u06cf\u06cc\3\2\2\2\u06cf\u06ce\3\2\2\2\u06cf")
        buf.write("\u06d0\3\2\2\2\u06d0\u0137\3\2\2\2\u06d1\u06d2\t\r\2\2")
        buf.write("\u06d2\u0139\3\2\2\2\u06d3\u06d4\5\36\20\2\u06d4\u013b")
        buf.write("\3\2\2\2\u06d5\u06d6\5\34\17\2\u06d6\u013d\3\2\2\2\u06d7")
        buf.write("\u06d8\7f\2\2\u06d8\u06d9\7~\2\2\u06d9\u06dd\5\u0140\u00a1")
        buf.write("\2\u06da\u06dc\7x\2\2\u06db\u06da\3\2\2\2\u06dc\u06df")
        buf.write("\3\2\2\2\u06dd\u06db\3\2\2\2\u06dd\u06de\3\2\2\2\u06de")
        buf.write("\u013f\3\2\2\2\u06df\u06dd\3\2\2\2\u06e0\u06e1\7j\2\2")
        buf.write("\u06e1\u06e4\5\u0142\u00a2\2\u06e2\u06e3\7u\2\2\u06e3")
        buf.write("\u06e5\5\u0144\u00a3\2\u06e4\u06e2\3\2\2\2\u06e4\u06e5")
        buf.write("\3\2\2\2\u06e5\u0141\3\2\2\2\u06e6\u06e7\5\32\16\2\u06e7")
        buf.write("\u0143\3\2\2\2\u06e8\u06e9\5\32\16\2\u06e9\u0145\3\2\2")
        buf.write("\2\u06ea\u06eb\7c\2\2\u06eb\u06ef\7~\2\2\u06ec\u06f0\5")
        buf.write("\u0148\u00a5\2\u06ed\u06f0\7\u0087\2\2\u06ee\u06f0\7x")
        buf.write("\2\2\u06ef\u06ec\3\2\2\2\u06ef\u06ed\3\2\2\2\u06ef\u06ee")
        buf.write("\3\2\2\2\u06f0\u06f1\3\2\2\2\u06f1\u06ef\3\2\2\2\u06f1")
        buf.write("\u06f2\3\2\2\2\u06f2\u0147\3\2\2\2\u06f3\u06f4\5\u014a")
        buf.write("\u00a6\2\u06f4\u06f5\7\u0080\2\2\u06f5\u06f6\5\u011c\u008f")
        buf.write("\2\u06f6\u06f7\7\u0081\2\2\u06f7\u0149\3\2\2\2\u06f8\u06f9")
        buf.write("\5\32\16\2\u06f9\u014b\3\2\2\2\u06fa\u06fb\7)\2\2\u06fb")
        buf.write("\u06fc\7\u0080\2\2\u06fc\u06fd\5\u014e\u00a8\2\u06fd\u06fe")
        buf.write("\7\u0081\2\2\u06fe\u014d\3\2\2\2\u06ff\u0704\5\32\16\2")
        buf.write("\u0700\u0701\7\u0087\2\2\u0701\u0703\5\32\16\2\u0702\u0700")
        buf.write("\3\2\2\2\u0703\u0706\3\2\2\2\u0704\u0702\3\2\2\2\u0704")
        buf.write("\u0705\3\2\2\2\u0705\u014f\3\2\2\2\u0706\u0704\3\2\2\2")
        buf.write("\u0707\u0708\7(\2\2\u0708\u0709\5&\24\2\u0709\u0151\3")
        buf.write("\2\2\2\u070a\u070b\7%\2\2\u070b\u070c\5&\24\2\u070c\u0153")
        buf.write("\3\2\2\2\u070d\u0712\7 \2\2\u070e\u070f\7\u0080\2\2\u070f")
        buf.write("\u0710\5\u0156\u00ac\2\u0710\u0711\7\u0081\2\2\u0711\u0713")
        buf.write("\3\2\2\2\u0712\u070e\3\2\2\2\u0712\u0713\3\2\2\2\u0713")
        buf.write("\u0155\3\2\2\2\u0714\u0715\7]\2\2\u0715\u0157\3\2\2\2")
        buf.write("\u0716\u0717\7\"\2\2\u0717\u0718\7\u0080\2\2\u0718\u0719")
        buf.write("\5\34\17\2\u0719\u071a\7\u0081\2\2\u071a\u0159\3\2\2\2")
        buf.write("\u071b\u071c\7!\2\2\u071c\u071d\7\u0080\2\2\u071d\u071e")
        buf.write("\5\u015c\u00af\2\u071e\u071f\7\u0081\2\2\u071f\u015b\3")
        buf.write("\2\2\2\u0720\u0721\5\32\16\2\u0721\u015d\3\2\2\2\u0722")
        buf.write("\u0723\7#\2\2\u0723\u0724\5&\24\2\u0724\u015f\3\2\2\2")
        buf.write("\u0725\u0726\7&\2\2\u0726\u0727\5&\24\2\u0727\u0161\3")
        buf.write("\2\2\2\u0728\u0729\7\'\2\2\u0729\u072a\5&\24\2\u072a\u0163")
        buf.write("\3\2\2\2\u072b\u072c\7$\2\2\u072c\u072d\5&\24\2\u072d")
        buf.write("\u0165\3\2\2\2\u072e\u072f\7*\2\2\u072f\u0730\7\u0080")
        buf.write("\2\2\u0730\u0731\5\u0168\u00b5\2\u0731\u0732\7\u0081\2")
        buf.write("\2\u0732\u0167\3\2\2\2\u0733\u0734\5\32\16\2\u0734\u0169")
        buf.write("\3\2\2\2\u0735\u0739\5\u016c\u00b7\2\u0736\u0738\7x\2")
        buf.write("\2\u0737\u0736\3\2\2\2\u0738\u073b\3\2\2\2\u0739\u0737")
        buf.write("\3\2\2\2\u0739\u073a\3\2\2\2\u073a\u073c\3\2\2\2\u073b")
        buf.write("\u0739\3\2\2\2\u073c\u0740\5\u0186\u00c4\2\u073d\u073f")
        buf.write("\7x\2\2\u073e\u073d\3\2\2\2\u073f\u0742\3\2\2\2\u0740")
        buf.write("\u073e\3\2\2\2\u0740\u0741\3\2\2\2\u0741\u016b\3\2\2\2")
        buf.write("\u0742\u0740\3\2\2\2\u0743\u0745\7\u0082\2\2\u0744\u0746")
        buf.write("\5\u016e\u00b8\2\u0745\u0744\3\2\2\2\u0745\u0746\3\2\2")
        buf.write("\2\u0746\u0747\3\2\2\2\u0747\u0749\5\u0184\u00c3\2\u0748")
        buf.write("\u074a\5\u0170\u00b9\2\u0749\u0748\3\2\2\2\u0749\u074a")
        buf.write("\3\2\2\2\u074a\u0753\3\2\2\2\u074b\u074d\7~\2\2\u074c")
        buf.write("\u074e\5\u017a\u00be\2\u074d\u074c\3\2\2\2\u074d\u074e")
        buf.write("\3\2\2\2\u074e\u0751\3\2\2\2\u074f\u0750\7~\2\2\u0750")
        buf.write("\u0752\5\u0174\u00bb\2\u0751\u074f\3\2\2\2\u0751\u0752")
        buf.write("\3\2\2\2\u0752\u0754\3\2\2\2\u0753\u074b\3\2\2\2\u0753")
        buf.write("\u0754\3\2\2\2\u0754\u0755\3\2\2\2\u0755\u0757\7\u0083")
        buf.write("\2\2\u0756\u0758\7x\2\2\u0757\u0756\3\2\2\2\u0757\u0758")
        buf.write("\3\2\2\2\u0758\u016d\3\2\2\2\u0759\u075a\5\32\16\2\u075a")
        buf.write("\u075b\7\u0088\2\2\u075b\u075d\3\2\2\2\u075c\u0759\3\2")
        buf.write("\2\2\u075c\u075d\3\2\2\2\u075d\u075e\3\2\2\2\u075e\u075f")
        buf.write("\5\32\16\2\u075f\u0760\t\16\2\2\u0760\u0761\7}\2\2\u0761")
        buf.write("\u016f\3\2\2\2\u0762\u0763\7u\2\2\u0763\u0764\5\u0172")
        buf.write("\u00ba\2\u0764\u0171\3\2\2\2\u0765\u0766\5\32\16\2\u0766")
        buf.write("\u0173\3\2\2\2\u0767\u076a\5\u0176\u00bc\2\u0768\u076a")
        buf.write("\5&\24\2\u0769\u0767\3\2\2\2\u0769\u0768\3\2\2\2\u076a")
        buf.write("\u0175\3\2\2\2\u076b\u0770\5\u0178\u00bd\2\u076c\u076d")
        buf.write("\7\u008a\2\2\u076d\u076f\5\u0178\u00bd\2\u076e\u076c\3")
        buf.write("\2\2\2\u076f\u0772\3\2\2\2\u0770\u076e\3\2\2\2\u0770\u0771")
        buf.write("\3\2\2\2\u0771\u0177\3\2\2\2\u0772\u0770\3\2\2\2\u0773")
        buf.write("\u0779\5\32\16\2\u0774\u0779\7z\2\2\u0775\u0779\7\u0086")
        buf.write("\2\2\u0776\u0779\7\u0085\2\2\u0777\u0779\7\u0088\2\2\u0778")
        buf.write("\u0773\3\2\2\2\u0778\u0774\3\2\2\2\u0778\u0775\3\2\2\2")
        buf.write("\u0778\u0776\3\2\2\2\u0778\u0777\3\2\2\2\u0779\u077a\3")
        buf.write("\2\2\2\u077a\u0778\3\2\2\2\u077a\u077b\3\2\2\2\u077b\u0179")
        buf.write("\3\2\2\2\u077c\u077e\t\17\2\2\u077d\u077c\3\2\2\2\u077d")
        buf.write("\u077e\3\2\2\2\u077e\u077f\3\2\2\2\u077f\u0780\5\u0182")
        buf.write("\u00c2\2\u0780\u017b\3\2\2\2\u0781\u0785\5\32\16\2\u0782")
        buf.write("\u0785\7\u0086\2\2\u0783\u0785\7z\2\2\u0784\u0781\3\2")
        buf.write("\2\2\u0784\u0782\3\2\2\2\u0784\u0783\3\2\2\2\u0785\u0786")
        buf.write("\3\2\2\2\u0786\u0784\3\2\2\2\u0786\u0787\3\2\2\2\u0787")
        buf.write("\u017d\3\2\2\2\u0788\u0789\7|\2\2\u0789\u078a\5\32\16")
        buf.write("\2\u078a\u078b\7}\2\2\u078b\u017f\3\2\2\2\u078c\u078f")
        buf.write("\5\u017c\u00bf\2\u078d\u078f\5\u017e\u00c0\2\u078e\u078c")
        buf.write("\3\2\2\2\u078e\u078d\3\2\2\2\u078f\u0181\3\2\2\2\u0790")
        buf.write("\u079b\7\u008a\2\2\u0791\u0792\7\u008a\2\2\u0792\u0794")
        buf.write("\5\u0180\u00c1\2\u0793\u0791\3\2\2\2\u0794\u0795\3\2\2")
        buf.write("\2\u0795\u0793\3\2\2\2\u0795\u0796\3\2\2\2\u0796\u0798")
        buf.write("\3\2\2\2\u0797\u0799\7\u008a\2\2\u0798\u0797\3\2\2\2\u0798")
        buf.write("\u0799\3\2\2\2\u0799\u079b\3\2\2\2\u079a\u0790\3\2\2\2")
        buf.write("\u079a\u0793\3\2\2\2\u079b\u0183\3\2\2\2\u079c\u079d\5")
        buf.write("\32\16\2\u079d\u0185\3\2\2\2\u079e\u07a0\5\u018a\u00c6")
        buf.write("\2\u079f\u079e\3\2\2\2\u07a0\u07a3\3\2\2\2\u07a1\u079f")
        buf.write("\3\2\2\2\u07a1\u07a2\3\2\2\2\u07a2\u07a7\3\2\2\2\u07a3")
        buf.write("\u07a1\3\2\2\2\u07a4\u07a6\5\u0190\u00c9\2\u07a5\u07a4")
        buf.write("\3\2\2\2\u07a6\u07a9\3\2\2\2\u07a7\u07a5\3\2\2\2\u07a7")
        buf.write("\u07a8\3\2\2\2\u07a8\u07ab\3\2\2\2\u07a9\u07a7\3\2\2\2")
        buf.write("\u07aa\u07ac\5\u0188\u00c5\2\u07ab\u07aa\3\2\2\2\u07ab")
        buf.write("\u07ac\3\2\2\2\u07ac\u07b0\3\2\2\2\u07ad\u07af\7x\2\2")
        buf.write("\u07ae\u07ad\3\2\2\2\u07af\u07b2\3\2\2\2\u07b0\u07ae\3")
        buf.write("\2\2\2\u07b0\u07b1\3\2\2\2\u07b1\u07b6\3\2\2\2\u07b2\u07b0")
        buf.write("\3\2\2\2\u07b3\u07b5\5\u0198\u00cd\2\u07b4\u07b3\3\2\2")
        buf.write("\2\u07b5\u07b8\3\2\2\2\u07b6\u07b4\3\2\2\2\u07b6\u07b7")
        buf.write("\3\2\2\2\u07b7\u0187\3\2\2\2\u07b8\u07b6\3\2\2\2\u07b9")
        buf.write("\u07ba\5&\24\2\u07ba\u0189\3\2\2\2\u07bb\u07bc\5\u018c")
        buf.write("\u00c7\2\u07bc\u07bd\7\u0099\2\2\u07bd\u07c4\5\u018e\u00c8")
        buf.write("\2\u07be\u07c0\7x\2\2\u07bf\u07be\3\2\2\2\u07c0\u07c1")
        buf.write("\3\2\2\2\u07c1\u07bf\3\2\2\2\u07c1\u07c2\3\2\2\2\u07c2")
        buf.write("\u07c5\3\2\2\2\u07c3\u07c5\7\2\2\3\u07c4\u07bf\3\2\2\2")
        buf.write("\u07c4\u07c3\3\2\2\2\u07c5\u018b\3\2\2\2\u07c6\u07c7\5")
        buf.write("\32\16\2\u07c7\u018d\3\2\2\2\u07c8\u07c9\7\u009d\2\2\u07c9")
        buf.write("\u018f\3\2\2\2\u07ca\u07cb\5\u0192\u00ca\2\u07cb\u07cd")
        buf.write("\7\u0080\2\2\u07cc\u07ce\5\u0194\u00cb\2\u07cd\u07cc\3")
        buf.write("\2\2\2\u07cd\u07ce\3\2\2\2\u07ce\u07cf\3\2\2\2\u07cf\u07d1")
        buf.write("\7\u0081\2\2\u07d0\u07d2\5*\26\2\u07d1\u07d0\3\2\2\2\u07d1")
        buf.write("\u07d2\3\2\2\2\u07d2\u07d9\3\2\2\2\u07d3\u07d5\7x\2\2")
        buf.write("\u07d4\u07d3\3\2\2\2\u07d5\u07d6\3\2\2\2\u07d6\u07d4\3")
        buf.write("\2\2\2\u07d6\u07d7\3\2\2\2\u07d7\u07da\3\2\2\2\u07d8\u07da")
        buf.write("\7\2\2\3\u07d9\u07d4\3\2\2\2\u07d9\u07d8\3\2\2\2\u07da")
        buf.write("\u0191\3\2\2\2\u07db\u07dc\5\32\16\2\u07dc\u0193\3\2\2")
        buf.write("\2\u07dd\u07e2\5\u0196\u00cc\2\u07de\u07df\7\u0087\2\2")
        buf.write("\u07df\u07e1\5\u0196\u00cc\2\u07e0\u07de\3\2\2\2\u07e1")
        buf.write("\u07e4\3\2\2\2\u07e2\u07e0\3\2\2\2\u07e2\u07e3\3\2\2\2")
        buf.write("\u07e3\u0195\3\2\2\2\u07e4\u07e2\3\2\2\2\u07e5\u07e7\7")
        buf.write("\u0088\2\2\u07e6\u07e5\3\2\2\2\u07e6\u07e7\3\2\2\2\u07e7")
        buf.write("\u07e8\3\2\2\2\u07e8\u07e9\5\32\16\2\u07e9\u0197\3\2\2")
        buf.write("\2\u07ea\u07fc\5\u019a\u00ce\2\u07eb\u07fc\5\u01a6\u00d4")
        buf.write("\2\u07ec\u07fc\5\u01ac\u00d7\2\u07ed\u07fc\5\u01b0\u00d9")
        buf.write("\2\u07ee\u07fc\5\u01b4\u00db\2\u07ef\u07fc\5\u01fe\u0100")
        buf.write("\2\u07f0\u07fc\5\u0200\u0101\2\u07f1\u07fc\5\u0202\u0102")
        buf.write("\2\u07f2\u07fc\5\u0204\u0103\2\u07f3\u07fc\5\u01b6\u00dc")
        buf.write("\2\u07f4\u07fc\5\u0206\u0104\2\u07f5\u07fc\5\u0208\u0105")
        buf.write("\2\u07f6\u07fc\5\u0222\u0112\2\u07f7\u07fc\5\u0224\u0113")
        buf.write("\2\u07f8\u07fc\5\u0226\u0114\2\u07f9\u07fc\5\u0228\u0115")
        buf.write("\2\u07fa\u07fc\7x\2\2\u07fb\u07ea\3\2\2\2\u07fb\u07eb")
        buf.write("\3\2\2\2\u07fb\u07ec\3\2\2\2\u07fb\u07ed\3\2\2\2\u07fb")
        buf.write("\u07ee\3\2\2\2\u07fb\u07ef\3\2\2\2\u07fb\u07f0\3\2\2\2")
        buf.write("\u07fb\u07f1\3\2\2\2\u07fb\u07f2\3\2\2\2\u07fb\u07f3\3")
        buf.write("\2\2\2\u07fb\u07f4\3\2\2\2\u07fb\u07f5\3\2\2\2\u07fb\u07f6")
        buf.write("\3\2\2\2\u07fb\u07f7\3\2\2\2\u07fb\u07f8\3\2\2\2\u07fb")
        buf.write("\u07f9\3\2\2\2\u07fb\u07fa\3\2\2\2\u07fc\u0199\3\2\2\2")
        buf.write("\u07fd\u07fe\7\6\2\2\u07fe\u0801\7\u0080\2\2\u07ff\u0802")
        buf.write("\5\u019c\u00cf\2\u0800\u0802\7x\2\2\u0801\u07ff\3\2\2")
        buf.write("\2\u0801\u0800\3\2\2\2\u0802\u0803\3\2\2\2\u0803\u0801")
        buf.write("\3\2\2\2\u0803\u0804\3\2\2\2\u0804\u0805\3\2\2\2\u0805")
        buf.write("\u0806\7\u0081\2\2\u0806\u019b\3\2\2\2\u0807\u0809\5\u019e")
        buf.write("\u00d0\2\u0808\u080a\5\u01a0\u00d1\2\u0809\u0808\3\2\2")
        buf.write("\2\u0809\u080a\3\2\2\2\u080a\u080c\3\2\2\2\u080b\u080d")
        buf.write("\5\u01a2\u00d2\2\u080c\u080b\3\2\2\2\u080c\u080d\3\2\2")
        buf.write("\2\u080d\u080f\3\2\2\2\u080e\u0810\7\u0087\2\2\u080f\u080e")
        buf.write("\3\2\2\2\u080f\u0810\3\2\2\2\u0810\u0812\3\2\2\2\u0811")
        buf.write("\u0813\7x\2\2\u0812\u0811\3\2\2\2\u0812\u0813\3\2\2\2")
        buf.write("\u0813\u019d\3\2\2\2\u0814\u0817\5\36\20\2\u0815\u0817")
        buf.write("\5\34\17\2\u0816\u0814\3\2\2\2\u0816\u0815\3\2\2\2\u0817")
        buf.write("\u019f\3\2\2\2\u0818\u0819\5*\26\2\u0819\u01a1\3\2\2\2")
        buf.write("\u081a\u081b\7\u008b\2\2\u081b\u0825\7}\2\2\u081c\u0826")
        buf.write("\7\u008f\2\2\u081d\u0822\5\u01a4\u00d3\2\u081e\u081f\7")
        buf.write("\u0087\2\2\u081f\u0821\5\u01a4\u00d3\2\u0820\u081e\3\2")
        buf.write("\2\2\u0821\u0824\3\2\2\2\u0822\u0820\3\2\2\2\u0822\u0823")
        buf.write("\3\2\2\2\u0823\u0826\3\2\2\2\u0824\u0822\3\2\2\2\u0825")
        buf.write("\u081c\3\2\2\2\u0825\u081d\3\2\2\2\u0826\u01a3\3\2\2\2")
        buf.write("\u0827\u0828\5\32\16\2\u0828\u01a5\3\2\2\2\u0829\u082c")
        buf.write("\5\u01a8\u00d5\2\u082a\u082b\7\u0088\2\2\u082b\u082d\5")
        buf.write("\u01aa\u00d6\2\u082c\u082a\3\2\2\2\u082c\u082d\3\2\2\2")
        buf.write("\u082d\u01a7\3\2\2\2\u082e\u082f\t\20\2\2\u082f\u01a9")
        buf.write("\3\2\2\2\u0830\u0831\5\32\16\2\u0831\u01ab\3\2\2\2\u0832")
        buf.write("\u0835\7\37\2\2\u0833\u0834\7\u0088\2\2\u0834\u0836\5")
        buf.write("\u01ae\u00d8\2\u0835\u0833\3\2\2\2\u0835\u0836\3\2\2\2")
        buf.write("\u0836\u0837\3\2\2\2\u0837\u0838\5*\26\2\u0838\u01ad\3")
        buf.write("\2\2\2\u0839\u083a\5\32\16\2\u083a\u01af\3\2\2\2\u083b")
        buf.write("\u083e\7\36\2\2\u083c\u083d\7\u0088\2\2\u083d\u083f\5")
        buf.write("\u01b2\u00da\2\u083e\u083c\3\2\2\2\u083e\u083f\3\2\2\2")
        buf.write("\u083f\u0840\3\2\2\2\u0840\u0841\5*\26\2\u0841\u01b1\3")
        buf.write("\2\2\2\u0842\u0843\5\32\16\2\u0843\u01b3\3\2\2\2\u0844")
        buf.write("\u0845\7\30\2\2\u0845\u0846\5\u01b8\u00dd\2\u0846\u01b5")
        buf.write("\3\2\2\2\u0847\u0848\7\25\2\2\u0848\u0849\5\u01b8\u00dd")
        buf.write("\2\u0849\u01b7\3\2\2\2\u084a\u084b\7\u0088\2\2\u084b\u084d")
        buf.write("\5\u01bc\u00df\2\u084c\u084a\3\2\2\2\u084c\u084d\3\2\2")
        buf.write("\2\u084d\u084e\3\2\2\2\u084e\u0852\7\u0080\2\2\u084f\u0851")
        buf.write("\7x\2\2\u0850\u084f\3\2\2\2\u0851\u0854\3\2\2\2\u0852")
        buf.write("\u0850\3\2\2\2\u0852\u0853\3\2\2\2\u0853\u0855\3\2\2\2")
        buf.write("\u0854\u0852\3\2\2\2\u0855\u0857\5\u01c6\u00e4\2\u0856")
        buf.write("\u0858\5\u01c8\u00e5\2\u0857\u0856\3\2\2\2\u0857\u0858")
        buf.write("\3\2\2\2\u0858\u086a\3\2\2\2\u0859\u0869\5\u01ca\u00e6")
        buf.write("\2\u085a\u0869\5\u01de\u00f0\2\u085b\u0869\5\u01e4\u00f3")
        buf.write("\2\u085c\u0869\5\u01f6\u00fc\2\u085d\u0869\5\u01dc\u00ef")
        buf.write("\2\u085e\u0869\5\u01d4\u00eb\2\u085f\u0869\5\u01da\u00ee")
        buf.write("\2\u0860\u0869\5\u01d6\u00ec\2\u0861\u0869\5\u01d8\u00ed")
        buf.write("\2\u0862\u0869\5\u01cc\u00e7\2\u0863\u0869\5\u01d0\u00e9")
        buf.write("\2\u0864\u0869\5\u01e6\u00f4\2\u0865\u0869\5\u01ea\u00f6")
        buf.write("\2\u0866\u0869\7x\2\2\u0867\u0869\7\u0087\2\2\u0868\u0859")
        buf.write("\3\2\2\2\u0868\u085a\3\2\2\2\u0868\u085b\3\2\2\2\u0868")
        buf.write("\u085c\3\2\2\2\u0868\u085d\3\2\2\2\u0868\u085e\3\2\2\2")
        buf.write("\u0868\u085f\3\2\2\2\u0868\u0860\3\2\2\2\u0868\u0861\3")
        buf.write("\2\2\2\u0868\u0862\3\2\2\2\u0868\u0863\3\2\2\2\u0868\u0864")
        buf.write("\3\2\2\2\u0868\u0865\3\2\2\2\u0868\u0866\3\2\2\2\u0868")
        buf.write("\u0867\3\2\2\2\u0869\u086c\3\2\2\2\u086a\u0868\3\2\2\2")
        buf.write("\u086a\u086b\3\2\2\2\u086b\u0870\3\2\2\2\u086c\u086a\3")
        buf.write("\2\2\2\u086d\u086f\7x\2\2\u086e\u086d\3\2\2\2\u086f\u0872")
        buf.write("\3\2\2\2\u0870\u086e\3\2\2\2\u0870\u0871\3\2\2\2\u0871")
        buf.write("\u0875\3\2\2\2\u0872\u0870\3\2\2\2\u0873\u0876\5\u01be")
        buf.write("\u00e0\2\u0874\u0876\5\u01c2\u00e2\2\u0875\u0873\3\2\2")
        buf.write("\2\u0875\u0874\3\2\2\2\u0875\u0876\3\2\2\2\u0876\u087a")
        buf.write("\3\2\2\2\u0877\u0879\7x\2\2\u0878\u0877\3\2\2\2\u0879")
        buf.write("\u087c\3\2\2\2\u087a\u0878\3\2\2\2\u087a\u087b\3\2\2\2")
        buf.write("\u087b\u0880\3\2\2\2\u087c\u087a\3\2\2\2\u087d\u087f\5")
        buf.write("\u01ba\u00de\2\u087e\u087d\3\2\2\2\u087f\u0882\3\2\2\2")
        buf.write("\u0880\u087e\3\2\2\2\u0880\u0881\3\2\2\2\u0881\u0886\3")
        buf.write("\2\2\2\u0882\u0880\3\2\2\2\u0883\u0885\7x\2\2\u0884\u0883")
        buf.write("\3\2\2\2\u0885\u0888\3\2\2\2\u0886\u0884\3\2\2\2\u0886")
        buf.write("\u0887\3\2\2\2\u0887\u0889\3\2\2\2\u0888\u0886\3\2\2\2")
        buf.write("\u0889\u088a\7\u0081\2\2\u088a\u01b9\3\2\2\2\u088b\u088f")
        buf.write("\5\u01e2\u00f2\2\u088c\u088e\7x\2\2\u088d\u088c\3\2\2")
        buf.write("\2\u088e\u0891\3\2\2\2\u088f\u088d\3\2\2\2\u088f\u0890")
        buf.write("\3\2\2\2\u0890\u0892\3\2\2\2\u0891\u088f\3\2\2\2\u0892")
        buf.write("\u0896\7\u0080\2\2\u0893\u0895\7x\2\2\u0894\u0893\3\2")
        buf.write("\2\2\u0895\u0898\3\2\2\2\u0896\u0894\3\2\2\2\u0896\u0897")
        buf.write("\3\2\2\2\u0897\u0899\3\2\2\2\u0898\u0896\3\2\2\2\u0899")
        buf.write("\u089d\5\u0186\u00c4\2\u089a\u089c\7x\2\2\u089b\u089a")
        buf.write("\3\2\2\2\u089c\u089f\3\2\2\2\u089d\u089b\3\2\2\2\u089d")
        buf.write("\u089e\3\2\2\2\u089e\u08a0\3\2\2\2\u089f\u089d\3\2\2\2")
        buf.write("\u08a0\u08a4\7\u0081\2\2\u08a1\u08a3\7x\2\2\u08a2\u08a1")
        buf.write("\3\2\2\2\u08a3\u08a6\3\2\2\2\u08a4\u08a2\3\2\2\2\u08a4")
        buf.write("\u08a5\3\2\2\2\u08a5\u01bb\3\2\2\2\u08a6\u08a4\3\2\2\2")
        buf.write("\u08a7\u08a8\5\32\16\2\u08a8\u01bd\3\2\2\2\u08a9\u08aa")
        buf.write("\7\u0080\2\2\u08aa\u08ab\5\u01c0\u00e1\2\u08ab\u08ac\7")
        buf.write("\u0081\2\2\u08ac\u08ae\3\2\2\2\u08ad\u08a9\3\2\2\2\u08ad")
        buf.write("\u08ae\3\2\2\2\u08ae\u08af\3\2\2\2\u08af\u08b0\7\u008b")
        buf.write("\2\2\u08b0\u08b1\7}\2\2\u08b1\u08b2\5*\26\2\u08b2\u01bf")
        buf.write("\3\2\2\2\u08b3\u08b4\t\21\2\2\u08b4\u01c1\3\2\2\2\u08b5")
        buf.write("\u08b6\7\u0080\2\2\u08b6\u08b7\5\u01c0\u00e1\2\u08b7\u08b8")
        buf.write("\7\u0081\2\2\u08b8\u08ba\3\2\2\2\u08b9\u08b5\3\2\2\2\u08b9")
        buf.write("\u08ba\3\2\2\2\u08ba\u08bb\3\2\2\2\u08bb\u08bc\7\u008b")
        buf.write("\2\2\u08bc\u08bd\7}\2\2\u08bd\u08be\5\u01c4\u00e3\2\u08be")
        buf.write("\u01c3\3\2\2\2\u08bf\u08c0\t\3\2\2\u08c0\u01c5\3\2\2\2")
        buf.write("\u08c1\u08c4\5\36\20\2\u08c2\u08c4\5\34\17\2\u08c3\u08c1")
        buf.write("\3\2\2\2\u08c3\u08c2\3\2\2\2\u08c4\u01c7\3\2\2\2\u08c5")
        buf.write("\u08c6\5*\26\2\u08c6\u01c9\3\2\2\2\u08c7\u08c8\7F\2\2")
        buf.write("\u08c8\u08c9\7~\2\2\u08c9\u08ca\5\32\16\2\u08ca\u01cb")
        buf.write("\3\2\2\2\u08cb\u08cc\7P\2\2\u08cc\u08cd\7~\2\2\u08cd\u08ce")
        buf.write("\5\u01ce\u00e8\2\u08ce\u01cd\3\2\2\2\u08cf\u08d0\t\3\2")
        buf.write("\2\u08d0\u01cf\3\2\2\2\u08d1\u08d2\7O\2\2\u08d2\u08d3")
        buf.write("\7~\2\2\u08d3\u08d4\5\u01d2\u00ea\2\u08d4\u01d1\3\2\2")
        buf.write("\2\u08d5\u08d6\t\3\2\2\u08d6\u01d3\3\2\2\2\u08d7\u08d8")
        buf.write("\7T\2\2\u08d8\u08d9\7~\2\2\u08d9\u08da\5\32\16\2\u08da")
        buf.write("\u01d5\3\2\2\2\u08db\u08df\7R\2\2\u08dc\u08e0\5(\25\2")
        buf.write("\u08dd\u08de\7~\2\2\u08de\u08e0\5*\26\2\u08df\u08dc\3")
        buf.write("\2\2\2\u08df\u08dd\3\2\2\2\u08e0\u01d7\3\2\2\2\u08e1\u08e5")
        buf.write("\7Q\2\2\u08e2\u08e6\5(\25\2\u08e3\u08e4\7~\2\2\u08e4\u08e6")
        buf.write("\5*\26\2\u08e5\u08e2\3\2\2\2\u08e5\u08e3\3\2\2\2\u08e6")
        buf.write("\u01d9\3\2\2\2\u08e7\u08e8\7S\2\2\u08e8\u08e9\7~\2\2\u08e9")
        buf.write("\u08ea\5\32\16\2\u08ea\u01db\3\2\2\2\u08eb\u08ec\7U\2")
        buf.write("\2\u08ec\u08ed\7~\2\2\u08ed\u08ee\5\32\16\2\u08ee\u01dd")
        buf.write("\3\2\2\2\u08ef\u08f0\7[\2\2\u08f0\u08f1\7~\2\2\u08f1\u08f2")
        buf.write("\5\u01e0\u00f1\2\u08f2\u01df\3\2\2\2\u08f3\u08f8\5\u01e2")
        buf.write("\u00f2\2\u08f4\u08f5\7\u0087\2\2\u08f5\u08f7\5\u01e2\u00f2")
        buf.write("\2\u08f6\u08f4\3\2\2\2\u08f7\u08fa\3\2\2\2\u08f8\u08f6")
        buf.write("\3\2\2\2\u08f8\u08f9\3\2\2\2\u08f9\u01e1\3\2\2\2\u08fa")
        buf.write("\u08f8\3\2\2\2\u08fb\u08fc\t\22\2\2\u08fc\u01e3\3\2\2")
        buf.write("\2\u08fd\u08fe\7s\2\2\u08fe\u08ff\7~\2\2\u08ff\u0900\5")
        buf.write("\u01ee\u00f8\2\u0900\u01e5\3\2\2\2\u0901\u0902\7n\2\2")
        buf.write("\u0902\u0903\7~\2\2\u0903\u0904\5\u01e8\u00f5\2\u0904")
        buf.write("\u01e7\3\2\2\2\u0905\u0906\t\f\2\2\u0906\u01e9\3\2\2\2")
        buf.write("\u0907\u0908\7H\2\2\u0908\u0909\7~\2\2\u0909\u090a\5\u01ec")
        buf.write("\u00f7\2\u090a\u01eb\3\2\2\2\u090b\u090c\7w\2\2\u090c")
        buf.write("\u01ed\3\2\2\2\u090d\u0912\5\u01f0\u00f9\2\u090e\u090f")
        buf.write("\7\u0087\2\2\u090f\u0911\5\u01f0\u00f9\2\u0910\u090e\3")
        buf.write("\2\2\2\u0911\u0914\3\2\2\2\u0912\u0910\3\2\2\2\u0912\u0913")
        buf.write("\3\2\2\2\u0913\u01ef\3\2\2\2\u0914\u0912\3\2\2\2\u0915")
        buf.write("\u0917\5\u01f2\u00fa\2\u0916\u0918\5\u01f4\u00fb\2\u0917")
        buf.write("\u0916\3\2\2\2\u0917\u0918\3\2\2\2\u0918\u01f1\3\2\2\2")
        buf.write("\u0919\u091f\7\u008f\2\2\u091a\u091c\7\177\2\2\u091b\u091a")
        buf.write("\3\2\2\2\u091b\u091c\3\2\2\2\u091c\u091d\3\2\2\2\u091d")
        buf.write("\u091f\5\32\16\2\u091e\u0919\3\2\2\2\u091e\u091b\3\2\2")
        buf.write("\2\u091f\u01f3\3\2\2\2\u0920\u0921\5*\26\2\u0921\u01f5")
        buf.write("\3\2\2\2\u0922\u0923\7V\2\2\u0923\u0924\7~\2\2\u0924\u0925")
        buf.write("\5\u01f8\u00fd\2\u0925\u01f7\3\2\2\2\u0926\u092b\5\u01fa")
        buf.write("\u00fe\2\u0927\u0928\7\u0087\2\2\u0928\u092a\5\u01fa\u00fe")
        buf.write("\2\u0929\u0927\3\2\2\2\u092a\u092d\3\2\2\2\u092b\u0929")
        buf.write("\3\2\2\2\u092b\u092c\3\2\2\2\u092c\u01f9\3\2\2\2\u092d")
        buf.write("\u092b\3\2\2\2\u092e\u092f\5\u01fc\u00ff\2\u092f\u01fb")
        buf.write("\3\2\2\2\u0930\u0936\7\u008f\2\2\u0931\u0933\7\177\2\2")
        buf.write("\u0932\u0931\3\2\2\2\u0932\u0933\3\2\2\2\u0933\u0934\3")
        buf.write("\2\2\2\u0934\u0936\5\32\16\2\u0935\u0930\3\2\2\2\u0935")
        buf.write("\u0932\3\2\2\2\u0936\u01fd\3\2\2\2\u0937\u0939\7\33\2")
        buf.write("\2\u0938\u093a\5*\26\2\u0939\u0938\3\2\2\2\u0939\u093a")
        buf.write("\3\2\2\2\u093a\u01ff\3\2\2\2\u093b\u093d\7\35\2\2\u093c")
        buf.write("\u093e\5*\26\2\u093d\u093c\3\2\2\2\u093d\u093e\3\2\2\2")
        buf.write("\u093e\u0201\3\2\2\2\u093f\u0940\7\32\2\2\u0940\u0941")
        buf.write("\5\u01b8\u00dd\2\u0941\u0203\3\2\2\2\u0942\u0943\7\31")
        buf.write("\2\2\u0943\u0944\5\u01b8\u00dd\2\u0944\u0205\3\2\2\2\u0945")
        buf.write("\u0946\7\27\2\2\u0946\u0947\5\u01b8\u00dd\2\u0947\u0207")
        buf.write("\3\2\2\2\u0948\u0949\7\24\2\2\u0949\u094a\7\u0088\2\2")
        buf.write("\u094a\u094b\5\u020a\u0106\2\u094b\u094f\7\u0080\2\2\u094c")
        buf.write("\u094e\7x\2\2\u094d\u094c\3\2\2\2\u094e\u0951\3\2\2\2")
        buf.write("\u094f\u094d\3\2\2\2\u094f\u0950\3\2\2\2\u0950\u0953\3")
        buf.write("\2\2\2\u0951\u094f\3\2\2\2\u0952\u0954\5\u020c\u0107\2")
        buf.write("\u0953\u0952\3\2\2\2\u0954\u0955\3\2\2\2\u0955\u0953\3")
        buf.write("\2\2\2\u0955\u0956\3\2\2\2\u0956\u095a\3\2\2\2\u0957\u0959")
        buf.write("\7x\2\2\u0958\u0957\3\2\2\2\u0959\u095c\3\2\2\2\u095a")
        buf.write("\u0958\3\2\2\2\u095a\u095b\3\2\2\2\u095b\u095d\3\2\2\2")
        buf.write("\u095c\u095a\3\2\2\2\u095d\u095e\7\u0081\2\2\u095e\u0209")
        buf.write("\3\2\2\2\u095f\u0960\5\32\16\2\u0960\u020b\3\2\2\2\u0961")
        buf.write("\u0963\7\u0087\2\2\u0962\u0961\3\2\2\2\u0962\u0963\3\2")
        buf.write("\2\2\u0963\u0967\3\2\2\2\u0964\u0966\7x\2\2\u0965\u0964")
        buf.write("\3\2\2\2\u0966\u0969\3\2\2\2\u0967\u0965\3\2\2\2\u0967")
        buf.write("\u0968\3\2\2\2\u0968\u096b\3\2\2\2\u0969\u0967\3\2\2\2")
        buf.write("\u096a\u096c\5\u0212\u010a\2\u096b\u096a\3\2\2\2\u096b")
        buf.write("\u096c\3\2\2\2\u096c\u096d\3\2\2\2\u096d\u0970\5\u0220")
        buf.write("\u0111\2\u096e\u0971\5\u0210\u0109\2\u096f\u0971\5\u020e")
        buf.write("\u0108\2\u0970\u096e\3\2\2\2\u0970\u096f\3\2\2\2\u0971")
        buf.write("\u0975\3\2\2\2\u0972\u0974\7x\2\2\u0973\u0972\3\2\2\2")
        buf.write("\u0974\u0977\3\2\2\2\u0975\u0973\3\2\2\2\u0975\u0976\3")
        buf.write("\2\2\2\u0976\u020d\3\2\2\2\u0977\u0975\3\2\2\2\u0978\u097b")
        buf.write("\7~\2\2\u0979\u097c\5\u021c\u010f\2\u097a\u097c\5\u021a")
        buf.write("\u010e\2\u097b\u0979\3\2\2\2\u097b\u097a\3\2\2\2\u097c")
        buf.write("\u020f\3\2\2\2\u097d\u097e\5(\25\2\u097e\u0211\3\2\2\2")
        buf.write("\u097f\u0980\7\u0082\2\2\u0980\u0985\5\u0214\u010b\2\u0981")
        buf.write("\u0982\7\u0087\2\2\u0982\u0984\5\u0214\u010b\2\u0983\u0981")
        buf.write("\3\2\2\2\u0984\u0987\3\2\2\2\u0985\u0983\3\2\2\2\u0985")
        buf.write("\u0986\3\2\2\2\u0986\u0988\3\2\2\2\u0987\u0985\3\2\2\2")
        buf.write("\u0988\u0989\7\u0083\2\2\u0989\u0213\3\2\2\2\u098a\u098b")
        buf.write("\5\u0216\u010c\2\u098b\u098c\7\u008b\2\2\u098c\u098d\5")
        buf.write("\u0218\u010d\2\u098d\u0215\3\2\2\2\u098e\u098f\5\32\16")
        buf.write("\2\u098f\u0217\3\2\2\2\u0990\u0994\7\u0092\2\2\u0991\u0994")
        buf.write("\7\u0093\2\2\u0992\u0994\5\32\16\2\u0993\u0990\3\2\2\2")
        buf.write("\u0993\u0991\3\2\2\2\u0993\u0992\3\2\2\2\u0994\u0219\3")
        buf.write("\2\2\2\u0995\u0996\t\3\2\2\u0996\u021b\3\2\2\2\u0997\u0998")
        buf.write("\7N\2\2\u0998\u0999\7\u0080\2\2\u0999\u099a\5\u021e\u0110")
        buf.write("\2\u099a\u099b\7\u0081\2\2\u099b\u021d\3\2\2\2\u099c\u099d")
        buf.write("\5\32\16\2\u099d\u099e\7\u0088\2\2\u099e\u09a0\3\2\2\2")
        buf.write("\u099f\u099c\3\2\2\2\u099f\u09a0\3\2\2\2\u09a0\u09a1\3")
        buf.write("\2\2\2\u09a1\u09a2\5\32\16\2\u09a2\u021f\3\2\2\2\u09a3")
        buf.write("\u09a7\7\u0092\2\2\u09a4\u09a7\7\u0093\2\2\u09a5\u09a7")
        buf.write("\5\32\16\2\u09a6\u09a3\3\2\2\2\u09a6\u09a4\3\2\2\2\u09a6")
        buf.write("\u09a5\3\2\2\2\u09a7\u0221\3\2\2\2\u09a8\u09a9\7\26\2")
        buf.write("\2\u09a9\u09aa\5\u01b8\u00dd\2\u09aa\u0223\3\2\2\2\u09ab")
        buf.write("\u09ac\7\21\2\2\u09ac\u0225\3\2\2\2\u09ad\u09af\7\23\2")
        buf.write("\2\u09ae\u09b0\5*\26\2\u09af\u09ae\3\2\2\2\u09af\u09b0")
        buf.write("\3\2\2\2\u09b0\u0227\3\2\2\2\u09b1\u09b2\7\34\2\2\u09b2")
        buf.write("\u09b3\7\u0080\2\2\u09b3\u09b4\5\u022a\u0116\2\u09b4\u09b5")
        buf.write("\7\u0081\2\2\u09b5\u0229\3\2\2\2\u09b6\u09b7\7z\2\2\u09b7")
        buf.write("\u022b\3\2\2\2\u0106\u022f\u0235\u023b\u023f\u0244\u0246")
        buf.write("\u024b\u024f\u0254\u0256\u025b\u0263\u0268\u0270\u0277")
        buf.write("\u027a\u0283\u0289\u028c\u029b\u02a2\u02a7\u02af\u02b5")
        buf.write("\u02ba\u02bd\u02c0\u02c4\u02cc\u02de\u02e5\u02ec\u02f1")
        buf.write("\u02f6\u02fb\u0302\u0306\u030b\u0311\u0316\u0322\u0326")
        buf.write("\u032b\u0330\u0334\u033a\u0344\u034c\u034f\u0354\u035c")
        buf.write("\u0364\u0369\u036d\u0373\u0377\u037f\u0386\u038e\u0396")
        buf.write("\u039b\u039f\u03a2\u03a7\u03ae\u03b8\u03ba\u03c0\u03c2")
        buf.write("\u03c8\u03ca\u03cf\u03dc\u03eb\u03f4\u0400\u0405\u040a")
        buf.write("\u0410\u0416\u041c\u0422\u042a\u042d\u0431\u0435\u0440")
        buf.write("\u0446\u044b\u0452\u0459\u045e\u0461\u0464\u0469\u046c")
        buf.write("\u0470\u0475\u047a\u047f\u0492\u0496\u04b4\u04d3\u04d7")
        buf.write("\u04e2\u04e6\u04ed\u04f7\u0500\u0504\u050b\u051a\u0524")
        buf.write("\u052d\u0536\u0545\u054e\u0552\u0555\u0574\u0584\u0586")
        buf.write("\u058c\u0590\u0595\u059d\u05a5\u05ab\u05b5\u05c3\u05cd")
        buf.write("\u05cf\u05d3\u05ec\u05f1\u0601\u060a\u0613\u061c\u0625")
        buf.write("\u062e\u0639\u063c\u0640\u0649\u064f\u0655\u0657\u0666")
        buf.write("\u0668\u0673\u067b\u0680\u0686\u068b\u0691\u0696\u069c")
        buf.write("\u06a5\u06ae\u06b5\u06ba\u06c6\u06cf\u06dd\u06e4\u06ef")
        buf.write("\u06f1\u0704\u0712\u0739\u0740\u0745\u0749\u074d\u0751")
        buf.write("\u0753\u0757\u075c\u0769\u0770\u0778\u077a\u077d\u0784")
        buf.write("\u0786\u078e\u0795\u0798\u079a\u07a1\u07a7\u07ab\u07b0")
        buf.write("\u07b6\u07c1\u07c4\u07cd\u07d1\u07d6\u07d9\u07e2\u07e6")
        buf.write("\u07fb\u0801\u0803\u0809\u080c\u080f\u0812\u0816\u0822")
        buf.write("\u0825\u082c\u0835\u083e\u084c\u0852\u0857\u0868\u086a")
        buf.write("\u0870\u0875\u087a\u0880\u0886\u088f\u0896\u089d\u08a4")
        buf.write("\u08ad\u08b9\u08c3\u08df\u08e5\u08f8\u0912\u0917\u091b")
        buf.write("\u091e\u092b\u0932\u0935\u0939\u093d\u094f\u0955\u095a")
        buf.write("\u0962\u0967\u096b\u0970\u0975\u097b\u0985\u0993\u099f")
        buf.write("\u09a6\u09af")
        return buf.getvalue()


class ZmeiLangParser ( Parser ):

    grammarFileName = "ZmeiLangParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'@admin'", "'@suit'", "'@celery'", "'@stream'", 
                     "'@channels'", "'@docker'", "'@api'", "'@rest'", "'@filer'", 
                     "'@gitlab'", "'@react'", "'@react_client'", "'@react_server'", 
                     "'@theme'", "'@@'", "'@file'", "'@get'", "'@menu'", 
                     "'@crud'", "'@crud_detail'", "'@crud_list'", "'@crud_delete'", 
                     "'@crud_edit'", "'@crud_create'", "'@post'", "'@error'", 
                     "'@auth'", "'@markdown'", "'@html'", "'@tree'", "'@date_tree'", 
                     "'@mixin'", "'@m2m_changed'", "'@post_delete'", "'@pre_delete'", 
                     "'@post_save'", "'@pre_save'", "'@clean'", "'@order'", 
                     "'@sortable'", "'@langs'", "'basic'", "'session'", 
                     "'token'", "'text'", "'html'", "'html_media'", "'float'", 
                     "'decimal'", "'date'", "'datetime'", "'create_time'", 
                     "'update_time'", "'image'", "'file'", "'filer_image'", 
                     "'filer_file'", "'filer_folder'", "'filer_image_folder'", 
                     "'str'", "'int'", "'slug'", "'bool'", "'one'", "'one2one'", 
                     "'many'", "'choices'", "'theme'", "'install'", "'header'", 
                     "'services'", "'selenium_pytest'", "'child'", "'filter_out'", 
                     "'filter_in'", "'page'", "'link_suffix'", "'url_prefix'", 
                     "'can_edit'", "'object_expr'", "'block'", "'item_name'", 
                     "'pk_param'", "'list_fields'", "'delete'", "'edit'", 
                     "'create'", "'detail'", "'skip'", "'from'", "'+polymorphic_list'", 
                     "'css'", "'js'", "'tabular'", "'stacked'", "'polymorphic'", 
                     "'inline'", "'type'", "'user_field'", "'annotate'", 
                     "'on_create'", "'query'", "'auth'", "'count'", "'i18n'", 
                     "'extension'", "'tabs'", "'list'", "'read_only'", "'list_editable'", 
                     "'list_filter'", "'list_search'", "'fields'", "'import'", 
                     "'as'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'<'", "'>'", "':'", "'^'", 
                     "'('", "')'", "'['", "']'", "'?'", "'_'", "'-'", "','", 
                     "'.'", "'#'", "'/'", "'='", "'$'", "'&'", "'!'", "'*'", 
                     "'~'", "'|'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "' '", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "';'", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "AN_ADMIN", "AN_SUIT", "AN_CELERY", "AN_STREAM", 
                      "AN_CHANNELS", "AN_DOCKER", "AN_API", "AN_REST", "AN_FILER", 
                      "AN_GITLAB", "AN_REACT", "AN_REACT_CLIENT", "AN_REACT_SERVER", 
                      "AN_THEME", "AN_PRIORITY", "AN_FILE", "AN_GET", "AN_MENU", 
                      "AN_CRUD", "AN_CRUD_DETAIL", "AN_CRUD_LIST", "AN_CRUD_DELETE", 
                      "AN_CRUD_EDIT", "AN_CRUD_CREATE", "AN_POST", "AN_ERROR", 
                      "AN_AUTH", "AN_MARKDOWN", "AN_HTML", "AN_TREE", "AN_DATE_TREE", 
                      "AN_MIXIN", "AN_M2M_CHANGED", "AN_POST_DELETE", "AN_PRE_DELETE", 
                      "AN_POST_SAVE", "AN_PRE_SAVE", "AN_CLEAN", "AN_ORDER", 
                      "AN_SORTABLE", "AN_LANGS", "KW_AUTH_TYPE_BASIC", "KW_AUTH_TYPE_SESSION", 
                      "KW_AUTH_TYPE_TOKEN", "COL_FIELD_TYPE_LONGTEXT", "COL_FIELD_TYPE_HTML", 
                      "COL_FIELD_TYPE_HTML_MEDIA", "COL_FIELD_TYPE_FLOAT", 
                      "COL_FIELD_TYPE_DECIMAL", "COL_FIELD_TYPE_DATE", "COL_FIELD_TYPE_DATETIME", 
                      "COL_FIELD_TYPE_CREATE_TIME", "COL_FIELD_TYPE_UPDATE_TIME", 
                      "COL_FIELD_TYPE_IMAGE", "COL_FIELD_TYPE_FILE", "COL_FIELD_TYPE_FILER_IMAGE", 
                      "COL_FIELD_TYPE_FILER_FILE", "COL_FIELD_TYPE_FILER_FOLDER", 
                      "COL_FIELD_TYPE_FILER_IMAGE_FOLDER", "COL_FIELD_TYPE_TEXT", 
                      "COL_FIELD_TYPE_INT", "COL_FIELD_TYPE_SLUG", "COL_FIELD_TYPE_BOOL", 
                      "COL_FIELD_TYPE_ONE", "COL_FIELD_TYPE_ONE2ONE", "COL_FIELD_TYPE_MANY", 
                      "COL_FIELD_CHOICES", "KW_THEME", "KW_INSTALL", "KW_HEADER", 
                      "KW_SERVICES", "KW_SELENIUM_PYTEST", "KW_CHILD", "KW_FILTER_OUT", 
                      "KW_FILTER_IN", "KW_PAGE", "KW_LINK_SUFFIX", "KW_URL_PREFIX", 
                      "KW_CAN_EDIT", "KW_OBJECT_EXPR", "KW_BLOCK", "KW_ITEM_NAME", 
                      "KW_PK_PARAM", "KW_LIST_FIELDS", "KW_DELETE", "KW_EDIT", 
                      "KW_CREATE", "KW_DETAIL", "KW_SKIP", "KW_FROM", "KW_POLY_LIST", 
                      "KW_CSS", "KW_JS", "KW_INLINE_TYPE_TABULAR", "KW_INLINE_TYPE_STACKED", 
                      "KW_INLINE_TYPE_POLYMORPHIC", "KW_INLINE", "KW_TYPE", 
                      "KW_USER_FIELD", "KW_ANNOTATE", "KW_ON_CREATE", "KW_QUERY", 
                      "KW_AUTH", "KW_COUNT", "KW_I18N", "KW_EXTENSION", 
                      "KW_TABS", "KW_LIST", "KW_READ_ONLY", "KW_LIST_EDITABLE", 
                      "KW_LIST_FILTER", "KW_LIST_SEARCH", "KW_FIELDS", "KW_IMPORT", 
                      "KW_AS", "WRITE_MODE", "BOOL", "NL", "ID", "DIGIT", 
                      "SIZE2D", "LT", "GT", "COLON", "EXCLUDE", "BRACE_OPEN", 
                      "BRACE_CLOSE", "SQ_BRACE_OPEN", "SQ_BRACE_CLOSE", 
                      "QUESTION_MARK", "UNDERSCORE", "DASH", "COMA", "DOT", 
                      "HASH", "SLASH", "EQUALS", "DOLLAR", "AMP", "EXCLAM", 
                      "STAR", "APPROX", "PIPE", "STRING_DQ", "STRING_SQ", 
                      "COMMENT_LINE", "COMMENT_BLOCK", "UNICODE", "WS", 
                      "COL_FIELD_CALCULATED", "ASSIGN", "ASSIGN_STATIC", 
                      "CODE_BLOCK", "ERRCHAR", "PYTHON_CODE", "PYTHON_LINE_ERRCHAR", 
                      "PYTHON_LINE_END", "PYTHON_EXPR_ERRCHAR", "PYTHON_LINE_NL" ]

    RULE_col_file = 0
    RULE_page_imports = 1
    RULE_model_imports = 2
    RULE_page_import_statement = 3
    RULE_model_import_statement = 4
    RULE_import_statement = 5
    RULE_import_source = 6
    RULE_import_list = 7
    RULE_import_item = 8
    RULE_import_item_name = 9
    RULE_import_item_alias = 10
    RULE_import_item_all = 11
    RULE_id_or_kw = 12
    RULE_classname = 13
    RULE_model_ref = 14
    RULE_field_list_expr = 15
    RULE_field_list_expr_field = 16
    RULE_write_mode_expr = 17
    RULE_python_code = 18
    RULE_code_line = 19
    RULE_code_block = 20
    RULE_cs_annotation = 21
    RULE_an_suit = 22
    RULE_an_suit_app_name = 23
    RULE_an_celery = 24
    RULE_an_channels = 25
    RULE_an_docker = 26
    RULE_an_filer = 27
    RULE_an_gitlab = 28
    RULE_an_gitlab_test_declaration = 29
    RULE_an_gitlab_test_declaration_selenium_pytest = 30
    RULE_an_gitlab_test_services = 31
    RULE_an_gitlab_test_service = 32
    RULE_an_gitlab_test_service_name = 33
    RULE_an_gitlab_branch_declaration = 34
    RULE_an_gitlab_branch_deploy_type = 35
    RULE_an_gitlab_branch_name = 36
    RULE_an_gitlab_deployment_name = 37
    RULE_an_gitlab_deployment_host = 38
    RULE_an_gitlab_deployment_variable = 39
    RULE_an_gitlab_deployment_variable_name = 40
    RULE_an_gitlab_deployment_variable_value = 41
    RULE_an_file = 42
    RULE_an_file_name = 43
    RULE_an_theme = 44
    RULE_an_theme_install = 45
    RULE_an_theme_name = 46
    RULE_an_langs = 47
    RULE_an_langs_list = 48
    RULE_col = 49
    RULE_col_str_expr = 50
    RULE_col_header = 51
    RULE_col_header_line_separator = 52
    RULE_col_verbose_name = 53
    RULE_verbose_name_part = 54
    RULE_col_base_name = 55
    RULE_col_name = 56
    RULE_col_field = 57
    RULE_col_field_expr_or_def = 58
    RULE_col_field_custom = 59
    RULE_col_field_extend = 60
    RULE_col_field_extend_append = 61
    RULE_wrong_field_type = 62
    RULE_col_field_expr = 63
    RULE_col_field_expr_marker = 64
    RULE_col_feild_expr_code = 65
    RULE_string_or_quoted = 66
    RULE_col_field_help_text = 67
    RULE_col_field_verbose_name = 68
    RULE_col_field_name = 69
    RULE_col_modifier = 70
    RULE_col_field_def = 71
    RULE_field_longtext = 72
    RULE_field_html = 73
    RULE_field_html_media = 74
    RULE_field_float = 75
    RULE_field_decimal = 76
    RULE_field_date = 77
    RULE_field_datetime = 78
    RULE_field_create_time = 79
    RULE_field_update_time = 80
    RULE_field_file = 81
    RULE_field_filer_file = 82
    RULE_field_filer_folder = 83
    RULE_field_text = 84
    RULE_field_text_size = 85
    RULE_field_text_choices = 86
    RULE_field_text_choice = 87
    RULE_field_text_choice_val = 88
    RULE_field_text_choice_key = 89
    RULE_field_int = 90
    RULE_field_int_choices = 91
    RULE_field_int_choice = 92
    RULE_field_int_choice_val = 93
    RULE_field_int_choice_key = 94
    RULE_field_slug = 95
    RULE_field_slug_ref_field = 96
    RULE_field_slug_ref_field_id = 97
    RULE_field_bool = 98
    RULE_field_bool_default = 99
    RULE_field_image = 100
    RULE_filer_image_type = 101
    RULE_field_image_sizes = 102
    RULE_field_image_size = 103
    RULE_field_image_size_dimensions = 104
    RULE_field_image_size_name = 105
    RULE_field_image_filters = 106
    RULE_field_image_filter = 107
    RULE_field_relation = 108
    RULE_field_relation_type = 109
    RULE_field_relation_cascade_marker = 110
    RULE_field_relation_target_ref = 111
    RULE_field_relation_target_class = 112
    RULE_field_relation_related_name = 113
    RULE_model_annotation = 114
    RULE_an_admin = 115
    RULE_an_admin_js = 116
    RULE_an_admin_css = 117
    RULE_an_admin_css_file_name = 118
    RULE_an_admin_js_file_name = 119
    RULE_an_admin_inlines = 120
    RULE_an_admin_inline = 121
    RULE_inline_name = 122
    RULE_inline_type = 123
    RULE_inline_type_name = 124
    RULE_inline_extension = 125
    RULE_inline_fields = 126
    RULE_an_admin_tabs = 127
    RULE_an_admin_tab = 128
    RULE_tab_name = 129
    RULE_tab_verbose_name = 130
    RULE_an_admin_list = 131
    RULE_an_admin_read_only = 132
    RULE_an_admin_list_editable = 133
    RULE_an_admin_list_filter = 134
    RULE_an_admin_list_search = 135
    RULE_an_admin_fields = 136
    RULE_an_api = 137
    RULE_an_api_all = 138
    RULE_an_api_name = 139
    RULE_an_rest = 140
    RULE_an_rest_config = 141
    RULE_an_rest_main_part = 142
    RULE_an_rest_descriptor = 143
    RULE_an_rest_i18n = 144
    RULE_an_rest_query = 145
    RULE_an_rest_on_create = 146
    RULE_an_rest_filter_in = 147
    RULE_an_rest_filter_out = 148
    RULE_an_rest_read_only = 149
    RULE_an_rest_user_field = 150
    RULE_an_rest_fields = 151
    RULE_an_rest_fields_write_mode = 152
    RULE_an_rest_auth = 153
    RULE_an_rest_auth_type = 154
    RULE_an_rest_auth_type_name = 155
    RULE_an_rest_auth_token_model = 156
    RULE_an_rest_auth_token_class = 157
    RULE_an_rest_annotate = 158
    RULE_an_rest_annotate_count = 159
    RULE_an_rest_annotate_count_field = 160
    RULE_an_rest_annotate_count_alias = 161
    RULE_an_rest_inline = 162
    RULE_an_rest_inline_decl = 163
    RULE_an_rest_inline_name = 164
    RULE_an_order = 165
    RULE_an_order_fields = 166
    RULE_an_clean = 167
    RULE_an_pre_delete = 168
    RULE_an_tree = 169
    RULE_an_tree_poly = 170
    RULE_an_mixin = 171
    RULE_an_date_tree = 172
    RULE_an_date_tree_field = 173
    RULE_an_m2m_changed = 174
    RULE_an_post_save = 175
    RULE_an_pre_save = 176
    RULE_an_post_delete = 177
    RULE_an_sortable = 178
    RULE_an_sortable_field_name = 179
    RULE_page = 180
    RULE_page_header = 181
    RULE_page_base = 182
    RULE_page_alias = 183
    RULE_page_alias_name = 184
    RULE_page_template = 185
    RULE_template_name = 186
    RULE_file_name_part = 187
    RULE_page_url = 188
    RULE_url_part = 189
    RULE_url_param = 190
    RULE_url_segment = 191
    RULE_url_segments = 192
    RULE_page_name = 193
    RULE_page_body = 194
    RULE_page_code = 195
    RULE_page_field = 196
    RULE_page_field_name = 197
    RULE_page_field_code = 198
    RULE_page_function = 199
    RULE_page_function_name = 200
    RULE_page_function_args = 201
    RULE_page_function_arg = 202
    RULE_page_annotation = 203
    RULE_an_stream = 204
    RULE_an_stream_model = 205
    RULE_an_stream_target_model = 206
    RULE_an_stream_target_filter = 207
    RULE_an_stream_field_list = 208
    RULE_an_stream_field_name = 209
    RULE_an_react = 210
    RULE_an_react_type = 211
    RULE_an_react_descriptor = 212
    RULE_an_html = 213
    RULE_an_html_descriptor = 214
    RULE_an_markdown = 215
    RULE_an_markdown_descriptor = 216
    RULE_an_crud_delete = 217
    RULE_an_crud = 218
    RULE_an_crud_params = 219
    RULE_an_crud_page_override = 220
    RULE_an_crud_descriptor = 221
    RULE_an_crud_next_page = 222
    RULE_an_crud_next_page_event_name = 223
    RULE_an_crud_next_page_url = 224
    RULE_an_crud_next_page_url_val = 225
    RULE_an_crud_target_model = 226
    RULE_an_crud_target_filter = 227
    RULE_an_crud_theme = 228
    RULE_an_crud_url_prefix = 229
    RULE_an_crud_url_prefix_val = 230
    RULE_an_crud_link_suffix = 231
    RULE_an_crud_link_suffix_val = 232
    RULE_an_crud_item_name = 233
    RULE_an_crud_object_expr = 234
    RULE_an_crud_can_edit = 235
    RULE_an_crud_block = 236
    RULE_an_crud_pk_param = 237
    RULE_an_crud_skip = 238
    RULE_an_crud_skip_values = 239
    RULE_an_crud_view_name = 240
    RULE_an_crud_fields = 241
    RULE_an_crud_list_type = 242
    RULE_an_crud_list_type_var = 243
    RULE_an_crud_header = 244
    RULE_an_crud_header_enabled = 245
    RULE_an_crud_fields_expr = 246
    RULE_an_crud_field = 247
    RULE_an_crud_field_spec = 248
    RULE_an_crud_field_filter = 249
    RULE_an_crud_list_fields = 250
    RULE_an_crud_list_fields_expr = 251
    RULE_an_crud_list_field = 252
    RULE_an_crud_list_field_spec = 253
    RULE_an_post = 254
    RULE_an_auth = 255
    RULE_an_crud_create = 256
    RULE_an_crud_edit = 257
    RULE_an_crud_list = 258
    RULE_an_menu = 259
    RULE_an_menu_descriptor = 260
    RULE_an_menu_item = 261
    RULE_an_menu_target = 262
    RULE_an_menu_item_code = 263
    RULE_an_menu_item_args = 264
    RULE_an_menu_item_arg = 265
    RULE_an_menu_item_arg_key = 266
    RULE_an_menu_item_arg_val = 267
    RULE_an_menu_item_url = 268
    RULE_an_menu_item_page = 269
    RULE_an_menu_item_page_ref = 270
    RULE_an_menu_label = 271
    RULE_an_crud_detail = 272
    RULE_an_priority_marker = 273
    RULE_an_get = 274
    RULE_an_error = 275
    RULE_an_error_code = 276

    ruleNames =  [ "col_file", "page_imports", "model_imports", "page_import_statement", 
                   "model_import_statement", "import_statement", "import_source", 
                   "import_list", "import_item", "import_item_name", "import_item_alias", 
                   "import_item_all", "id_or_kw", "classname", "model_ref", 
                   "field_list_expr", "field_list_expr_field", "write_mode_expr", 
                   "python_code", "code_line", "code_block", "cs_annotation", 
                   "an_suit", "an_suit_app_name", "an_celery", "an_channels", 
                   "an_docker", "an_filer", "an_gitlab", "an_gitlab_test_declaration", 
                   "an_gitlab_test_declaration_selenium_pytest", "an_gitlab_test_services", 
                   "an_gitlab_test_service", "an_gitlab_test_service_name", 
                   "an_gitlab_branch_declaration", "an_gitlab_branch_deploy_type", 
                   "an_gitlab_branch_name", "an_gitlab_deployment_name", 
                   "an_gitlab_deployment_host", "an_gitlab_deployment_variable", 
                   "an_gitlab_deployment_variable_name", "an_gitlab_deployment_variable_value", 
                   "an_file", "an_file_name", "an_theme", "an_theme_install", 
                   "an_theme_name", "an_langs", "an_langs_list", "col", 
                   "col_str_expr", "col_header", "col_header_line_separator", 
                   "col_verbose_name", "verbose_name_part", "col_base_name", 
                   "col_name", "col_field", "col_field_expr_or_def", "col_field_custom", 
                   "col_field_extend", "col_field_extend_append", "wrong_field_type", 
                   "col_field_expr", "col_field_expr_marker", "col_feild_expr_code", 
                   "string_or_quoted", "col_field_help_text", "col_field_verbose_name", 
                   "col_field_name", "col_modifier", "col_field_def", "field_longtext", 
                   "field_html", "field_html_media", "field_float", "field_decimal", 
                   "field_date", "field_datetime", "field_create_time", 
                   "field_update_time", "field_file", "field_filer_file", 
                   "field_filer_folder", "field_text", "field_text_size", 
                   "field_text_choices", "field_text_choice", "field_text_choice_val", 
                   "field_text_choice_key", "field_int", "field_int_choices", 
                   "field_int_choice", "field_int_choice_val", "field_int_choice_key", 
                   "field_slug", "field_slug_ref_field", "field_slug_ref_field_id", 
                   "field_bool", "field_bool_default", "field_image", "filer_image_type", 
                   "field_image_sizes", "field_image_size", "field_image_size_dimensions", 
                   "field_image_size_name", "field_image_filters", "field_image_filter", 
                   "field_relation", "field_relation_type", "field_relation_cascade_marker", 
                   "field_relation_target_ref", "field_relation_target_class", 
                   "field_relation_related_name", "model_annotation", "an_admin", 
                   "an_admin_js", "an_admin_css", "an_admin_css_file_name", 
                   "an_admin_js_file_name", "an_admin_inlines", "an_admin_inline", 
                   "inline_name", "inline_type", "inline_type_name", "inline_extension", 
                   "inline_fields", "an_admin_tabs", "an_admin_tab", "tab_name", 
                   "tab_verbose_name", "an_admin_list", "an_admin_read_only", 
                   "an_admin_list_editable", "an_admin_list_filter", "an_admin_list_search", 
                   "an_admin_fields", "an_api", "an_api_all", "an_api_name", 
                   "an_rest", "an_rest_config", "an_rest_main_part", "an_rest_descriptor", 
                   "an_rest_i18n", "an_rest_query", "an_rest_on_create", 
                   "an_rest_filter_in", "an_rest_filter_out", "an_rest_read_only", 
                   "an_rest_user_field", "an_rest_fields", "an_rest_fields_write_mode", 
                   "an_rest_auth", "an_rest_auth_type", "an_rest_auth_type_name", 
                   "an_rest_auth_token_model", "an_rest_auth_token_class", 
                   "an_rest_annotate", "an_rest_annotate_count", "an_rest_annotate_count_field", 
                   "an_rest_annotate_count_alias", "an_rest_inline", "an_rest_inline_decl", 
                   "an_rest_inline_name", "an_order", "an_order_fields", 
                   "an_clean", "an_pre_delete", "an_tree", "an_tree_poly", 
                   "an_mixin", "an_date_tree", "an_date_tree_field", "an_m2m_changed", 
                   "an_post_save", "an_pre_save", "an_post_delete", "an_sortable", 
                   "an_sortable_field_name", "page", "page_header", "page_base", 
                   "page_alias", "page_alias_name", "page_template", "template_name", 
                   "file_name_part", "page_url", "url_part", "url_param", 
                   "url_segment", "url_segments", "page_name", "page_body", 
                   "page_code", "page_field", "page_field_name", "page_field_code", 
                   "page_function", "page_function_name", "page_function_args", 
                   "page_function_arg", "page_annotation", "an_stream", 
                   "an_stream_model", "an_stream_target_model", "an_stream_target_filter", 
                   "an_stream_field_list", "an_stream_field_name", "an_react", 
                   "an_react_type", "an_react_descriptor", "an_html", "an_html_descriptor", 
                   "an_markdown", "an_markdown_descriptor", "an_crud_delete", 
                   "an_crud", "an_crud_params", "an_crud_page_override", 
                   "an_crud_descriptor", "an_crud_next_page", "an_crud_next_page_event_name", 
                   "an_crud_next_page_url", "an_crud_next_page_url_val", 
                   "an_crud_target_model", "an_crud_target_filter", "an_crud_theme", 
                   "an_crud_url_prefix", "an_crud_url_prefix_val", "an_crud_link_suffix", 
                   "an_crud_link_suffix_val", "an_crud_item_name", "an_crud_object_expr", 
                   "an_crud_can_edit", "an_crud_block", "an_crud_pk_param", 
                   "an_crud_skip", "an_crud_skip_values", "an_crud_view_name", 
                   "an_crud_fields", "an_crud_list_type", "an_crud_list_type_var", 
                   "an_crud_header", "an_crud_header_enabled", "an_crud_fields_expr", 
                   "an_crud_field", "an_crud_field_spec", "an_crud_field_filter", 
                   "an_crud_list_fields", "an_crud_list_fields_expr", "an_crud_list_field", 
                   "an_crud_list_field_spec", "an_post", "an_auth", "an_crud_create", 
                   "an_crud_edit", "an_crud_list", "an_menu", "an_menu_descriptor", 
                   "an_menu_item", "an_menu_target", "an_menu_item_code", 
                   "an_menu_item_args", "an_menu_item_arg", "an_menu_item_arg_key", 
                   "an_menu_item_arg_val", "an_menu_item_url", "an_menu_item_page", 
                   "an_menu_item_page_ref", "an_menu_label", "an_crud_detail", 
                   "an_priority_marker", "an_get", "an_error", "an_error_code" ]

    EOF = Token.EOF
    AN_ADMIN=1
    AN_SUIT=2
    AN_CELERY=3
    AN_STREAM=4
    AN_CHANNELS=5
    AN_DOCKER=6
    AN_API=7
    AN_REST=8
    AN_FILER=9
    AN_GITLAB=10
    AN_REACT=11
    AN_REACT_CLIENT=12
    AN_REACT_SERVER=13
    AN_THEME=14
    AN_PRIORITY=15
    AN_FILE=16
    AN_GET=17
    AN_MENU=18
    AN_CRUD=19
    AN_CRUD_DETAIL=20
    AN_CRUD_LIST=21
    AN_CRUD_DELETE=22
    AN_CRUD_EDIT=23
    AN_CRUD_CREATE=24
    AN_POST=25
    AN_ERROR=26
    AN_AUTH=27
    AN_MARKDOWN=28
    AN_HTML=29
    AN_TREE=30
    AN_DATE_TREE=31
    AN_MIXIN=32
    AN_M2M_CHANGED=33
    AN_POST_DELETE=34
    AN_PRE_DELETE=35
    AN_POST_SAVE=36
    AN_PRE_SAVE=37
    AN_CLEAN=38
    AN_ORDER=39
    AN_SORTABLE=40
    AN_LANGS=41
    KW_AUTH_TYPE_BASIC=42
    KW_AUTH_TYPE_SESSION=43
    KW_AUTH_TYPE_TOKEN=44
    COL_FIELD_TYPE_LONGTEXT=45
    COL_FIELD_TYPE_HTML=46
    COL_FIELD_TYPE_HTML_MEDIA=47
    COL_FIELD_TYPE_FLOAT=48
    COL_FIELD_TYPE_DECIMAL=49
    COL_FIELD_TYPE_DATE=50
    COL_FIELD_TYPE_DATETIME=51
    COL_FIELD_TYPE_CREATE_TIME=52
    COL_FIELD_TYPE_UPDATE_TIME=53
    COL_FIELD_TYPE_IMAGE=54
    COL_FIELD_TYPE_FILE=55
    COL_FIELD_TYPE_FILER_IMAGE=56
    COL_FIELD_TYPE_FILER_FILE=57
    COL_FIELD_TYPE_FILER_FOLDER=58
    COL_FIELD_TYPE_FILER_IMAGE_FOLDER=59
    COL_FIELD_TYPE_TEXT=60
    COL_FIELD_TYPE_INT=61
    COL_FIELD_TYPE_SLUG=62
    COL_FIELD_TYPE_BOOL=63
    COL_FIELD_TYPE_ONE=64
    COL_FIELD_TYPE_ONE2ONE=65
    COL_FIELD_TYPE_MANY=66
    COL_FIELD_CHOICES=67
    KW_THEME=68
    KW_INSTALL=69
    KW_HEADER=70
    KW_SERVICES=71
    KW_SELENIUM_PYTEST=72
    KW_CHILD=73
    KW_FILTER_OUT=74
    KW_FILTER_IN=75
    KW_PAGE=76
    KW_LINK_SUFFIX=77
    KW_URL_PREFIX=78
    KW_CAN_EDIT=79
    KW_OBJECT_EXPR=80
    KW_BLOCK=81
    KW_ITEM_NAME=82
    KW_PK_PARAM=83
    KW_LIST_FIELDS=84
    KW_DELETE=85
    KW_EDIT=86
    KW_CREATE=87
    KW_DETAIL=88
    KW_SKIP=89
    KW_FROM=90
    KW_POLY_LIST=91
    KW_CSS=92
    KW_JS=93
    KW_INLINE_TYPE_TABULAR=94
    KW_INLINE_TYPE_STACKED=95
    KW_INLINE_TYPE_POLYMORPHIC=96
    KW_INLINE=97
    KW_TYPE=98
    KW_USER_FIELD=99
    KW_ANNOTATE=100
    KW_ON_CREATE=101
    KW_QUERY=102
    KW_AUTH=103
    KW_COUNT=104
    KW_I18N=105
    KW_EXTENSION=106
    KW_TABS=107
    KW_LIST=108
    KW_READ_ONLY=109
    KW_LIST_EDITABLE=110
    KW_LIST_FILTER=111
    KW_LIST_SEARCH=112
    KW_FIELDS=113
    KW_IMPORT=114
    KW_AS=115
    WRITE_MODE=116
    BOOL=117
    NL=118
    ID=119
    DIGIT=120
    SIZE2D=121
    LT=122
    GT=123
    COLON=124
    EXCLUDE=125
    BRACE_OPEN=126
    BRACE_CLOSE=127
    SQ_BRACE_OPEN=128
    SQ_BRACE_CLOSE=129
    QUESTION_MARK=130
    UNDERSCORE=131
    DASH=132
    COMA=133
    DOT=134
    HASH=135
    SLASH=136
    EQUALS=137
    DOLLAR=138
    AMP=139
    EXCLAM=140
    STAR=141
    APPROX=142
    PIPE=143
    STRING_DQ=144
    STRING_SQ=145
    COMMENT_LINE=146
    COMMENT_BLOCK=147
    UNICODE=148
    WS=149
    COL_FIELD_CALCULATED=150
    ASSIGN=151
    ASSIGN_STATIC=152
    CODE_BLOCK=153
    ERRCHAR=154
    PYTHON_CODE=155
    PYTHON_LINE_ERRCHAR=156
    PYTHON_LINE_END=157
    PYTHON_EXPR_ERRCHAR=158
    PYTHON_LINE_NL=159

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Col_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def cs_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Cs_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Cs_annotationContext,i)


        def page_imports(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_importsContext,0)


        def page(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.PageContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.PageContext,i)


        def model_imports(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_importsContext,0)


        def col(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.ColContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.ColContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_file" ):
                listener.enterCol_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_file" ):
                listener.exitCol_file(self)




    def col_file(self):

        localctx = ZmeiLangParser.Col_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_col_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 554
                    self.match(ZmeiLangParser.NL) 
                self.state = 559
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 560
                    self.cs_annotation() 
                self.state = 565
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 569
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 566
                    self.match(ZmeiLangParser.NL) 
                self.state = 571
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 580
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 572
                    self.page_imports()


                self.state = 576 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 575
                    self.page()
                    self.state = 578 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.SQ_BRACE_OPEN):
                        break



            self.state = 585
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 582
                    self.match(ZmeiLangParser.NL) 
                self.state = 587
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 596
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 90)) & ~0x3f) == 0 and ((1 << (_la - 90)) & ((1 << (ZmeiLangParser.KW_FROM - 90)) | (1 << (ZmeiLangParser.KW_IMPORT - 90)) | (1 << (ZmeiLangParser.HASH - 90)))) != 0):
                self.state = 589
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT:
                    self.state = 588
                    self.model_imports()


                self.state = 592 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 591
                    self.col()
                    self.state = 594 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZmeiLangParser.HASH):
                        break



            self.state = 601
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 598
                self.match(ZmeiLangParser.NL)
                self.state = 603
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 604
            self.match(ZmeiLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_importsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_import_statementContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_import_statementContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_imports" ):
                listener.enterPage_imports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_imports" ):
                listener.exitPage_imports(self)




    def page_imports(self):

        localctx = ZmeiLangParser.Page_importsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_page_imports)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 606
                self.page_import_statement()
                self.state = 609 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_importsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Model_import_statementContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Model_import_statementContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_imports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_imports" ):
                listener.enterModel_imports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_imports" ):
                listener.exitModel_imports(self)




    def model_imports(self):

        localctx = ZmeiLangParser.Model_importsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_model_imports)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 611
                self.model_import_statement()
                self.state = 614 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.KW_FROM or _la==ZmeiLangParser.KW_IMPORT):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_statementContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_import_statement" ):
                listener.enterPage_import_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_import_statement" ):
                listener.exitPage_import_statement(self)




    def page_import_statement(self):

        localctx = ZmeiLangParser.Page_import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_page_import_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            self.import_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_statement(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_statementContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_import_statement" ):
                listener.enterModel_import_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_import_statement" ):
                listener.exitModel_import_statement(self)




    def model_import_statement(self):

        localctx = ZmeiLangParser.Model_import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_model_import_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 618
            self.import_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def import_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_listContext,0)


        def KW_FROM(self):
            return self.getToken(ZmeiLangParser.KW_FROM, 0)

        def import_source(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_sourceContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_statement" ):
                listener.enterImport_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_statement" ):
                listener.exitImport_statement(self)




    def import_statement(self):

        localctx = ZmeiLangParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_import_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_FROM:
                self.state = 620
                self.match(ZmeiLangParser.KW_FROM)
                self.state = 621
                self.import_source()


            self.state = 624
            self.match(ZmeiLangParser.KW_IMPORT)
            self.state = 625
            self.import_list()
            self.state = 627 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 626
                self.match(ZmeiLangParser.NL)
                self.state = 629 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.NL):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_sourceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_source" ):
                listener.enterImport_source(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_source" ):
                listener.exitImport_source(self)




    def import_source(self):

        localctx = ZmeiLangParser.Import_sourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_import_source)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 631
                self.match(ZmeiLangParser.DOT)


            self.state = 634
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Import_itemContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Import_itemContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_list" ):
                listener.enterImport_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_list" ):
                listener.exitImport_list(self)




    def import_list(self):

        localctx = ZmeiLangParser.Import_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_import_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
            self.import_item()
            self.state = 641
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 637
                self.match(ZmeiLangParser.COMA)
                self.state = 638
                self.import_item()
                self.state = 643
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_item_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_nameContext,0)


        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def import_item_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_aliasContext,0)


        def import_item_all(self):
            return self.getTypedRuleContext(ZmeiLangParser.Import_item_allContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item" ):
                listener.enterImport_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item" ):
                listener.exitImport_item(self)




    def import_item(self):

        localctx = ZmeiLangParser.Import_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_import_item)
        self._la = 0 # Token type
        try:
            self.state = 650
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.import_item_name()
                self.state = 647
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.KW_AS:
                    self.state = 645
                    self.match(ZmeiLangParser.KW_AS)
                    self.state = 646
                    self.import_item_alias()


                pass
            elif token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 649
                self.import_item_all()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_item_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_name" ):
                listener.enterImport_item_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_name" ):
                listener.exitImport_item_name(self)




    def import_item_name(self):

        localctx = ZmeiLangParser.Import_item_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_item_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_alias" ):
                listener.enterImport_item_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_alias" ):
                listener.exitImport_item_alias(self)




    def import_item_alias(self):

        localctx = ZmeiLangParser.Import_item_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_import_item_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_item_allContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_import_item_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_item_all" ):
                listener.enterImport_item_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_item_all" ):
                listener.exitImport_item_all(self)




    def import_item_all(self):

        localctx = ZmeiLangParser.Import_item_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_import_item_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.match(ZmeiLangParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_or_kwContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ZmeiLangParser.ID, 0)

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def WRITE_MODE(self):
            return self.getToken(ZmeiLangParser.WRITE_MODE, 0)

        def KW_AUTH_TYPE_BASIC(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_BASIC, 0)

        def KW_AUTH_TYPE_SESSION(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_SESSION, 0)

        def KW_AUTH_TYPE_TOKEN(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_TOKEN, 0)

        def COL_FIELD_TYPE_LONGTEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, 0)

        def COL_FIELD_TYPE_HTML(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML, 0)

        def COL_FIELD_TYPE_HTML_MEDIA(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, 0)

        def COL_FIELD_TYPE_FLOAT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FLOAT, 0)

        def COL_FIELD_TYPE_DECIMAL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, 0)

        def COL_FIELD_TYPE_DATE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATE, 0)

        def COL_FIELD_TYPE_DATETIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATETIME, 0)

        def COL_FIELD_TYPE_CREATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, 0)

        def COL_FIELD_TYPE_UPDATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, 0)

        def COL_FIELD_TYPE_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE, 0)

        def COL_FIELD_TYPE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, 0)

        def COL_FIELD_TYPE_FILER_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, 0)

        def COL_FIELD_TYPE_FILER_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, 0)

        def COL_FIELD_TYPE_TEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_TEXT, 0)

        def COL_FIELD_TYPE_INT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_INT, 0)

        def COL_FIELD_TYPE_SLUG(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SLUG, 0)

        def COL_FIELD_TYPE_BOOL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_BOOL, 0)

        def COL_FIELD_TYPE_ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE, 0)

        def COL_FIELD_TYPE_ONE2ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, 0)

        def COL_FIELD_TYPE_MANY(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_MANY, 0)

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def KW_THEME(self):
            return self.getToken(ZmeiLangParser.KW_THEME, 0)

        def KW_INSTALL(self):
            return self.getToken(ZmeiLangParser.KW_INSTALL, 0)

        def KW_HEADER(self):
            return self.getToken(ZmeiLangParser.KW_HEADER, 0)

        def KW_SERVICES(self):
            return self.getToken(ZmeiLangParser.KW_SERVICES, 0)

        def KW_SELENIUM_PYTEST(self):
            return self.getToken(ZmeiLangParser.KW_SELENIUM_PYTEST, 0)

        def KW_CHILD(self):
            return self.getToken(ZmeiLangParser.KW_CHILD, 0)

        def KW_FILTER_OUT(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_OUT, 0)

        def KW_FILTER_IN(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_IN, 0)

        def KW_PAGE(self):
            return self.getToken(ZmeiLangParser.KW_PAGE, 0)

        def KW_LINK_SUFFIX(self):
            return self.getToken(ZmeiLangParser.KW_LINK_SUFFIX, 0)

        def KW_URL_PREFIX(self):
            return self.getToken(ZmeiLangParser.KW_URL_PREFIX, 0)

        def KW_CAN_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_CAN_EDIT, 0)

        def KW_OBJECT_EXPR(self):
            return self.getToken(ZmeiLangParser.KW_OBJECT_EXPR, 0)

        def KW_BLOCK(self):
            return self.getToken(ZmeiLangParser.KW_BLOCK, 0)

        def KW_ITEM_NAME(self):
            return self.getToken(ZmeiLangParser.KW_ITEM_NAME, 0)

        def KW_PK_PARAM(self):
            return self.getToken(ZmeiLangParser.KW_PK_PARAM, 0)

        def KW_LIST_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FIELDS, 0)

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_DETAIL(self):
            return self.getToken(ZmeiLangParser.KW_DETAIL, 0)

        def KW_SKIP(self):
            return self.getToken(ZmeiLangParser.KW_SKIP, 0)

        def KW_FROM(self):
            return self.getToken(ZmeiLangParser.KW_FROM, 0)

        def KW_POLY_LIST(self):
            return self.getToken(ZmeiLangParser.KW_POLY_LIST, 0)

        def KW_CSS(self):
            return self.getToken(ZmeiLangParser.KW_CSS, 0)

        def KW_JS(self):
            return self.getToken(ZmeiLangParser.KW_JS, 0)

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def KW_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_TYPE, 0)

        def KW_USER_FIELD(self):
            return self.getToken(ZmeiLangParser.KW_USER_FIELD, 0)

        def KW_ANNOTATE(self):
            return self.getToken(ZmeiLangParser.KW_ANNOTATE, 0)

        def KW_ON_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_ON_CREATE, 0)

        def KW_QUERY(self):
            return self.getToken(ZmeiLangParser.KW_QUERY, 0)

        def KW_AUTH(self):
            return self.getToken(ZmeiLangParser.KW_AUTH, 0)

        def KW_COUNT(self):
            return self.getToken(ZmeiLangParser.KW_COUNT, 0)

        def KW_I18N(self):
            return self.getToken(ZmeiLangParser.KW_I18N, 0)

        def KW_EXTENSION(self):
            return self.getToken(ZmeiLangParser.KW_EXTENSION, 0)

        def KW_TABS(self):
            return self.getToken(ZmeiLangParser.KW_TABS, 0)

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def KW_READ_ONLY(self):
            return self.getToken(ZmeiLangParser.KW_READ_ONLY, 0)

        def KW_LIST_EDITABLE(self):
            return self.getToken(ZmeiLangParser.KW_LIST_EDITABLE, 0)

        def KW_LIST_FILTER(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FILTER, 0)

        def KW_LIST_SEARCH(self):
            return self.getToken(ZmeiLangParser.KW_LIST_SEARCH, 0)

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def KW_IMPORT(self):
            return self.getToken(ZmeiLangParser.KW_IMPORT, 0)

        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_id_or_kw

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_or_kw" ):
                listener.enterId_or_kw(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_or_kw" ):
                listener.exitId_or_kw(self)




    def id_or_kw(self):

        localctx = ZmeiLangParser.Id_or_kwContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_id_or_kw)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 658
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_FROM - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTENSION - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.WRITE_MODE - 64)) | (1 << (ZmeiLangParser.BOOL - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_classname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassname" ):
                listener.enterClassname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassname" ):
                listener.exitClassname(self)




    def classname(self):

        localctx = ZmeiLangParser.ClassnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_classname)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 660
            self.id_or_kw()
            self.state = 665
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.DOT:
                self.state = 661
                self.match(ZmeiLangParser.DOT)
                self.state = 662
                self.id_or_kw()
                self.state = 667
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_ref" ):
                listener.enterModel_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_ref" ):
                listener.exitModel_ref(self)




    def model_ref(self):

        localctx = ZmeiLangParser.Model_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_model_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 668
            self.match(ZmeiLangParser.HASH)
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 669
                self.id_or_kw()
                self.state = 670
                self.match(ZmeiLangParser.DOT)


            self.state = 674
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_list_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def EXCLUDE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.EXCLUDE)
            else:
                return self.getToken(ZmeiLangParser.EXCLUDE, i)

        def field_list_expr_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_list_expr_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_list_expr_fieldContext,i)


        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_list_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list_expr" ):
                listener.enterField_list_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list_expr" ):
                listener.exitField_list_expr(self)




    def field_list_expr(self):

        localctx = ZmeiLangParser.Field_list_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_field_list_expr)
        self._la = 0 # Token type
        try:
            self.state = 699
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DOT, ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 677
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT:
                    self.state = 676
                    self.match(ZmeiLangParser.DOT)


                self.state = 679
                self.match(ZmeiLangParser.STAR)
                self.state = 685
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 680
                        self.match(ZmeiLangParser.COMA)
                        self.state = 681
                        self.match(ZmeiLangParser.EXCLUDE)
                        self.state = 682
                        self.field_list_expr_field() 
                    self.state = 687
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 688
                self.id_or_kw()
                self.state = 696
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 689
                        self.match(ZmeiLangParser.COMA)
                        self.state = 691
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.EXCLUDE:
                            self.state = 690
                            self.match(ZmeiLangParser.EXCLUDE)


                        self.state = 693
                        self.field_list_expr_field() 
                    self.state = 698
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_list_expr_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_list_expr_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_list_expr_field" ):
                listener.enterField_list_expr_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_list_expr_field" ):
                listener.exitField_list_expr_field(self)




    def field_list_expr_field(self):

        localctx = ZmeiLangParser.Field_list_expr_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_field_list_expr_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 702
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 701
                self.match(ZmeiLangParser.STAR)


            self.state = 704
            self.id_or_kw()
            self.state = 706
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STAR:
                self.state = 705
                self.match(ZmeiLangParser.STAR)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_mode_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def WRITE_MODE(self):
            return self.getToken(ZmeiLangParser.WRITE_MODE, 0)

        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_write_mode_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrite_mode_expr" ):
                listener.enterWrite_mode_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrite_mode_expr" ):
                listener.exitWrite_mode_expr(self)




    def write_mode_expr(self):

        localctx = ZmeiLangParser.Write_mode_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_write_mode_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 709
            self.match(ZmeiLangParser.WRITE_MODE)
            self.state = 710
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Python_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_python_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPython_code" ):
                listener.enterPython_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPython_code" ):
                listener.exitPython_code(self)




    def python_code(self):

        localctx = ZmeiLangParser.Python_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_python_code)
        try:
            self.state = 714
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 712
                self.code_block()
                pass
            elif token in [ZmeiLangParser.ASSIGN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
                self.code_line()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_lineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_code_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_line" ):
                listener.enterCode_line(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_line" ):
                listener.exitCode_line(self)




    def code_line(self):

        localctx = ZmeiLangParser.Code_lineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_code_line)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 717
            self.match(ZmeiLangParser.PYTHON_CODE)
            self.state = 718
            self.match(ZmeiLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CODE_BLOCK(self):
            return self.getToken(ZmeiLangParser.CODE_BLOCK, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = ZmeiLangParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.match(ZmeiLangParser.CODE_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cs_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_suit(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_suitContext,0)


        def an_celery(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_celeryContext,0)


        def an_channels(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_channelsContext,0)


        def an_docker(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_dockerContext,0)


        def an_filer(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_filerContext,0)


        def an_gitlab(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlabContext,0)


        def an_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_fileContext,0)


        def an_theme(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_themeContext,0)


        def an_langs(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_langsContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_cs_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCs_annotation" ):
                listener.enterCs_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCs_annotation" ):
                listener.exitCs_annotation(self)




    def cs_annotation(self):

        localctx = ZmeiLangParser.Cs_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_cs_annotation)
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_SUIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 722
                self.an_suit()
                pass
            elif token in [ZmeiLangParser.AN_CELERY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 723
                self.an_celery()
                pass
            elif token in [ZmeiLangParser.AN_CHANNELS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 724
                self.an_channels()
                pass
            elif token in [ZmeiLangParser.AN_DOCKER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 725
                self.an_docker()
                pass
            elif token in [ZmeiLangParser.AN_FILER]:
                self.enterOuterAlt(localctx, 5)
                self.state = 726
                self.an_filer()
                pass
            elif token in [ZmeiLangParser.AN_GITLAB]:
                self.enterOuterAlt(localctx, 6)
                self.state = 727
                self.an_gitlab()
                pass
            elif token in [ZmeiLangParser.AN_FILE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 728
                self.an_file()
                pass
            elif token in [ZmeiLangParser.AN_THEME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 729
                self.an_theme()
                pass
            elif token in [ZmeiLangParser.AN_LANGS]:
                self.enterOuterAlt(localctx, 9)
                self.state = 730
                self.an_langs()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 10)
                self.state = 731
                self.match(ZmeiLangParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_suitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_SUIT(self):
            return self.getToken(ZmeiLangParser.AN_SUIT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_suit_app_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_suit_app_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_suit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_suit" ):
                listener.enterAn_suit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_suit" ):
                listener.exitAn_suit(self)




    def an_suit(self):

        localctx = ZmeiLangParser.An_suitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_an_suit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(ZmeiLangParser.AN_SUIT)
            self.state = 739
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 735
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 736
                self.an_suit_app_name()
                self.state = 737
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_suit_app_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_suit_app_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_suit_app_name" ):
                listener.enterAn_suit_app_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_suit_app_name" ):
                listener.exitAn_suit_app_name(self)




    def an_suit_app_name(self):

        localctx = ZmeiLangParser.An_suit_app_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_an_suit_app_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_celeryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CELERY(self):
            return self.getToken(ZmeiLangParser.AN_CELERY, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_celery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_celery" ):
                listener.enterAn_celery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_celery" ):
                listener.exitAn_celery(self)




    def an_celery(self):

        localctx = ZmeiLangParser.An_celeryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_an_celery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 743
            self.match(ZmeiLangParser.AN_CELERY)
            self.state = 746
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 744
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 745
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_channelsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CHANNELS(self):
            return self.getToken(ZmeiLangParser.AN_CHANNELS, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_channels

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_channels" ):
                listener.enterAn_channels(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_channels" ):
                listener.exitAn_channels(self)




    def an_channels(self):

        localctx = ZmeiLangParser.An_channelsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_an_channels)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 748
            self.match(ZmeiLangParser.AN_CHANNELS)
            self.state = 751
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 749
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 750
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_dockerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_DOCKER(self):
            return self.getToken(ZmeiLangParser.AN_DOCKER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_docker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_docker" ):
                listener.enterAn_docker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_docker" ):
                listener.exitAn_docker(self)




    def an_docker(self):

        localctx = ZmeiLangParser.An_dockerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_an_docker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.match(ZmeiLangParser.AN_DOCKER)
            self.state = 756
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 754
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 755
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_filerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_FILER(self):
            return self.getToken(ZmeiLangParser.AN_FILER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_filer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_filer" ):
                listener.enterAn_filer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_filer" ):
                listener.exitAn_filer(self)




    def an_filer(self):

        localctx = ZmeiLangParser.An_filerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_an_filer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 758
            self.match(ZmeiLangParser.AN_FILER)
            self.state = 761
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 759
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 760
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlabContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_GITLAB(self):
            return self.getToken(ZmeiLangParser.AN_GITLAB, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_declaration(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_declarationContext,0)


        def an_gitlab_branch_declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_branch_declarationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_declarationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab" ):
                listener.enterAn_gitlab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab" ):
                listener.exitAn_gitlab(self)




    def an_gitlab(self):

        localctx = ZmeiLangParser.An_gitlabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_an_gitlab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 763
            self.match(ZmeiLangParser.AN_GITLAB)
            self.state = 764
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 768
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 765
                    self.match(ZmeiLangParser.NL) 
                self.state = 770
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 772
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 771
                self.an_gitlab_test_declaration()


            self.state = 777
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 774
                self.match(ZmeiLangParser.NL)
                self.state = 779
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 781 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 780
                self.an_gitlab_branch_declaration()
                self.state = 783 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
                    break

            self.state = 788
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 785
                self.match(ZmeiLangParser.NL)
                self.state = 790
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 791
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_test_declaration_selenium_pytest(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_declaration" ):
                listener.enterAn_gitlab_test_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_declaration" ):
                listener.exitAn_gitlab_test_declaration(self)




    def an_gitlab_test_declaration(self):

        localctx = ZmeiLangParser.An_gitlab_test_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_an_gitlab_test_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 793
            self.an_gitlab_test_declaration_selenium_pytest()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_declaration_selenium_pytestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SELENIUM_PYTEST(self):
            return self.getToken(ZmeiLangParser.KW_SELENIUM_PYTEST, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_services(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_servicesContext,0)


        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_declaration_selenium_pytest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_declaration_selenium_pytest" ):
                listener.enterAn_gitlab_test_declaration_selenium_pytest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_declaration_selenium_pytest" ):
                listener.exitAn_gitlab_test_declaration_selenium_pytest(self)




    def an_gitlab_test_declaration_selenium_pytest(self):

        localctx = ZmeiLangParser.An_gitlab_test_declaration_selenium_pytestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_an_gitlab_test_declaration_selenium_pytest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
            self.match(ZmeiLangParser.KW_SELENIUM_PYTEST)
            self.state = 796
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 800
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 797
                    self.match(ZmeiLangParser.NL) 
                self.state = 802
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 804
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.state = 803
                self.an_gitlab_test_services()


            self.state = 809
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 806
                    self.match(ZmeiLangParser.NL) 
                self.state = 811
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

            self.state = 818
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 812
                    self.an_gitlab_deployment_variable()
                    self.state = 814
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==ZmeiLangParser.COMA:
                        self.state = 813
                        self.match(ZmeiLangParser.COMA)

             
                self.state = 820
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

            self.state = 824
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 821
                self.match(ZmeiLangParser.NL)
                self.state = 826
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 827
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_servicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SERVICES(self):
            return self.getToken(ZmeiLangParser.KW_SERVICES, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_gitlab_test_service(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_test_serviceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_serviceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_services

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_services" ):
                listener.enterAn_gitlab_test_services(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_services" ):
                listener.exitAn_gitlab_test_services(self)




    def an_gitlab_test_services(self):

        localctx = ZmeiLangParser.An_gitlab_test_servicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_an_gitlab_test_services)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 829
            self.match(ZmeiLangParser.KW_SERVICES)
            self.state = 830
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 834
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 831
                    self.match(ZmeiLangParser.NL) 
                self.state = 836
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

            self.state = 845
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.state = 837
                self.an_gitlab_test_service()
                self.state = 842
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.COMA:
                    self.state = 838
                    self.match(ZmeiLangParser.COMA)
                    self.state = 839
                    self.an_gitlab_test_service()
                    self.state = 844
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 850
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 847
                self.match(ZmeiLangParser.NL)
                self.state = 852
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 853
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_serviceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_test_service_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_test_service_nameContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_service

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_service" ):
                listener.enterAn_gitlab_test_service(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_service" ):
                listener.exitAn_gitlab_test_service(self)




    def an_gitlab_test_service(self):

        localctx = ZmeiLangParser.An_gitlab_test_serviceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_an_gitlab_test_service)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 858
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 855
                self.match(ZmeiLangParser.NL)
                self.state = 860
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 861
            self.an_gitlab_test_service_name()
            self.state = 885
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 862
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 866
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 863
                        self.match(ZmeiLangParser.NL) 
                    self.state = 868
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                self.state = 875
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 869
                        self.an_gitlab_deployment_variable()
                        self.state = 871
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 870
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 877
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

                self.state = 881
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 878
                    self.match(ZmeiLangParser.NL)
                    self.state = 883
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 884
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_test_service_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_test_service_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_test_service_name" ):
                listener.enterAn_gitlab_test_service_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_test_service_name" ):
                listener.exitAn_gitlab_test_service_name(self)




    def an_gitlab_test_service_name(self):

        localctx = ZmeiLangParser.An_gitlab_test_service_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_an_gitlab_test_service_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 887
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_branch_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_nameContext,0)


        def an_gitlab_branch_deploy_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_branch_deploy_typeContext,0)


        def an_gitlab_deployment_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_gitlab_deployment_host(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_hostContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_gitlab_deployment_variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_gitlab_deployment_variableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variableContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_declaration" ):
                listener.enterAn_gitlab_branch_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_declaration" ):
                listener.exitAn_gitlab_branch_declaration(self)




    def an_gitlab_branch_declaration(self):

        localctx = ZmeiLangParser.An_gitlab_branch_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_an_gitlab_branch_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 889
            self.an_gitlab_branch_name()
            self.state = 893
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 890
                self.match(ZmeiLangParser.NL)
                self.state = 895
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 896
            self.an_gitlab_branch_deploy_type()
            self.state = 900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 897
                self.match(ZmeiLangParser.NL)
                self.state = 902
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 903
            self.an_gitlab_deployment_name()
            self.state = 904
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 908
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 905
                self.match(ZmeiLangParser.NL)
                self.state = 910
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 911
            self.an_gitlab_deployment_host()
            self.state = 928
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 912
                self.match(ZmeiLangParser.COLON)
                self.state = 916
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,59,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 913
                        self.match(ZmeiLangParser.NL) 
                    self.state = 918
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,59,self._ctx)

                self.state = 925
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,61,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 919
                        self.an_gitlab_deployment_variable()
                        self.state = 921
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==ZmeiLangParser.COMA:
                            self.state = 920
                            self.match(ZmeiLangParser.COMA)

                 
                    self.state = 927
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,61,self._ctx)



            self.state = 933
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 930
                self.match(ZmeiLangParser.NL)
                self.state = 935
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 936
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 940
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,64,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 937
                    self.match(ZmeiLangParser.NL) 
                self.state = 942
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,64,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_deploy_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_deploy_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_deploy_type" ):
                listener.enterAn_gitlab_branch_deploy_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_deploy_type" ):
                listener.exitAn_gitlab_branch_deploy_type(self)




    def an_gitlab_branch_deploy_type(self):

        localctx = ZmeiLangParser.An_gitlab_branch_deploy_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_an_gitlab_branch_deploy_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 943
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.EQUALS or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 944
            self.match(ZmeiLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_branch_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_branch_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_branch_name" ):
                listener.enterAn_gitlab_branch_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_branch_name" ):
                listener.exitAn_gitlab_branch_name(self)




    def an_gitlab_branch_name(self):

        localctx = ZmeiLangParser.An_gitlab_branch_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_an_gitlab_branch_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 950 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 950
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 946
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 947
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 948
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 949
                    self.match(ZmeiLangParser.SLASH)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 952 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_name" ):
                listener.enterAn_gitlab_deployment_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_name" ):
                listener.exitAn_gitlab_deployment_name(self)




    def an_gitlab_deployment_name(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_an_gitlab_deployment_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 958 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 958
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 954
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 955
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.SLASH]:
                    self.state = 956
                    self.match(ZmeiLangParser.SLASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 957
                    self.match(ZmeiLangParser.STAR)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 960 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.SLASH - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_hostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def STAR(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.STAR)
            else:
                return self.getToken(ZmeiLangParser.STAR, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_host

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_host" ):
                listener.enterAn_gitlab_deployment_host(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_host" ):
                listener.exitAn_gitlab_deployment_host(self)




    def an_gitlab_deployment_host(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_hostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_an_gitlab_deployment_host)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 966 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 966
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 962
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 963
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.STAR]:
                    self.state = 964
                    self.match(ZmeiLangParser.STAR)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 965
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 968 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.DOT - 106)) | (1 << (ZmeiLangParser.STAR - 106)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_gitlab_deployment_variable_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variable_nameContext,0)


        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_gitlab_deployment_variable_value(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_gitlab_deployment_variable_valueContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable" ):
                listener.enterAn_gitlab_deployment_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable" ):
                listener.exitAn_gitlab_deployment_variable(self)




    def an_gitlab_deployment_variable(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_an_gitlab_deployment_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 973
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 970
                self.match(ZmeiLangParser.NL)
                self.state = 975
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 976
            self.an_gitlab_deployment_variable_name()
            self.state = 977
            self.match(ZmeiLangParser.EQUALS)
            self.state = 978
            self.an_gitlab_deployment_variable_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable_name" ):
                listener.enterAn_gitlab_deployment_variable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable_name" ):
                listener.exitAn_gitlab_deployment_variable_name(self)




    def an_gitlab_deployment_variable_name(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_an_gitlab_deployment_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 980
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_gitlab_deployment_variable_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_gitlab_deployment_variable_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_gitlab_deployment_variable_value" ):
                listener.enterAn_gitlab_deployment_variable_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_gitlab_deployment_variable_value" ):
                listener.exitAn_gitlab_deployment_variable_value(self)




    def an_gitlab_deployment_variable_value(self):

        localctx = ZmeiLangParser.An_gitlab_deployment_variable_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_an_gitlab_deployment_variable_value)
        try:
            self.state = 986
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 982
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 983
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.DIGIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 984
                self.match(ZmeiLangParser.DIGIT)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 985
                self.id_or_kw()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_FILE(self):
            return self.getToken(ZmeiLangParser.AN_FILE, 0)

        def an_file_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_file_nameContext,0)


        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_file" ):
                listener.enterAn_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_file" ):
                listener.exitAn_file(self)




    def an_file(self):

        localctx = ZmeiLangParser.An_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_an_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 988
            self.match(ZmeiLangParser.AN_FILE)
            self.state = 989
            self.an_file_name()
            self.state = 990
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_file_name" ):
                listener.enterAn_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_file_name" ):
                listener.exitAn_file_name(self)




    def an_file_name(self):

        localctx = ZmeiLangParser.An_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_an_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 992
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_themeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_THEME(self):
            return self.getToken(ZmeiLangParser.AN_THEME, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_theme_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_theme_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def KW_INSTALL(self):
            return self.getToken(ZmeiLangParser.KW_INSTALL, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_theme_install(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_theme_installContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_theme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme" ):
                listener.enterAn_theme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme" ):
                listener.exitAn_theme(self)




    def an_theme(self):

        localctx = ZmeiLangParser.An_themeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_an_theme)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 994
            self.match(ZmeiLangParser.AN_THEME)
            self.state = 995
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 996
            self.an_theme_name()
            self.state = 1001
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 997
                self.match(ZmeiLangParser.COMA)
                self.state = 998
                self.match(ZmeiLangParser.KW_INSTALL)
                self.state = 999
                self.match(ZmeiLangParser.EQUALS)
                self.state = 1000
                self.an_theme_install()


            self.state = 1003
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_theme_installContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_theme_install

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme_install" ):
                listener.enterAn_theme_install(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme_install" ):
                listener.exitAn_theme_install(self)




    def an_theme_install(self):

        localctx = ZmeiLangParser.An_theme_installContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_an_theme_install)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1005
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_theme_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_theme_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_theme_name" ):
                listener.enterAn_theme_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_theme_name" ):
                listener.exitAn_theme_name(self)




    def an_theme_name(self):

        localctx = ZmeiLangParser.An_theme_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_an_theme_name)
        try:
            self.state = 1010
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1007
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1008
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1009
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_langsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_LANGS(self):
            return self.getToken(ZmeiLangParser.AN_LANGS, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_langs_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_langs_listContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_langs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_langs" ):
                listener.enterAn_langs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_langs" ):
                listener.exitAn_langs(self)




    def an_langs(self):

        localctx = ZmeiLangParser.An_langsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_an_langs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1012
            self.match(ZmeiLangParser.AN_LANGS)
            self.state = 1013
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1014
            self.an_langs_list()
            self.state = 1015
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_langs_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.ID)
            else:
                return self.getToken(ZmeiLangParser.ID, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_langs_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_langs_list" ):
                listener.enterAn_langs_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_langs_list" ):
                listener.exitAn_langs_list(self)




    def an_langs_list(self):

        localctx = ZmeiLangParser.An_langs_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_an_langs_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1017
            self.match(ZmeiLangParser.ID)
            self.state = 1022
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1018
                self.match(ZmeiLangParser.COMA)
                self.state = 1019
                self.match(ZmeiLangParser.ID)
                self.state = 1024
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_header(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_headerContext,0)


        def col_str_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_str_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def col_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Col_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Col_fieldContext,i)


        def model_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Model_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Model_annotationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol" ):
                listener.enterCol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol" ):
                listener.exitCol(self)




    def col(self):

        localctx = ZmeiLangParser.ColContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_col)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.col_header()
            self.state = 1027
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.state = 1026
                self.col_str_expr()


            self.state = 1032
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,77,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1029
                    self.match(ZmeiLangParser.NL) 
                self.state = 1034
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,77,self._ctx)

            self.state = 1038
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.EQUALS - 106)) | (1 << (ZmeiLangParser.DOLLAR - 106)) | (1 << (ZmeiLangParser.AMP - 106)) | (1 << (ZmeiLangParser.EXCLAM - 106)) | (1 << (ZmeiLangParser.STAR - 106)) | (1 << (ZmeiLangParser.APPROX - 106)))) != 0):
                self.state = 1035
                self.col_field()
                self.state = 1040
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1044
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,79,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1041
                    self.match(ZmeiLangParser.NL) 
                self.state = 1046
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,79,self._ctx)

            self.state = 1050
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,80,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1047
                    self.model_annotation() 
                self.state = 1052
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,80,self._ctx)

            self.state = 1056
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,81,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1053
                    self.match(ZmeiLangParser.NL) 
                self.state = 1058
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,81,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_str_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_str_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_str_expr" ):
                listener.enterCol_str_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_str_expr" ):
                listener.exitCol_str_expr(self)




    def col_str_expr(self):

        localctx = ZmeiLangParser.Col_str_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_col_str_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1059
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1060
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1067
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1062 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1061
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1064 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1066
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HASH(self):
            return self.getToken(ZmeiLangParser.HASH, 0)

        def col_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_nameContext,0)


        def col_header_line_separator(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_header_line_separatorContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def col_base_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_base_nameContext,0)


        def col_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_verbose_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_header" ):
                listener.enterCol_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_header" ):
                listener.exitCol_header(self)




    def col_header(self):

        localctx = ZmeiLangParser.Col_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_col_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1069
            self.match(ZmeiLangParser.HASH)
            self.state = 1071
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,84,self._ctx)
            if la_ == 1:
                self.state = 1070
                self.col_base_name()


            self.state = 1073
            self.col_name()
            self.state = 1075
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1074
                self.col_verbose_name()


            self.state = 1077
            self.col_header_line_separator()
            self.state = 1078
            self.match(ZmeiLangParser.NL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_header_line_separatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_header_line_separator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_header_line_separator" ):
                listener.enterCol_header_line_separator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_header_line_separator" ):
                listener.exitCol_header_line_separator(self)




    def col_header_line_separator(self):

        localctx = ZmeiLangParser.Col_header_line_separatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_col_header_line_separator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1080
            self.match(ZmeiLangParser.NL)
            self.state = 1081
            self.match(ZmeiLangParser.DASH)
            self.state = 1082
            self.match(ZmeiLangParser.DASH)
            self.state = 1084 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1083
                self.match(ZmeiLangParser.DASH)
                self.state = 1086 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ZmeiLangParser.DASH):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def verbose_name_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Verbose_name_partContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Verbose_name_partContext,i)


        def SLASH(self):
            return self.getToken(ZmeiLangParser.SLASH, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_verbose_name" ):
                listener.enterCol_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_verbose_name" ):
                listener.exitCol_verbose_name(self)




    def col_verbose_name(self):

        localctx = ZmeiLangParser.Col_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_col_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1088
            self.match(ZmeiLangParser.COLON)
            self.state = 1089
            self.verbose_name_part()
            self.state = 1092
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1090
                self.match(ZmeiLangParser.SLASH)
                self.state = 1091
                self.verbose_name_part()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Verbose_name_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_verbose_name_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVerbose_name_part" ):
                listener.enterVerbose_name_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVerbose_name_part" ):
                listener.exitVerbose_name_part(self)




    def verbose_name_part(self):

        localctx = ZmeiLangParser.Verbose_name_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_verbose_name_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1097
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1094
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1095
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1096
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_base_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_base_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_base_name" ):
                listener.enterCol_base_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_base_name" ):
                listener.exitCol_base_name(self)




    def col_base_name(self):

        localctx = ZmeiLangParser.Col_base_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_col_base_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1099
            self.id_or_kw()
            self.state = 1104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.DASH]:
                self.state = 1100
                self.match(ZmeiLangParser.DASH)
                self.state = 1101
                self.match(ZmeiLangParser.GT)
                pass
            elif token in [ZmeiLangParser.APPROX]:
                self.state = 1102
                self.match(ZmeiLangParser.APPROX)
                self.state = 1103
                self.match(ZmeiLangParser.GT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_name" ):
                listener.enterCol_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_name" ):
                listener.exitCol_name(self)




    def col_name(self):

        localctx = ZmeiLangParser.Col_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_col_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1106
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_nameContext,0)


        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def col_modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Col_modifierContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Col_modifierContext,i)


        def col_field_expr_or_def(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_expr_or_defContext,0)


        def col_field_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_verbose_nameContext,0)


        def col_field_help_text(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_help_textContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field" ):
                listener.enterCol_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field" ):
                listener.exitCol_field(self)




    def col_field(self):

        localctx = ZmeiLangParser.Col_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_col_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (ZmeiLangParser.EQUALS - 137)) | (1 << (ZmeiLangParser.DOLLAR - 137)) | (1 << (ZmeiLangParser.AMP - 137)) | (1 << (ZmeiLangParser.EXCLAM - 137)) | (1 << (ZmeiLangParser.STAR - 137)) | (1 << (ZmeiLangParser.APPROX - 137)))) != 0):
                self.state = 1108
                self.col_modifier()
                self.state = 1113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1114
            self.col_field_name()
            self.state = 1116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 124)) & ~0x3f) == 0 and ((1 << (_la - 124)) & ((1 << (ZmeiLangParser.COLON - 124)) | (1 << (ZmeiLangParser.ASSIGN - 124)) | (1 << (ZmeiLangParser.ASSIGN_STATIC - 124)))) != 0):
                self.state = 1115
                self.col_field_expr_or_def()


            self.state = 1119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SLASH:
                self.state = 1118
                self.col_field_verbose_name()


            self.state = 1122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.QUESTION_MARK:
                self.state = 1121
                self.col_field_help_text()


            self.state = 1130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1125 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1124
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1127 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,94,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1129
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_expr_or_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_exprContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def col_field_def(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_defContext,0)


        def wrong_field_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Wrong_field_typeContext,0)


        def col_field_custom(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_customContext,0)


        def col_field_extend(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_extendContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr_or_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr_or_def" ):
                listener.enterCol_field_expr_or_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr_or_def" ):
                listener.exitCol_field_expr_or_def(self)




    def col_field_expr_or_def(self):

        localctx = ZmeiLangParser.Col_field_expr_or_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_col_field_expr_or_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.state = 1132
                self.match(ZmeiLangParser.COLON)
                self.state = 1134
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1133
                    self.col_field_custom()


                pass

            elif la_ == 2:
                self.state = 1136
                self.match(ZmeiLangParser.COLON)
                self.state = 1137
                self.col_field_def()
                self.state = 1139
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.CODE_BLOCK:
                    self.state = 1138
                    self.col_field_extend()


                pass

            elif la_ == 3:
                self.state = 1141
                self.match(ZmeiLangParser.COLON)
                self.state = 1142
                self.wrong_field_type()
                pass

            elif la_ == 4:
                self.state = 1143
                self.col_field_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_customContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_custom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_custom" ):
                listener.enterCol_field_custom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_custom" ):
                listener.exitCol_field_custom(self)




    def col_field_custom(self):

        localctx = ZmeiLangParser.Col_field_customContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_col_field_custom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1146
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_extendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def col_field_extend_append(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_extend_appendContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_extend

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_extend" ):
                listener.enterCol_field_extend(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_extend" ):
                listener.exitCol_field_extend(self)




    def col_field_extend(self):

        localctx = ZmeiLangParser.Col_field_extendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_col_field_extend)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1148
                self.col_field_extend_append()


            self.state = 1151
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_extend_appendContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_extend_append

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_extend_append" ):
                listener.enterCol_field_extend_append(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_extend_append" ):
                listener.exitCol_field_extend_append(self)




    def col_field_extend_append(self):

        localctx = ZmeiLangParser.Col_field_extend_appendContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_col_field_extend_append)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1153
            self.match(ZmeiLangParser.DOT)
            self.state = 1154
            self.match(ZmeiLangParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Wrong_field_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_wrong_field_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWrong_field_type" ):
                listener.enterWrong_field_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWrong_field_type" ):
                listener.exitWrong_field_type(self)




    def wrong_field_type(self):

        localctx = ZmeiLangParser.Wrong_field_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_wrong_field_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1156
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_field_expr_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_field_expr_markerContext,0)


        def col_feild_expr_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Col_feild_expr_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr" ):
                listener.enterCol_field_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr" ):
                listener.exitCol_field_expr(self)




    def col_field_expr(self):

        localctx = ZmeiLangParser.Col_field_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_col_field_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1158
            self.col_field_expr_marker()
            self.state = 1159
            self.col_feild_expr_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_expr_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def ASSIGN_STATIC(self):
            return self.getToken(ZmeiLangParser.ASSIGN_STATIC, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_expr_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_expr_marker" ):
                listener.enterCol_field_expr_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_expr_marker" ):
                listener.exitCol_field_expr_marker(self)




    def col_field_expr_marker(self):

        localctx = ZmeiLangParser.Col_field_expr_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_col_field_expr_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1161
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.ASSIGN_STATIC):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_feild_expr_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_feild_expr_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_feild_expr_code" ):
                listener.enterCol_feild_expr_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_feild_expr_code" ):
                listener.exitCol_feild_expr_code(self)




    def col_feild_expr_code(self):

        localctx = ZmeiLangParser.Col_feild_expr_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_col_feild_expr_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1163
            self.match(ZmeiLangParser.PYTHON_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_or_quotedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_string_or_quoted

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_or_quoted" ):
                listener.enterString_or_quoted(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_or_quoted" ):
                listener.exitString_or_quoted(self)




    def string_or_quoted(self):

        localctx = ZmeiLangParser.String_or_quotedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_string_or_quoted)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1166 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 1165
                    self.id_or_kw()
                    self.state = 1168 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN) | (1 << ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML) | (1 << ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FLOAT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DECIMAL) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_DATETIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME) | (1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER) | (1 << ZmeiLangParser.COL_FIELD_TYPE_TEXT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_INT) | (1 << ZmeiLangParser.COL_FIELD_TYPE_SLUG) | (1 << ZmeiLangParser.COL_FIELD_TYPE_BOOL))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 64)) | (1 << (ZmeiLangParser.KW_THEME - 64)) | (1 << (ZmeiLangParser.KW_INSTALL - 64)) | (1 << (ZmeiLangParser.KW_HEADER - 64)) | (1 << (ZmeiLangParser.KW_SERVICES - 64)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 64)) | (1 << (ZmeiLangParser.KW_CHILD - 64)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 64)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 64)) | (1 << (ZmeiLangParser.KW_PAGE - 64)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 64)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 64)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 64)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 64)) | (1 << (ZmeiLangParser.KW_BLOCK - 64)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 64)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 64)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_DELETE - 64)) | (1 << (ZmeiLangParser.KW_EDIT - 64)) | (1 << (ZmeiLangParser.KW_CREATE - 64)) | (1 << (ZmeiLangParser.KW_DETAIL - 64)) | (1 << (ZmeiLangParser.KW_SKIP - 64)) | (1 << (ZmeiLangParser.KW_FROM - 64)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 64)) | (1 << (ZmeiLangParser.KW_CSS - 64)) | (1 << (ZmeiLangParser.KW_JS - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 64)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 64)) | (1 << (ZmeiLangParser.KW_INLINE - 64)) | (1 << (ZmeiLangParser.KW_TYPE - 64)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 64)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 64)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 64)) | (1 << (ZmeiLangParser.KW_QUERY - 64)) | (1 << (ZmeiLangParser.KW_AUTH - 64)) | (1 << (ZmeiLangParser.KW_COUNT - 64)) | (1 << (ZmeiLangParser.KW_I18N - 64)) | (1 << (ZmeiLangParser.KW_EXTENSION - 64)) | (1 << (ZmeiLangParser.KW_TABS - 64)) | (1 << (ZmeiLangParser.KW_LIST - 64)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 64)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 64)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 64)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 64)) | (1 << (ZmeiLangParser.KW_FIELDS - 64)) | (1 << (ZmeiLangParser.KW_IMPORT - 64)) | (1 << (ZmeiLangParser.KW_AS - 64)) | (1 << (ZmeiLangParser.WRITE_MODE - 64)) | (1 << (ZmeiLangParser.BOOL - 64)) | (1 << (ZmeiLangParser.ID - 64)))) != 0)):
                        break

                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1170
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1171
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_help_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION_MARK(self):
            return self.getToken(ZmeiLangParser.QUESTION_MARK, 0)

        def string_or_quoted(self):
            return self.getTypedRuleContext(ZmeiLangParser.String_or_quotedContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_help_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_help_text" ):
                listener.enterCol_field_help_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_help_text" ):
                listener.exitCol_field_help_text(self)




    def col_field_help_text(self):

        localctx = ZmeiLangParser.Col_field_help_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_col_field_help_text)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1174
            self.match(ZmeiLangParser.QUESTION_MARK)
            self.state = 1175
            self.string_or_quoted()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self):
            return self.getToken(ZmeiLangParser.SLASH, 0)

        def string_or_quoted(self):
            return self.getTypedRuleContext(ZmeiLangParser.String_or_quotedContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_verbose_name" ):
                listener.enterCol_field_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_verbose_name" ):
                listener.exitCol_field_verbose_name(self)




    def col_field_verbose_name(self):

        localctx = ZmeiLangParser.Col_field_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_col_field_verbose_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1177
            self.match(ZmeiLangParser.SLASH)
            self.state = 1178
            self.string_or_quoted()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_name" ):
                listener.enterCol_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_name" ):
                listener.exitCol_field_name(self)




    def col_field_name(self):

        localctx = ZmeiLangParser.Col_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_col_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1180
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_modifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def DOLLAR(self):
            return self.getToken(ZmeiLangParser.DOLLAR, 0)

        def AMP(self):
            return self.getToken(ZmeiLangParser.AMP, 0)

        def EXCLAM(self):
            return self.getToken(ZmeiLangParser.EXCLAM, 0)

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_modifier" ):
                listener.enterCol_modifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_modifier" ):
                listener.exitCol_modifier(self)




    def col_modifier(self):

        localctx = ZmeiLangParser.Col_modifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_col_modifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1182
            _la = self._input.LA(1)
            if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (ZmeiLangParser.EQUALS - 137)) | (1 << (ZmeiLangParser.DOLLAR - 137)) | (1 << (ZmeiLangParser.AMP - 137)) | (1 << (ZmeiLangParser.EXCLAM - 137)) | (1 << (ZmeiLangParser.STAR - 137)) | (1 << (ZmeiLangParser.APPROX - 137)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Col_field_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_longtext(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_longtextContext,0)


        def field_html_media(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_html_mediaContext,0)


        def field_html(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_htmlContext,0)


        def field_float(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_floatContext,0)


        def field_decimal(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_decimalContext,0)


        def field_date(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_dateContext,0)


        def field_datetime(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_datetimeContext,0)


        def field_create_time(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_create_timeContext,0)


        def field_update_time(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_update_timeContext,0)


        def field_text(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_textContext,0)


        def field_int(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_intContext,0)


        def field_slug(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_slugContext,0)


        def field_bool(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_boolContext,0)


        def field_relation(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relationContext,0)


        def field_image(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_imageContext,0)


        def field_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_fileContext,0)


        def field_filer_file(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_fileContext,0)


        def field_filer_folder(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_filer_folderContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_col_field_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCol_field_def" ):
                listener.enterCol_field_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCol_field_def" ):
                listener.exitCol_field_def(self)




    def col_field_def(self):

        localctx = ZmeiLangParser.Col_field_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_col_field_def)
        try:
            self.state = 1202
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1184
                self.field_longtext()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1185
                self.field_html_media()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1186
                self.field_html()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FLOAT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1187
                self.field_float()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DECIMAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1188
                self.field_decimal()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1189
                self.field_date()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_DATETIME]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1190
                self.field_datetime()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1191
                self.field_create_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1192
                self.field_update_time()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_TEXT]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1193
                self.field_text()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_INT]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1194
                self.field_int()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_SLUG]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1195
                self.field_slug()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_BOOL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1196
                self.field_bool()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1197
                self.field_relation()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1198
                self.field_image()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILE]:
                self.enterOuterAlt(localctx, 16)
                self.state = 1199
                self.field_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE]:
                self.enterOuterAlt(localctx, 17)
                self.state = 1200
                self.field_filer_file()
                pass
            elif token in [ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER]:
                self.enterOuterAlt(localctx, 18)
                self.state = 1201
                self.field_filer_folder()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_longtextContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_LONGTEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_longtext

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_longtext" ):
                listener.enterField_longtext(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_longtext" ):
                listener.exitField_longtext(self)




    def field_longtext(self):

        localctx = ZmeiLangParser.Field_longtextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_field_longtext)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1204
            self.match(ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_htmlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_HTML(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_html

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_html" ):
                listener.enterField_html(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_html" ):
                listener.exitField_html(self)




    def field_html(self):

        localctx = ZmeiLangParser.Field_htmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_field_html)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1206
            self.match(ZmeiLangParser.COL_FIELD_TYPE_HTML)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_html_mediaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_HTML_MEDIA(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_html_media

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_html_media" ):
                listener.enterField_html_media(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_html_media" ):
                listener.exitField_html_media(self)




    def field_html_media(self):

        localctx = ZmeiLangParser.Field_html_mediaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_field_html_media)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1208
            self.match(ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FLOAT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FLOAT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_float" ):
                listener.enterField_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_float" ):
                listener.exitField_float(self)




    def field_float(self):

        localctx = ZmeiLangParser.Field_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_field_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1210
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_decimalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DECIMAL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_decimal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_decimal" ):
                listener.enterField_decimal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_decimal" ):
                listener.exitField_decimal(self)




    def field_decimal(self):

        localctx = ZmeiLangParser.Field_decimalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_field_decimal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1212
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DECIMAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_dateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DATE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_date

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_date" ):
                listener.enterField_date(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_date" ):
                listener.exitField_date(self)




    def field_date(self):

        localctx = ZmeiLangParser.Field_dateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_field_date)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1214
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_datetimeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_DATETIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_DATETIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_datetime

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_datetime" ):
                listener.enterField_datetime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_datetime" ):
                listener.exitField_datetime(self)




    def field_datetime(self):

        localctx = ZmeiLangParser.Field_datetimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_field_datetime)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1216
            self.match(ZmeiLangParser.COL_FIELD_TYPE_DATETIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_create_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_CREATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_create_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_create_time" ):
                listener.enterField_create_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_create_time" ):
                listener.exitField_create_time(self)




    def field_create_time(self):

        localctx = ZmeiLangParser.Field_create_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_field_create_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1218
            self.match(ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_update_timeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_UPDATE_TIME(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_update_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_update_time" ):
                listener.enterField_update_time(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_update_time" ):
                listener.exitField_update_time(self)




    def field_update_time(self):

        localctx = ZmeiLangParser.Field_update_timeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_field_update_time)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1220
            self.match(ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_file" ):
                listener.enterField_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_file" ):
                listener.exitField_file(self)




    def field_file(self):

        localctx = ZmeiLangParser.Field_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_field_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1222
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_filer_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILER_FILE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_filer_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_filer_file" ):
                listener.enterField_filer_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_filer_file" ):
                listener.exitField_filer_file(self)




    def field_filer_file(self):

        localctx = ZmeiLangParser.Field_filer_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_field_filer_file)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1224
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_filer_folderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_FILER_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_filer_folder

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_filer_folder" ):
                listener.enterField_filer_folder(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_filer_folder" ):
                listener.exitField_filer_folder(self)




    def field_filer_folder(self):

        localctx = ZmeiLangParser.Field_filer_folderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_field_filer_folder)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
            self.match(ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_textContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_TEXT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_TEXT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_text_size(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_sizeContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def field_text_choices(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choicesContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text" ):
                listener.enterField_text(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text" ):
                listener.exitField_text(self)




    def field_text(self):

        localctx = ZmeiLangParser.Field_textContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_field_text)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1228
            self.match(ZmeiLangParser.COL_FIELD_TYPE_TEXT)
            self.state = 1237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1229
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1230
                self.field_text_size()
                self.state = 1233
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COMA:
                    self.state = 1231
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1232
                    self.field_text_choices()


                self.state = 1235
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_text_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def QUESTION_MARK(self):
            return self.getToken(ZmeiLangParser.QUESTION_MARK, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_size" ):
                listener.enterField_text_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_size" ):
                listener.exitField_text_size(self)




    def field_text_size(self):

        localctx = ZmeiLangParser.Field_text_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_field_text_size)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1239
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DIGIT or _la==ZmeiLangParser.QUESTION_MARK):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_text_choicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def field_text_choice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_text_choiceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_text_choiceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choices" ):
                listener.enterField_text_choices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choices" ):
                listener.exitField_text_choices(self)




    def field_text_choices(self):

        localctx = ZmeiLangParser.Field_text_choicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_field_text_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1241
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1242
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1243
            self.field_text_choice()
            self.state = 1248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1244
                self.match(ZmeiLangParser.COMA)
                self.state = 1245
                self.field_text_choice()
                self.state = 1250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_text_choiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_text_choice_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choice_valContext,0)


        def field_text_choice_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_text_choice_keyContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice" ):
                listener.enterField_text_choice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice" ):
                listener.exitField_text_choice(self)




    def field_text_choice(self):

        localctx = ZmeiLangParser.Field_text_choiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_field_text_choice)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,106,self._ctx)
            if la_ == 1:
                self.state = 1251
                self.field_text_choice_key()


            self.state = 1254
            self.field_text_choice_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_text_choice_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice_val" ):
                listener.enterField_text_choice_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice_val" ):
                listener.exitField_text_choice_val(self)




    def field_text_choice_val(self):

        localctx = ZmeiLangParser.Field_text_choice_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_field_text_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1259
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1256
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1257
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1258
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_text_choice_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_text_choice_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_text_choice_key" ):
                listener.enterField_text_choice_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_text_choice_key" ):
                listener.exitField_text_choice_key(self)




    def field_text_choice_key(self):

        localctx = ZmeiLangParser.Field_text_choice_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_field_text_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1261
            self.id_or_kw()
            self.state = 1262
            self.match(ZmeiLangParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_INT(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_INT, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_int_choices(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choicesContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int" ):
                listener.enterField_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int" ):
                listener.exitField_int(self)




    def field_int(self):

        localctx = ZmeiLangParser.Field_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_field_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1264
            self.match(ZmeiLangParser.COL_FIELD_TYPE_INT)
            self.state = 1269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1265
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1266
                self.field_int_choices()
                self.state = 1267
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_int_choicesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_CHOICES(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_CHOICES, 0)

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def field_int_choice(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_int_choiceContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_int_choiceContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choices" ):
                listener.enterField_int_choices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choices" ):
                listener.exitField_int_choices(self)




    def field_int_choices(self):

        localctx = ZmeiLangParser.Field_int_choicesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_field_int_choices)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1271
            self.match(ZmeiLangParser.COL_FIELD_CHOICES)
            self.state = 1272
            self.match(ZmeiLangParser.EQUALS)
            self.state = 1273
            self.field_int_choice()
            self.state = 1278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1274
                self.match(ZmeiLangParser.COMA)
                self.state = 1275
                self.field_int_choice()
                self.state = 1280
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_int_choiceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_int_choice_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choice_valContext,0)


        def field_int_choice_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_int_choice_keyContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice" ):
                listener.enterField_int_choice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice" ):
                listener.exitField_int_choice(self)




    def field_int_choice(self):

        localctx = ZmeiLangParser.Field_int_choiceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_field_int_choice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DIGIT:
                self.state = 1281
                self.field_int_choice_key()


            self.state = 1284
            self.field_int_choice_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_int_choice_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice_val" ):
                listener.enterField_int_choice_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice_val" ):
                listener.exitField_int_choice_val(self)




    def field_int_choice_val(self):

        localctx = ZmeiLangParser.Field_int_choice_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_field_int_choice_val)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1289
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1286
                self.id_or_kw()
                pass
            elif token in [ZmeiLangParser.STRING_DQ]:
                self.state = 1287
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.state = 1288
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_int_choice_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_int_choice_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_int_choice_key" ):
                listener.enterField_int_choice_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_int_choice_key" ):
                listener.exitField_int_choice_key(self)




    def field_int_choice_key(self):

        localctx = ZmeiLangParser.Field_int_choice_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_field_int_choice_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1291
            self.match(ZmeiLangParser.DIGIT)
            self.state = 1292
            self.match(ZmeiLangParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_slugContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_SLUG(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_SLUG, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_slug_ref_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_slug_ref_fieldContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug" ):
                listener.enterField_slug(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug" ):
                listener.exitField_slug(self)




    def field_slug(self):

        localctx = ZmeiLangParser.Field_slugContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_field_slug)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1294
            self.match(ZmeiLangParser.COL_FIELD_TYPE_SLUG)
            self.state = 1295
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1296
            self.field_slug_ref_field()
            self.state = 1297
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_slug_ref_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_slug_ref_field_id(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_slug_ref_field_idContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_slug_ref_field_idContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug_ref_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug_ref_field" ):
                listener.enterField_slug_ref_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug_ref_field" ):
                listener.exitField_slug_ref_field(self)




    def field_slug_ref_field(self):

        localctx = ZmeiLangParser.Field_slug_ref_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_field_slug_ref_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1299
            self.field_slug_ref_field_id()
            self.state = 1304
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1300
                self.match(ZmeiLangParser.COMA)
                self.state = 1301
                self.field_slug_ref_field_id()
                self.state = 1306
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_slug_ref_field_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_slug_ref_field_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_slug_ref_field_id" ):
                listener.enterField_slug_ref_field_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_slug_ref_field_id" ):
                listener.exitField_slug_ref_field_id(self)




    def field_slug_ref_field_id(self):

        localctx = ZmeiLangParser.Field_slug_ref_field_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_field_slug_ref_field_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1307
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_boolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_BOOL(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_BOOL, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_bool_default(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_bool_defaultContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_bool

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_bool" ):
                listener.enterField_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_bool" ):
                listener.exitField_bool(self)




    def field_bool(self):

        localctx = ZmeiLangParser.Field_boolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_field_bool)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1309
            self.match(ZmeiLangParser.COL_FIELD_TYPE_BOOL)
            self.state = 1314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1310
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1311
                self.field_bool_default()
                self.state = 1312
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_bool_defaultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_bool_default

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_bool_default" ):
                listener.enterField_bool_default(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_bool_default" ):
                listener.exitField_bool_default(self)




    def field_bool_default(self):

        localctx = ZmeiLangParser.Field_bool_defaultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_field_bool_default)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1316
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_imageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def filer_image_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Filer_image_typeContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_image_sizes(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_sizesContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image" ):
                listener.enterField_image(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image" ):
                listener.exitField_image(self)




    def field_image(self):

        localctx = ZmeiLangParser.Field_imageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_field_image)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1318
            self.filer_image_type()
            self.state = 1323
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1319
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1320
                self.field_image_sizes()
                self.state = 1321
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Filer_image_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, 0)

        def COL_FIELD_TYPE_FILER_IMAGE_FOLDER(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_filer_image_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFiler_image_type" ):
                listener.enterFiler_image_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFiler_image_type" ):
                listener.exitFiler_image_type(self)




    def filer_image_type(self):

        localctx = ZmeiLangParser.Filer_image_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_filer_image_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1325
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.COL_FIELD_TYPE_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE) | (1 << ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_sizesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_image_sizeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_image_sizeContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_sizes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_sizes" ):
                listener.enterField_image_sizes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_sizes" ):
                listener.exitField_image_sizes(self)




    def field_image_sizes(self):

        localctx = ZmeiLangParser.Field_image_sizesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_field_image_sizes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1327
            self.field_image_size()
            self.state = 1332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1328
                self.match(ZmeiLangParser.COMA)
                self.state = 1329
                self.field_image_size()
                self.state = 1334
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_size_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_size_nameContext,0)


        def field_image_size_dimensions(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_size_dimensionsContext,0)


        def field_image_filters(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_image_filtersContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size" ):
                listener.enterField_image_size(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size" ):
                listener.exitField_image_size(self)




    def field_image_size(self):

        localctx = ZmeiLangParser.Field_image_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_field_image_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1335
            self.field_image_size_name()
            self.state = 1336
            self.field_image_size_dimensions()
            self.state = 1337
            self.field_image_filters()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_size_dimensionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIZE2D(self):
            return self.getToken(ZmeiLangParser.SIZE2D, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size_dimensions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size_dimensions" ):
                listener.enterField_image_size_dimensions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size_dimensions" ):
                listener.exitField_image_size_dimensions(self)




    def field_image_size_dimensions(self):

        localctx = ZmeiLangParser.Field_image_size_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_field_image_size_dimensions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1339
            self.match(ZmeiLangParser.SIZE2D)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_size_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_size_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_size_name" ):
                listener.enterField_image_size_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_size_name" ):
                listener.exitField_image_size_name(self)




    def field_image_size_name(self):

        localctx = ZmeiLangParser.Field_image_size_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_field_image_size_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1341
            self.id_or_kw()
            self.state = 1342
            self.match(ZmeiLangParser.EQUALS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_filtersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_image_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Field_image_filterContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Field_image_filterContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_filters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_filters" ):
                listener.enterField_image_filters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_filters" ):
                listener.exitField_image_filters(self)




    def field_image_filters(self):

        localctx = ZmeiLangParser.Field_image_filtersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_field_image_filters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.PIPE:
                self.state = 1344
                self.field_image_filter()
                self.state = 1349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_image_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIPE(self):
            return self.getToken(ZmeiLangParser.PIPE, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_image_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_image_filter" ):
                listener.enterField_image_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_image_filter" ):
                listener.exitField_image_filter(self)




    def field_image_filter(self):

        localctx = ZmeiLangParser.Field_image_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_field_image_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1350
            self.match(ZmeiLangParser.PIPE)
            self.state = 1351
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field_relation_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_typeContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def field_relation_target_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_target_refContext,0)


        def field_relation_target_class(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_target_classContext,0)


        def field_relation_cascade_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_cascade_markerContext,0)


        def field_relation_related_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_relation_related_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation" ):
                listener.enterField_relation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation" ):
                listener.exitField_relation(self)




    def field_relation(self):

        localctx = ZmeiLangParser.Field_relationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_field_relation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1353
            self.field_relation_type()
            self.state = 1354
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EXCLAM or _la==ZmeiLangParser.APPROX:
                self.state = 1355
                self.field_relation_cascade_marker()


            self.state = 1360
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.state = 1358
                self.field_relation_target_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1359
                self.field_relation_target_class()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 1363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DASH:
                self.state = 1362
                self.field_relation_related_name()


            self.state = 1365
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relation_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COL_FIELD_TYPE_ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE, 0)

        def COL_FIELD_TYPE_ONE2ONE(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, 0)

        def COL_FIELD_TYPE_MANY(self):
            return self.getToken(ZmeiLangParser.COL_FIELD_TYPE_MANY, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_type" ):
                listener.enterField_relation_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_type" ):
                listener.exitField_relation_type(self)




    def field_relation_type(self):

        localctx = ZmeiLangParser.Field_relation_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_field_relation_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1367
            _la = self._input.LA(1)
            if not(((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 64)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 64)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relation_cascade_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def EXCLAM(self):
            return self.getToken(ZmeiLangParser.EXCLAM, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_cascade_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_cascade_marker" ):
                listener.enterField_relation_cascade_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_cascade_marker" ):
                listener.exitField_relation_cascade_marker(self)




    def field_relation_cascade_marker(self):

        localctx = ZmeiLangParser.Field_relation_cascade_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_field_relation_cascade_marker)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1369
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.EXCLAM or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relation_target_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_target_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_target_ref" ):
                listener.enterField_relation_target_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_target_ref" ):
                listener.exitField_relation_target_ref(self)




    def field_relation_target_ref(self):

        localctx = ZmeiLangParser.Field_relation_target_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_field_relation_target_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1371
            self.model_ref()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relation_target_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_target_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_target_class" ):
                listener.enterField_relation_target_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_target_class" ):
                listener.exitField_relation_target_class(self)




    def field_relation_target_class(self):

        localctx = ZmeiLangParser.Field_relation_target_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_field_relation_target_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1373
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Field_relation_related_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_field_relation_related_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterField_relation_related_name" ):
                listener.enterField_relation_related_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitField_relation_related_name" ):
                listener.exitField_relation_related_name(self)




    def field_relation_related_name(self):

        localctx = ZmeiLangParser.Field_relation_related_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_field_relation_related_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1375
            self.match(ZmeiLangParser.DASH)
            self.state = 1376
            self.match(ZmeiLangParser.GT)
            self.state = 1377
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Model_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_admin(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_adminContext,0)


        def an_api(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_apiContext,0)


        def an_rest(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_restContext,0)


        def an_order(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_orderContext,0)


        def an_clean(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_cleanContext,0)


        def an_pre_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_deleteContext,0)


        def an_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_treeContext,0)


        def an_mixin(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_mixinContext,0)


        def an_date_tree(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_date_treeContext,0)


        def an_m2m_changed(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_m2m_changedContext,0)


        def an_post_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_saveContext,0)


        def an_pre_save(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_pre_saveContext,0)


        def an_post_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_post_deleteContext,0)


        def an_sortable(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_sortableContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_model_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel_annotation" ):
                listener.enterModel_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel_annotation" ):
                listener.exitModel_annotation(self)




    def model_annotation(self):

        localctx = ZmeiLangParser.Model_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_model_annotation)
        try:
            self.state = 1394
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_ADMIN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1379
                self.an_admin()
                pass
            elif token in [ZmeiLangParser.AN_API]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1380
                self.an_api()
                pass
            elif token in [ZmeiLangParser.AN_REST]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1381
                self.an_rest()
                pass
            elif token in [ZmeiLangParser.AN_ORDER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1382
                self.an_order()
                pass
            elif token in [ZmeiLangParser.AN_CLEAN]:
                self.enterOuterAlt(localctx, 5)
                self.state = 1383
                self.an_clean()
                pass
            elif token in [ZmeiLangParser.AN_PRE_DELETE]:
                self.enterOuterAlt(localctx, 6)
                self.state = 1384
                self.an_pre_delete()
                pass
            elif token in [ZmeiLangParser.AN_TREE]:
                self.enterOuterAlt(localctx, 7)
                self.state = 1385
                self.an_tree()
                pass
            elif token in [ZmeiLangParser.AN_MIXIN]:
                self.enterOuterAlt(localctx, 8)
                self.state = 1386
                self.an_mixin()
                pass
            elif token in [ZmeiLangParser.AN_DATE_TREE]:
                self.enterOuterAlt(localctx, 9)
                self.state = 1387
                self.an_date_tree()
                pass
            elif token in [ZmeiLangParser.AN_M2M_CHANGED]:
                self.enterOuterAlt(localctx, 10)
                self.state = 1388
                self.an_m2m_changed()
                pass
            elif token in [ZmeiLangParser.AN_POST_SAVE]:
                self.enterOuterAlt(localctx, 11)
                self.state = 1389
                self.an_post_save()
                pass
            elif token in [ZmeiLangParser.AN_PRE_SAVE]:
                self.enterOuterAlt(localctx, 12)
                self.state = 1390
                self.an_pre_save()
                pass
            elif token in [ZmeiLangParser.AN_POST_DELETE]:
                self.enterOuterAlt(localctx, 13)
                self.state = 1391
                self.an_post_delete()
                pass
            elif token in [ZmeiLangParser.AN_SORTABLE]:
                self.enterOuterAlt(localctx, 14)
                self.state = 1392
                self.an_sortable()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 15)
                self.state = 1393
                self.match(ZmeiLangParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_adminContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ADMIN(self):
            return self.getToken(ZmeiLangParser.AN_ADMIN, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_admin_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_listContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_listContext,i)


        def an_admin_read_only(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_read_onlyContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_read_onlyContext,i)


        def an_admin_list_editable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_editableContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_editableContext,i)


        def an_admin_list_filter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_filterContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_filterContext,i)


        def an_admin_list_search(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_list_searchContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_list_searchContext,i)


        def an_admin_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_fieldsContext,i)


        def an_admin_tabs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_tabsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_tabsContext,i)


        def an_admin_inlines(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_inlinesContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_inlinesContext,i)


        def an_admin_css(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_cssContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_cssContext,i)


        def an_admin_js(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_jsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_jsContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin" ):
                listener.enterAn_admin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin" ):
                listener.exitAn_admin(self)




    def an_admin(self):

        localctx = ZmeiLangParser.An_adminContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_an_admin)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1396
            self.match(ZmeiLangParser.AN_ADMIN)
            self.state = 1422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1397
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,122,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 1410
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [ZmeiLangParser.KW_LIST]:
                            self.state = 1398
                            self.an_admin_list()
                            pass
                        elif token in [ZmeiLangParser.KW_READ_ONLY]:
                            self.state = 1399
                            self.an_admin_read_only()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_EDITABLE]:
                            self.state = 1400
                            self.an_admin_list_editable()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_FILTER]:
                            self.state = 1401
                            self.an_admin_list_filter()
                            pass
                        elif token in [ZmeiLangParser.KW_LIST_SEARCH]:
                            self.state = 1402
                            self.an_admin_list_search()
                            pass
                        elif token in [ZmeiLangParser.KW_FIELDS]:
                            self.state = 1403
                            self.an_admin_fields()
                            pass
                        elif token in [ZmeiLangParser.KW_TABS]:
                            self.state = 1404
                            self.an_admin_tabs()
                            pass
                        elif token in [ZmeiLangParser.KW_INLINE]:
                            self.state = 1405
                            self.an_admin_inlines()
                            pass
                        elif token in [ZmeiLangParser.KW_CSS]:
                            self.state = 1406
                            self.an_admin_css()
                            pass
                        elif token in [ZmeiLangParser.KW_JS]:
                            self.state = 1407
                            self.an_admin_js()
                            pass
                        elif token in [ZmeiLangParser.NL]:
                            self.state = 1408
                            self.match(ZmeiLangParser.NL)
                            pass
                        elif token in [ZmeiLangParser.COMA]:
                            self.state = 1409
                            self.match(ZmeiLangParser.COMA)
                            pass
                        else:
                            raise NoViableAltException(self)
                 
                    self.state = 1414
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,122,self._ctx)

                self.state = 1418
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==ZmeiLangParser.NL:
                    self.state = 1415
                    self.match(ZmeiLangParser.NL)
                    self.state = 1420
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1421
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 1427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,125,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1424
                    self.match(ZmeiLangParser.NL) 
                self.state = 1429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,125,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_jsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_JS(self):
            return self.getToken(ZmeiLangParser.KW_JS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_js_file_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_js_file_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_js_file_nameContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_js

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_js" ):
                listener.enterAn_admin_js(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_js" ):
                listener.exitAn_admin_js(self)




    def an_admin_js(self):

        localctx = ZmeiLangParser.An_admin_jsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_an_admin_js)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1430
            self.match(ZmeiLangParser.KW_JS)
            self.state = 1431
            self.match(ZmeiLangParser.COLON)
            self.state = 1435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 1432
                self.match(ZmeiLangParser.NL)
                self.state = 1437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1438
            self.an_admin_js_file_name()
            self.state = 1449
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,128,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1439
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1443
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.NL:
                        self.state = 1440
                        self.match(ZmeiLangParser.NL)
                        self.state = 1445
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 1446
                    self.an_admin_js_file_name() 
                self.state = 1451
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,128,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_cssContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CSS(self):
            return self.getToken(ZmeiLangParser.KW_CSS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_css_file_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_css_file_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_css_file_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_css

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_css" ):
                listener.enterAn_admin_css(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_css" ):
                listener.exitAn_admin_css(self)




    def an_admin_css(self):

        localctx = ZmeiLangParser.An_admin_cssContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_an_admin_css)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1452
            self.match(ZmeiLangParser.KW_CSS)
            self.state = 1453
            self.match(ZmeiLangParser.COLON)
            self.state = 1454
            self.an_admin_css_file_name()
            self.state = 1459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,129,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1455
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1456
                    self.an_admin_css_file_name() 
                self.state = 1461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,129,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_css_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_css_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_css_file_name" ):
                listener.enterAn_admin_css_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_css_file_name" ):
                listener.exitAn_admin_css_file_name(self)




    def an_admin_css_file_name(self):

        localctx = ZmeiLangParser.An_admin_css_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_an_admin_css_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1462
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_js_file_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_js_file_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_js_file_name" ):
                listener.enterAn_admin_js_file_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_js_file_name" ):
                listener.exitAn_admin_js_file_name(self)




    def an_admin_js_file_name(self):

        localctx = ZmeiLangParser.An_admin_js_file_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_an_admin_js_file_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1464
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_inlinesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_inline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_inlineContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_inlineContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_inlines

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_inlines" ):
                listener.enterAn_admin_inlines(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_inlines" ):
                listener.exitAn_admin_inlines(self)




    def an_admin_inlines(self):

        localctx = ZmeiLangParser.An_admin_inlinesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_an_admin_inlines)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1466
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1467
            self.match(ZmeiLangParser.COLON)
            self.state = 1468
            self.an_admin_inline()
            self.state = 1473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,130,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1469
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1470
                    self.an_admin_inline() 
                self.state = 1475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,130,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inline_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Inline_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def inline_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_typeContext,i)


        def inline_extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_extensionContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_extensionContext,i)


        def inline_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Inline_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Inline_fieldsContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_inline" ):
                listener.enterAn_admin_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_inline" ):
                listener.exitAn_admin_inline(self)




    def an_admin_inline(self):

        localctx = ZmeiLangParser.An_admin_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_an_admin_inline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1476
            self.inline_name()
            self.state = 1489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1477
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1485
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (ZmeiLangParser.KW_TYPE - 98)) | (1 << (ZmeiLangParser.KW_EXTENSION - 98)) | (1 << (ZmeiLangParser.KW_FIELDS - 98)) | (1 << (ZmeiLangParser.NL - 98)) | (1 << (ZmeiLangParser.COMA - 98)))) != 0):
                    self.state = 1483
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_TYPE]:
                        self.state = 1478
                        self.inline_type()
                        pass
                    elif token in [ZmeiLangParser.KW_EXTENSION]:
                        self.state = 1479
                        self.inline_extension()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1480
                        self.inline_fields()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1481
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1482
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 1487
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 1488
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_name" ):
                listener.enterInline_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_name" ):
                listener.exitInline_name(self)




    def inline_name(self):

        localctx = ZmeiLangParser.Inline_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1491
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TYPE(self):
            return self.getToken(ZmeiLangParser.KW_TYPE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def inline_type_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Inline_type_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_type" ):
                listener.enterInline_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_type" ):
                listener.exitInline_type(self)




    def inline_type(self):

        localctx = ZmeiLangParser.Inline_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_inline_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1493
            self.match(ZmeiLangParser.KW_TYPE)
            self.state = 1494
            self.match(ZmeiLangParser.COLON)
            self.state = 1495
            self.inline_type_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_type_name" ):
                listener.enterInline_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_type_name" ):
                listener.exitInline_type_name(self)




    def inline_type_name(self):

        localctx = ZmeiLangParser.Inline_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_inline_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1497
            _la = self._input.LA(1)
            if not(((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 94)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_extensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_EXTENSION(self):
            return self.getToken(ZmeiLangParser.KW_EXTENSION, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_extension" ):
                listener.enterInline_extension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_extension" ):
                listener.exitInline_extension(self)




    def inline_extension(self):

        localctx = ZmeiLangParser.Inline_extensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_inline_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1499
            self.match(ZmeiLangParser.KW_EXTENSION)
            self.state = 1500
            self.match(ZmeiLangParser.COLON)
            self.state = 1501
            self.match(ZmeiLangParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_inline_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_fields" ):
                listener.enterInline_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_fields" ):
                listener.exitInline_fields(self)




    def inline_fields(self):

        localctx = ZmeiLangParser.Inline_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_inline_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1503
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1504
            self.match(ZmeiLangParser.COLON)
            self.state = 1505
            self.field_list_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_tabsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_TABS(self):
            return self.getToken(ZmeiLangParser.KW_TABS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_admin_tab(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_admin_tabContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_admin_tabContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_tabs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_tabs" ):
                listener.enterAn_admin_tabs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_tabs" ):
                listener.exitAn_admin_tabs(self)




    def an_admin_tabs(self):

        localctx = ZmeiLangParser.An_admin_tabsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_an_admin_tabs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1507
            self.match(ZmeiLangParser.KW_TABS)
            self.state = 1508
            self.match(ZmeiLangParser.COLON)
            self.state = 1509
            self.an_admin_tab()
            self.state = 1514
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,134,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1510
                    self.match(ZmeiLangParser.COMA)
                    self.state = 1511
                    self.an_admin_tab() 
                self.state = 1516
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,134,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_tabContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tab_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Tab_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def tab_verbose_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Tab_verbose_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_tab

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_tab" ):
                listener.enterAn_admin_tab(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_tab" ):
                listener.exitAn_admin_tab(self)




    def an_admin_tab(self):

        localctx = ZmeiLangParser.An_admin_tabContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_an_admin_tab)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1517
            self.tab_name()
            self.state = 1519
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ:
                self.state = 1518
                self.tab_verbose_name()


            self.state = 1521
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1522
            self.field_list_expr()
            self.state = 1523
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tab_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_tab_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab_name" ):
                listener.enterTab_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab_name" ):
                listener.exitTab_name(self)




    def tab_name(self):

        localctx = ZmeiLangParser.Tab_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_tab_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1525
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tab_verbose_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_tab_verbose_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTab_verbose_name" ):
                listener.enterTab_verbose_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTab_verbose_name" ):
                listener.exitTab_verbose_name(self)




    def tab_verbose_name(self):

        localctx = ZmeiLangParser.Tab_verbose_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_tab_verbose_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1527
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list" ):
                listener.enterAn_admin_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list" ):
                listener.exitAn_admin_list(self)




    def an_admin_list(self):

        localctx = ZmeiLangParser.An_admin_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_an_admin_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1529
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 1530
            self.match(ZmeiLangParser.COLON)
            self.state = 1531
            self.field_list_expr()
            self.state = 1535
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,136,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1532
                    self.match(ZmeiLangParser.NL) 
                self.state = 1537
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,136,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_read_onlyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_READ_ONLY(self):
            return self.getToken(ZmeiLangParser.KW_READ_ONLY, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_read_only

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_read_only" ):
                listener.enterAn_admin_read_only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_read_only" ):
                listener.exitAn_admin_read_only(self)




    def an_admin_read_only(self):

        localctx = ZmeiLangParser.An_admin_read_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_an_admin_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1538
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1539
            self.match(ZmeiLangParser.COLON)
            self.state = 1540
            self.field_list_expr()
            self.state = 1544
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,137,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1541
                    self.match(ZmeiLangParser.NL) 
                self.state = 1546
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,137,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_list_editableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_EDITABLE(self):
            return self.getToken(ZmeiLangParser.KW_LIST_EDITABLE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_editable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_editable" ):
                listener.enterAn_admin_list_editable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_editable" ):
                listener.exitAn_admin_list_editable(self)




    def an_admin_list_editable(self):

        localctx = ZmeiLangParser.An_admin_list_editableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_an_admin_list_editable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1547
            self.match(ZmeiLangParser.KW_LIST_EDITABLE)
            self.state = 1548
            self.match(ZmeiLangParser.COLON)
            self.state = 1549
            self.field_list_expr()
            self.state = 1553
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,138,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1550
                    self.match(ZmeiLangParser.NL) 
                self.state = 1555
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,138,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_list_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_FILTER(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FILTER, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_filter" ):
                listener.enterAn_admin_list_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_filter" ):
                listener.exitAn_admin_list_filter(self)




    def an_admin_list_filter(self):

        localctx = ZmeiLangParser.An_admin_list_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_an_admin_list_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1556
            self.match(ZmeiLangParser.KW_LIST_FILTER)
            self.state = 1557
            self.match(ZmeiLangParser.COLON)
            self.state = 1558
            self.field_list_expr()
            self.state = 1562
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,139,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1559
                    self.match(ZmeiLangParser.NL) 
                self.state = 1564
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,139,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_list_searchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_SEARCH(self):
            return self.getToken(ZmeiLangParser.KW_LIST_SEARCH, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_list_search

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_list_search" ):
                listener.enterAn_admin_list_search(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_list_search" ):
                listener.exitAn_admin_list_search(self)




    def an_admin_list_search(self):

        localctx = ZmeiLangParser.An_admin_list_searchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_an_admin_list_search)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1565
            self.match(ZmeiLangParser.KW_LIST_SEARCH)
            self.state = 1566
            self.match(ZmeiLangParser.COLON)
            self.state = 1567
            self.field_list_expr()
            self.state = 1571
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,140,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1568
                    self.match(ZmeiLangParser.NL) 
                self.state = 1573
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,140,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_admin_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_admin_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_admin_fields" ):
                listener.enterAn_admin_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_admin_fields" ):
                listener.exitAn_admin_fields(self)




    def an_admin_fields(self):

        localctx = ZmeiLangParser.An_admin_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_an_admin_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1574
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1575
            self.match(ZmeiLangParser.COLON)
            self.state = 1576
            self.field_list_expr()
            self.state = 1580
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,141,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1577
                    self.match(ZmeiLangParser.NL) 
                self.state = 1582
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,141,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_apiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_API(self):
            return self.getToken(ZmeiLangParser.AN_API, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_api_all(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_api_allContext,0)


        def an_api_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_api_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_api_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api" ):
                listener.enterAn_api(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api" ):
                listener.exitAn_api(self)




    def an_api(self):

        localctx = ZmeiLangParser.An_apiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_an_api)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1583
            self.match(ZmeiLangParser.AN_API)
            self.state = 1598
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1584
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1594
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.STAR]:
                    self.state = 1585
                    self.an_api_all()
                    pass
                elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1586
                    self.an_api_name()
                    self.state = 1591
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==ZmeiLangParser.COMA:
                        self.state = 1587
                        self.match(ZmeiLangParser.COMA)
                        self.state = 1588
                        self.an_api_name()
                        self.state = 1593
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1596
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_api_allContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api_all

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api_all" ):
                listener.enterAn_api_all(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api_all" ):
                listener.exitAn_api_all(self)




    def an_api_all(self):

        localctx = ZmeiLangParser.An_api_allContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_an_api_all)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1600
            self.match(ZmeiLangParser.STAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_api_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_api_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_api_name" ):
                listener.enterAn_api_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_api_name" ):
                listener.exitAn_api_name(self)




    def an_api_name(self):

        localctx = ZmeiLangParser.An_api_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_an_api_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1602
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_restContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_REST(self):
            return self.getToken(ZmeiLangParser.AN_REST, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_rest_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_descriptorContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_config(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_configContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest" ):
                listener.enterAn_rest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest" ):
                listener.exitAn_rest(self)




    def an_rest(self):

        localctx = ZmeiLangParser.An_restContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_an_rest)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1604
            self.match(ZmeiLangParser.AN_REST)
            self.state = 1607
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 1605
                self.match(ZmeiLangParser.DOT)
                self.state = 1606
                self.an_rest_descriptor()


            self.state = 1613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1609
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1610
                self.an_rest_config()
                self.state = 1611
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_configContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_main_part(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_main_partContext,0)


        def an_rest_inline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_inlineContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_inlineContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_config

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_config" ):
                listener.enterAn_rest_config(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_config" ):
                listener.exitAn_rest_config(self)




    def an_rest_config(self):

        localctx = ZmeiLangParser.An_rest_configContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_an_rest_config)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1615
            self.an_rest_main_part()
            self.state = 1621
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 97)) & ~0x3f) == 0 and ((1 << (_la - 97)) & ((1 << (ZmeiLangParser.KW_INLINE - 97)) | (1 << (ZmeiLangParser.NL - 97)) | (1 << (ZmeiLangParser.COMA - 97)))) != 0):
                self.state = 1619
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_INLINE]:
                    self.state = 1616
                    self.an_rest_inline()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 1617
                    self.match(ZmeiLangParser.NL)
                    pass
                elif token in [ZmeiLangParser.COMA]:
                    self.state = 1618
                    self.match(ZmeiLangParser.COMA)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1623
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_main_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_fieldsContext,i)


        def an_rest_i18n(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_i18nContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_i18nContext,i)


        def an_rest_auth(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_authContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_authContext,i)


        def an_rest_query(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_queryContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_queryContext,i)


        def an_rest_on_create(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_on_createContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_on_createContext,i)


        def an_rest_filter_in(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_filter_inContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_filter_inContext,i)


        def an_rest_filter_out(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_filter_outContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_filter_outContext,i)


        def an_rest_read_only(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_read_onlyContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_read_onlyContext,i)


        def an_rest_user_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_user_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_user_fieldContext,i)


        def an_rest_annotate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_annotateContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotateContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_main_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_main_part" ):
                listener.enterAn_rest_main_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_main_part" ):
                listener.exitAn_rest_main_part(self)




    def an_rest_main_part(self):

        localctx = ZmeiLangParser.An_rest_main_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_an_rest_main_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1638
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,150,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1636
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 1624
                        self.an_rest_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_I18N]:
                        self.state = 1625
                        self.an_rest_i18n()
                        pass
                    elif token in [ZmeiLangParser.KW_AUTH]:
                        self.state = 1626
                        self.an_rest_auth()
                        pass
                    elif token in [ZmeiLangParser.KW_QUERY]:
                        self.state = 1627
                        self.an_rest_query()
                        pass
                    elif token in [ZmeiLangParser.KW_ON_CREATE]:
                        self.state = 1628
                        self.an_rest_on_create()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_IN]:
                        self.state = 1629
                        self.an_rest_filter_in()
                        pass
                    elif token in [ZmeiLangParser.KW_FILTER_OUT]:
                        self.state = 1630
                        self.an_rest_filter_out()
                        pass
                    elif token in [ZmeiLangParser.KW_READ_ONLY]:
                        self.state = 1631
                        self.an_rest_read_only()
                        pass
                    elif token in [ZmeiLangParser.KW_USER_FIELD]:
                        self.state = 1632
                        self.an_rest_user_field()
                        pass
                    elif token in [ZmeiLangParser.KW_ANNOTATE]:
                        self.state = 1633
                        self.an_rest_annotate()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1634
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1635
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 1640
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,150,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_descriptor" ):
                listener.enterAn_rest_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_descriptor" ):
                listener.exitAn_rest_descriptor(self)




    def an_rest_descriptor(self):

        localctx = ZmeiLangParser.An_rest_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_an_rest_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1641
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_i18nContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_I18N(self):
            return self.getToken(ZmeiLangParser.KW_I18N, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_i18n

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_i18n" ):
                listener.enterAn_rest_i18n(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_i18n" ):
                listener.exitAn_rest_i18n(self)




    def an_rest_i18n(self):

        localctx = ZmeiLangParser.An_rest_i18nContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_an_rest_i18n)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1643
            self.match(ZmeiLangParser.KW_I18N)
            self.state = 1644
            self.match(ZmeiLangParser.COLON)
            self.state = 1645
            self.match(ZmeiLangParser.BOOL)
            self.state = 1649
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,151,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1646
                    self.match(ZmeiLangParser.NL) 
                self.state = 1651
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,151,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_queryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_QUERY(self):
            return self.getToken(ZmeiLangParser.KW_QUERY, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_query" ):
                listener.enterAn_rest_query(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_query" ):
                listener.exitAn_rest_query(self)




    def an_rest_query(self):

        localctx = ZmeiLangParser.An_rest_queryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_an_rest_query)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1652
            self.match(ZmeiLangParser.KW_QUERY)
            self.state = 1653
            self.python_code()
            self.state = 1657
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,152,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1654
                    self.match(ZmeiLangParser.NL) 
                self.state = 1659
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,152,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_on_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ON_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_ON_CREATE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_on_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_on_create" ):
                listener.enterAn_rest_on_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_on_create" ):
                listener.exitAn_rest_on_create(self)




    def an_rest_on_create(self):

        localctx = ZmeiLangParser.An_rest_on_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_an_rest_on_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1660
            self.match(ZmeiLangParser.KW_ON_CREATE)
            self.state = 1662
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1661
                self.match(ZmeiLangParser.COLON)


            self.state = 1664
            self.python_code()
            self.state = 1668
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1665
                    self.match(ZmeiLangParser.NL) 
                self.state = 1670
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_filter_inContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FILTER_IN(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_IN, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_filter_in

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_filter_in" ):
                listener.enterAn_rest_filter_in(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_filter_in" ):
                listener.exitAn_rest_filter_in(self)




    def an_rest_filter_in(self):

        localctx = ZmeiLangParser.An_rest_filter_inContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_an_rest_filter_in)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1671
            self.match(ZmeiLangParser.KW_FILTER_IN)
            self.state = 1673
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1672
                self.match(ZmeiLangParser.COLON)


            self.state = 1675
            self.python_code()
            self.state = 1679
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,156,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1676
                    self.match(ZmeiLangParser.NL) 
                self.state = 1681
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,156,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_filter_outContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FILTER_OUT(self):
            return self.getToken(ZmeiLangParser.KW_FILTER_OUT, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_filter_out

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_filter_out" ):
                listener.enterAn_rest_filter_out(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_filter_out" ):
                listener.exitAn_rest_filter_out(self)




    def an_rest_filter_out(self):

        localctx = ZmeiLangParser.An_rest_filter_outContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_an_rest_filter_out)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1682
            self.match(ZmeiLangParser.KW_FILTER_OUT)
            self.state = 1684
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1683
                self.match(ZmeiLangParser.COLON)


            self.state = 1686
            self.python_code()
            self.state = 1690
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1687
                    self.match(ZmeiLangParser.NL) 
                self.state = 1692
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_read_onlyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_READ_ONLY(self):
            return self.getToken(ZmeiLangParser.KW_READ_ONLY, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_read_only

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_read_only" ):
                listener.enterAn_rest_read_only(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_read_only" ):
                listener.exitAn_rest_read_only(self)




    def an_rest_read_only(self):

        localctx = ZmeiLangParser.An_rest_read_onlyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_an_rest_read_only)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1693
            self.match(ZmeiLangParser.KW_READ_ONLY)
            self.state = 1694
            self.match(ZmeiLangParser.COLON)
            self.state = 1695
            self.field_list_expr()
            self.state = 1699
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,159,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1696
                    self.match(ZmeiLangParser.NL) 
                self.state = 1701
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,159,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_user_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_USER_FIELD(self):
            return self.getToken(ZmeiLangParser.KW_USER_FIELD, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_user_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_user_field" ):
                listener.enterAn_rest_user_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_user_field" ):
                listener.exitAn_rest_user_field(self)




    def an_rest_user_field(self):

        localctx = ZmeiLangParser.An_rest_user_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_an_rest_user_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1702
            self.match(ZmeiLangParser.KW_USER_FIELD)
            self.state = 1703
            self.match(ZmeiLangParser.COLON)
            self.state = 1704
            self.id_or_kw()
            self.state = 1708
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,160,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1705
                    self.match(ZmeiLangParser.NL) 
                self.state = 1710
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,160,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def field_list_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Field_list_exprContext,0)


        def an_rest_fields_write_mode(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_fields_write_modeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_fields" ):
                listener.enterAn_rest_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_fields" ):
                listener.exitAn_rest_fields(self)




    def an_rest_fields(self):

        localctx = ZmeiLangParser.An_rest_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_an_rest_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1711
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 1712
            self.match(ZmeiLangParser.COLON)
            self.state = 1713
            self.field_list_expr()
            self.state = 1715
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 1714
                self.an_rest_fields_write_mode()


            self.state = 1720
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,162,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1717
                    self.match(ZmeiLangParser.NL) 
                self.state = 1722
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,162,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_fields_write_modeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def write_mode_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.Write_mode_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_fields_write_mode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_fields_write_mode" ):
                listener.enterAn_rest_fields_write_mode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_fields_write_mode" ):
                listener.exitAn_rest_fields_write_mode(self)




    def an_rest_fields_write_mode(self):

        localctx = ZmeiLangParser.An_rest_fields_write_modeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_an_rest_fields_write_mode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1723
            self.write_mode_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_authContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AUTH(self):
            return self.getToken(ZmeiLangParser.KW_AUTH, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_auth_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_auth_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_typeContext,i)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth" ):
                listener.enterAn_rest_auth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth" ):
                listener.exitAn_rest_auth(self)




    def an_rest_auth(self):

        localctx = ZmeiLangParser.An_rest_authContext(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_an_rest_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1725
            self.match(ZmeiLangParser.KW_AUTH)
            self.state = 1726
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1727
            self.an_rest_auth_type()
            self.state = 1732
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1728
                self.match(ZmeiLangParser.COMA)
                self.state = 1729
                self.an_rest_auth_type()
                self.state = 1734
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1735
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_auth_type_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_type_nameContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_auth_token_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_token_modelContext,0)


        def an_rest_auth_token_class(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_auth_token_classContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_type" ):
                listener.enterAn_rest_auth_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_type" ):
                listener.exitAn_rest_auth_type(self)




    def an_rest_auth_type(self):

        localctx = ZmeiLangParser.An_rest_auth_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_an_rest_auth_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1737
            self.an_rest_auth_type_name()
            self.state = 1741
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.COLON]:
                self.state = 1738
                self.match(ZmeiLangParser.COLON)
                self.state = 1739
                self.an_rest_auth_token_model()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 1740
                self.an_rest_auth_token_class()
                pass
            elif token in [ZmeiLangParser.BRACE_CLOSE, ZmeiLangParser.COMA]:
                pass
            else:
                pass
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_type_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AUTH_TYPE_BASIC(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_BASIC, 0)

        def KW_AUTH_TYPE_SESSION(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_SESSION, 0)

        def KW_AUTH_TYPE_TOKEN(self):
            return self.getToken(ZmeiLangParser.KW_AUTH_TYPE_TOKEN, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_type_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_type_name" ):
                listener.enterAn_rest_auth_type_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_type_name" ):
                listener.exitAn_rest_auth_type_name(self)




    def an_rest_auth_type_name(self):

        localctx = ZmeiLangParser.An_rest_auth_type_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_an_rest_auth_type_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1743
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.KW_AUTH_TYPE_BASIC) | (1 << ZmeiLangParser.KW_AUTH_TYPE_SESSION) | (1 << ZmeiLangParser.KW_AUTH_TYPE_TOKEN))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_token_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_token_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_token_model" ):
                listener.enterAn_rest_auth_token_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_token_model" ):
                listener.exitAn_rest_auth_token_model(self)




    def an_rest_auth_token_model(self):

        localctx = ZmeiLangParser.An_rest_auth_token_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_an_rest_auth_token_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1745
            self.model_ref()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_auth_token_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_auth_token_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_auth_token_class" ):
                listener.enterAn_rest_auth_token_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_auth_token_class" ):
                listener.exitAn_rest_auth_token_class(self)




    def an_rest_auth_token_class(self):

        localctx = ZmeiLangParser.An_rest_auth_token_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_an_rest_auth_token_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1747
            self.classname()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ANNOTATE(self):
            return self.getToken(ZmeiLangParser.KW_ANNOTATE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_annotate_count(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_countContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate" ):
                listener.enterAn_rest_annotate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate" ):
                listener.exitAn_rest_annotate(self)




    def an_rest_annotate(self):

        localctx = ZmeiLangParser.An_rest_annotateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_an_rest_annotate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1749
            self.match(ZmeiLangParser.KW_ANNOTATE)
            self.state = 1750
            self.match(ZmeiLangParser.COLON)
            self.state = 1751
            self.an_rest_annotate_count()
            self.state = 1755
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,165,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1752
                    self.match(ZmeiLangParser.NL) 
                self.state = 1757
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,165,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_countContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_COUNT(self):
            return self.getToken(ZmeiLangParser.KW_COUNT, 0)

        def an_rest_annotate_count_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_count_fieldContext,0)


        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def an_rest_annotate_count_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_annotate_count_aliasContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count" ):
                listener.enterAn_rest_annotate_count(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count" ):
                listener.exitAn_rest_annotate_count(self)




    def an_rest_annotate_count(self):

        localctx = ZmeiLangParser.An_rest_annotate_countContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_an_rest_annotate_count)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1758
            self.match(ZmeiLangParser.KW_COUNT)
            self.state = 1759
            self.an_rest_annotate_count_field()
            self.state = 1762
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1760
                self.match(ZmeiLangParser.KW_AS)
                self.state = 1761
                self.an_rest_annotate_count_alias()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_count_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count_field" ):
                listener.enterAn_rest_annotate_count_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count_field" ):
                listener.exitAn_rest_annotate_count_field(self)




    def an_rest_annotate_count_field(self):

        localctx = ZmeiLangParser.An_rest_annotate_count_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_an_rest_annotate_count_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1764
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_annotate_count_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_annotate_count_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_annotate_count_alias" ):
                listener.enterAn_rest_annotate_count_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_annotate_count_alias" ):
                listener.exitAn_rest_annotate_count_alias(self)




    def an_rest_annotate_count_alias(self):

        localctx = ZmeiLangParser.An_rest_annotate_count_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_an_rest_annotate_count_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1766
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inlineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE(self):
            return self.getToken(ZmeiLangParser.KW_INLINE, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_rest_inline_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_rest_inline_declContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_rest_inline_declContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline" ):
                listener.enterAn_rest_inline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline" ):
                listener.exitAn_rest_inline(self)




    def an_rest_inline(self):

        localctx = ZmeiLangParser.An_rest_inlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_an_rest_inline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1768
            self.match(ZmeiLangParser.KW_INLINE)
            self.state = 1769
            self.match(ZmeiLangParser.COLON)
            self.state = 1773 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1773
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                        self.state = 1770
                        self.an_rest_inline_decl()
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 1771
                        self.match(ZmeiLangParser.COMA)
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 1772
                        self.match(ZmeiLangParser.NL)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 1775 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,168,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inline_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_rest_inline_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_inline_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_rest_config(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_rest_configContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline_decl" ):
                listener.enterAn_rest_inline_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline_decl" ):
                listener.exitAn_rest_inline_decl(self)




    def an_rest_inline_decl(self):

        localctx = ZmeiLangParser.An_rest_inline_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_an_rest_inline_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1777
            self.an_rest_inline_name()
            self.state = 1778
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1779
            self.an_rest_config()
            self.state = 1780
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_rest_inline_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_rest_inline_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_rest_inline_name" ):
                listener.enterAn_rest_inline_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_rest_inline_name" ):
                listener.exitAn_rest_inline_name(self)




    def an_rest_inline_name(self):

        localctx = ZmeiLangParser.An_rest_inline_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_an_rest_inline_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1782
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_orderContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ORDER(self):
            return self.getToken(ZmeiLangParser.AN_ORDER, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_order_fields(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_order_fieldsContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_order

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_order" ):
                listener.enterAn_order(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_order" ):
                listener.exitAn_order(self)




    def an_order(self):

        localctx = ZmeiLangParser.An_orderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_an_order)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1784
            self.match(ZmeiLangParser.AN_ORDER)
            self.state = 1785
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1786
            self.an_order_fields()
            self.state = 1787
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_order_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_order_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_order_fields" ):
                listener.enterAn_order_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_order_fields" ):
                listener.exitAn_order_fields(self)




    def an_order_fields(self):

        localctx = ZmeiLangParser.An_order_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_an_order_fields)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1789
            self.id_or_kw()
            self.state = 1794
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 1790
                self.match(ZmeiLangParser.COMA)
                self.state = 1791
                self.id_or_kw()
                self.state = 1796
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_cleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CLEAN(self):
            return self.getToken(ZmeiLangParser.AN_CLEAN, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_clean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_clean" ):
                listener.enterAn_clean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_clean" ):
                listener.exitAn_clean(self)




    def an_clean(self):

        localctx = ZmeiLangParser.An_cleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_an_clean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1797
            self.match(ZmeiLangParser.AN_CLEAN)
            self.state = 1798
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_pre_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRE_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_PRE_DELETE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_pre_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_pre_delete" ):
                listener.enterAn_pre_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_pre_delete" ):
                listener.exitAn_pre_delete(self)




    def an_pre_delete(self):

        localctx = ZmeiLangParser.An_pre_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_an_pre_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1800
            self.match(ZmeiLangParser.AN_PRE_DELETE)
            self.state = 1801
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_treeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_TREE(self):
            return self.getToken(ZmeiLangParser.AN_TREE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_tree_poly(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_tree_polyContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_tree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_tree" ):
                listener.enterAn_tree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_tree" ):
                listener.exitAn_tree(self)




    def an_tree(self):

        localctx = ZmeiLangParser.An_treeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_an_tree)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1803
            self.match(ZmeiLangParser.AN_TREE)
            self.state = 1808
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 1804
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 1805
                self.an_tree_poly()
                self.state = 1806
                self.match(ZmeiLangParser.BRACE_CLOSE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_tree_polyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_POLY_LIST(self):
            return self.getToken(ZmeiLangParser.KW_POLY_LIST, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_tree_poly

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_tree_poly" ):
                listener.enterAn_tree_poly(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_tree_poly" ):
                listener.exitAn_tree_poly(self)




    def an_tree_poly(self):

        localctx = ZmeiLangParser.An_tree_polyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_an_tree_poly)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1810
            self.match(ZmeiLangParser.KW_POLY_LIST)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_mixinContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MIXIN(self):
            return self.getToken(ZmeiLangParser.AN_MIXIN, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_mixin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_mixin" ):
                listener.enterAn_mixin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_mixin" ):
                listener.exitAn_mixin(self)




    def an_mixin(self):

        localctx = ZmeiLangParser.An_mixinContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_an_mixin)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1812
            self.match(ZmeiLangParser.AN_MIXIN)

            self.state = 1813
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1814
            self.classname()
            self.state = 1815
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_date_treeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_DATE_TREE(self):
            return self.getToken(ZmeiLangParser.AN_DATE_TREE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_date_tree_field(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_date_tree_fieldContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_date_tree

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_date_tree" ):
                listener.enterAn_date_tree(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_date_tree" ):
                listener.exitAn_date_tree(self)




    def an_date_tree(self):

        localctx = ZmeiLangParser.An_date_treeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_an_date_tree)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1817
            self.match(ZmeiLangParser.AN_DATE_TREE)

            self.state = 1818
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1819
            self.an_date_tree_field()
            self.state = 1820
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_date_tree_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_date_tree_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_date_tree_field" ):
                listener.enterAn_date_tree_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_date_tree_field" ):
                listener.exitAn_date_tree_field(self)




    def an_date_tree_field(self):

        localctx = ZmeiLangParser.An_date_tree_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_an_date_tree_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1822
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_m2m_changedContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_M2M_CHANGED(self):
            return self.getToken(ZmeiLangParser.AN_M2M_CHANGED, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_m2m_changed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_m2m_changed" ):
                listener.enterAn_m2m_changed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_m2m_changed" ):
                listener.exitAn_m2m_changed(self)




    def an_m2m_changed(self):

        localctx = ZmeiLangParser.An_m2m_changedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_an_m2m_changed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
            self.match(ZmeiLangParser.AN_M2M_CHANGED)
            self.state = 1825
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_post_saveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST_SAVE(self):
            return self.getToken(ZmeiLangParser.AN_POST_SAVE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post_save

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post_save" ):
                listener.enterAn_post_save(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post_save" ):
                listener.exitAn_post_save(self)




    def an_post_save(self):

        localctx = ZmeiLangParser.An_post_saveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_an_post_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1827
            self.match(ZmeiLangParser.AN_POST_SAVE)
            self.state = 1828
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_pre_saveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRE_SAVE(self):
            return self.getToken(ZmeiLangParser.AN_PRE_SAVE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_pre_save

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_pre_save" ):
                listener.enterAn_pre_save(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_pre_save" ):
                listener.exitAn_pre_save(self)




    def an_pre_save(self):

        localctx = ZmeiLangParser.An_pre_saveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_an_pre_save)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1830
            self.match(ZmeiLangParser.AN_PRE_SAVE)
            self.state = 1831
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_post_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_POST_DELETE, 0)

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post_delete" ):
                listener.enterAn_post_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post_delete" ):
                listener.exitAn_post_delete(self)




    def an_post_delete(self):

        localctx = ZmeiLangParser.An_post_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_an_post_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1833
            self.match(ZmeiLangParser.AN_POST_DELETE)
            self.state = 1834
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_sortableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_SORTABLE(self):
            return self.getToken(ZmeiLangParser.AN_SORTABLE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_sortable_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_sortable_field_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_sortable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_sortable" ):
                listener.enterAn_sortable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_sortable" ):
                listener.exitAn_sortable(self)




    def an_sortable(self):

        localctx = ZmeiLangParser.An_sortableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_an_sortable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1836
            self.match(ZmeiLangParser.AN_SORTABLE)
            self.state = 1837
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1838
            self.an_sortable_field_name()
            self.state = 1839
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_sortable_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_sortable_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_sortable_field_name" ):
                listener.enterAn_sortable_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_sortable_field_name" ):
                listener.exitAn_sortable_field_name(self)




    def an_sortable_field_name(self):

        localctx = ZmeiLangParser.An_sortable_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_an_sortable_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1841
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_header(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_headerContext,0)


        def page_body(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_bodyContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage" ):
                listener.enterPage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage" ):
                listener.exitPage(self)




    def page(self):

        localctx = ZmeiLangParser.PageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1843
            self.page_header()
            self.state = 1847
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,171,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1844
                    self.match(ZmeiLangParser.NL) 
                self.state = 1849
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,171,self._ctx)

            self.state = 1850
            self.page_body()
            self.state = 1854
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,172,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1851
                    self.match(ZmeiLangParser.NL) 
                self.state = 1856
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,172,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def page_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_nameContext,0)


        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def page_base(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_baseContext,0)


        def page_alias(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_aliasContext,0)


        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COLON)
            else:
                return self.getToken(ZmeiLangParser.COLON, i)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def page_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_urlContext,0)


        def page_template(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_templateContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_header" ):
                listener.enterPage_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_header" ):
                listener.exitPage_header(self)




    def page_header(self):

        localctx = ZmeiLangParser.Page_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_page_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1857
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 1859
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,173,self._ctx)
            if la_ == 1:
                self.state = 1858
                self.page_base()


            self.state = 1861
            self.page_name()
            self.state = 1863
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.KW_AS:
                self.state = 1862
                self.page_alias()


            self.state = 1873
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COLON:
                self.state = 1865
                self.match(ZmeiLangParser.COLON)
                self.state = 1867
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 134)) & ~0x3f) == 0 and ((1 << (_la - 134)) & ((1 << (ZmeiLangParser.DOT - 134)) | (1 << (ZmeiLangParser.SLASH - 134)) | (1 << (ZmeiLangParser.DOLLAR - 134)))) != 0):
                    self.state = 1866
                    self.page_url()


                self.state = 1871
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.COLON:
                    self.state = 1869
                    self.match(ZmeiLangParser.COLON)
                    self.state = 1870
                    self.page_template()




            self.state = 1875
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
            self.state = 1877
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,178,self._ctx)
            if la_ == 1:
                self.state = 1876
                self.match(ZmeiLangParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def DASH(self):
            return self.getToken(ZmeiLangParser.DASH, 0)

        def APPROX(self):
            return self.getToken(ZmeiLangParser.APPROX, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_base" ):
                listener.enterPage_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_base" ):
                listener.exitPage_base(self)




    def page_base(self):

        localctx = ZmeiLangParser.Page_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_page_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1882
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,179,self._ctx)
            if la_ == 1:
                self.state = 1879
                self.id_or_kw()
                self.state = 1880
                self.match(ZmeiLangParser.DOT)


            self.state = 1884
            self.id_or_kw()
            self.state = 1885
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.DASH or _la==ZmeiLangParser.APPROX):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 1886
            self.match(ZmeiLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_aliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_AS(self):
            return self.getToken(ZmeiLangParser.KW_AS, 0)

        def page_alias_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_alias_nameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_alias

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_alias" ):
                listener.enterPage_alias(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_alias" ):
                listener.exitPage_alias(self)




    def page_alias(self):

        localctx = ZmeiLangParser.Page_aliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_page_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1888
            self.match(ZmeiLangParser.KW_AS)
            self.state = 1889
            self.page_alias_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_alias_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_alias_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_alias_name" ):
                listener.enterPage_alias_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_alias_name" ):
                listener.exitPage_alias_name(self)




    def page_alias_name(self):

        localctx = ZmeiLangParser.Page_alias_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_page_alias_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1891
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_templateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def template_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Template_nameContext,0)


        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_template

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_template" ):
                listener.enterPage_template(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_template" ):
                listener.exitPage_template(self)




    def page_template(self):

        localctx = ZmeiLangParser.Page_templateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_page_template)
        try:
            self.state = 1895
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.UNDERSCORE, ZmeiLangParser.DASH, ZmeiLangParser.DOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1893
                self.template_name()
                pass
            elif token in [ZmeiLangParser.ASSIGN, ZmeiLangParser.CODE_BLOCK]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1894
                self.python_code()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Template_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def file_name_part(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.File_name_partContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.File_name_partContext,i)


        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_template_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemplate_name" ):
                listener.enterTemplate_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemplate_name" ):
                listener.exitTemplate_name(self)




    def template_name(self):

        localctx = ZmeiLangParser.Template_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_template_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1897
            self.file_name_part()
            self.state = 1902
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.SLASH:
                self.state = 1898
                self.match(ZmeiLangParser.SLASH)
                self.state = 1899
                self.file_name_part()
                self.state = 1904
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class File_name_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DIGIT)
            else:
                return self.getToken(ZmeiLangParser.DIGIT, i)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def UNDERSCORE(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.UNDERSCORE)
            else:
                return self.getToken(ZmeiLangParser.UNDERSCORE, i)

        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DOT)
            else:
                return self.getToken(ZmeiLangParser.DOT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_file_name_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile_name_part" ):
                listener.enterFile_name_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile_name_part" ):
                listener.exitFile_name_part(self)




    def file_name_part(self):

        localctx = ZmeiLangParser.File_name_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_file_name_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1910 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1910
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1905
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1906
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1907
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.UNDERSCORE]:
                    self.state = 1908
                    self.match(ZmeiLangParser.UNDERSCORE)
                    pass
                elif token in [ZmeiLangParser.DOT]:
                    self.state = 1909
                    self.match(ZmeiLangParser.DOT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1912 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DIGIT - 106)) | (1 << (ZmeiLangParser.UNDERSCORE - 106)) | (1 << (ZmeiLangParser.DASH - 106)) | (1 << (ZmeiLangParser.DOT - 106)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def url_segments(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_segmentsContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def DOLLAR(self):
            return self.getToken(ZmeiLangParser.DOLLAR, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_url" ):
                listener.enterPage_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_url" ):
                listener.exitPage_url(self)




    def page_url(self):

        localctx = ZmeiLangParser.Page_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1915
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR:
                self.state = 1914
                _la = self._input.LA(1)
                if not(_la==ZmeiLangParser.DOT or _la==ZmeiLangParser.DOLLAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 1917
            self.url_segments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_partContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DASH)
            else:
                return self.getToken(ZmeiLangParser.DASH, i)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.DIGIT)
            else:
                return self.getToken(ZmeiLangParser.DIGIT, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_part" ):
                listener.enterUrl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_part" ):
                listener.exitUrl_part(self)




    def url_part(self):

        localctx = ZmeiLangParser.Url_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_url_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1922 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1922
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                    self.state = 1919
                    self.id_or_kw()
                    pass
                elif token in [ZmeiLangParser.DASH]:
                    self.state = 1920
                    self.match(ZmeiLangParser.DASH)
                    pass
                elif token in [ZmeiLangParser.DIGIT]:
                    self.state = 1921
                    self.match(ZmeiLangParser.DIGIT)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 1924 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DIGIT - 106)) | (1 << (ZmeiLangParser.DASH - 106)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ZmeiLangParser.LT, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_param" ):
                listener.enterUrl_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_param" ):
                listener.exitUrl_param(self)




    def url_param(self):

        localctx = ZmeiLangParser.Url_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_url_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1926
            self.match(ZmeiLangParser.LT)
            self.state = 1927
            self.id_or_kw()
            self.state = 1928
            self.match(ZmeiLangParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_segmentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def url_part(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_partContext,0)


        def url_param(self):
            return self.getTypedRuleContext(ZmeiLangParser.Url_paramContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_segment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_segment" ):
                listener.enterUrl_segment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_segment" ):
                listener.exitUrl_segment(self)




    def url_segment(self):

        localctx = ZmeiLangParser.Url_segmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_url_segment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1932
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.DIGIT, ZmeiLangParser.DASH]:
                self.state = 1930
                self.url_part()
                pass
            elif token in [ZmeiLangParser.LT]:
                self.state = 1931
                self.url_param()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Url_segmentsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLASH(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.SLASH)
            else:
                return self.getToken(ZmeiLangParser.SLASH, i)

        def url_segment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Url_segmentContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Url_segmentContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_url_segments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUrl_segments" ):
                listener.enterUrl_segments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUrl_segments" ):
                listener.exitUrl_segments(self)




    def url_segments(self):

        localctx = ZmeiLangParser.Url_segmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_url_segments)
        self._la = 0 # Token type
        try:
            self.state = 1944
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,190,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1934
                self.match(ZmeiLangParser.SLASH)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1937 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1935
                        self.match(ZmeiLangParser.SLASH)
                        self.state = 1936
                        self.url_segment()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1939 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,188,self._ctx)

                self.state = 1942
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.SLASH:
                    self.state = 1941
                    self.match(ZmeiLangParser.SLASH)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_name" ):
                listener.enterPage_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_name" ):
                listener.exitPage_name(self)




    def page_name(self):

        localctx = ZmeiLangParser.Page_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_page_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1946
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_fieldContext,i)


        def page_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_functionContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_functionContext,i)


        def page_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_codeContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def page_annotation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_annotationContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_annotationContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_body" ):
                listener.enterPage_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_body" ):
                listener.exitPage_body(self)




    def page_body(self):

        localctx = ZmeiLangParser.Page_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_page_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1951
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,191,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1948
                    self.page_field() 
                self.state = 1953
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,191,self._ctx)

            self.state = 1957
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,192,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1954
                    self.page_function() 
                self.state = 1959
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,192,self._ctx)

            self.state = 1961
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.ASSIGN or _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1960
                self.page_code()


            self.state = 1966
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,194,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1963
                    self.match(ZmeiLangParser.NL) 
                self.state = 1968
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,194,self._ctx)

            self.state = 1972
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,195,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1969
                    self.page_annotation() 
                self.state = 1974
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,195,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def python_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Python_codeContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_code" ):
                listener.enterPage_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_code" ):
                listener.exitPage_code(self)




    def page_code(self):

        localctx = ZmeiLangParser.Page_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_page_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1975
            self.python_code()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_field_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_field_nameContext,0)


        def ASSIGN(self):
            return self.getToken(ZmeiLangParser.ASSIGN, 0)

        def page_field_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_field_codeContext,0)


        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field" ):
                listener.enterPage_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field" ):
                listener.exitPage_field(self)




    def page_field(self):

        localctx = ZmeiLangParser.Page_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_page_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1977
            self.page_field_name()
            self.state = 1978
            self.match(ZmeiLangParser.ASSIGN)
            self.state = 1979
            self.page_field_code()
            self.state = 1986
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 1981 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1980
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 1983 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 1985
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field_name" ):
                listener.enterPage_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field_name" ):
                listener.exitPage_field_name(self)




    def page_field_name(self):

        localctx = ZmeiLangParser.Page_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_page_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1988
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_field_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PYTHON_CODE(self):
            return self.getToken(ZmeiLangParser.PYTHON_CODE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_field_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_field_code" ):
                listener.enterPage_field_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_field_code" ):
                listener.exitPage_field_code(self)




    def page_field_code(self):

        localctx = ZmeiLangParser.Page_field_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_page_field_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1990
            self.match(ZmeiLangParser.PYTHON_CODE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_function_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_function_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def EOF(self):
            return self.getToken(ZmeiLangParser.EOF, 0)

        def page_function_args(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_function_argsContext,0)


        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function" ):
                listener.enterPage_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function" ):
                listener.exitPage_function(self)




    def page_function(self):

        localctx = ZmeiLangParser.Page_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_page_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1992
            self.page_function_name()
            self.state = 1993
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 1995
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.DOT - 106)))) != 0):
                self.state = 1994
                self.page_function_args()


            self.state = 1997
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 1999
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 1998
                self.code_block()


            self.state = 2007
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.NL]:
                self.state = 2002 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 2001
                        self.match(ZmeiLangParser.NL)

                    else:
                        raise NoViableAltException(self)
                    self.state = 2004 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,200,self._ctx)

                pass
            elif token in [ZmeiLangParser.EOF]:
                self.state = 2006
                self.match(ZmeiLangParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_function_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_name" ):
                listener.enterPage_function_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_name" ):
                listener.exitPage_function_name(self)




    def page_function_name(self):

        localctx = ZmeiLangParser.Page_function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_page_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2009
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_function_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def page_function_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Page_function_argContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Page_function_argContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_args" ):
                listener.enterPage_function_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_args" ):
                listener.exitPage_function_args(self)




    def page_function_args(self):

        localctx = ZmeiLangParser.Page_function_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_page_function_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2011
            self.page_function_arg()
            self.state = 2016
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2012
                self.match(ZmeiLangParser.COMA)
                self.state = 2013
                self.page_function_arg()
                self.state = 2018
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_function_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_function_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_function_arg" ):
                listener.enterPage_function_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_function_arg" ):
                listener.exitPage_function_arg(self)




    def page_function_arg(self):

        localctx = ZmeiLangParser.Page_function_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_page_function_arg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2020
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2019
                self.match(ZmeiLangParser.DOT)


            self.state = 2022
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Page_annotationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_stream(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_streamContext,0)


        def an_react(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_reactContext,0)


        def an_html(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_htmlContext,0)


        def an_markdown(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_markdownContext,0)


        def an_crud_delete(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_deleteContext,0)


        def an_post(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_postContext,0)


        def an_auth(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_authContext,0)


        def an_crud_create(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_createContext,0)


        def an_crud_edit(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_editContext,0)


        def an_crud(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crudContext,0)


        def an_crud_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_listContext,0)


        def an_menu(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menuContext,0)


        def an_crud_detail(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_detailContext,0)


        def an_priority_marker(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_priority_markerContext,0)


        def an_get(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_getContext,0)


        def an_error(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_errorContext,0)


        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_page_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPage_annotation" ):
                listener.enterPage_annotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPage_annotation" ):
                listener.exitPage_annotation(self)




    def page_annotation(self):

        localctx = ZmeiLangParser.Page_annotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_page_annotation)
        try:
            self.state = 2041
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.AN_STREAM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2024
                self.an_stream()
                pass
            elif token in [ZmeiLangParser.AN_REACT, ZmeiLangParser.AN_REACT_CLIENT, ZmeiLangParser.AN_REACT_SERVER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2025
                self.an_react()
                pass
            elif token in [ZmeiLangParser.AN_HTML]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2026
                self.an_html()
                pass
            elif token in [ZmeiLangParser.AN_MARKDOWN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2027
                self.an_markdown()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DELETE]:
                self.enterOuterAlt(localctx, 5)
                self.state = 2028
                self.an_crud_delete()
                pass
            elif token in [ZmeiLangParser.AN_POST]:
                self.enterOuterAlt(localctx, 6)
                self.state = 2029
                self.an_post()
                pass
            elif token in [ZmeiLangParser.AN_AUTH]:
                self.enterOuterAlt(localctx, 7)
                self.state = 2030
                self.an_auth()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_CREATE]:
                self.enterOuterAlt(localctx, 8)
                self.state = 2031
                self.an_crud_create()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_EDIT]:
                self.enterOuterAlt(localctx, 9)
                self.state = 2032
                self.an_crud_edit()
                pass
            elif token in [ZmeiLangParser.AN_CRUD]:
                self.enterOuterAlt(localctx, 10)
                self.state = 2033
                self.an_crud()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_LIST]:
                self.enterOuterAlt(localctx, 11)
                self.state = 2034
                self.an_crud_list()
                pass
            elif token in [ZmeiLangParser.AN_MENU]:
                self.enterOuterAlt(localctx, 12)
                self.state = 2035
                self.an_menu()
                pass
            elif token in [ZmeiLangParser.AN_CRUD_DETAIL]:
                self.enterOuterAlt(localctx, 13)
                self.state = 2036
                self.an_crud_detail()
                pass
            elif token in [ZmeiLangParser.AN_PRIORITY]:
                self.enterOuterAlt(localctx, 14)
                self.state = 2037
                self.an_priority_marker()
                pass
            elif token in [ZmeiLangParser.AN_GET]:
                self.enterOuterAlt(localctx, 15)
                self.state = 2038
                self.an_get()
                pass
            elif token in [ZmeiLangParser.AN_ERROR]:
                self.enterOuterAlt(localctx, 16)
                self.state = 2039
                self.an_error()
                pass
            elif token in [ZmeiLangParser.NL]:
                self.enterOuterAlt(localctx, 17)
                self.state = 2040
                self.match(ZmeiLangParser.NL)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_streamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_STREAM(self):
            return self.getToken(ZmeiLangParser.AN_STREAM, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def an_stream_model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_stream_modelContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_stream_modelContext,i)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream" ):
                listener.enterAn_stream(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream" ):
                listener.exitAn_stream(self)




    def an_stream(self):

        localctx = ZmeiLangParser.An_streamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_an_stream)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2043
            self.match(ZmeiLangParser.AN_STREAM)

            self.state = 2044
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2047 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2047
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.HASH]:
                    self.state = 2045
                    self.an_stream_model()
                    pass
                elif token in [ZmeiLangParser.NL]:
                    self.state = 2046
                    self.match(ZmeiLangParser.NL)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 2049 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 42)) & ~0x3f) == 0 and ((1 << (_la - 42)) & ((1 << (ZmeiLangParser.KW_AUTH_TYPE_BASIC - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_SESSION - 42)) | (1 << (ZmeiLangParser.KW_AUTH_TYPE_TOKEN - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FLOAT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DECIMAL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_DATETIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_TEXT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_INT - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_SLUG - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_BOOL - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE - 42)) | (1 << (ZmeiLangParser.COL_FIELD_TYPE_MANY - 42)) | (1 << (ZmeiLangParser.COL_FIELD_CHOICES - 42)) | (1 << (ZmeiLangParser.KW_THEME - 42)) | (1 << (ZmeiLangParser.KW_INSTALL - 42)) | (1 << (ZmeiLangParser.KW_HEADER - 42)) | (1 << (ZmeiLangParser.KW_SERVICES - 42)) | (1 << (ZmeiLangParser.KW_SELENIUM_PYTEST - 42)) | (1 << (ZmeiLangParser.KW_CHILD - 42)) | (1 << (ZmeiLangParser.KW_FILTER_OUT - 42)) | (1 << (ZmeiLangParser.KW_FILTER_IN - 42)) | (1 << (ZmeiLangParser.KW_PAGE - 42)) | (1 << (ZmeiLangParser.KW_LINK_SUFFIX - 42)) | (1 << (ZmeiLangParser.KW_URL_PREFIX - 42)) | (1 << (ZmeiLangParser.KW_CAN_EDIT - 42)) | (1 << (ZmeiLangParser.KW_OBJECT_EXPR - 42)) | (1 << (ZmeiLangParser.KW_BLOCK - 42)) | (1 << (ZmeiLangParser.KW_ITEM_NAME - 42)) | (1 << (ZmeiLangParser.KW_PK_PARAM - 42)) | (1 << (ZmeiLangParser.KW_LIST_FIELDS - 42)) | (1 << (ZmeiLangParser.KW_DELETE - 42)) | (1 << (ZmeiLangParser.KW_EDIT - 42)) | (1 << (ZmeiLangParser.KW_CREATE - 42)) | (1 << (ZmeiLangParser.KW_DETAIL - 42)) | (1 << (ZmeiLangParser.KW_SKIP - 42)) | (1 << (ZmeiLangParser.KW_FROM - 42)) | (1 << (ZmeiLangParser.KW_POLY_LIST - 42)) | (1 << (ZmeiLangParser.KW_CSS - 42)) | (1 << (ZmeiLangParser.KW_JS - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 42)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 42)) | (1 << (ZmeiLangParser.KW_INLINE - 42)) | (1 << (ZmeiLangParser.KW_TYPE - 42)) | (1 << (ZmeiLangParser.KW_USER_FIELD - 42)) | (1 << (ZmeiLangParser.KW_ANNOTATE - 42)) | (1 << (ZmeiLangParser.KW_ON_CREATE - 42)) | (1 << (ZmeiLangParser.KW_QUERY - 42)) | (1 << (ZmeiLangParser.KW_AUTH - 42)) | (1 << (ZmeiLangParser.KW_COUNT - 42)) | (1 << (ZmeiLangParser.KW_I18N - 42)))) != 0) or ((((_la - 106)) & ~0x3f) == 0 and ((1 << (_la - 106)) & ((1 << (ZmeiLangParser.KW_EXTENSION - 106)) | (1 << (ZmeiLangParser.KW_TABS - 106)) | (1 << (ZmeiLangParser.KW_LIST - 106)) | (1 << (ZmeiLangParser.KW_READ_ONLY - 106)) | (1 << (ZmeiLangParser.KW_LIST_EDITABLE - 106)) | (1 << (ZmeiLangParser.KW_LIST_FILTER - 106)) | (1 << (ZmeiLangParser.KW_LIST_SEARCH - 106)) | (1 << (ZmeiLangParser.KW_FIELDS - 106)) | (1 << (ZmeiLangParser.KW_IMPORT - 106)) | (1 << (ZmeiLangParser.KW_AS - 106)) | (1 << (ZmeiLangParser.WRITE_MODE - 106)) | (1 << (ZmeiLangParser.BOOL - 106)) | (1 << (ZmeiLangParser.NL - 106)) | (1 << (ZmeiLangParser.ID - 106)) | (1 << (ZmeiLangParser.HASH - 106)))) != 0)):
                    break

            self.state = 2051
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_stream_target_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_target_modelContext,0)


        def an_stream_target_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_target_filterContext,0)


        def an_stream_field_list(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_stream_field_listContext,0)


        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def NL(self):
            return self.getToken(ZmeiLangParser.NL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_model" ):
                listener.enterAn_stream_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_model" ):
                listener.exitAn_stream_model(self)




    def an_stream_model(self):

        localctx = ZmeiLangParser.An_stream_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_an_stream_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2053
            self.an_stream_target_model()
            self.state = 2055
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2054
                self.an_stream_target_filter()


            self.state = 2058
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.EQUALS:
                self.state = 2057
                self.an_stream_field_list()


            self.state = 2061
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2060
                self.match(ZmeiLangParser.COMA)


            self.state = 2064
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,210,self._ctx)
            if la_ == 1:
                self.state = 2063
                self.match(ZmeiLangParser.NL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_target_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_target_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_target_model" ):
                listener.enterAn_stream_target_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_target_model" ):
                listener.exitAn_stream_target_model(self)




    def an_stream_target_model(self):

        localctx = ZmeiLangParser.An_stream_target_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_an_stream_target_model)
        try:
            self.state = 2068
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2066
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2067
                self.classname()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_target_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_target_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_target_filter" ):
                listener.enterAn_stream_target_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_target_filter" ):
                listener.exitAn_stream_target_filter(self)




    def an_stream_target_filter(self):

        localctx = ZmeiLangParser.An_stream_target_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_an_stream_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2070
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_field_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def an_stream_field_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_stream_field_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_stream_field_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_field_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_field_list" ):
                listener.enterAn_stream_field_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_field_list" ):
                listener.exitAn_stream_field_list(self)




    def an_stream_field_list(self):

        localctx = ZmeiLangParser.An_stream_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_an_stream_field_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2072
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2073
            self.match(ZmeiLangParser.GT)
            self.state = 2083
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.state = 2074
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.state = 2075
                self.an_stream_field_name()
                self.state = 2080
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,212,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 2076
                        self.match(ZmeiLangParser.COMA)
                        self.state = 2077
                        self.an_stream_field_name() 
                    self.state = 2082
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,212,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_stream_field_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_stream_field_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_stream_field_name" ):
                listener.enterAn_stream_field_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_stream_field_name" ):
                listener.exitAn_stream_field_name(self)




    def an_stream_field_name(self):

        localctx = ZmeiLangParser.An_stream_field_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_an_stream_field_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2085
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_reactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_react_type(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_typeContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_react_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_react_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react" ):
                listener.enterAn_react(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react" ):
                listener.exitAn_react(self)




    def an_react(self):

        localctx = ZmeiLangParser.An_reactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_an_react)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2087
            self.an_react_type()
            self.state = 2090
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2088
                self.match(ZmeiLangParser.DOT)
                self.state = 2089
                self.an_react_descriptor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_react_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_REACT(self):
            return self.getToken(ZmeiLangParser.AN_REACT, 0)

        def AN_REACT_CLIENT(self):
            return self.getToken(ZmeiLangParser.AN_REACT_CLIENT, 0)

        def AN_REACT_SERVER(self):
            return self.getToken(ZmeiLangParser.AN_REACT_SERVER, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react_type" ):
                listener.enterAn_react_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react_type" ):
                listener.exitAn_react_type(self)




    def an_react_type(self):

        localctx = ZmeiLangParser.An_react_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_an_react_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2092
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZmeiLangParser.AN_REACT) | (1 << ZmeiLangParser.AN_REACT_CLIENT) | (1 << ZmeiLangParser.AN_REACT_SERVER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_react_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_react_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_react_descriptor" ):
                listener.enterAn_react_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_react_descriptor" ):
                listener.exitAn_react_descriptor(self)




    def an_react_descriptor(self):

        localctx = ZmeiLangParser.An_react_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_an_react_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2094
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_htmlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_HTML(self):
            return self.getToken(ZmeiLangParser.AN_HTML, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_html_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_html_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_html

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_html" ):
                listener.enterAn_html(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_html" ):
                listener.exitAn_html(self)




    def an_html(self):

        localctx = ZmeiLangParser.An_htmlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_an_html)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2096
            self.match(ZmeiLangParser.AN_HTML)
            self.state = 2099
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2097
                self.match(ZmeiLangParser.DOT)
                self.state = 2098
                self.an_html_descriptor()


            self.state = 2101
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_html_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_html_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_html_descriptor" ):
                listener.enterAn_html_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_html_descriptor" ):
                listener.exitAn_html_descriptor(self)




    def an_html_descriptor(self):

        localctx = ZmeiLangParser.An_html_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_an_html_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2103
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_markdownContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MARKDOWN(self):
            return self.getToken(ZmeiLangParser.AN_MARKDOWN, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_markdown_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_markdown_descriptorContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_markdown

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_markdown" ):
                listener.enterAn_markdown(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_markdown" ):
                listener.exitAn_markdown(self)




    def an_markdown(self):

        localctx = ZmeiLangParser.An_markdownContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_an_markdown)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2105
            self.match(ZmeiLangParser.AN_MARKDOWN)
            self.state = 2108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2106
                self.match(ZmeiLangParser.DOT)
                self.state = 2107
                self.an_markdown_descriptor()


            self.state = 2110
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_markdown_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_markdown_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_markdown_descriptor" ):
                listener.enterAn_markdown_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_markdown_descriptor" ):
                listener.exitAn_markdown_descriptor(self)




    def an_markdown_descriptor(self):

        localctx = ZmeiLangParser.An_markdown_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_an_markdown_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2112
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_deleteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_DELETE(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_DELETE, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_delete

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_delete" ):
                listener.enterAn_crud_delete(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_delete" ):
                listener.exitAn_crud_delete(self)




    def an_crud_delete(self):

        localctx = ZmeiLangParser.An_crud_deleteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_an_crud_delete)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2114
            self.match(ZmeiLangParser.AN_CRUD_DELETE)
            self.state = 2115
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crudContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD(self):
            return self.getToken(ZmeiLangParser.AN_CRUD, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud" ):
                listener.enterAn_crud(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud" ):
                listener.exitAn_crud(self)




    def an_crud(self):

        localctx = ZmeiLangParser.An_crudContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_an_crud)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2117
            self.match(ZmeiLangParser.AN_CRUD)
            self.state = 2118
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_paramsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_target_model(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_target_modelContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_crud_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_descriptorContext,0)


        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_crud_target_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_target_filterContext,0)


        def an_crud_theme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_themeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_themeContext,i)


        def an_crud_skip(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_skipContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_skipContext,i)


        def an_crud_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_fieldsContext,i)


        def an_crud_list_fields(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_fieldsContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fieldsContext,i)


        def an_crud_pk_param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_pk_paramContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_pk_paramContext,i)


        def an_crud_item_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_item_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_item_nameContext,i)


        def an_crud_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_blockContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_blockContext,i)


        def an_crud_object_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_object_exprContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_object_exprContext,i)


        def an_crud_can_edit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_can_editContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_can_editContext,i)


        def an_crud_url_prefix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_url_prefixContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_url_prefixContext,i)


        def an_crud_link_suffix(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_link_suffixContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_link_suffixContext,i)


        def an_crud_list_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_typeContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_typeContext,i)


        def an_crud_header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_headerContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_headerContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def an_crud_next_page(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_pageContext,0)


        def an_crud_next_page_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_urlContext,0)


        def an_crud_page_override(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_page_overrideContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_page_overrideContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_params" ):
                listener.enterAn_crud_params(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_params" ):
                listener.exitAn_crud_params(self)




    def an_crud_params(self):

        localctx = ZmeiLangParser.An_crud_paramsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_an_crud_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.DOT:
                self.state = 2120
                self.match(ZmeiLangParser.DOT)
                self.state = 2121
                self.an_crud_descriptor()


            self.state = 2124
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2125
                self.match(ZmeiLangParser.NL)
                self.state = 2130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2131
            self.an_crud_target_model()
            self.state = 2133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2132
                self.an_crud_target_filter()


            self.state = 2152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,221,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2150
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [ZmeiLangParser.KW_THEME]:
                        self.state = 2135
                        self.an_crud_theme()
                        pass
                    elif token in [ZmeiLangParser.KW_SKIP]:
                        self.state = 2136
                        self.an_crud_skip()
                        pass
                    elif token in [ZmeiLangParser.KW_FIELDS]:
                        self.state = 2137
                        self.an_crud_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST_FIELDS]:
                        self.state = 2138
                        self.an_crud_list_fields()
                        pass
                    elif token in [ZmeiLangParser.KW_PK_PARAM]:
                        self.state = 2139
                        self.an_crud_pk_param()
                        pass
                    elif token in [ZmeiLangParser.KW_ITEM_NAME]:
                        self.state = 2140
                        self.an_crud_item_name()
                        pass
                    elif token in [ZmeiLangParser.KW_BLOCK]:
                        self.state = 2141
                        self.an_crud_block()
                        pass
                    elif token in [ZmeiLangParser.KW_OBJECT_EXPR]:
                        self.state = 2142
                        self.an_crud_object_expr()
                        pass
                    elif token in [ZmeiLangParser.KW_CAN_EDIT]:
                        self.state = 2143
                        self.an_crud_can_edit()
                        pass
                    elif token in [ZmeiLangParser.KW_URL_PREFIX]:
                        self.state = 2144
                        self.an_crud_url_prefix()
                        pass
                    elif token in [ZmeiLangParser.KW_LINK_SUFFIX]:
                        self.state = 2145
                        self.an_crud_link_suffix()
                        pass
                    elif token in [ZmeiLangParser.KW_LIST]:
                        self.state = 2146
                        self.an_crud_list_type()
                        pass
                    elif token in [ZmeiLangParser.KW_HEADER]:
                        self.state = 2147
                        self.an_crud_header()
                        pass
                    elif token in [ZmeiLangParser.NL]:
                        self.state = 2148
                        self.match(ZmeiLangParser.NL)
                        pass
                    elif token in [ZmeiLangParser.COMA]:
                        self.state = 2149
                        self.match(ZmeiLangParser.COMA)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 2154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,221,self._ctx)

            self.state = 2158
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,222,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2155
                    self.match(ZmeiLangParser.NL) 
                self.state = 2160
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,222,self._ctx)

            self.state = 2163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,223,self._ctx)
            if la_ == 1:
                self.state = 2161
                self.an_crud_next_page()

            elif la_ == 2:
                self.state = 2162
                self.an_crud_next_page_url()


            self.state = 2168
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,224,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2165
                    self.match(ZmeiLangParser.NL) 
                self.state = 2170
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,224,self._ctx)

            self.state = 2174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)) | (1 << (ZmeiLangParser.KW_DETAIL - 85)) | (1 << (ZmeiLangParser.KW_LIST - 85)))) != 0):
                self.state = 2171
                self.an_crud_page_override()
                self.state = 2176
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2177
                self.match(ZmeiLangParser.NL)
                self.state = 2182
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2183
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_page_overrideContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_view_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_view_nameContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def page_body(self):
            return self.getTypedRuleContext(ZmeiLangParser.Page_bodyContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_page_override

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_page_override" ):
                listener.enterAn_crud_page_override(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_page_override" ):
                listener.exitAn_crud_page_override(self)




    def an_crud_page_override(self):

        localctx = ZmeiLangParser.An_crud_page_overrideContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_an_crud_page_override)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2185
            self.an_crud_view_name()
            self.state = 2189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2186
                self.match(ZmeiLangParser.NL)
                self.state = 2191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2192
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,228,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2193
                    self.match(ZmeiLangParser.NL) 
                self.state = 2198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,228,self._ctx)

            self.state = 2199
            self.page_body()
            self.state = 2203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2200
                self.match(ZmeiLangParser.NL)
                self.state = 2205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2206
            self.match(ZmeiLangParser.BRACE_CLOSE)
            self.state = 2210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,230,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2207
                    self.match(ZmeiLangParser.NL) 
                self.state = 2212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,230,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_descriptor" ):
                listener.enterAn_crud_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_descriptor" ):
                listener.exitAn_crud_descriptor(self)




    def an_crud_descriptor(self):

        localctx = ZmeiLangParser.An_crud_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_an_crud_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2213
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_pageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_next_page_event_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_event_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page" ):
                listener.enterAn_crud_next_page(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page" ):
                listener.exitAn_crud_next_page(self)




    def an_crud_next_page(self):

        localctx = ZmeiLangParser.An_crud_next_pageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_an_crud_next_page)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2215
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2216
                self.an_crud_next_page_event_name()
                self.state = 2217
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2221
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2222
            self.match(ZmeiLangParser.GT)
            self.state = 2223
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_page_event_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_event_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_event_name" ):
                listener.enterAn_crud_next_page_event_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_event_name" ):
                listener.exitAn_crud_next_page_event_name(self)




    def an_crud_next_page_event_name(self):

        localctx = ZmeiLangParser.An_crud_next_page_event_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_an_crud_next_page_event_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2225
            _la = self._input.LA(1)
            if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_page_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def GT(self):
            return self.getToken(ZmeiLangParser.GT, 0)

        def an_crud_next_page_url_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_url_valContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_crud_next_page_event_name(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_next_page_event_nameContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_url" ):
                listener.enterAn_crud_next_page_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_url" ):
                listener.exitAn_crud_next_page_url(self)




    def an_crud_next_page_url(self):

        localctx = ZmeiLangParser.An_crud_next_page_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_an_crud_next_page_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.BRACE_OPEN:
                self.state = 2227
                self.match(ZmeiLangParser.BRACE_OPEN)
                self.state = 2228
                self.an_crud_next_page_event_name()
                self.state = 2229
                self.match(ZmeiLangParser.BRACE_CLOSE)


            self.state = 2233
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2234
            self.match(ZmeiLangParser.GT)
            self.state = 2235
            self.an_crud_next_page_url_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_next_page_url_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_next_page_url_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_next_page_url_val" ):
                listener.enterAn_crud_next_page_url_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_next_page_url_val" ):
                listener.exitAn_crud_next_page_url_val(self)




    def an_crud_next_page_url_val(self):

        localctx = ZmeiLangParser.An_crud_next_page_url_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_an_crud_next_page_url_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2237
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_target_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def model_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.Model_refContext,0)


        def classname(self):
            return self.getTypedRuleContext(ZmeiLangParser.ClassnameContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_target_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_target_model" ):
                listener.enterAn_crud_target_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_target_model" ):
                listener.exitAn_crud_target_model(self)




    def an_crud_target_model(self):

        localctx = ZmeiLangParser.An_crud_target_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_an_crud_target_model)
        try:
            self.state = 2241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.HASH]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2239
                self.model_ref()
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2240
                self.classname()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_target_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_target_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_target_filter" ):
                listener.enterAn_crud_target_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_target_filter" ):
                listener.exitAn_crud_target_filter(self)




    def an_crud_target_filter(self):

        localctx = ZmeiLangParser.An_crud_target_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_an_crud_target_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2243
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_themeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_THEME(self):
            return self.getToken(ZmeiLangParser.KW_THEME, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_theme

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_theme" ):
                listener.enterAn_crud_theme(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_theme" ):
                listener.exitAn_crud_theme(self)




    def an_crud_theme(self):

        localctx = ZmeiLangParser.An_crud_themeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_an_crud_theme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2245
            self.match(ZmeiLangParser.KW_THEME)
            self.state = 2246
            self.match(ZmeiLangParser.COLON)
            self.state = 2247
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_url_prefixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_URL_PREFIX(self):
            return self.getToken(ZmeiLangParser.KW_URL_PREFIX, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_url_prefix_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_url_prefix_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_url_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_url_prefix" ):
                listener.enterAn_crud_url_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_url_prefix" ):
                listener.exitAn_crud_url_prefix(self)




    def an_crud_url_prefix(self):

        localctx = ZmeiLangParser.An_crud_url_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_an_crud_url_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2249
            self.match(ZmeiLangParser.KW_URL_PREFIX)
            self.state = 2250
            self.match(ZmeiLangParser.COLON)
            self.state = 2251
            self.an_crud_url_prefix_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_url_prefix_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_url_prefix_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_url_prefix_val" ):
                listener.enterAn_crud_url_prefix_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_url_prefix_val" ):
                listener.exitAn_crud_url_prefix_val(self)




    def an_crud_url_prefix_val(self):

        localctx = ZmeiLangParser.An_crud_url_prefix_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_an_crud_url_prefix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2253
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_link_suffixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LINK_SUFFIX(self):
            return self.getToken(ZmeiLangParser.KW_LINK_SUFFIX, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_link_suffix_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_link_suffix_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_link_suffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_link_suffix" ):
                listener.enterAn_crud_link_suffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_link_suffix" ):
                listener.exitAn_crud_link_suffix(self)




    def an_crud_link_suffix(self):

        localctx = ZmeiLangParser.An_crud_link_suffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 462, self.RULE_an_crud_link_suffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2255
            self.match(ZmeiLangParser.KW_LINK_SUFFIX)
            self.state = 2256
            self.match(ZmeiLangParser.COLON)
            self.state = 2257
            self.an_crud_link_suffix_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_link_suffix_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_link_suffix_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_link_suffix_val" ):
                listener.enterAn_crud_link_suffix_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_link_suffix_val" ):
                listener.exitAn_crud_link_suffix_val(self)




    def an_crud_link_suffix_val(self):

        localctx = ZmeiLangParser.An_crud_link_suffix_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 464, self.RULE_an_crud_link_suffix_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2259
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_item_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_ITEM_NAME(self):
            return self.getToken(ZmeiLangParser.KW_ITEM_NAME, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_item_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_item_name" ):
                listener.enterAn_crud_item_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_item_name" ):
                listener.exitAn_crud_item_name(self)




    def an_crud_item_name(self):

        localctx = ZmeiLangParser.An_crud_item_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_an_crud_item_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2261
            self.match(ZmeiLangParser.KW_ITEM_NAME)
            self.state = 2262
            self.match(ZmeiLangParser.COLON)
            self.state = 2263
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_object_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_OBJECT_EXPR(self):
            return self.getToken(ZmeiLangParser.KW_OBJECT_EXPR, 0)

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_object_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_object_expr" ):
                listener.enterAn_crud_object_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_object_expr" ):
                listener.exitAn_crud_object_expr(self)




    def an_crud_object_expr(self):

        localctx = ZmeiLangParser.An_crud_object_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_an_crud_object_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2265
            self.match(ZmeiLangParser.KW_OBJECT_EXPR)
            self.state = 2269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2266
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2267
                self.match(ZmeiLangParser.COLON)
                self.state = 2268
                self.code_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_can_editContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CAN_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_CAN_EDIT, 0)

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_can_edit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_can_edit" ):
                listener.enterAn_crud_can_edit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_can_edit" ):
                listener.exitAn_crud_can_edit(self)




    def an_crud_can_edit(self):

        localctx = ZmeiLangParser.An_crud_can_editContext(self, self._ctx, self.state)
        self.enterRule(localctx, 470, self.RULE_an_crud_can_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2271
            self.match(ZmeiLangParser.KW_CAN_EDIT)
            self.state = 2275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2272
                self.code_line()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2273
                self.match(ZmeiLangParser.COLON)
                self.state = 2274
                self.code_block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_BLOCK(self):
            return self.getToken(ZmeiLangParser.KW_BLOCK, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_block" ):
                listener.enterAn_crud_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_block" ):
                listener.exitAn_crud_block(self)




    def an_crud_block(self):

        localctx = ZmeiLangParser.An_crud_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 472, self.RULE_an_crud_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2277
            self.match(ZmeiLangParser.KW_BLOCK)
            self.state = 2278
            self.match(ZmeiLangParser.COLON)
            self.state = 2279
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_pk_paramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PK_PARAM(self):
            return self.getToken(ZmeiLangParser.KW_PK_PARAM, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_pk_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_pk_param" ):
                listener.enterAn_crud_pk_param(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_pk_param" ):
                listener.exitAn_crud_pk_param(self)




    def an_crud_pk_param(self):

        localctx = ZmeiLangParser.An_crud_pk_paramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 474, self.RULE_an_crud_pk_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2281
            self.match(ZmeiLangParser.KW_PK_PARAM)
            self.state = 2282
            self.match(ZmeiLangParser.COLON)
            self.state = 2283
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_skipContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SKIP(self):
            return self.getToken(ZmeiLangParser.KW_SKIP, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_skip_values(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_skip_valuesContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_skip

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_skip" ):
                listener.enterAn_crud_skip(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_skip" ):
                listener.exitAn_crud_skip(self)




    def an_crud_skip(self):

        localctx = ZmeiLangParser.An_crud_skipContext(self, self._ctx, self.state)
        self.enterRule(localctx, 476, self.RULE_an_crud_skip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2285
            self.match(ZmeiLangParser.KW_SKIP)
            self.state = 2286
            self.match(ZmeiLangParser.COLON)
            self.state = 2287
            self.an_crud_skip_values()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_skip_valuesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_view_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_view_nameContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_view_nameContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_skip_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_skip_values" ):
                listener.enterAn_crud_skip_values(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_skip_values" ):
                listener.exitAn_crud_skip_values(self)




    def an_crud_skip_values(self):

        localctx = ZmeiLangParser.An_crud_skip_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 478, self.RULE_an_crud_skip_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2289
            self.an_crud_view_name()
            self.state = 2294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,236,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2290
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2291
                    self.an_crud_view_name() 
                self.state = 2296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,236,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_view_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_DELETE(self):
            return self.getToken(ZmeiLangParser.KW_DELETE, 0)

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def KW_CREATE(self):
            return self.getToken(ZmeiLangParser.KW_CREATE, 0)

        def KW_EDIT(self):
            return self.getToken(ZmeiLangParser.KW_EDIT, 0)

        def KW_DETAIL(self):
            return self.getToken(ZmeiLangParser.KW_DETAIL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_view_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_view_name" ):
                listener.enterAn_crud_view_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_view_name" ):
                listener.exitAn_crud_view_name(self)




    def an_crud_view_name(self):

        localctx = ZmeiLangParser.An_crud_view_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 480, self.RULE_an_crud_view_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2297
            _la = self._input.LA(1)
            if not(((((_la - 85)) & ~0x3f) == 0 and ((1 << (_la - 85)) & ((1 << (ZmeiLangParser.KW_DELETE - 85)) | (1 << (ZmeiLangParser.KW_EDIT - 85)) | (1 << (ZmeiLangParser.KW_CREATE - 85)) | (1 << (ZmeiLangParser.KW_DETAIL - 85)) | (1 << (ZmeiLangParser.KW_LIST - 85)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_fields_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_fields_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_fields" ):
                listener.enterAn_crud_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_fields" ):
                listener.exitAn_crud_fields(self)




    def an_crud_fields(self):

        localctx = ZmeiLangParser.An_crud_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 482, self.RULE_an_crud_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2299
            self.match(ZmeiLangParser.KW_FIELDS)
            self.state = 2300
            self.match(ZmeiLangParser.COLON)
            self.state = 2301
            self.an_crud_fields_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST(self):
            return self.getToken(ZmeiLangParser.KW_LIST, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_list_type_var(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_type_varContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_type" ):
                listener.enterAn_crud_list_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_type" ):
                listener.exitAn_crud_list_type(self)




    def an_crud_list_type(self):

        localctx = ZmeiLangParser.An_crud_list_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 484, self.RULE_an_crud_list_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2303
            self.match(ZmeiLangParser.KW_LIST)
            self.state = 2304
            self.match(ZmeiLangParser.COLON)
            self.state = 2305
            self.an_crud_list_type_var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_type_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_INLINE_TYPE_TABULAR(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_TABULAR, 0)

        def KW_INLINE_TYPE_STACKED(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_STACKED, 0)

        def KW_INLINE_TYPE_POLYMORPHIC(self):
            return self.getToken(ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_type_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_type_var" ):
                listener.enterAn_crud_list_type_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_type_var" ):
                listener.exitAn_crud_list_type_var(self)




    def an_crud_list_type_var(self):

        localctx = ZmeiLangParser.An_crud_list_type_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 486, self.RULE_an_crud_list_type_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2307
            _la = self._input.LA(1)
            if not(((((_la - 94)) & ~0x3f) == 0 and ((1 << (_la - 94)) & ((1 << (ZmeiLangParser.KW_INLINE_TYPE_TABULAR - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_STACKED - 94)) | (1 << (ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC - 94)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_headerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_HEADER(self):
            return self.getToken(ZmeiLangParser.KW_HEADER, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_header_enabled(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_header_enabledContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_header" ):
                listener.enterAn_crud_header(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_header" ):
                listener.exitAn_crud_header(self)




    def an_crud_header(self):

        localctx = ZmeiLangParser.An_crud_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 488, self.RULE_an_crud_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2309
            self.match(ZmeiLangParser.KW_HEADER)
            self.state = 2310
            self.match(ZmeiLangParser.COLON)
            self.state = 2311
            self.an_crud_header_enabled()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_header_enabledContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOL(self):
            return self.getToken(ZmeiLangParser.BOOL, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_header_enabled

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_header_enabled" ):
                listener.enterAn_crud_header_enabled(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_header_enabled" ):
                listener.exitAn_crud_header_enabled(self)




    def an_crud_header_enabled(self):

        localctx = ZmeiLangParser.An_crud_header_enabledContext(self, self._ctx, self.state)
        self.enterRule(localctx, 490, self.RULE_an_crud_header_enabled)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2313
            self.match(ZmeiLangParser.BOOL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_fields_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_fieldContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_fields_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_fields_expr" ):
                listener.enterAn_crud_fields_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_fields_expr" ):
                listener.exitAn_crud_fields_expr(self)




    def an_crud_fields_expr(self):

        localctx = ZmeiLangParser.An_crud_fields_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 492, self.RULE_an_crud_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2315
            self.an_crud_field()
            self.state = 2320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,237,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2316
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2317
                    self.an_crud_field() 
                self.state = 2322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,237,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_field_spec(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_field_specContext,0)


        def an_crud_field_filter(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_field_filterContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field" ):
                listener.enterAn_crud_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field" ):
                listener.exitAn_crud_field(self)




    def an_crud_field(self):

        localctx = ZmeiLangParser.An_crud_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 494, self.RULE_an_crud_field)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2323
            self.an_crud_field_spec()
            self.state = 2325
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2324
                self.an_crud_field_filter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_field_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def EXCLUDE(self):
            return self.getToken(ZmeiLangParser.EXCLUDE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field_spec" ):
                listener.enterAn_crud_field_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field_spec" ):
                listener.exitAn_crud_field_spec(self)




    def an_crud_field_spec(self):

        localctx = ZmeiLangParser.An_crud_field_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 496, self.RULE_an_crud_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2332
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2327
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2328
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2331
                self.id_or_kw()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_field_filterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_field_filter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_field_filter" ):
                listener.enterAn_crud_field_filter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_field_filter" ):
                listener.exitAn_crud_field_filter(self)




    def an_crud_field_filter(self):

        localctx = ZmeiLangParser.An_crud_field_filterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 498, self.RULE_an_crud_field_filter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2334
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fieldsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_LIST_FIELDS(self):
            return self.getToken(ZmeiLangParser.KW_LIST_FIELDS, 0)

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_crud_list_fields_expr(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fields_exprContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_fields

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_fields" ):
                listener.enterAn_crud_list_fields(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_fields" ):
                listener.exitAn_crud_list_fields(self)




    def an_crud_list_fields(self):

        localctx = ZmeiLangParser.An_crud_list_fieldsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 500, self.RULE_an_crud_list_fields)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2336
            self.match(ZmeiLangParser.KW_LIST_FIELDS)
            self.state = 2337
            self.match(ZmeiLangParser.COLON)
            self.state = 2338
            self.an_crud_list_fields_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fields_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_list_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_crud_list_fieldContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_fieldContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_fields_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_fields_expr" ):
                listener.enterAn_crud_list_fields_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_fields_expr" ):
                listener.exitAn_crud_list_fields_expr(self)




    def an_crud_list_fields_expr(self):

        localctx = ZmeiLangParser.An_crud_list_fields_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 502, self.RULE_an_crud_list_fields_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2340
            self.an_crud_list_field()
            self.state = 2345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,241,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2341
                    self.match(ZmeiLangParser.COMA)
                    self.state = 2342
                    self.an_crud_list_field() 
                self.state = 2347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,241,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_fieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_crud_list_field_spec(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_list_field_specContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_field

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_field" ):
                listener.enterAn_crud_list_field(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_field" ):
                listener.exitAn_crud_list_field(self)




    def an_crud_list_field(self):

        localctx = ZmeiLangParser.An_crud_list_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 504, self.RULE_an_crud_list_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2348
            self.an_crud_list_field_spec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_list_field_specContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STAR(self):
            return self.getToken(ZmeiLangParser.STAR, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def EXCLUDE(self):
            return self.getToken(ZmeiLangParser.EXCLUDE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list_field_spec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list_field_spec" ):
                listener.enterAn_crud_list_field_spec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list_field_spec" ):
                listener.exitAn_crud_list_field_spec(self)




    def an_crud_list_field_spec(self):

        localctx = ZmeiLangParser.An_crud_list_field_specContext(self, self._ctx, self.state)
        self.enterRule(localctx, 506, self.RULE_an_crud_list_field_spec)
        self._la = 0 # Token type
        try:
            self.state = 2355
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2350
                self.match(ZmeiLangParser.STAR)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID, ZmeiLangParser.EXCLUDE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2352
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZmeiLangParser.EXCLUDE:
                    self.state = 2351
                    self.match(ZmeiLangParser.EXCLUDE)


                self.state = 2354
                self.id_or_kw()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_postContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_POST(self):
            return self.getToken(ZmeiLangParser.AN_POST, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_post

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_post" ):
                listener.enterAn_post(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_post" ):
                listener.exitAn_post(self)




    def an_post(self):

        localctx = ZmeiLangParser.An_postContext(self, self._ctx, self.state)
        self.enterRule(localctx, 508, self.RULE_an_post)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2357
            self.match(ZmeiLangParser.AN_POST)
            self.state = 2359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2358
                self.code_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_authContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_AUTH(self):
            return self.getToken(ZmeiLangParser.AN_AUTH, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_auth

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_auth" ):
                listener.enterAn_auth(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_auth" ):
                listener.exitAn_auth(self)




    def an_auth(self):

        localctx = ZmeiLangParser.An_authContext(self, self._ctx, self.state)
        self.enterRule(localctx, 510, self.RULE_an_auth)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2361
            self.match(ZmeiLangParser.AN_AUTH)
            self.state = 2363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2362
                self.code_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_createContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_CREATE(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_CREATE, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_create" ):
                listener.enterAn_crud_create(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_create" ):
                listener.exitAn_crud_create(self)




    def an_crud_create(self):

        localctx = ZmeiLangParser.An_crud_createContext(self, self._ctx, self.state)
        self.enterRule(localctx, 512, self.RULE_an_crud_create)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2365
            self.match(ZmeiLangParser.AN_CRUD_CREATE)
            self.state = 2366
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_editContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_EDIT(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_EDIT, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_edit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_edit" ):
                listener.enterAn_crud_edit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_edit" ):
                listener.exitAn_crud_edit(self)




    def an_crud_edit(self):

        localctx = ZmeiLangParser.An_crud_editContext(self, self._ctx, self.state)
        self.enterRule(localctx, 514, self.RULE_an_crud_edit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2368
            self.match(ZmeiLangParser.AN_CRUD_EDIT)
            self.state = 2369
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_LIST(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_LIST, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_list" ):
                listener.enterAn_crud_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_list" ):
                listener.exitAn_crud_list(self)




    def an_crud_list(self):

        localctx = ZmeiLangParser.An_crud_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 516, self.RULE_an_crud_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2371
            self.match(ZmeiLangParser.AN_CRUD_LIST)
            self.state = 2372
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menuContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_MENU(self):
            return self.getToken(ZmeiLangParser.AN_MENU, 0)

        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def an_menu_descriptor(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_descriptorContext,0)


        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_menu_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_menu_itemContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_menu_itemContext,i)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu" ):
                listener.enterAn_menu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu" ):
                listener.exitAn_menu(self)




    def an_menu(self):

        localctx = ZmeiLangParser.An_menuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 518, self.RULE_an_menu)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2374
            self.match(ZmeiLangParser.AN_MENU)
            self.state = 2375
            self.match(ZmeiLangParser.DOT)
            self.state = 2376
            self.an_menu_descriptor()
            self.state = 2377
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2381
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,246,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2378
                    self.match(ZmeiLangParser.NL) 
                self.state = 2383
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,246,self._ctx)

            self.state = 2385 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2384
                    self.an_menu_item()

                else:
                    raise NoViableAltException(self)
                self.state = 2387 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,247,self._ctx)

            self.state = 2392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2389
                self.match(ZmeiLangParser.NL)
                self.state = 2394
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2395
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_descriptorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_descriptor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_descriptor" ):
                listener.enterAn_menu_descriptor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_descriptor" ):
                listener.exitAn_menu_descriptor(self)




    def an_menu_descriptor(self):

        localctx = ZmeiLangParser.An_menu_descriptorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 520, self.RULE_an_menu_descriptor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2397
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_itemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_menu_label(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_labelContext,0)


        def an_menu_item_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_codeContext,0)


        def an_menu_target(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_targetContext,0)


        def COMA(self):
            return self.getToken(ZmeiLangParser.COMA, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.NL)
            else:
                return self.getToken(ZmeiLangParser.NL, i)

        def an_menu_item_args(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_argsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item" ):
                listener.enterAn_menu_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item" ):
                listener.exitAn_menu_item(self)




    def an_menu_item(self):

        localctx = ZmeiLangParser.An_menu_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 522, self.RULE_an_menu_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.COMA:
                self.state = 2399
                self.match(ZmeiLangParser.COMA)


            self.state = 2405
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.NL:
                self.state = 2402
                self.match(ZmeiLangParser.NL)
                self.state = 2407
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.SQ_BRACE_OPEN:
                self.state = 2408
                self.an_menu_item_args()


            self.state = 2411
            self.an_menu_label()
            self.state = 2414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.ASSIGN]:
                self.state = 2412
                self.an_menu_item_code()
                pass
            elif token in [ZmeiLangParser.COLON]:
                self.state = 2413
                self.an_menu_target()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2419
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,253,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2416
                    self.match(ZmeiLangParser.NL) 
                self.state = 2421
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,253,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_targetContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(ZmeiLangParser.COLON, 0)

        def an_menu_item_page(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_pageContext,0)


        def an_menu_item_url(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_urlContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_target" ):
                listener.enterAn_menu_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_target" ):
                listener.exitAn_menu_target(self)




    def an_menu_target(self):

        localctx = ZmeiLangParser.An_menu_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 524, self.RULE_an_menu_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2422
            self.match(ZmeiLangParser.COLON)
            self.state = 2425
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.KW_PAGE]:
                self.state = 2423
                self.an_menu_item_page()
                pass
            elif token in [ZmeiLangParser.STRING_DQ, ZmeiLangParser.STRING_SQ]:
                self.state = 2424
                self.an_menu_item_url()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def code_line(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_lineContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_code" ):
                listener.enterAn_menu_item_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_code" ):
                listener.exitAn_menu_item_code(self)




    def an_menu_item_code(self):

        localctx = ZmeiLangParser.An_menu_item_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 526, self.RULE_an_menu_item_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2427
            self.code_line()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SQ_BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_OPEN, 0)

        def an_menu_item_arg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.An_menu_item_argContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_argContext,i)


        def SQ_BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.SQ_BRACE_CLOSE, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(ZmeiLangParser.COMA)
            else:
                return self.getToken(ZmeiLangParser.COMA, i)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_args" ):
                listener.enterAn_menu_item_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_args" ):
                listener.exitAn_menu_item_args(self)




    def an_menu_item_args(self):

        localctx = ZmeiLangParser.An_menu_item_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 528, self.RULE_an_menu_item_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2429
            self.match(ZmeiLangParser.SQ_BRACE_OPEN)
            self.state = 2430
            self.an_menu_item_arg()
            self.state = 2435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ZmeiLangParser.COMA:
                self.state = 2431
                self.match(ZmeiLangParser.COMA)
                self.state = 2432
                self.an_menu_item_arg()
                self.state = 2437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 2438
            self.match(ZmeiLangParser.SQ_BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_argContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def an_menu_item_arg_key(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_arg_keyContext,0)


        def EQUALS(self):
            return self.getToken(ZmeiLangParser.EQUALS, 0)

        def an_menu_item_arg_val(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_arg_valContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg" ):
                listener.enterAn_menu_item_arg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg" ):
                listener.exitAn_menu_item_arg(self)




    def an_menu_item_arg(self):

        localctx = ZmeiLangParser.An_menu_item_argContext(self, self._ctx, self.state)
        self.enterRule(localctx, 530, self.RULE_an_menu_item_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2440
            self.an_menu_item_arg_key()
            self.state = 2441
            self.match(ZmeiLangParser.EQUALS)
            self.state = 2442
            self.an_menu_item_arg_val()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_arg_keyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg_key

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg_key" ):
                listener.enterAn_menu_item_arg_key(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg_key" ):
                listener.exitAn_menu_item_arg_key(self)




    def an_menu_item_arg_key(self):

        localctx = ZmeiLangParser.An_menu_item_arg_keyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 532, self.RULE_an_menu_item_arg_key)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2444
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_arg_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_arg_val

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_arg_val" ):
                listener.enterAn_menu_item_arg_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_arg_val" ):
                listener.exitAn_menu_item_arg_val(self)




    def an_menu_item_arg_val(self):

        localctx = ZmeiLangParser.An_menu_item_arg_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 534, self.RULE_an_menu_item_arg_val)
        try:
            self.state = 2449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2446
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2447
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2448
                self.id_or_kw()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_urlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_url

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_url" ):
                listener.enterAn_menu_item_url(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_url" ):
                listener.exitAn_menu_item_url(self)




    def an_menu_item_url(self):

        localctx = ZmeiLangParser.An_menu_item_urlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 536, self.RULE_an_menu_item_url)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2451
            _la = self._input.LA(1)
            if not(_la==ZmeiLangParser.STRING_DQ or _la==ZmeiLangParser.STRING_SQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_pageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_PAGE(self):
            return self.getToken(ZmeiLangParser.KW_PAGE, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_menu_item_page_ref(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_menu_item_page_refContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_page

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_page" ):
                listener.enterAn_menu_item_page(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_page" ):
                listener.exitAn_menu_item_page(self)




    def an_menu_item_page(self):

        localctx = ZmeiLangParser.An_menu_item_pageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 538, self.RULE_an_menu_item_page)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2453
            self.match(ZmeiLangParser.KW_PAGE)
            self.state = 2454
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2455
            self.an_menu_item_page_ref()
            self.state = 2456
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_item_page_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_or_kw(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZmeiLangParser.Id_or_kwContext)
            else:
                return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,i)


        def DOT(self):
            return self.getToken(ZmeiLangParser.DOT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_item_page_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_item_page_ref" ):
                listener.enterAn_menu_item_page_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_item_page_ref" ):
                listener.exitAn_menu_item_page_ref(self)




    def an_menu_item_page_ref(self):

        localctx = ZmeiLangParser.An_menu_item_page_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 540, self.RULE_an_menu_item_page_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2461
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,257,self._ctx)
            if la_ == 1:
                self.state = 2458
                self.id_or_kw()
                self.state = 2459
                self.match(ZmeiLangParser.DOT)


            self.state = 2463
            self.id_or_kw()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_menu_labelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_DQ(self):
            return self.getToken(ZmeiLangParser.STRING_DQ, 0)

        def STRING_SQ(self):
            return self.getToken(ZmeiLangParser.STRING_SQ, 0)

        def id_or_kw(self):
            return self.getTypedRuleContext(ZmeiLangParser.Id_or_kwContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_menu_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_menu_label" ):
                listener.enterAn_menu_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_menu_label" ):
                listener.exitAn_menu_label(self)




    def an_menu_label(self):

        localctx = ZmeiLangParser.An_menu_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 542, self.RULE_an_menu_label)
        try:
            self.state = 2468
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZmeiLangParser.STRING_DQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2465
                self.match(ZmeiLangParser.STRING_DQ)
                pass
            elif token in [ZmeiLangParser.STRING_SQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2466
                self.match(ZmeiLangParser.STRING_SQ)
                pass
            elif token in [ZmeiLangParser.KW_AUTH_TYPE_BASIC, ZmeiLangParser.KW_AUTH_TYPE_SESSION, ZmeiLangParser.KW_AUTH_TYPE_TOKEN, ZmeiLangParser.COL_FIELD_TYPE_LONGTEXT, ZmeiLangParser.COL_FIELD_TYPE_HTML, ZmeiLangParser.COL_FIELD_TYPE_HTML_MEDIA, ZmeiLangParser.COL_FIELD_TYPE_FLOAT, ZmeiLangParser.COL_FIELD_TYPE_DECIMAL, ZmeiLangParser.COL_FIELD_TYPE_DATE, ZmeiLangParser.COL_FIELD_TYPE_DATETIME, ZmeiLangParser.COL_FIELD_TYPE_CREATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_UPDATE_TIME, ZmeiLangParser.COL_FIELD_TYPE_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FILE, ZmeiLangParser.COL_FIELD_TYPE_FILER_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_FILER_IMAGE_FOLDER, ZmeiLangParser.COL_FIELD_TYPE_TEXT, ZmeiLangParser.COL_FIELD_TYPE_INT, ZmeiLangParser.COL_FIELD_TYPE_SLUG, ZmeiLangParser.COL_FIELD_TYPE_BOOL, ZmeiLangParser.COL_FIELD_TYPE_ONE, ZmeiLangParser.COL_FIELD_TYPE_ONE2ONE, ZmeiLangParser.COL_FIELD_TYPE_MANY, ZmeiLangParser.COL_FIELD_CHOICES, ZmeiLangParser.KW_THEME, ZmeiLangParser.KW_INSTALL, ZmeiLangParser.KW_HEADER, ZmeiLangParser.KW_SERVICES, ZmeiLangParser.KW_SELENIUM_PYTEST, ZmeiLangParser.KW_CHILD, ZmeiLangParser.KW_FILTER_OUT, ZmeiLangParser.KW_FILTER_IN, ZmeiLangParser.KW_PAGE, ZmeiLangParser.KW_LINK_SUFFIX, ZmeiLangParser.KW_URL_PREFIX, ZmeiLangParser.KW_CAN_EDIT, ZmeiLangParser.KW_OBJECT_EXPR, ZmeiLangParser.KW_BLOCK, ZmeiLangParser.KW_ITEM_NAME, ZmeiLangParser.KW_PK_PARAM, ZmeiLangParser.KW_LIST_FIELDS, ZmeiLangParser.KW_DELETE, ZmeiLangParser.KW_EDIT, ZmeiLangParser.KW_CREATE, ZmeiLangParser.KW_DETAIL, ZmeiLangParser.KW_SKIP, ZmeiLangParser.KW_FROM, ZmeiLangParser.KW_POLY_LIST, ZmeiLangParser.KW_CSS, ZmeiLangParser.KW_JS, ZmeiLangParser.KW_INLINE_TYPE_TABULAR, ZmeiLangParser.KW_INLINE_TYPE_STACKED, ZmeiLangParser.KW_INLINE_TYPE_POLYMORPHIC, ZmeiLangParser.KW_INLINE, ZmeiLangParser.KW_TYPE, ZmeiLangParser.KW_USER_FIELD, ZmeiLangParser.KW_ANNOTATE, ZmeiLangParser.KW_ON_CREATE, ZmeiLangParser.KW_QUERY, ZmeiLangParser.KW_AUTH, ZmeiLangParser.KW_COUNT, ZmeiLangParser.KW_I18N, ZmeiLangParser.KW_EXTENSION, ZmeiLangParser.KW_TABS, ZmeiLangParser.KW_LIST, ZmeiLangParser.KW_READ_ONLY, ZmeiLangParser.KW_LIST_EDITABLE, ZmeiLangParser.KW_LIST_FILTER, ZmeiLangParser.KW_LIST_SEARCH, ZmeiLangParser.KW_FIELDS, ZmeiLangParser.KW_IMPORT, ZmeiLangParser.KW_AS, ZmeiLangParser.WRITE_MODE, ZmeiLangParser.BOOL, ZmeiLangParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2467
                self.id_or_kw()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_crud_detailContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_CRUD_DETAIL(self):
            return self.getToken(ZmeiLangParser.AN_CRUD_DETAIL, 0)

        def an_crud_params(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_crud_paramsContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_crud_detail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_crud_detail" ):
                listener.enterAn_crud_detail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_crud_detail" ):
                listener.exitAn_crud_detail(self)




    def an_crud_detail(self):

        localctx = ZmeiLangParser.An_crud_detailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 544, self.RULE_an_crud_detail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2470
            self.match(ZmeiLangParser.AN_CRUD_DETAIL)
            self.state = 2471
            self.an_crud_params()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_priority_markerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_PRIORITY(self):
            return self.getToken(ZmeiLangParser.AN_PRIORITY, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_priority_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_priority_marker" ):
                listener.enterAn_priority_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_priority_marker" ):
                listener.exitAn_priority_marker(self)




    def an_priority_marker(self):

        localctx = ZmeiLangParser.An_priority_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 546, self.RULE_an_priority_marker)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2473
            self.match(ZmeiLangParser.AN_PRIORITY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_getContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_GET(self):
            return self.getToken(ZmeiLangParser.AN_GET, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZmeiLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_get

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_get" ):
                listener.enterAn_get(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_get" ):
                listener.exitAn_get(self)




    def an_get(self):

        localctx = ZmeiLangParser.An_getContext(self, self._ctx, self.state)
        self.enterRule(localctx, 548, self.RULE_an_get)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2475
            self.match(ZmeiLangParser.AN_GET)
            self.state = 2477
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZmeiLangParser.CODE_BLOCK:
                self.state = 2476
                self.code_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_errorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AN_ERROR(self):
            return self.getToken(ZmeiLangParser.AN_ERROR, 0)

        def BRACE_OPEN(self):
            return self.getToken(ZmeiLangParser.BRACE_OPEN, 0)

        def an_error_code(self):
            return self.getTypedRuleContext(ZmeiLangParser.An_error_codeContext,0)


        def BRACE_CLOSE(self):
            return self.getToken(ZmeiLangParser.BRACE_CLOSE, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_error

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_error" ):
                listener.enterAn_error(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_error" ):
                listener.exitAn_error(self)




    def an_error(self):

        localctx = ZmeiLangParser.An_errorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 550, self.RULE_an_error)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2479
            self.match(ZmeiLangParser.AN_ERROR)
            self.state = 2480
            self.match(ZmeiLangParser.BRACE_OPEN)
            self.state = 2481
            self.an_error_code()
            self.state = 2482
            self.match(ZmeiLangParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class An_error_codeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIGIT(self):
            return self.getToken(ZmeiLangParser.DIGIT, 0)

        def getRuleIndex(self):
            return ZmeiLangParser.RULE_an_error_code

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAn_error_code" ):
                listener.enterAn_error_code(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAn_error_code" ):
                listener.exitAn_error_code(self)




    def an_error_code(self):

        localctx = ZmeiLangParser.An_error_codeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 552, self.RULE_an_error_code)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2484
            self.match(ZmeiLangParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






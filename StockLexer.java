// Generated from Stock.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class StockLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, DATE=8, TIME=9, 
		FLOAT=10, INT=11, NEWLINE=12, WHITESPACE=13;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "DATE", "TIME", 
			"FLOAT", "INT", "NEWLINE", "WHITESPACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Date'", "','", "'Open'", "'High'", "'Low'", "'Close'", "'Volume'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, "DATE", "TIME", "FLOAT", 
			"INT", "NEWLINE", "WHITESPACE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public StockLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Stock.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\rp\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0004\u0007?\b\u0007\u000b\u0007\f\u0007@\u0001\u0007"+
		"\u0001\u0007\u0004\u0007E\b\u0007\u000b\u0007\f\u0007F\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0004"+
		"\tY\b\t\u000b\t\f\tZ\u0001\t\u0001\t\u0004\t_\b\t\u000b\t\f\t`\u0001\n"+
		"\u0004\nd\b\n\u000b\n\f\ne\u0001\u000b\u0003\u000bi\b\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0000\u0000\r\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u0001\u0000\u0002\u0001"+
		"\u000009\u0002\u0000\t\t  u\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0001\u001b\u0001"+
		"\u0000\u0000\u0000\u0003 \u0001\u0000\u0000\u0000\u0005\"\u0001\u0000"+
		"\u0000\u0000\u0007\'\u0001\u0000\u0000\u0000\t,\u0001\u0000\u0000\u0000"+
		"\u000b0\u0001\u0000\u0000\u0000\r6\u0001\u0000\u0000\u0000\u000f>\u0001"+
		"\u0000\u0000\u0000\u0011N\u0001\u0000\u0000\u0000\u0013X\u0001\u0000\u0000"+
		"\u0000\u0015c\u0001\u0000\u0000\u0000\u0017h\u0001\u0000\u0000\u0000\u0019"+
		"l\u0001\u0000\u0000\u0000\u001b\u001c\u0005D\u0000\u0000\u001c\u001d\u0005"+
		"a\u0000\u0000\u001d\u001e\u0005t\u0000\u0000\u001e\u001f\u0005e\u0000"+
		"\u0000\u001f\u0002\u0001\u0000\u0000\u0000 !\u0005,\u0000\u0000!\u0004"+
		"\u0001\u0000\u0000\u0000\"#\u0005O\u0000\u0000#$\u0005p\u0000\u0000$%"+
		"\u0005e\u0000\u0000%&\u0005n\u0000\u0000&\u0006\u0001\u0000\u0000\u0000"+
		"\'(\u0005H\u0000\u0000()\u0005i\u0000\u0000)*\u0005g\u0000\u0000*+\u0005"+
		"h\u0000\u0000+\b\u0001\u0000\u0000\u0000,-\u0005L\u0000\u0000-.\u0005"+
		"o\u0000\u0000./\u0005w\u0000\u0000/\n\u0001\u0000\u0000\u000001\u0005"+
		"C\u0000\u000012\u0005l\u0000\u000023\u0005o\u0000\u000034\u0005s\u0000"+
		"\u000045\u0005e\u0000\u00005\f\u0001\u0000\u0000\u000067\u0005V\u0000"+
		"\u000078\u0005o\u0000\u000089\u0005l\u0000\u00009:\u0005u\u0000\u0000"+
		":;\u0005m\u0000\u0000;<\u0005e\u0000\u0000<\u000e\u0001\u0000\u0000\u0000"+
		"=?\u0007\u0000\u0000\u0000>=\u0001\u0000\u0000\u0000?@\u0001\u0000\u0000"+
		"\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AB\u0001\u0000"+
		"\u0000\u0000BD\u0005/\u0000\u0000CE\u0007\u0000\u0000\u0000DC\u0001\u0000"+
		"\u0000\u0000EF\u0001\u0000\u0000\u0000FD\u0001\u0000\u0000\u0000FG\u0001"+
		"\u0000\u0000\u0000GH\u0001\u0000\u0000\u0000HI\u0005/\u0000\u0000IJ\u0007"+
		"\u0000\u0000\u0000JK\u0007\u0000\u0000\u0000KL\u0007\u0000\u0000\u0000"+
		"LM\u0007\u0000\u0000\u0000M\u0010\u0001\u0000\u0000\u0000NO\u0007\u0000"+
		"\u0000\u0000OP\u0007\u0000\u0000\u0000PQ\u0005:\u0000\u0000QR\u0007\u0000"+
		"\u0000\u0000RS\u0007\u0000\u0000\u0000ST\u0005:\u0000\u0000TU\u0007\u0000"+
		"\u0000\u0000UV\u0007\u0000\u0000\u0000V\u0012\u0001\u0000\u0000\u0000"+
		"WY\u0007\u0000\u0000\u0000XW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000ZX\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0001\u0000"+
		"\u0000\u0000\\^\u0005.\u0000\u0000]_\u0007\u0000\u0000\u0000^]\u0001\u0000"+
		"\u0000\u0000_`\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000a\u0014\u0001\u0000\u0000\u0000bd\u0007\u0000\u0000"+
		"\u0000cb\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000ec\u0001\u0000"+
		"\u0000\u0000ef\u0001\u0000\u0000\u0000f\u0016\u0001\u0000\u0000\u0000"+
		"gi\u0005\r\u0000\u0000hg\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000"+
		"ij\u0001\u0000\u0000\u0000jk\u0005\n\u0000\u0000k\u0018\u0001\u0000\u0000"+
		"\u0000lm\u0007\u0001\u0000\u0000mn\u0001\u0000\u0000\u0000no\u0006\f\u0000"+
		"\u0000o\u001a\u0001\u0000\u0000\u0000\u0007\u0000@FZ`eh\u0001\u0006\u0000"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
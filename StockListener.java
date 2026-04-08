// Generated from Stock.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link StockParser}.
 */
public interface StockListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link StockParser#file}.
	 * @param ctx the parse tree
	 */
	void enterFile(StockParser.FileContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#file}.
	 * @param ctx the parse tree
	 */
	void exitFile(StockParser.FileContext ctx);
	/**
	 * Enter a parse tree produced by {@link StockParser#header}.
	 * @param ctx the parse tree
	 */
	void enterHeader(StockParser.HeaderContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#header}.
	 * @param ctx the parse tree
	 */
	void exitHeader(StockParser.HeaderContext ctx);
	/**
	 * Enter a parse tree produced by {@link StockParser#row}.
	 * @param ctx the parse tree
	 */
	void enterRow(StockParser.RowContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#row}.
	 * @param ctx the parse tree
	 */
	void exitRow(StockParser.RowContext ctx);
	/**
	 * Enter a parse tree produced by {@link StockParser#datetime}.
	 * @param ctx the parse tree
	 */
	void enterDatetime(StockParser.DatetimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#datetime}.
	 * @param ctx the parse tree
	 */
	void exitDatetime(StockParser.DatetimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link StockParser#price}.
	 * @param ctx the parse tree
	 */
	void enterPrice(StockParser.PriceContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#price}.
	 * @param ctx the parse tree
	 */
	void exitPrice(StockParser.PriceContext ctx);
	/**
	 * Enter a parse tree produced by {@link StockParser#volume}.
	 * @param ctx the parse tree
	 */
	void enterVolume(StockParser.VolumeContext ctx);
	/**
	 * Exit a parse tree produced by {@link StockParser#volume}.
	 * @param ctx the parse tree
	 */
	void exitVolume(StockParser.VolumeContext ctx);
}
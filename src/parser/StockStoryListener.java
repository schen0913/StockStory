package src.parser;
import java.util.ArrayList;
import java.util.List;

public class StockStoryListener extends StockBaseListener 
{

    private List<StockRecord> records = new ArrayList<>();

    @Override
    public void enterRow(StockParser.RowContext ctx) {
        String date   = ctx.datetime().DATE().getText();
        float open    = Float.parseFloat(ctx.price(0).getText());
        float high    = Float.parseFloat(ctx.price(1).getText());
        float low     = Float.parseFloat(ctx.price(2).getText());
        float close   = Float.parseFloat(ctx.price(3).getText());
        long volume   = Long.parseLong(ctx.volume().INT().getText());

        records.add(new StockRecord(date, open, high, low, close, volume));
    }

    public List<StockRecord> getRecords() {
        return records;
    }
}

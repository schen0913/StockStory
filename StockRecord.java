public class StockRecord 
{
    public String date;
    public float open;
    public float high;
    public float low;
    public float close;
    public long volume;

    public StockRecord(String date, float open, float high,float low, float close, long volume) 
    {
        this.date   = date;
        this.open   = open;
        this.high   = high;
        this.low    = low;
        this.close  = close;
        this.volume = volume;
    }

    @Override
    public String toString() 
    {
        return date + " O:" + open + " H:" + high + " L:" + low + " C:" + close + " V:" + volume;
    }
}
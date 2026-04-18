import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;

import src.parser.StockRecord;
import src.parser.StockStoryListener;

import java.io.*;
import java.util.List;

public class Main 
{
    public static void main(String[] args) throws Exception 
    {
        String inputPath  = args[0];   // ex. input.csv
        String outputPath = args[1];   // ex. records.json

        // Lex and Parse
        CharStream input         = CharStreams.fromFileName(inputPath);
        StockLexer lexer         = new StockLexer(input);
        CommonTokenStream tokens  = new CommonTokenStream(lexer);
        StockParser parser        = new StockParser(tokens);

        ParseTree tree = parser.file();

        // Walk tree with listener
        StockStoryListener listener = new StockStoryListener();
        ParseTreeWalker.DEFAULT.walk(listener, tree);

        // Write JSON
        List<StockRecord> records = listener.getRecords();
        writeJSON(records, outputPath);

        System.out.println("Parsed " + records.size() + " rows -> " + outputPath);
    
    }//end main

    private static void writeJSON(List<StockRecord> records, String path) throws Exception 
    {
        StringBuilder sb = new StringBuilder();
        
        sb.append("[\n");
        for (int i = 0; i < records.size(); i++) 
            {
            StockRecord r = records.get(i);
            sb.append("  {");
            sb.append("\"date\":\"").append(r.date).append("\",");
            sb.append("\"open\":").append(r.open).append(",");
            sb.append("\"high\":").append(r.high).append(",");
            sb.append("\"low\":").append(r.low).append(",");
            sb.append("\"close\":").append(r.close).append(",");
            sb.append("\"volume\":").append(r.volume);
            sb.append("}");
            if (i < records.size() - 1) sb.append(",");
            sb.append("\n");
        }
        sb.append("]");

        FileWriter fw = new FileWriter(path);
        fw.write(sb.toString());
        fw.close();

    }//end writeJSON
}
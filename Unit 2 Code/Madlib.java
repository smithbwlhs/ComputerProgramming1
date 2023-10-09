import java.util.Scanner;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.io.File;
import java.io.FileWriter;

public class Madlib {
    static void parse(File input, File output) throws Exception {
        FileWriter results = new FileWriter(output);
        Scanner entry = new Scanner(System.in);
        Scanner source = new Scanner(input);

        System.out.print("Enter your name: ");
        String name = entry.nextLine();
        if(!name.isBlank()) results.write("Name: " + name + "\n");

        DateTimeFormatter form = DateTimeFormatter.ofPattern("MM/dd/yyyy");
        LocalDate date = LocalDate.now();
        results.write("Date: " + form.format(date) + "\n\n");

        boolean escape = false;
        String prompt = "";
        source.useDelimiter("");

        while(source.hasNext()) {
            char next = source.next().charAt(0);
            if(escape) {
                escape = false;
                if(prompt.length() == 0) results.write(next);
                else prompt += next;
                continue;
            }
            if(next == '\\') {
                escape = true;
                continue;
            }
            if(!prompt.isEmpty()) {
                if(next == '_') {
                    if(prompt.trim().matches("^[aeiou].*")) System.out.print("Enter an" + prompt + ": ");
                    else System.out.print("Enter a" + prompt + ": ");
                    results.write(entry.nextLine());
                    prompt = "";
                }
                else prompt = prompt + next;
                continue;
            }
            if(next == '_') {
                prompt = prompt + " "; 
                continue;
            }
            results.write(next);
        }

        results.close();
        source.close();
    }

    static void validate(String input, String output) throws Exception {
        final String red = "\u001B[31m";
        final String green = "\u001B[32m";
        final String def = "\u001B[0m";

        File in = new File(input);
        if(!in.canRead()) {
            System.out.println(red + "Error:" + def + " Cannot open source file.");
            return;
        }

        File out = new File(output);
        try {
            if(out.exists()) out.delete();
            out.createNewFile();
            if(!out.canWrite()) {
                System.out.println(red + "Error:" + def + " Cannot write output file.");
                return;
            }
        }
        catch(Exception e) {
            System.out.println(red + "Error:" + def + " Cannot write output file.");
            return;
        }
        
        parse(in, out);
        System.out.println(green + "Complete:" + def + " View your results in " + output + ".");
    }

    static void help() {
        String h1 = "Usage: java Madlib.java input [output]\n";
        String h2 = "Default output file: results.txt\n";
        String h3 = "\n";
        String h4 = "Source File Syntax:\n";
        String h5 = "   Underscores denote user input.\n";
        String h6 = "   For example, _verb_ denotes a user entry for a verb.\n";
        String h7 = "   Backslashes can be used to escape special characters.\n";
        String h8 = "   For example, \\_ prints a backslash without prompting for user input.\n";
        System.out.println(h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8);
    }

    public static void main(String[] args) throws Exception {
        switch(args.length) {
            case 1: validate(args[0], "results.txt");
            break;
            case 2: validate(args[0], args[1]);
            break;
            default: help();
            break;
        }
    }
}
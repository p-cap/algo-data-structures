// next time will have package info
import java.util.Arrays;
import java.util.List;
import java.util.Collections;


class Reverse {
    public static void main(String[] args) {
        System.out.println(reverse_sentence(args[0]));
    }

    public static String reverse_sentence(String sentence) {

        String[] cleanSample = sentence.replaceAll("\\s+", " ").split(" ");;

        List<String> saved = Arrays.asList(cleanSample);

        Collections.reverse(saved);

        String finalString = String.join(" ", saved);

        return finalString;
    }
}


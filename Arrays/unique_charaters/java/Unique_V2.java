import java.util.*; 

class Unique_V2 {
    public static void main(String[] args) {
        System.out.println(unikwa(args[0]));
    }

    public static Boolean unikwa (String characters) {
        Set<String> my_set = new HashSet<String>(); 

        for(int i = 0; i < characters.length(); i++) {
            char c = characters.charAt(i);
            String s = String.valueOf(c);

            if(my_set.contains(s)) {
                return false;
            } else {
                my_set.add(s);
            }
        }

        return true;
    }

}
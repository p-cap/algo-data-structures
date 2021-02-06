import java.util.*; 

class Unique {
    public static void main(String[] args) {
        
        Set<String> my_set = new HashSet<String>(); 

        for(int i = 0; i < args[0].length(); i++) {
            char c = args[0].charAt(i);
            String s = String.valueOf(c);
            my_set.add(s);
        }

        if (my_set.size() != args[0].length()) {            
            System.out.println("NOT");
        } else {
            System.out.println("The characters are UNIQUE");
        }
    }

}


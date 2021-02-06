import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.Stack;

class BalanceCheck {
    public static void main(String[] args) {
        BalanceCheck balanceCheck = new BalanceCheck();
        System.out.println(balanceCheck.balance(args[0]));
    }

    public Boolean balance(String bracString) {
        
        // creates the set to store all potential openning brackets
        Set<String> openningBracketSet = new HashSet<String>();
        openningBracketSet.add("(");
        openningBracketSet.add("[");
        openningBracketSet.add("{");

        // creates the pairing between the openning and closing bracket
        Map<String, String> brackets = new HashMap<String, String>();
        brackets.put("(", ")");
        brackets.put("[", "]");
        brackets.put("{", "}");

        // changes bracString into an array of characters
        char[] chars = bracString.toCharArray();

        // creates an empty stack temporarily store openning brackets
        Stack<String> storedOpenningBrackets = new Stack<String>();

        for(char item: chars) {

            // converted item into string so it can be compared to 
            // openning bracket set
            String temp = Character.toString(item);
            if(openningBracketSet.contains(temp)) {
                storedOpenningBrackets.add(temp);
            }
            else {
               if (storedOpenningBrackets.size() == 0) {
                    return false;                   
                }
                String lastOpenBracket = storedOpenningBrackets.pop();
                if(!brackets.get(lastOpenBracket).equals(temp)) {
                    return false;
                }
            }
        }
        return storedOpenningBrackets.size() == 0;
    }
}
public class ContinuousSum {
    public static void main(String args[]) {
        int[] myArray = {1,2,-1,3,4,10,10,-10,-1};

        System.out.println(maxSum(myArray));
    }

    public static int maxSum (int [] arr) {

        int max = arr[0];
        int current = arr[0];
        
        for (int i = 1; i < arr.length; i++) {
            current = Math.max(current + arr[i], arr[i]);

            max = Math.max(current, max);
        }

        return max;
    }
}

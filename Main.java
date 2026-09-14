public class Main {
    public static void main(String []args) {

        Boolean prime = true; 
        for(int i=2; i<500; i++)
        {
            for (int j = 2; j<(i/2+1); j++) 
            {
                if( i % j == 0) {
                    prime = false;
                    break;
                }   else {
                    prime = true; 
                }
            }
            if (prime)
                System.out.println(i);
        }



    }
}
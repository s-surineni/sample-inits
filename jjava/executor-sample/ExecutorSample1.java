import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class ExecutorSample1 {
    public static void main(String[] args) {
        System.out.println("Hi");
        ExecutorService executorService = Executors.newFixedThreadPool(10);

        executorService.execute(new Runnable() {
            public void run() {
                System.out.println("Asynchronous task");
            }
        });

        executorService.shutdown();

    }
}


import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class MapSample {
    public static void main(String[] args) {
        HashMap<String, List<String>> dcPod = new HashMap<>();
//        ArrayList<String> lo2Pods = new ArrayList<>();
        String[] lo2Pods = {"cs119"};
        dcPod.put("lo2", Arrays.asList(lo2Pods));

        String[] ia2Pods = {"cs29","cs34","cs36","cs37","na122","na136","na141"};
        dcPod.put("ia2", Arrays.asList(ia2Pods));

        for (String dc: dcPod.keySet()) {
            System.out.println(dcPod.get(dc));
        }
    }
}

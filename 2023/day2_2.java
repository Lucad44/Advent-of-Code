import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class day2_2 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        int ans = 0;
        try {
            String line = br.readLine();
            int id;
            int i = 1;
            while (line != null) {
                if (i < 10) {
                    id = line.charAt(5) - '0';
                }
                else if (i < 100) {
                    id = Integer.parseInt(line.substring(5, 7));
                }
                else {
                    id = 100;
                }
                int start = 7 + ((i >= 10) ? 1 : 0) + ((i >= 100) ? 1 : 0);
                line = line.substring(start);
                String[] lineSplit = line.split(";");
                int[] maximums = new int[3];
                for (String s: lineSplit) {
                    Pattern pattern = Pattern.compile("(\\d+)\\s+(\\w+)");
                    Matcher matcher = pattern.matcher(s);
                    int[] counter = new int[3];
                    while (matcher.find()) {
                        String colour = matcher.group(2);
                        int num = Integer.parseInt(matcher.group(1));
                        switch (colour) {
                            case "red":
                                counter[0] = num;
                                break;
                            case "green":
                                counter[1] = num;
                                break;
                            case "blue":
                                counter[2] = num;
                                break;
                        }
                    }
                    for (int j = 0; j < 3; ++j) {
                        maximums[j] = Math.max(maximums[j], counter[j]);
                    }
                }
                int curr = 1;
                for (int x: maximums) {
                    curr *= x;
                }
                ans += curr;
                line = br.readLine();
                i++;
            }
        }
        finally {
            br.close();
        }
        System.out.println("ans: " + ans);
    }
}

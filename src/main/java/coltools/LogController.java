package coltools;

import com.google.gson.Gson;

import java.util.List;

/**
 * Created by elliot on 09/08/2018.
 */
public class LogController {

    public static String[] getLog(Environment enviro, String id){

        CollibraRest utils = new CollibraRest(enviro.getBaseUrl(), enviro.getUsername(), enviro.getPassword());

        String output = utils.getData("log/service/" + id + "/content?filename=dgc.log&lines=200");

        System.out.println(output);

        output = output.replace("[", "");
        output = output.replace("]", "");



        return output.split(",");
    }
}

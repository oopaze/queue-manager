package ClientTS.managers;

public class MessageManager {
    public static String ARGS_TEMPLATE = "{\"action\": \"%s\", \"args\": [%s]}";
    public static String ACTION_TEMPLATE = "{\"action\": \"%s\"}";

    public static String decode(String message) {
        return message;
    }

    public static String encode(String message) {
        return String.format(MessageManager.ACTION_TEMPLATE, message);
    }

    public static String encode(String message, String[] args) {
        String argsStr = "";
        Integer counter = 0;


        for(String arg: args) {
            argsStr += arg;
            
            if (!counter.equals(args.length)) {
                argsStr += ", ";
            }
            counter++;
        }

        return String.format(MessageManager.ARGS_TEMPLATE, message, argsStr);
    }
}

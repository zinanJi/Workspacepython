import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class stream{
    public static void main(String[] args){
        List<String> list = Arrays.asList("www","vip","vipshop","com");
        list.stream().map(String::toUpperCase).filter(s->s.length()==3).sorted().collect(Collectors.toList()).forEach(System.out::println);;


        // Optional.ofNullable(list).orElse(new ArrayList<String>()).stream().peek(System.out::println).filter(s->s.length() == 3).findFirst().get();

        // list.stream().peek(System.out::println).filter(s->s.length() == 3).findFirst().get();
    }
    
}

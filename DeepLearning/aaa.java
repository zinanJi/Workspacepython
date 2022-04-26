
@FunctionalInterface
interface Converter<F, T> {
    T convert(F from);
}

Converter<String, Integer> converter = (from) -> Integer.valueOf(from);
Integer converted = converter.convert("123");
System.out.println(converted);    // 123


Converter<String, Integer> converter = Interger::valueOf;
Integer converted = converter.convert("123");
System.out.println(converted);    // 123

class Something {
    String s;

    Something(String s) {
        this.s = s
    }
    
    String startsWith() {
        return String.valueOf(s.charAt(0));
    }
}

Something something = new Something();
Converter<String, String> converter = (from) -> something.startsWith(from);
String converted = converter.convert(new Somthing("Java"));
System.out.println(converted);    // "J"

Something something = new Something();
Converter<String, String> converter = something::startsWith;
String converted = converter.convert(new Somthing("Java"));
System.out.println(converted);    // "J"

Something something = new Something();
Converter<String, String> converter = Something::startsWith;
String converted = converter.convert(new Somthing("Java"));
System.out.println(converted);    // "J"



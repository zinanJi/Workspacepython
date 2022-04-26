class Person {
    String firstName;
    String lastName;

    Person() {}

    Person(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}

// Person 工厂
interface PersonFactory<P extends Person> {
    P create(String firstName, String lastName);


// 直接引用 Person 构造器
PersonFactory<Person> personFactory = Person::new;
Person person = personFactory.create("Peter", "Parker");
}
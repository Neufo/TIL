using System;

namespace DISample
{
    class Program
    {
        static void Main(string[] args)
        {
            IPeople people = new PersonList();
            IPerson p1 = new Person("tako");
            IPerson p2 = new Person("hara");
            IPerson p3 = new Person("nao");
            people.Add(p1);
            people.Add(p2);
            people.Add(p3);

            people.Hello();

        }
    }
}

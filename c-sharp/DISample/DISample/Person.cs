using System;
using System.Collections.Generic;
using System.Text;

namespace DISample
{
    internal class Person : IPerson
    {
        private string Name { get; set; }

        public Person(string name)
        {
            this.Name = name;
        }

        public void Hello()
        {
            Console.WriteLine($"Hello. I'm {this.Name}.");
        }
    }
}

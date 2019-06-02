using System;
using System.Collections.Generic;
using System.Text;

namespace DISample
{
    internal class PersonList: IPeople
    {
        private List<IPerson> People { get; } = new List<IPerson>();

        public void Add(IPerson person)
        {
            this.People.Add(person);
        }

        public void Hello()
        {
            foreach (IPerson person in this.People)
            {
                person.Hello();
            }
        }
    }
}

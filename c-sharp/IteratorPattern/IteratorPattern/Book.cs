using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorPattern
{
    public class Book
    {
        public String Name { get; }

        public Book(string name)
        {
            this.Name = name;
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorPattern
{
    class Program
    {
        static void Main(string[] args)
        {
            var shelf = new BookShelf();
            for (int i = 0; i < 10; i++)
            {
                shelf.AppendBook(new Book("name" + i));
            }

            var iter = shelf.Iterator();
            while(iter.HasNext())
            {
                Console.WriteLine(iter.Next().Name);
            }
        }
    }
}

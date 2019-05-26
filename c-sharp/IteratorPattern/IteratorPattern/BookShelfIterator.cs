using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorPattern
{
    public class BookShelfIterator : IIterator<Book>
    {
        private BookShelf BookShelf { get; }

        private int Index { get; set; }

        public BookShelfIterator(BookShelf shelf)
        {
            this.BookShelf = shelf;
        }

        public bool HasNext()
        {
            return this.Index < this.BookShelf.Length;
        }

        public Book Next()
        {
            if(this.HasNext())
            {
                var next = this.BookShelf.GetBookAt(this.Index);
                this.Index++;
                return next;
            }
            else
            {
                return null;
            }
        }
    }
}

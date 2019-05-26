using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace IteratorPattern
{
    public class BookShelf:IAggregate<Book>
    {
        private Book[] books = new Book[0];

        public int Length
        {
            get => this.books.Length;
        }

        public IIterator<Book> Iterator() => new BookShelfIterator(this);

        public Book GetBookAt(int i)
        {
            if(i < books.Length)
            {
                return this.books[i];
            }
            else
            {
                throw new IndexOutOfRangeException();
            }
        }

        public void AppendBook(Book book)
        {
            var cache = this.books;
            this.books = new Book[this.books.Length+1];
            for(int i = 0; i < this.books.Length -1; i++)
            {
                this.books[i] = cache[i];
            }

            this.books[this.books.Length - 1] = book;
        }
    }
}

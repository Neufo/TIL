using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Singleton
{
    public class Singleton
    {
        private static Singleton instance = new Singleton();

        public static Singleton Instance { get => Singleton.instance; }

        private Singleton()
        {
            Console.WriteLine("constructor executed");
        }

        public void Hello()
        {
            Console.WriteLine("hello!");
        }
    }
}

using System;
using System.Collections.Generic;
using System.Text;

namespace DISample
{
    interface IPeople : IPerson
    {
        void Add(IPerson person);
    }
}

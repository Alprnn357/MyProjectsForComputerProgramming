using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TakingFactorial
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int input;

            Console.Write("Enter a number (Bir sayı giriniz): ");
            input = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("{0}! = {1}", input, fakt(input));
            Console.ReadKey();

        }

        static int fakt(int number)
        {
            int result = 1;
            if(number == 0 || number == 1)
            {
                return result;
            }
            else if(number < 0)
            {
                return result;
            }
            else
            {
                return result * number * fakt(number - 1);
            }

        }
    }
}

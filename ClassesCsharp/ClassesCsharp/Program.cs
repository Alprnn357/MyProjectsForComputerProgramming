using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace ClassesCsharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Personal ps1 = new Personal();
            Global gl1 = new Global();

            Console.Write("Type your first name: ");
            ps1.Fname = Console.ReadLine();

            Console.Write("Type your last name: ");
            ps1.Lname = Console.ReadLine();

            Console.Write("Type your ID number: ");
            ps1.Id = Convert.ToInt32(Console.ReadLine());

            Console.Write("Type your Profession: ");
            gl1.ProfName = Console.ReadLine();

            Console.Write("Type your revenue: ");
            gl1.Revenue = Convert.ToInt64(Console.ReadLine());

            Console.Write("Type your city that live in: ");
            gl1.City = Console.ReadLine();


            Console.Clear();

            ps1.ShowInfo();
            gl1.ShowInfo();

            Console.ReadKey();
        }
    }

    public class Personal
    {
        public string Fname { get; set; }
        public string Lname { get; set; }
        public int Id { get; set; }

        public void ShowInfo()
        {
            Console.WriteLine("Name: " +  Fname);
            Console.WriteLine("Surname: " +  Lname);
            Console.WriteLine("Your ID: " +  Id);
        }

    }

    public class Global
    {
        public string ProfName { get; set; }
        public long Revenue { get; set; }
        public string City { get; set; }
        public void ShowInfo()
        {
            Console.WriteLine("Profession name: " + ProfName);
            Console.WriteLine("Your revenue: " + Revenue);
            Console.WriteLine("Your city that live in: " + City);
        }
    }

}

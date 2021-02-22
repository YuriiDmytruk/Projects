using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace Task1Class
{
    static class Validator
    {
        public static string Validate(string value, string validateInfo)
        {
            if (value == "null" | value == null)
            {
                return null;
            }
            else
            {
                if (!Regex.IsMatch(value, GetPatern(validateInfo)))
                {
                    value = null;
                }
                return value;
            }
        }
        public static bool ValidateAndInform(string value, string validateInfo)
        {
            if (value == "null" | value == null)
            {
                Console.WriteLine("The entered value has not been validated");
                return false;
            }
            else
            {
                if (!Regex.IsMatch(value, GetPatern(validateInfo)))
                {
                    Console.WriteLine("The entered value has not been validated");
                    return false;
                }
                return true;
            }
        }
        private static string GetPatern(string validateInfo)
        {
            string patern = validateInfo;
            Dictionary<string, string> defaultPaterns = new Dictionary<string, string>
        {
            {"numbers", @"^[0-9]+$"},
            {"letters", @"^[a-zA-Z]+$"},
            //dd-mm-yyyy
            {"date", @"(((0|1)[0-9]|2[0-9]|3[0-1])\-(0[1-9]|1[0-2])\-((19|20)\d\d))$"},
            //www.*.com
            {"url", @"www.[a-zA-Z0-9]+.com$"},
            //+nnn(nn)nnn-nn-nn
            {"phone", @"\+[0-9]{3}\([0-9]{2}\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}"},
            {"double", @"^[\+\-]?\d*\.?[Ee]?[\+\-]?\d*$"},
            //*@*.*
            {"email", @"[a-zA-Z0-9]+(@)[a-zA-Z]+(.)[a-zA-Z]+"}
        };
            if (!defaultPaterns.TryGetValue(validateInfo, out patern))
            {
                patern = validateInfo;
            }
            return patern;
        }
    }
}

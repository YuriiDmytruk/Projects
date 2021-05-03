using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace RestAPI
{
    public class Validator
    {
        public List<string> errorList = new List<string>();

        public string Validate(string value, string validateInfo)
        {
            if (value != null & validateInfo != null)
            {
                if (!Regex.IsMatch(value, GetPatern(validateInfo)))
                {
                    value = null;
                    errorList.Add("Validation Error in " + validateInfo + " field");
                }
                return value;
            }
            else
            {
                return null;
            }
        }

        public void Add(string value)
        {
            errorList.Add(value);
        }

        private static string GetPatern(string validateInfo)
        {
            string patern = validateInfo;
            Dictionary<string, string> defaultPaterns = new Dictionary<string, string>
        {
            {"title", @"^[a-zA-Z]+$"},
            {"director_name", @"^[a-zA-Z]+$"},
            {"website_url", @"www.[a-zA-Z0-9]+.com$"},
            {"phone_number", @"\+[0-9]{3}\([0-9]{2}\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}"},
            {"monthly_budget", @"^[\+\-]?\d*\.?[Ee]?[\+\-]?\d*$"},
            {"yearly_budget", @"^[\+\-]?\d*\.?[Ee]?[\+\-]?\d*$"}
        };
            if (!defaultPaterns.TryGetValue(validateInfo, out patern))
            {
                patern = validateInfo;
            }
            return patern;
        }


    }
}
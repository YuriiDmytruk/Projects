using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task1Class
{
    class Validator
    {
        public string value;
        public string key;

        public void Set(string new_value, string new_key)
        {
            value = new_value;
            key = new_key;
        }

        public Validator(string value, string key)
        {
            this.value = value;
            this.key = key;
        }

        public char[] GetAllowSymbols()
        {


            string allow_str = "";


            string numbers = "0123456789";
            string letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM";
            string url = letters + ".";
            string phone = numbers + "()-+";
            string all_allowed = url + phone;


            switch (key)
            {
                case "all":
                    allow_str = all_allowed;
                    break;
                case "numbers":
                    allow_str = numbers;
                    break;
                case "url":
                    allow_str = url;
                    break;
                case "phone":
                    allow_str = phone;
                    break;
                case "letters":
                    allow_str = letters;
                    break;
                default:
                    Console.WriteLine("Unknown key");
                    break;
            }

            char[] allow_arr = new char[allow_str.Length];
            allow_arr = allow_str.ToCharArray();
            return allow_arr;
        }

        public string Validate()
        {
            string word = value;
            char[] word_arr = new char[word.Length];
            word_arr = word.ToCharArray();
            char[] allow_symbols = GetAllowSymbols();
            word_arr = DeleteNotAllowedSymbols(word_arr, allow_symbols);
            word = CharArrToStr(word_arr);
            return word;
        }

        public char[] DeleteNotAllowedSymbols(char[] word_arr, char[] symbols_arr)
        {
            List<char> help_list = new List<char>();
            for (int word_iterator = 0; word_iterator < word_arr.Length; word_iterator++)
            {
                for (int symbol_iterator = 0; symbol_iterator < symbols_arr.Length; symbol_iterator++)
                {
                    if (word_arr[word_iterator] == symbols_arr[symbol_iterator])
                    {
                        help_list.Add(word_arr[word_iterator]);
                    }
                }
            }
            char[] help_arr = new char[help_list.Count];
            for (int i = 0; i < help_list.Count; i++)
            {
                help_arr[i] = help_list[i];
            }
            return help_arr;
        }

        public string CharArrToStr(char[] arr)
        {
            string word = "";
            foreach(char x in arr)
            {
                word += x;
            }
            return word;
        }
    } 
}

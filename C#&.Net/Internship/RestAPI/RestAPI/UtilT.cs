using System;
using System.Collections.Generic;

namespace RestAPI
{
    public class UtilT<T>
    {
        public static List<T> Swap(List<T> list, int x, int y)
        {
            if (list != null & x >= 0 & y > 0)
            {
                T t = list[x];
                list[x] = list[y];
                list[y] = t;

                return list;
            }
            else
            {
                return new List<T>();
            }
        }

        public static bool Contains(T container, T textToFind)
        {
            if (container != null & textToFind != null)
            {
                char[] find_arr = Convert.ToString(textToFind).ToCharArray();
                char[] check_arr = Convert.ToString(container).ToCharArray();
                char[] plus_arr = new char[find_arr.Length];
                for (int check_counter = 0; check_counter < check_arr.Length - find_arr.Length + 1; check_counter++)
                {
                    for (int find_counter = 0; find_counter < find_arr.Length; find_counter++)
                    {
                        if (find_arr[find_counter] == check_arr[check_counter + find_counter])
                        {
                            plus_arr[find_counter] = '+';
                        }
                        else
                        {
                            plus_arr[find_counter] = '-';
                        }
                    }
                    bool x = true;
                    for (int i = 0; i < plus_arr.Length; i++)
                    {

                        if (plus_arr[i] != '+')
                        {
                            x = false;
                            break;
                        }
                    }
                    if (x)
                    {
                        return true;
                    }
                }
                return false;
            }
            else
            {
                return false;
            }
        }

        public static string DeleteLastChar(T value)
        {
            if (value != null)
            {
                string str = value.ToString();
                List<char> list = new List<char>(str.ToCharArray());
                list.RemoveAt(list.Count - 1);
                str = "";
                foreach (char x in list)
                {
                    str += x;
                }
                return str;
            }
            else
            {
                return "";
            }
        }
    }
}

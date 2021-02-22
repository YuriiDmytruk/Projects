﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

namespace Task1Class
{
    static class Util
    {
        public static bool Contains(string container, string find)
        {
            char[] find_arr = find.ToCharArray();
            char[] check_arr = container.ToCharArray();
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
        public static List<object> Swap(List<object> list, int indexFrom, int indexTo)
        {
            Object help = list[indexFrom];
            list[indexFrom] = list[indexTo];
            list[indexTo] = help;
            return list;
        }
        public static int FindElement(List<object> dataList, string text)
        {
            string id;
            Console.Write(text);
            id = Console.ReadLine();
            int listId = -1;
            for (int i = 0; i < dataList.Count; i++)
            {
                if (ObjectManager.GetValue(dataList[i], "id") == id)
                {
                    listId = i;
                    break;
                }
            }
            return listId;
        }
        public static List<string> GetFiles(string directoryName)
        {
            string projectDirectory = Directory.GetParent(directoryName).Parent.FullName;
            string folderName = @"\DataFiles";
            return new List<string>(Directory.GetFiles(projectDirectory + folderName, "*.txt"));
        }
        public static List<string> ToFileNamesOnly(List<string> files)
        {
            List<string> fileNames = new List<string>();
            for (int index = 0; index < files.Count; index++)
            {
                fileNames.Add(files[index].Split('\\')[files[index].Split('\\').Length - 1]);
            }
            return fileNames;
        }
        public static int AskUserForChoice(List<string> options)
        {
            for (int index = 0; index < options.Count; index++)
            {
                Console.WriteLine("{0} - {1}", index, options[index]);
            }

            while (true)
            {
                Console.Write("Select: ");
                string choise = Console.ReadLine();
                if (Regex.IsMatch(choise, "^[0-9]+$"))
                {
                    int result = Convert.ToInt32(choise);
                    if (result >= 0 & result < options.Count)
                    {
                        return result;
                    }
                    else
                    {
                        Console.WriteLine("Wrong id");
                    }
                }
                else
                {
                    Console.WriteLine("The entered value is not a number");
                }
            }
        }

    }
}

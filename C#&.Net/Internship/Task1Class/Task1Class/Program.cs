using System;
using System.Collections.Generic;
using System.IO;

namespace Task1Class
{
    class Program
    {
        static void End()
        {
            Console.WriteLine("Press any key to exit.");
            System.Console.ReadKey();
        }

        static void Main(string[] args)
        {
            List<Department> dep_info_list = new List<Department>();
            dep_info_list = ReadFromFile(dep_info_list);

            Console.WriteLine("Information that was read from the file");
            PrintAll(dep_info_list);

            bool exit = false;
            while (exit == false)
            {
                Console.WriteLine("0 - Exit\n" +
                    "1 - Search\n" +
                    "2 - Sort\n" +
                    "3 - Delete\n" +
                    "4 - Add\n" +
                    "5 - Cheange\n" + 
                    "6 - Print\n");
                string choose = Console.ReadLine();
                switch (choose)
                {
                    case "0":
                        exit = true;
                        break;
                    case "1":
                        Search(dep_info_list);
                        break;
                    case "2":
                        Sort(dep_info_list);
                        break;
                    case "3":
                        Delete(dep_info_list);
                        break;
                    case "4":
                        Add(dep_info_list);
                        break;
                    case "5":
                        Cheange(dep_info_list);
                        break;
                    case "6":
                        PrintAll(dep_info_list);
                        break;
                    default:
                        Console.WriteLine("Unknown command");
                        break;
                }

            }
            End();
        }

        static List<Department> ReadFromFile(List<Department> dep_info_list)
            {
            string all_text = File.ReadAllText(@"C:\Users\Admin\source\repos\YuriiDmytruk\Projects\C#&.Net\Internship\Task1Class\Task1Class\DepInfoFile.txt");
            char[] text_by_letter = new char[all_text.Length];
            text_by_letter = all_text.ToCharArray();

            List<string> word_list = new List<string>();

            string word = "";
            foreach (char letter in text_by_letter)
            {
                if (letter == ';')
                {
                    Validator to_valid = new Validator(word, "all");
                    word = to_valid.Validate();
                    word_list.Add(word);
                    char[] x = new char[word.Length];
                    x = word.ToCharArray();
                    word = "";
                }
                else if(letter == ' ')
                {
                    continue;
                }
                else if (letter == ':')
                {

                    Department to_add = new Department();
                    to_add.SetDep(word_list);
                    dep_info_list.Add(to_add);
                    word_list.Clear();
                }
                else
                {
                    word += letter;
                }
            }
            return dep_info_list;
            }

        static void Search(List<Department> dep_info_list)
        {

            List<Department> found = new List<Department>();

            Console.WriteLine("Input text");
            string to_find = Console.ReadLine();

            string word_to_check;
            Department curent_dep;
            for(int dep_counter = 0; dep_counter < dep_info_list.Count; dep_counter++)
            {
                curent_dep = dep_info_list[dep_counter];
                for(int field_counter = 0; field_counter < curent_dep.Count(); field_counter++)
                {
                    word_to_check = curent_dep.Get(curent_dep.GetFieldName(field_counter));
                    
                    if (to_find.Length > word_to_check.Length) { break; }
                    else
                    {
                        bool find = false;
                        find = Comp(word_to_check, to_find);
                        if (find == true)
                        {
                            found.Add(curent_dep);
                            break;
                        }
                    }
                }
            }
            foreach(Department x in found)
            {
                x.Print();
            }
            if (found.Count == 0)
            {
                Console.WriteLine("Nothing found");
            }
        }

        static bool Comp(string check, string find)
        {
            char[] find_arr = new char[find.Length];
            char[] check_arr = new char[check.Length];
            check_arr = check.ToCharArray();
            find_arr = find.ToCharArray();
            char[] plus_arr = new char[find_arr.Length];
            for(int check_counter = 0; check_counter < check_arr.Length - find_arr.Length + 1; check_counter++)
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
                for(int i = 0; i < plus_arr.Length;i++)
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

        static List<Department> Sort(List<Department> dep_info_list)
        {
            Console.WriteLine("What do you want to sort by?");
            Console.WriteLine("id; title; director_name; phone_number; monthly_budget; yearly_budget; website_url");
            string key = Console.ReadLine();
            int len = dep_info_list.Count;

            List<Department> copy = new List<Department>();
            copy = dep_info_list;
            if (copy[0].Get(key) != null)
            {
                for (int i = 1; i < len; i++)
                {
                    for (int j = 0; j < len - i; j++)
                    {
                        if (String.Compare(copy[j].Get(key), copy[j + 1].Get(key)) > 0)
                        {
                            Swap(j, j + 1, copy);
                        }
                    }
                }
                dep_info_list = Save(dep_info_list, copy);
                return dep_info_list;
            }
            else
            {
                return dep_info_list;
            }
        }

        static List<Department> Swap (int x, int y, List<Department> dep_info_list)
        {
            Department help = dep_info_list[x];
            dep_info_list[x] = dep_info_list[y];
            dep_info_list[y] = help;
            return dep_info_list;
        }

        static void PrintAll(List<Department> dep_info_list)
        {
            foreach(Department x in dep_info_list)
            {
                x.Print();
            }
            Console.WriteLine("------------------------------");
        }

        static List<Department> Add(List<Department> dep_info_list)
        {
            Department new_dep = new Department();
            List<string> new_list = new List<string>();
            Console.WriteLine("Input department info:");
            string[] masseges = new string[] {"Id: ", "Title: ", "Director name: ", "Phone number: ", "Monthly budget: ", "Yearly budget: ", "Website url: "};
            string value_to_add;
            for(int i = 0; i < masseges.Length; i++)
            {
                Console.Write(masseges[i]);
                value_to_add = Console.ReadLine();
                new_list.Add(value_to_add);
            }
            List<Department> copy = new List<Department>();
            copy = dep_info_list;
            new_dep.SetDep(new_list);
            copy.Add(new_dep);
            dep_info_list = Save(dep_info_list, copy);
            return dep_info_list;
        }

        static List<Department> Delete(List<Department> dep_info_list)
        {
            int list_delete_id = FindElement(dep_info_list, "Input department id to delete: ");
            if (list_delete_id == -1)
            {
                Console.WriteLine("Nothing was found");
                return dep_info_list;
            }
            else
            {
                Console.WriteLine("This item will be deleted:");
                dep_info_list[list_delete_id].Print();
                List<Department> copy = new List<Department>();
                copy = dep_info_list;
                copy.RemoveAt(list_delete_id);
                dep_info_list = Save(dep_info_list, copy);
                return dep_info_list;
            }
        }

        static List<Department> Cheange(List<Department> dep_info_list)
        {
            int list_cheange_id = FindElement(dep_info_list, "Input department id to cheange: ");
            if (list_cheange_id == -1)
            {
                Console.WriteLine("Nothing was found");
                return dep_info_list;
            }
            else
            {
                Console.WriteLine("This item will be cheanget:");
                dep_info_list[list_cheange_id].Print();

                Console.WriteLine("What do you want to change?");
                Console.WriteLine("id; title; director_name; phone_number; monthly_budget; yearly_budget; website_url");
                string key = Console.ReadLine();
                if (dep_info_list[0].Get(key) != null)
                {
                    Console.Write("Input new value: ");
                    string value = Console.ReadLine();

                    List<Department> copy = new List<Department>();
                    copy = dep_info_list;
                    copy[list_cheange_id].Set(value, key);
                    dep_info_list = Save(dep_info_list, copy);
                    return dep_info_list;
                }
                else
                {
                    return dep_info_list;
                }
            }
        }

        static List<Department> Save(List<Department> old, List<Department> edited)
        {
            string save;
            Console.WriteLine("Your file will look like:");
            PrintAll(edited);
            Console.WriteLine("Save Cheanges?");
            Console.WriteLine("0 - No, 1 - Yes");
            save = Console.ReadLine();
            bool exit = false;
            while (exit == false)
            {
                if(save == "0")
                {
                    exit = true;
                    return old;
                }
                else if (save == "1")
                {
                    SaveToFile(edited);
                    exit = true;
                    return edited;
                }
                else
                {
                    Console.WriteLine("Unlnown command");
                }
            }
            return old;
        }

        static void SaveToFile(List<Department> to_save)
        {
            string text = "";
            for(int list_iter = 0; list_iter < to_save.Count; list_iter++)
            {
                for(int dep_iter = 0; dep_iter < to_save[list_iter].Count(); dep_iter++)
                {
                    text += to_save[list_iter].Get(to_save[list_iter].GetFieldName(dep_iter));
                    text += ";";
                }
                text += ":" + Environment.NewLine;
            }
            File.WriteAllText(@"C:\Users\Admin\source\repos\YuriiDmytruk\Projects\C#&.Net\Internship\Task1Class\Task1Class\DepInfoFile.txt", text);
            Console.WriteLine("Saved");
        }

        static int FindElement(List<Department> dep_info_list, string text)
        {
            string id;
            Console.Write(text);
            id = Console.ReadLine();
            int list_id = -1;
            for (int i = 0; i < dep_info_list.Count; i++)
            {
                if (dep_info_list[i].Get("id") == id)
                {
                    list_id = i;
                    break;
                }
            }
            return list_id;
        }
    }
}

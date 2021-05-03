using System;
using System.Collections.Generic;
using System.IO;

// Add wrong metaDate Exceptions


namespace Task1Class
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                List<string> files = Util<string>.GetFiles(Directory.GetCurrentDirectory());
                files.Insert(0, "Exit");
                Console.WriteLine("Select a file:");
                int fileID = Util<string>.AskUserForChoice(Util<string>.ToFileNamesOnly(files));

                if (fileID == 0)
                {
                    break;
                }
                else
                {
                    string fileName = files[fileID];
                    DataManager dataManager = new DataManager(fileName);

                    while (true)
                    {
                        int choice = Util<string>.AskUserForChoice(new List<string> { "Exit", "Add", "Delete", "Change", "Sort", "Search", "Print" });
                        if (choice == 0)
                        {
                            break;
                        }
                        else if (choice == 1)
                        {
                            dataManager.Add();
                            continue;
                        }
                        else if (choice == 2)
                        {
                            dataManager.Delete();
                            continue;
                        }
                        else if (choice == 3)
                        {
                            dataManager.Change();
                            continue;
                        }
                        else if (choice == 4)
                        {
                            dataManager.Sort();
                            continue;
                        }
                        else if (choice == 5)
                        {
                            dataManager.Search();
                            continue;
                        }
                        else if (choice == 6)
                        {
                            dataManager.Print();
                            continue;
                        }
                        else
                        {
                            Console.WriteLine("Unknown command");
                            continue;
                        }
                    }
                }
            }

            End();
        }
        static void End()
        {
            Console.WriteLine("Press any key to exit");
            System.Console.ReadKey();
        }

    }
}

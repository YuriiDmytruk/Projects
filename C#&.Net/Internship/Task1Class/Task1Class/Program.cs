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
                List<string> files = Util.GetFiles(Directory.GetCurrentDirectory());
                files.Insert(0, "Exit");
                Console.WriteLine("Select a file:");
                int fileID = Util.AskUserForChoice(Util.ToFileNamesOnly(files));

                if (fileID == 0)
                {
                    break;
                }
                else
                {
                    string fileName = files[fileID];
                    ObjectManager objectManager = new ObjectManager(fileName);

                    while (true)
                    {
                        int choice = Util.AskUserForChoice(new List<string> { "Exit", "Add", "Delete", "Change", "Sort", "Search", "Print" });
                        if (choice == 0)
                        {
                            break;
                        }
                        else if (choice == 1)
                        {
                            Add(objectManager);
                            continue;
                        }
                        else if (choice == 2)
                        {
                            Delete(objectManager);
                            continue;
                        }
                        else if (choice == 3)
                        {
                            Change(objectManager);
                            continue;
                        }
                        else if (choice == 4)
                        {
                            Sort(objectManager);
                            continue;
                        }
                        else if (choice == 5)
                        {
                            Search(objectManager);
                            continue;
                        }
                        else if (choice == 6)
                        {
                            objectManager.Print(objectManager.LoadData());
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
        static void Search(ObjectManager objectManager)
        {
            ObjectMetaData metaData = objectManager.GetMetaData();
            List<object> dataList = objectManager.LoadData();

            Console.WriteLine("Input text");
            string to_find = Console.ReadLine();

            string wordToCheck;
            for (int objectIndex = 0; objectIndex < dataList.Count; objectIndex++)
            {
                for (int fieldCounter = 0; fieldCounter < metaData.fieldNames.Count; fieldCounter++)
                {
                    wordToCheck = ObjectManager.GetValue(dataList[objectIndex], metaData.fieldNames[fieldCounter]);

                    if (to_find.Length > wordToCheck.Length) { break; }
                    else
                    {
                        if (Util.Contains(wordToCheck, to_find))
                        {
                            objectManager.Print(dataList[objectIndex]);
                            break;
                        }
                    }
                }
            }
        }
        static void Sort(ObjectManager objectManager)
        {
            Console.WriteLine("What do you want to sort by?");
            objectManager.PrintFields();

            string key = Console.ReadLine();
            List<object> dataList = objectManager.LoadData();
            if (ObjectManager.GetValue(dataList[0], key) == null)
            {
                return;
            }

            ObjectMetaData metaData = objectManager.GetMetaData();
            bool sortAscending = (Util.AskUserForChoice(new List<string> { "Descending", "Ascending" }) == 1);
            for (int i = 1; i < metaData.fieldNames.Count; i++)
            {
                for (int j = 0; j < dataList.Count - i; j++)
                {
                    if (sortAscending)
                    {
                        if (String.Compare(ObjectManager.GetValue(dataList[j], key), ObjectManager.GetValue(dataList[j + 1], key)) > 0)
                        {
                            Util.Swap(dataList, j, j + 1);
                        }
                    }
                    else
                    {
                        if (String.Compare(ObjectManager.GetValue(dataList[j], key), ObjectManager.GetValue(dataList[j + 1], key)) < 0)
                        {
                            Util.Swap(dataList, j, j + 1);
                        }
                    }
                }
            }

            PromptToSaveChanges(objectManager, dataList);
        }
        static void Add(ObjectManager objectManager)
        {
            List<string> fieldNames = objectManager.GetFormattedFieldNames();
            List<object> dataList = objectManager.LoadData();
            ObjectMetaData metaData = objectManager.GetMetaData();

            Console.WriteLine("Input info:");
            Object newObject = objectManager.CreateObject();

            string userInput = null;
            for (int i = 0; i < fieldNames.Count; i++)
            {
                while (true)
                {
                    Console.Write(fieldNames[i]);
                    userInput = Console.ReadLine();
                    if (!Validator.ValidateAndInform(userInput, metaData.validationRules[i]))
                    {
                        continue;
                    }
                    if (!ObjectManager.IsIdField(fieldNames[i]) & !ObjectManager.IsIdUnique(dataList, userInput))
                    {
                        continue;
                    }

                    break;
                }

                ObjectManager.SetValue(newObject, metaData.fieldNames[i], userInput);
            }
            dataList.Add(newObject);

            PromptToSaveChanges(objectManager, dataList);
        }
        static void Delete(ObjectManager objectManager)
        {
            List<object> dataList = objectManager.LoadData();
            int listDeleteId = Util.FindElement(dataList, "Input id to delete: ");
            if (listDeleteId == -1)
            {
                Console.WriteLine("Nothing was found");
            }
            else
            {
                Console.WriteLine("This item will be deleted: ");
                objectManager.Print(dataList[listDeleteId]);
                dataList.RemoveAt(listDeleteId);
                PromptToSaveChanges(objectManager, dataList);
            }
        }
        static void Change(ObjectManager objectManager)
        {
            List<object> dataList = objectManager.LoadData();
            int listChangeId = Util.FindElement(dataList, "Input id to change: ");
            if (listChangeId == -1)
            {
                Console.WriteLine("Nothing was found");
            }
            else
            {
                Console.WriteLine("This item will be changet:");
                objectManager.Print(dataList[listChangeId]);
                Console.WriteLine("What do you want to change?");
                objectManager.PrintFields();
                List<string> fieldNames = objectManager.GetFormattedFieldNames();
                string key = Console.ReadLine();
                string userInput = null;
                if (ObjectManager.GetValue(dataList[0], key) == null)
                {
                }
                else
                {
                    while (true)
                    {
                        ObjectMetaData metaData = objectManager.GetMetaData();
                        Console.Write("Input new value: ");
                        userInput = Console.ReadLine();
                        if (!Validator.ValidateAndInform(userInput, metaData.validationRules[objectManager.GetFieldIndexByKey(key)]))
                        {
                            Console.WriteLine("Id should contain only numbers");
                            continue;
                        }
                        if (!ObjectManager.IsIdField(fieldNames[objectManager.GetFieldIndexByKey(key)]) & !ObjectManager.IsIdUnique(dataList, userInput))
                        {
                            Console.WriteLine("Such id already exists");
                            continue;
                        }

                        break;
                    }
                    dataList[listChangeId] = ObjectManager.SetValue(dataList[listChangeId], key, userInput);
                    PromptToSaveChanges(objectManager, dataList);
                }
            }
        }
        static void End()
        {
            Console.WriteLine("Press any key to exit");
            System.Console.ReadKey();
        }
        private static void PromptToSaveChanges(ObjectManager objectManager, List<object> dataList)
        {
            Console.WriteLine("Your data list looks like: ");
            objectManager.Print(dataList);

            Console.WriteLine("Would you like to Save Changes?");
            if ((Util.AskUserForChoice(new List<string> { "No", "Yes" }) == 1))
            {
                objectManager.SaveData(dataList);
            }
        }

    }
}

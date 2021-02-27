using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task1Class
{
    class DataManager
    {
        private ObjectManager objectManager;
        private List<object> dataList = new List<object>();
        public DataManager(string fileName)
        {
            this.objectManager = new ObjectManager(fileName);
            this.dataList = objectManager.LoadData();
        }
        public void Search()
        {
            ObjectMetaData metaData = objectManager.GetMetaData();

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
                        if (Util<string>.Contains(wordToCheck, to_find))
                        {
                            objectManager.Print(dataList[objectIndex]);
                            break;
                        }
                    }
                }
            }
        }
        public void Sort()
        {
            Console.WriteLine("What do you want to sort by?");
            objectManager.PrintFields();

            string key = Console.ReadLine();
            if (ObjectManager.GetValue(dataList[0], key) == null)
            {
                return;
            }

            ObjectMetaData metaData = objectManager.GetMetaData();
            bool sortAscending = (Util<string>.AskUserForChoice(new List<string> { "Descending", "Ascending" }) == 1);
            for (int i = 1; i < metaData.fieldNames.Count; i++)
            {
                for (int j = 0; j < dataList.Count - i; j++)
                {
                    if (sortAscending)
                    {
                        if (String.Compare(ObjectManager.GetValue(dataList[j], key), ObjectManager.GetValue(dataList[j + 1], key)) > 0)
                        {
                            Util<object>.Swap(dataList, j, j + 1);
                        }
                    }
                    else
                    {
                        if (String.Compare(ObjectManager.GetValue(dataList[j], key), ObjectManager.GetValue(dataList[j + 1], key)) < 0)
                        {
                            Util<object>.Swap(dataList, j, j + 1);
                        }
                    }
                }
            }

            PromptToSaveChanges(objectManager, dataList);
        }
        public void Add()
        {
            List<string> fieldNames = objectManager.GetFormattedFieldNames();
            ObjectMetaData metaData = objectManager.GetMetaData();

            Console.WriteLine("Input info:");
            object newObject = objectManager.CreateObject();

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
        public void Delete()
        {
            Console.Write("Input id to delete: ");
            int listDeleteId = Util<object>.FindElement(dataList);
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
        public void Change()
        {
            Console.WriteLine("Input id to change: ");
            int listChangeId = Util<object>.FindElement(dataList);
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
        public void Print()
        {
            objectManager.Print(objectManager.LoadData());
        }
        private static void PromptToSaveChanges(ObjectManager objectManager, List<object> dataList)
        {
            Console.WriteLine("Your data list looks like: ");
            objectManager.Print(dataList);

            Console.WriteLine("Would you like to Save Changes?");
            if ((Util<string>.AskUserForChoice(new List<string> { "No", "Yes" }) == 1))
            {
                objectManager.SaveData(dataList);
            }
        }
    }
}
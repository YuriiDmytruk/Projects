using System;
using System.Collections.Generic;
using System.IO;
using System.Runtime.Remoting;
using System.Reflection;
using Newtonsoft.Json;

namespace Task1Class
{
    public class ObjectManager
    {
        private const char ValueSeparator = ';';
        private const string IdKeyName = "id";

        private ObjectMetaData metaData;
        private string originalFileName;

        public ObjectManager(string fileName)
        {
            this.originalFileName = fileName;
            this.metaData = LoadMetaData(fileName);
        }

        public ObjectMetaData GetMetaData()
        {
            return this.metaData;
        }

        public List<object> LoadData()
        {
            List<object> result = new List<object>();

            int lineIndex = 0;
            foreach (string line in File.ReadLines(originalFileName))
            {
                if (lineIndex++ < 3)
                {
                    continue;
                }
                else
                {
                    Object newObject = CreateObject();
                    newObject = SetAllValues(newObject, new List<string>(line.Split(ValueSeparator)));
                    result.Add(newObject);
                }
            }
            Console.WriteLine("Data Loaded, records: " + result.Count);
            return result;
        }

        public void SaveData(List<object> data)
        {
            string fileName = this.originalFileName;

            SaveMetaData(fileName);
            string text = "";
            for (int dataIter = 0; dataIter < data.Count; dataIter++)
            {
                for (int fieldIter = 0; fieldIter < metaData.fieldNames.Count; fieldIter++)
                {
                    text += defaultIfNull(GetValue(data[dataIter], metaData.fieldNames[fieldIter]));
                    if (fieldIter < metaData.fieldNames.Count - 1)
                    {
                        text += ValueSeparator;
                    }
                }
                text += Environment.NewLine;
            }

            File.AppendAllText(fileName, text);
            Console.WriteLine("Saved Data into file: " + fileName);
        }

        public static string GetValue(Object classObject, string key)
        {
            Type type = classObject.GetType();
            PropertyInfo prop = type.GetProperty(key);
            if (prop != null)
            {
                MethodInfo method = prop.GetGetMethod();

                string value = JsonConvert.SerializeObject(method.Invoke(classObject, null));
                return value.Trim('"');
            }
            Console.WriteLine("Key does not exist: " + key);
            return null;
        }

        public static Object SetValue(Object classObject, string key, string value)
        {
            Type t = classObject.GetType();
            PropertyInfo prop = t.GetProperty(key);
            if (prop != null)
            {
                prop.SetValue(classObject, value);
            }
            return classObject;
        }

        public void Print(List<object> dataToPrint)
        {
            for (int index = 0; index < dataToPrint.Count; index++)
            {
                Print(dataToPrint[index]);
            }
        }

        public void Print(object toPrint)
        {
            for (int fieldIndex = 0; fieldIndex < metaData.fieldNames.Count; fieldIndex++)
            {
                Console.Write(GetValue(toPrint, metaData.fieldNames[fieldIndex]).Trim('"') + ValueSeparator);
            }
            Console.WriteLine();
        }

        public void PrintFields()
        {
            Console.WriteLine(ListToText(metaData.fieldNames));
        }

        public Object CreateObject()
        {
            ObjectHandle handle = Activator.CreateInstance(null, metaData.className);
            return handle.Unwrap();
        }

        public List<string> GetFormattedFieldNames()
        {
            List<string> result = new List<string>(metaData.fieldNames);
            for (int i = 0; i < result.Count; i++)
            {
                result[i] = char.ToUpper(result[i][0]) + result[i].Substring(1) + ": ";
                result[i] = result[i].Replace('_', ' ');
            }
            return result;
        }

        public static bool IsIdField(string fieldNameToCheck)
        {
            return IdKeyName == fieldNameToCheck;
        }

        public static bool IsIdUnique(List<object> items, string idValueToCheck)
        {
            foreach (Object obj in items)
            {
                if (GetValue(obj, IdKeyName) == idValueToCheck)
                {
                    Console.WriteLine("An element with this id already exists");
                    return false;
                }
            }
            return true;
        }


        public int GetFieldIndexByKey(string key)
        {
            return metaData.fieldNames.IndexOf(key);
        }

        private Object SetAllValues(Object classObject, List<string> values)
        {
            Type t = classObject.GetType();
            for (int i = 0; i < metaData.fieldNames.Count; i++)
            {
                PropertyInfo prop = t.GetProperty(metaData.fieldNames[i]);
                if (prop != null)
                {
                    string validValue = Validator.Validate(values[i], metaData.validationRules[i]);
                    prop.SetValue(classObject, validValue);
                }
            }
            return classObject;
        }

        private void SaveMetaData(string fileName)
        {
            string text = metaData.className + Environment.NewLine;
            text += ListToText(metaData.fieldNames);
            text += ListToText(metaData.validationRules);

            File.WriteAllText(fileName, text);
            Console.WriteLine("MetaData Saved for: " + metaData.className);
        }

        private static string defaultIfNull(string value)
        {
            return (value == null) ? "null" : value;
        }

        private static string ListToText(List<string> list)
        {
            string result = "";
            for (int index = 0; index < list.Count; index++)
            {
                result += list[index];
                if (index < list.Count - 1)
                {
                    result += ValueSeparator;
                }
            }

            return result + Environment.NewLine;
        }

        private static ObjectMetaData LoadMetaData(string fileName)
        {
            ObjectMetaData result = new ObjectMetaData();

            int lineIndex = 0;
            foreach (string line in File.ReadLines(fileName))
            {
                if (lineIndex == 0)
                {
                    result.className = line;

                }
                else if (lineIndex == 1)
                {
                    result.fieldNames = new List<string>(line.Split(ValueSeparator));
                }
                else if (lineIndex == 2)
                {
                    result.validationRules = new List<string>(line.Split(ValueSeparator));
                }
                else
                {
                    break;
                }
                lineIndex++;
            }

            Console.WriteLine("MetaData Loaded for Class: " + result.className);
            return result;
        }
    }


    public class ObjectMetaData
    {
        public string className { get; set; }
        public List<string> fieldNames { get; set; }
        public List<string> validationRules { get; set; }
        public ObjectMetaData()
        {
            className = null;
            fieldNames = new List<string>();
            validationRules = new List<string>();
        }
    }
}

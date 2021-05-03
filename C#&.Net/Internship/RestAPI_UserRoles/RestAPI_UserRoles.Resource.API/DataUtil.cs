using System;
using System.Collections.Generic;
using System.Reflection;
using Newtonsoft.Json;

namespace RestAPI_UserRoles
{
    public class DataUtil

    {
        public static List<T> Search<T>(List<T> data, string find)
        {
            if (data != null && find != null)
            {
                List<T> result = new List<T>();
                Type type = typeof(T);

                string wordToCheck;
                for (int objectIndex = 0; objectIndex < data.Count; objectIndex++)
                {
                    for (int fieldCounter = 0; fieldCounter < type.GetProperties().Length; fieldCounter++)
                    {
                        wordToCheck = GetValue(data[objectIndex], type.GetProperties()[fieldCounter].Name);

                        if (find.Length <= wordToCheck.Length)
                        {
                            if (UtilT<string>.Contains(wordToCheck, find))
                            {
                                result.Add(data[objectIndex]);
                                break;
                            }
                        }
                    }
                }
                return result;
            }
            else
            {
                if (data == null)
                {
                    data = new List<T>();
                }
                return data;
            }
        }

        public static List<T> CreatePage<T>(List<T> data, int page, int page_size)
        {

            if (data != null & page >= 0 & page_size >= 0)
            {
                List<T> result = new List<T>();
                int fromIndex = page * page_size;
                int toIndex = page * page_size + page_size;

                if (toIndex > data.Count)
                {
                    toIndex = data.Count;
                }

                for (int i = fromIndex; i < toIndex; i++)
                {
                    result.Add(data[i]);
                }

                return result;
            }
            else
            {
                if (data == null)
                {
                    data = new List<T>();
                }
                return data;
            }

        }

        public static List<T> Sort<T>(List<T> data, string sort_by, string sort_type)
        {

            if (data != null & sort_by != null)
            {
                if (sort_type == null)
                {
                    sort_type = "asc";
                }
                if (GetValue(data[0], sort_by) == null)
                {
                    if (data == null)
                    {
                        data = new List<T>();
                    }
                    return data;
                }

                sort_by.Trim('"');
                sort_type.Trim('"');

                Type type = typeof(T);

                for (int i = 1; i < type.GetProperties().Length; i++)
                {
                    for (int j = 0; j < data.Count - i; j++)
                    {
                        if (sort_type == "asc")
                        {
                            if (String.Compare(GetValue(data[j], sort_by), GetValue(data[j + 1], sort_by)) > 0)
                            {
                                data = UtilT<T>.Swap(data, j, j + 1);
                            }
                        }
                        else
                        {
                            if (String.Compare(GetValue(data[j], sort_by), GetValue(data[j + 1], sort_by)) < 0)
                            {
                                data = UtilT<T>.Swap(data, j, j + 1);
                            }
                        }
                    }
                }
                return data;
            }
            else
            {
                if (data == null)
                {
                    data = new List<T>();
                }
                return data;
            }
        }

        private static string GetValue<T>(T data, string key)
        {
            if (data != null & key != null)
            {
                Type type = data.GetType();
                PropertyInfo prop = type.GetProperty(key);
                if (prop != null)
                {
                    MethodInfo method = prop.GetGetMethod();

                    string value = JsonConvert.SerializeObject(method.Invoke(data, null));
                    return value.Trim('"');
                }
                return null;
            }
            else
            {
                return null;
            }
        }
    }
}


using System;
using System.Collections.Generic;
using System.Reflection;
using Newtonsoft.Json;

namespace RestAPI
{
    public class DataUtil

    {
        public static List<DepartmentDTO> Search(List<DepartmentDTO> departments, string find)
        {
            if (departments != null && find != null)
            {
                List<DepartmentDTO> result = new List<DepartmentDTO>();
                Type type = typeof(DepartmentDTO);

                string wordToCheck;
                for (int objectIndex = 0; objectIndex < departments.Count; objectIndex++)
                {
                    for (int fieldCounter = 0; fieldCounter < type.GetProperties().Length; fieldCounter++)
                    {
                        wordToCheck = GetValue(departments[objectIndex], type.GetProperties()[fieldCounter].Name);

                        if (find.Length > wordToCheck.Length) { break; }
                        else
                        {
                            if (UtilT<string>.Contains(wordToCheck, find))
                            {
                                result.Add(departments[objectIndex]);
                                break;
                            }
                        }
                    }
                }
                return result;
            }
            else
            {
                if (departments == null)
                {
                    departments = new List<DepartmentDTO>();
                }
                return departments;
            }
        }

        public static List<DepartmentDTO> CreatePage(List<DepartmentDTO> departments, int page, int page_size)
        {
            
            if (departments != null & page >= 0 & page_size >= 0)
            {
                List<DepartmentDTO> result = new List<DepartmentDTO>();
                int fromIndex = page * page_size;
                int toIndex = page * page_size + page_size;

                if (toIndex > departments.Count)
                {
                    toIndex = departments.Count;
                }

                for (int i = fromIndex; i < toIndex; i++)
                {
                    result.Add(departments[i]);
                }

                return result;
            }
            else
            {
                if (departments == null)
                {
                    departments = new List<DepartmentDTO>();
                }
                return departments;
            }

        }

        public static List<DepartmentDTO> Sort(List<DepartmentDTO> departments, string sort_by, string sort_type)
        {

            if (departments != null & sort_by != null)
            {
                if (sort_type == null)
                {
                    sort_type = "asc";
                }
                if (GetValue(departments[0], sort_by) == null)
                {
                    if (departments == null)
                    {
                        departments = new List<DepartmentDTO>();
                    }
                    return departments;
                }

                sort_by.Trim('"');
                sort_type.Trim('"');

                Type type = typeof(DepartmentDTO);

                for (int i = 1; i < type.GetProperties().Length; i++)
                {
                    for (int j = 0; j < departments.Count - i; j++)
                    {
                        if (sort_type == "asc")
                        {
                            if (String.Compare(GetValue(departments[j], sort_by), GetValue(departments[j + 1], sort_by)) > 0)
                            {
                                departments = UtilT<DepartmentDTO>.Swap(departments, j, j + 1);
                            }
                        }
                        else
                        {
                            if (String.Compare(GetValue(departments[j], sort_by), GetValue(departments[j + 1], sort_by)) < 0)
                            {
                                departments = UtilT<DepartmentDTO>.Swap(departments, j, j + 1);
                            }
                        }
                    }
                }
                return departments;
            }
            else
            {
                if(departments == null)
                {
                    departments = new List<DepartmentDTO>();
                }
                return departments;
            }
        }

        private static string GetValue(DepartmentDTO department, string key)
        {
            if (department != null & key != null)
            {
                Type type = department.GetType();
                PropertyInfo prop = type.GetProperty(key);
                if (prop != null)
                {
                    MethodInfo method = prop.GetGetMethod();

                    string value = JsonConvert.SerializeObject(method.Invoke(department, null));
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


using System;
using System.Reflection;
using System.Collections.Generic;

namespace Task1Class
{
    class Department
    {
        private string id;
        private string title;
        private string director_name;
        private string phone_number;
        private string monthly_budget;
        private string yearly_budget;
        private string website_url;

        public Department(string id, string title, string director_name, string phone_number, string monthly_budget, string yearly_budget, string website_url)
        {
            this.id = id;
            this.title = title;
            this.director_name = director_name;
            this.phone_number = phone_number;
            this.monthly_budget = monthly_budget;
            this.yearly_budget = yearly_budget;
            this.website_url = website_url;
        }

        public Department()
        {
            id = null;
            title = null;
            director_name = null;
            phone_number = null;
            monthly_budget = null;
            yearly_budget = null;
            website_url = null;
        }

        public void SetDep(List<string> info)
        {
            Validator to_valid = new Validator(info[0], "numbers");
            id = to_valid.Validate();
            to_valid.Set(info[1], "letters");
            title = to_valid.Validate();
            to_valid.Set(info[2], "letters");
            director_name = to_valid.Validate();
            to_valid.Set(info[3], "phone");
            phone_number = to_valid.Validate();
            to_valid.Set(info[4], "numbers");
            monthly_budget = to_valid.Validate();
            to_valid.Set(info[5], "numbers");
            yearly_budget = to_valid.Validate();
            to_valid.Set(info[6], "url");
            website_url = to_valid.Validate();
        }

        public void Print()
        {
            Console.WriteLine(id + ", " + title + ", " + director_name + ", " + phone_number + ", " + monthly_budget + ", " + yearly_budget + ", " + website_url);
        }

        public int Count()
        {
            Type fieldsType = typeof(Department);
            FieldInfo[] fields = fieldsType.GetFields(BindingFlags.Public
                | BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.NonPublic);
            return fields.Length;
        }

        public string Get(string key)
        {
            Type fieldsType = typeof(Department);
            FieldInfo[] fields = fieldsType.GetFields(BindingFlags.Public
                | BindingFlags.Instance | BindingFlags.NonPublic | BindingFlags.NonPublic);
            int id = -1;
            for (int i = 0; i < fields.Length; i++)
            {
                if (fields[i].Name == key)
                {
                    id = i;
                    break;
                }
            }
            if (id == -1)
            {
                Console.WriteLine("Unknown key(Department Get Function)");
                return null;
            }
            else
            {
                return Convert.ToString(fields[id].GetValue(this));
            }
        }

        public string GetFieldName(int id)
        {
            if (id < Count())
            {
                Type fieldsType = typeof(Department);
                FieldInfo[] fields = fieldsType.GetFields(BindingFlags.Public
                    | BindingFlags.Instance | BindingFlags.NonPublic);
                return Convert.ToString(fields[id].Name);
            }
            else
            {
                Console.WriteLine("Unknown id (Department GetFieldName)");
                return null;
            }
            
        }

        public void Set(string value, string key)
        {
            Type fieldsType = typeof(Department);
            FieldInfo[] fields = fieldsType.GetFields(BindingFlags.Public
                | BindingFlags.Instance | BindingFlags.NonPublic);
            int id = -1;
            for (int i = 0; i < fields.Length; i++)
            {
                if (fields[i].Name == key)
                {
                    id = i;
                    break;
                }
            }
            if (id == -1)
            {
                Console.WriteLine("Unknown key(Department Set Function)");
            }
            else
            {
                fields[id].SetValue(this, value);
            }
        }
    }
}

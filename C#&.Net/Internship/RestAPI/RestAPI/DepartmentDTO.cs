using System;
using System.Collections.Generic;
using System.Reflection;

namespace RestAPI
{

    public class DepartmentDTO
    {
        public long id { get; set; }
        public string title { get; set; }
        public string director_name { get; set; }
        public string phone_number { get; set; }
        public string monthly_budget { get; set; }
        public string yearly_budget { get; set; }
        public string website_url { get; set; }



        public DepartmentDTO(long id, string title, string director_name, string phone_number, string monthly_budget, string yearly_budget, string website_url)
        {
            this.id = id;
            this.title = title;
            this.director_name = director_name;
            this.phone_number = phone_number;
            this.monthly_budget = monthly_budget;
            this.yearly_budget = yearly_budget;
            this.website_url = website_url;

        }

        public DepartmentDTO(List<string> createList)
        {
            this.id = -1;
            this.title = createList[0];
            this.director_name = createList[1];
            this.phone_number = createList[2];
            this.monthly_budget = createList[3];
            this.yearly_budget = createList[4];
            this.website_url = createList[5];
        }

        public static List<string> GetFieldList()
        {
            Type type = typeof(DepartmentDTO);
            PropertyInfo[] propList = type.GetProperties();
            List<string> result = new List<string>();
            foreach(PropertyInfo prop in propList)
            {
                result.Add(prop.Name.Trim('"'));
            }
            return result;
        }

        public List<string> GetValueList()
        {
            Type type = typeof(DepartmentDTO);
            PropertyInfo[] propList = type.GetProperties();

            List<string> valueList = new List<string>();

            foreach(PropertyInfo prop in propList)
            {
                if(prop.GetValue(this) == null)
                {
                    valueList.Add(null);
                }
                else
                {
                    valueList.Add(prop.GetValue(this).ToString());
                }
            }
            
            return valueList;
        }
    }
}

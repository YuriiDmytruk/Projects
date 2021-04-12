using System;
using System.Collections.Generic;
using System.Reflection;

namespace RestAPI_UserRoles.DTO
{
    public class CustomerDTO
    {
        public long id { get; set; }
        public string name { get; set; }
        public string email { get; set; }
        public string role { get; set; }

        public CustomerDTO(int id, string name, string email, string role)
        {
            this.id = id;
            this.name = name;
            this.email = email;
            this.role = role;
        }

        public CustomerDTO(List<string> createList)
        {
            id = -1;
            name = createList[0];
            email = createList[1];
            role = createList[2];
        }

        public static List<string> GetFieldList()
        {
            Type type = typeof(CustomerDTO);
            PropertyInfo[] propList = type.GetProperties();
            List<string> result = new List<string>();
            foreach (PropertyInfo prop in propList)
            {
                result.Add(prop.Name.Trim('"'));
            }
            return result;
        }

        public List<string> GetValueList()
        {
            Type type = typeof(CustomerDTO);
            PropertyInfo[] propList = type.GetProperties();

            List<string> valueList = new List<string>();

            foreach (PropertyInfo prop in propList)
            {
                if (prop.GetValue(this) == null)
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

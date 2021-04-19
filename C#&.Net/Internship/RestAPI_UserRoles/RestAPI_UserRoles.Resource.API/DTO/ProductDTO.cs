using System;
using System.Collections.Generic;
using System.Reflection;

namespace RestAPI_UserRoles.DTO
{
    public class ProductDTO
    {
        public long id { get; set; }
        public int amount { get; set; }
        public string productName { get; set; }

        public ProductDTO(int id, int amount, string productName)
        {
            this.id = id;
            this.productName = productName;
            this.amount = amount;
        }
        public ProductDTO(List<string> createList)
        {
            id = -1;
            amount = Convert.ToInt32(createList[0]);
            productName = createList[1];
        }
        public ProductDTO()
        {

        }


        public static List<string> GetFieldList()
        {
            Type type = typeof(ProductDTO);
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
            Type type = typeof(ProductDTO);
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

        public override string ToString()
        {
            return "{id: " + id + "; amount: " + amount + "; productName: " + productName + ";}";
        }
    }
}

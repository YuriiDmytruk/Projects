using System;
using System.Collections.Generic;
using System.Reflection;

namespace RestAPI_UserRoles.DTO
{
    public class OrderDTO
    {
        public long id { get; set; }
        public int amount { get; set; }
        public int user_id { get; set; }
        public int product_id { get; set; }
        public string time { get; set; }

        public OrderDTO()
        {

        }

        public OrderDTO(int id, int amount, int user_id, int product_id, string time)
        {
            this.id = id;
            this.amount = amount;
            this.user_id = user_id;
            this.product_id = product_id;
            this.time = time;
        }

        public OrderDTO(List<string> createList)
        {
            id = -1;
            amount = Convert.ToInt32(createList[0]);
            product_id = Convert.ToInt32(createList[1]);
            user_id = Convert.ToInt32(createList[2]);
            time = createList[3];
        }

        public static List<string> GetFieldList()
        {
            Type type = typeof(OrderDTO);
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
            Type type = typeof(OrderDTO);
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

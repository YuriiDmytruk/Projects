using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace RestAPI
{
    public class MySQLConnect
    {
        public static DataOut Connect(Func<DataIn, MySqlConnection, DataOut> func, DataIn data)
        {
            MySqlConnection connection = new MySqlConnection(env.GetConnectionString());
            connection.Open();

            DataOut result = func(data, connection);

            connection.Close();

            return result;
        }
    }

    public class DataOut
    {
        public List<DepartmentDTO> departments { get; set; }
        public bool success { get; set; }

        public DataOut(List<DepartmentDTO> departments, bool success)
        {
            this.departments = departments;
            this.success = success;
        }

        public DataOut()
        {
            this.departments = new List<DepartmentDTO>();
            this.success = false;
        }
    }

    public class DataIn
    {
        public DepartmentDTO department { get; set; }
        public int id { get; set; }
        
        public DataIn(DepartmentDTO department, int id)
        {
            this.department = department;
            this.id = id;
        }
    }
}

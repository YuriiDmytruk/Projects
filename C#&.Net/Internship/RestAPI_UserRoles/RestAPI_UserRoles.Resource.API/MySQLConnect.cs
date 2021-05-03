using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;

namespace RestAPI_UserRoles
{
    public class MySQLConnect
    {
        public static DataOut<T> Connect<T>(Func<DataIn<T>, MySqlConnection, DataOut<T>> func, DataIn<T> data)
        {
            MySqlConnection connection = new MySqlConnection(env.GetConnectionString());
            connection.Open();

            DataOut<T> result = func(data, connection);

            connection.Close();

            return result;
        }
    }

    public class DataOut<T>
    {
        public List<T> data { get; set; }
        public bool success { get; set; }
        public string errorMessage { get; set; }

        public DataOut(List<T> data, bool success)
        {
            this.data = data;
            this.success = success;
            errorMessage = "";
        }

        public DataOut(List<T> data, bool success, string errorMessage)
        {
            this.data = data;
            this.success = success;
            this.errorMessage = errorMessage;
        }
    }

    public class DataIn<T>
    {
        public T data { get; set; }
        public int id { get; set; }
        public int user_id { get; set; }
        
        public string user_role { get; set; }
        public string password { get; set; }

        public DataIn(T data, int id, string password)
        {
            this.data = data;
            this.id = id;
            this.password = password;
        }

        public DataIn(T data, int id, int user_id, string user_role)
        {
            this.data = data;
            this.id = id;
            this.user_id = user_id;
            this.user_role = user_role;
        }

        public DataIn(T data, int id)
        {
            this.data = data;
            this.id = id;
            password = "";
        }
    }
}

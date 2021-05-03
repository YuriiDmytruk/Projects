using System.Collections.Generic;
using System.Data;
using MySql.Data.MySqlClient;
using RestAPI_UserRoles.DTO;

namespace RestAPI_UserRoles
{
    public class DataManager
    {
        public static List<Account> Get()
        {

            MySqlConnection connection = new MySqlConnection(env.GetConnectionString());
            connection.Open();
            string sql = "SELECT * FROM customers";
            MySqlCommand customerCommand = new MySqlCommand(sql, connection);


            DataTable customerTable = new DataTable();
            MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
            adapter.Fill(customerTable);

            List<Account> result = new List<Account>();
            foreach (DataRow row in customerTable.Rows)
            {
                result.Add(new Account(row.Field<int>("id"),
                    row.Field<string>("email"),
                    row.Field<string>("password"),
                    row.Field<string>("role")));
            }

            connection.Close();
            return result;
        }
    }
}

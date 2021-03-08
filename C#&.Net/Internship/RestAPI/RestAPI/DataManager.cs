using System.Collections.Generic;
using System.Data;
using MySql.Data.MySqlClient;

namespace RestAPI
{
    public class DataManager
    {
        public static void CreaetDB()
        {
            string cs = GetConnectionString();

            var connection = new MySqlConnection(cs);
            connection.Open();

            connection.Close();
        }

        public static Customer GetCustomer(int id)
        {
            MySqlConnection connection = new MySqlConnection(GetConnectionString());
            connection.Open();

            string sql = "SELECT * FROM customers WHERE id = " + id;
            MySqlCommand customerCommand = new MySqlCommand(sql, connection);

            DataTable customerTable = new DataTable();
            MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
            adapter.Fill(customerTable);

            Customer result = null;
            if (customerTable.Rows.Count > 0)
            {
                DataRow row = customerTable.Rows[0];
                result = new Customer(row.Field<int>("id"), row.Field<string>("name"), row.Field<string>("email"));
            }

            connection.Close();
            return result;
        }

        public static List<Customer> GetAllCustomers()
        {
            MySqlConnection connection = new MySqlConnection(GetConnectionString());
            connection.Open();

            string sql = "SELECT * FROM customers";
            MySqlCommand customerCommand = new MySqlCommand(sql, connection);

            DataTable customerTable = new DataTable();
            MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
            adapter.Fill(customerTable);

            List<Customer> result = new List<Customer>();
            foreach (DataRow row in customerTable.Rows)
            {
                result.Add(new Customer(row.Field<int>("id"), row.Field<string>("name"), row.Field<string>("email")));
            }

            connection.Close();
            return result;
        }

        public static bool DeleteCustomer(int id)
        {
            MySqlConnection connection = new MySqlConnection(GetConnectionString());
            connection.Open();

            string sql = "DELETE FROM customers WHERE id = " + id;
            MySqlCommand command = new MySqlCommand(sql, connection);

            int result = command.ExecuteNonQuery();
            connection.Close();

            return result > 0;
        }

        public static Customer InsertCustomer(Customer customer)
        {
            MySqlConnection connection = new MySqlConnection(GetConnectionString());
            connection.Open();

            MySqlCommand command = new MySqlCommand();
            command.Connection = connection;
            command.CommandText = "INSERT INTO customers(name, email) VALUES(?name,?email)";
            command.Parameters.Add("?name", MySqlDbType.VarChar).Value = customer.name;
            command.Parameters.Add("?email", MySqlDbType.VarChar).Value = customer.email;

            command.ExecuteNonQuery();
            customer.id = command.LastInsertedId;
            connection.Close();

            return customer;
        }

        private static string GetConnectionString()
        {
            return "datasource=localhost;port=3306;database=rest_api;username=root;password=1111;";
        }
    }
}

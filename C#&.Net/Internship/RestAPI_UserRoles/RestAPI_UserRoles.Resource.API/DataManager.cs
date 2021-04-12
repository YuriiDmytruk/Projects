using System;
using System.Collections.Generic;
using System.Data;
using MySql.Data.MySqlClient;
using RestAPI_UserRoles.DTO;

namespace RestAPI_UserRoles
{
    public class CustomersDataManager
    {
        public static DataOut<CustomerDTO> GetId(DataIn<CustomerDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;
                string sql = "SELECT * FROM customers WHERE id = " + id;
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                CustomerDTO result = null;
                if (customerTable.Rows.Count > 0)
                {
                    DataRow row = customerTable.Rows[0];
                    result = new CustomerDTO(row.Field<int>("id"),
                        row.Field<string>("name"),
                        row.Field<string>("email"),
                        row.Field<string>("role"));
                }

                return new DataOut<CustomerDTO>(new List<CustomerDTO>() { result }, true);
            }
            else
            {
                return new DataOut<CustomerDTO>(new List<CustomerDTO>(), false);
            }

        }

        public static DataOut<CustomerDTO> Get(DataIn<CustomerDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                string sql = "SELECT * FROM customers";
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                List<CustomerDTO> result = new List<CustomerDTO>();
                foreach (DataRow row in customerTable.Rows)
                {
                    result.Add(new CustomerDTO(row.Field<int>("id"),
                        row.Field<string>("name"),
                        row.Field<string>("email"),
                        row.Field<string>("role")));
                }

                return new DataOut<CustomerDTO>(result, true);
            }
            else
            {
                return new DataOut<CustomerDTO>(new List<CustomerDTO>(), false);
            }
        }

        public static DataOut<CustomerDTO> Delete(DataIn<CustomerDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;

                string sql = "DELETE FROM customers WHERE id = " + id;
                MySqlCommand command = new MySqlCommand(sql, connection);

                int result = command.ExecuteNonQuery();

                return new DataOut<CustomerDTO>(null, result > 0);
            }
            else
            {
                return new DataOut<CustomerDTO>(new List<CustomerDTO>(), false);
            }
        }

        public static DataOut<CustomerDTO> Post(DataIn<CustomerDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                CustomerDTO customer = data.data;

                string commandText = "INSERT INTO customers(";

                List<string> fieldList = UtilT<CustomerDTO>.GetFieldList();
                fieldList.RemoveAt(0);

                foreach (string field in fieldList)
                {
                    commandText += field + ", ";
                }
                commandText += "password) VALUES(";

                List<string> valueList = customer.GetValueList();
                valueList.RemoveAt(0);

                foreach (string field in fieldList)
                {
                    commandText += "?" + field + ",";
                }

                commandText += "?password)";
                MySqlCommand command = new MySqlCommand();

                command.Connection = connection;
                command.CommandText = commandText;

                for (int i = 0; i < valueList.Count; i++)
                {
                    command.Parameters.Add("?" + fieldList[i], MySqlDbType.VarChar).Value = valueList[i];
                }

                command.Parameters.Add("?" + "password", MySqlDbType.VarChar).Value = data.password;

                command.ExecuteNonQuery();
                customer.id = command.LastInsertedId;

                return new DataOut<CustomerDTO>(new List<CustomerDTO>() { customer }, true);
            }
            else
            {
                return new DataOut<CustomerDTO>(new List<CustomerDTO>(), false);
            }
        }

        public static DataOut<CustomerDTO> Put(DataIn<CustomerDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                CustomerDTO customer = data.data;
                int id = data.id;

                string commandText = "UPDATE customers SET ";

                List<string> fieldArr = CustomerDTO.GetFieldList();
                fieldArr.RemoveAt(0);
                List<string> valueList = customer.GetValueList();
                valueList.RemoveAt(0);

                for (int i = 0; i < fieldArr.Count; i++)
                {
                    if (valueList[i] != null)
                    {
                        commandText += fieldArr[i] + "='" + valueList[i] + "',";
                    }
                }

                if (data.password == "")
                {
                    commandText = UtilT<string>.DeleteLastChar(commandText);
                }
                else
                {
                    commandText += "password" + "='" + data.password + "'";
                }


                commandText += " WHERE id=" + id;

                MySqlCommand command = new MySqlCommand(commandText, connection);

                int result = command.ExecuteNonQuery();
                return new DataOut<CustomerDTO>(null, result > 0);
            }
            else
            {
                return new DataOut<CustomerDTO>(new List<CustomerDTO>(), false);
            }
        }
    }

    public class ProductDataManager
    {
        public static DataOut<ProductDTO> Get(DataIn<ProductDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                string sql = "SELECT * FROM products";
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                List<ProductDTO> result = new List<ProductDTO>();
                foreach (DataRow row in customerTable.Rows)
                {
                    result.Add(new ProductDTO(row.Field<int>("id"),
                        row.Field<int>("amount"),
                        row.Field<string>("productName")));
                }

                return new DataOut<ProductDTO>(result, true);
            }
            else
            {
                return new DataOut<ProductDTO>(new List<ProductDTO>(), false);
            }
        }

        public static DataOut<ProductDTO> Post(DataIn<ProductDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                ProductDTO customer = data.data;

                string commandText = "INSERT INTO products(";

                List<string> fieldList = UtilT<ProductDTO>.GetFieldList();
                fieldList.RemoveAt(0);

                foreach (string field in fieldList)
                {
                    commandText += field + ", ";
                }

                commandText = UtilT<string>.DeleteLastChar(commandText);
                commandText = UtilT<string>.DeleteLastChar(commandText);

                commandText += ") VALUES(";

                List<string> valueList = customer.GetValueList();
                valueList.RemoveAt(0);

                foreach (string field in fieldList)
                {
                    commandText += "?" + field + ",";
                }

                commandText = UtilT<string>.DeleteLastChar(commandText);
                commandText += ")";

                MySqlCommand command = new MySqlCommand();

                command.Connection = connection;
                command.CommandText = commandText;

                for (int i = 0; i < valueList.Count; i++)
                {
                    command.Parameters.Add("?" + fieldList[i], MySqlDbType.VarChar).Value = valueList[i];
                }

                command.ExecuteNonQuery();
                customer.id = command.LastInsertedId;

                return new DataOut<ProductDTO>(new List<ProductDTO>() { customer }, true);
            }
            else
            {
                return new DataOut<ProductDTO>(new List<ProductDTO>(), false);
            }
        }

        public static DataOut<ProductDTO> Put(DataIn<ProductDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                ProductDTO customer = data.data;
                int id = data.id;

                string commandText = "UPDATE products SET ";

                List<string> fieldList = ProductDTO.GetFieldList();
                fieldList.RemoveAt(0);
                List<string> valueList = customer.GetValueList();
                valueList.RemoveAt(0);

                for (int i = 0; i < fieldList.Count; i++)
                {
                    if (valueList[i] != null)
                    {
                        commandText += fieldList[i] + "='" + valueList[i] + "',";
                    }
                }
                commandText = UtilT<string>.DeleteLastChar(commandText);

                commandText += " WHERE id=" + id;

                MySqlCommand command = new MySqlCommand(commandText, connection);

                int result = command.ExecuteNonQuery();
                return new DataOut<ProductDTO>(null, result > 0);
            }
            else
            {
                return new DataOut<ProductDTO>(new List<ProductDTO>(), false);
            }
        }

        public static DataOut<ProductDTO> GetId(DataIn<ProductDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;
                string sql = "SELECT * FROM products WHERE id = " + id;
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                ProductDTO result = null;
                if (customerTable.Rows.Count > 0)
                {
                    DataRow row = customerTable.Rows[0];
                    result = new ProductDTO(row.Field<int>("id"),
                        row.Field<int>("amount"),
                        row.Field<string>("productName"));
                }

                return new DataOut<ProductDTO>(new List<ProductDTO>() { result }, true);
            }
            else
            {
                return new DataOut<ProductDTO>(new List<ProductDTO>(), false);
            }

        }

        public static DataOut<ProductDTO> Delete(DataIn<ProductDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;

                string sql = "DELETE FROM products WHERE id = " + id;
                MySqlCommand command = new MySqlCommand(sql, connection);

                int result = command.ExecuteNonQuery();

                return new DataOut<ProductDTO>(null, result > 0);
            }
            else
            {
                return new DataOut<ProductDTO>(new List<ProductDTO>(), false);
            }
        }
    }

    public class OrderDataManager
    {
        public static DataOut<OrderDTO> Get(DataIn<OrderDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                string sql = "SELECT * FROM orders";
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                List<OrderDTO> result = new List<OrderDTO>();
                foreach (DataRow row in customerTable.Rows)
                {
                    result.Add(new OrderDTO(row.Field<int>("id"),
                        row.Field<int>("amount"),
                        row.Field<int>("user_id"),
                        row.Field<int>("product_id"),
                        row.Field<string>("time")));
                }

                return new DataOut<OrderDTO>(result, true);
            }
            else
            {
                return new DataOut<OrderDTO>(new List<OrderDTO>(), false);
            }
        }

        public static DataOut<OrderDTO> Post(DataIn<OrderDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                if (FixAmount(data.data, "take", connection))
                {
                    OrderDTO order = data.data;

                    string commandText = "INSERT INTO orders(";

                    List<string> fieldList = UtilT<OrderDTO>.GetFieldList();
                    fieldList.RemoveAt(0);

                    foreach (string field in fieldList)
                    {
                        commandText += field + ", ";
                    }

                    commandText = UtilT<string>.DeleteLastChar(commandText);
                    commandText = UtilT<string>.DeleteLastChar(commandText);

                    commandText += ") VALUES(";

                    List<string> valueList = order.GetValueList();
                    valueList.RemoveAt(0);

                    foreach (string field in fieldList)
                    {
                        commandText += "?" + field + ",";
                    }

                    commandText = UtilT<string>.DeleteLastChar(commandText);
                    commandText += ")";

                    MySqlCommand command = new MySqlCommand();

                    command.Connection = connection;
                    command.CommandText = commandText;

                    for (int i = 0; i < valueList.Count; i++)
                    {
                        command.Parameters.Add("?" + fieldList[i], MySqlDbType.VarChar).Value = valueList[i];
                    }

                    command.ExecuteNonQuery();
                    order.id = command.LastInsertedId;

                    return new DataOut<OrderDTO>(new List<OrderDTO>() { order }, true);
                }
                else
                {
                    return new DataOut<OrderDTO>(new List<OrderDTO>(), false, "AmountError");
                }
            }
            else
            {
                return new DataOut<OrderDTO>(new List<OrderDTO>(), false);
            }
        }

        public static DataOut<OrderDTO> GetId(DataIn<OrderDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;
                string sql = "SELECT * FROM orders WHERE id = " + id;
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                OrderDTO result = null;
                if (customerTable.Rows.Count > 0)
                {
                    DataRow row = customerTable.Rows[0];
                    result = new OrderDTO(row.Field<int>("id"),
                        row.Field<int>("amount"),
                        row.Field<int>("user_id"),
                        row.Field<int>("product_id"),
                        row.Field<string>("time"));
                }

                return new DataOut<OrderDTO>(new List<OrderDTO>() { result }, true);
            }
            else
            {
                return new DataOut<OrderDTO>(new List<OrderDTO>(), false);
            }

        }

        public static DataOut<OrderDTO> Delete(DataIn<OrderDTO> data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                string sql = "SELECT user_id FROM orders WHERE id = " + data.id;
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);
                MySqlDataReader reader = customerCommand.ExecuteReader();
                reader.Read();
                int curentUserId = Convert.ToInt32(reader.GetValue(0).ToString());
                reader.Close();

                if (curentUserId != data.user_id && data.user_role == "User")
                {
                    return new DataOut<OrderDTO>(null, false, "forbiden");
                }
                else
                {
                    data.data.id = data.id;
                    FixAmount(data.data, "return", connection);

                    int id = data.id;

                    sql = "DELETE FROM orders WHERE id = " + id;
                    MySqlCommand command = new MySqlCommand(sql, connection);

                    int result = command.ExecuteNonQuery();

                    return new DataOut<OrderDTO>(null, result > 0);
                }
            }
            else
            {
                return new DataOut<OrderDTO>(new List<OrderDTO>(), false);
            }
        }

        private static bool FixAmount(OrderDTO order, string key, MySqlConnection connection)
        {
            int amount;
            int product_id;

            if (order.product_id == 0)
            {
                string commandText = "SELECT amount, product_id FROM orders WHERE id = " + order.id;
                MySqlCommand command = new MySqlCommand(commandText, connection);
                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(command);
                adapter.Fill(customerTable);

                DataRow row = customerTable.Rows[0];
                amount = row.Field<int>("amount");
                product_id = row.Field<int>("product_id");
            }
            else
            {
                product_id = order.product_id;
                amount = order.amount;
            }


            // Get Curent product Amount
            string sql = "SELECT amount FROM products WHERE id = " + product_id;
            MySqlCommand customerCommand = new MySqlCommand(sql, connection);

            DataTable customer_table = new DataTable();
            MySqlDataAdapter adapter_ = new MySqlDataAdapter(customerCommand);
            adapter_.Fill(customer_table);

            DataRow row_ = customer_table.Rows[0];
            int productAmount = row_.Field<int>("amount");

            // Create new Amount
            int newAmount;
            if (key == "return")
            {
                newAmount = productAmount + amount;
            }
            else
            {
                newAmount = productAmount - amount;
            }

            // Set Amount
            if (newAmount >= 0)
            {
                string commandText = "UPDATE products SET amount=" + newAmount + " WHERE id =" + product_id;
                MySqlCommand command = new MySqlCommand(commandText, connection);
                
                command.ExecuteNonQuery();
                return true;
            }
            else
            {
                return false;
            }
        }
    }
}

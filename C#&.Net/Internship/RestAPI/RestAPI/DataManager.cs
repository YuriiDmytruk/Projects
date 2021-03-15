using System.Collections.Generic;
using System.Data;
using MySql.Data.MySqlClient;

namespace RestAPI
{
    public class DataManager
    {

        public static DataOut GetId(DataIn data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;
                string sql = "SELECT * FROM departments WHERE id = " + id;
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                DepartmentDTO result = null;
                if (customerTable.Rows.Count > 0)
                {
                    DataRow row = customerTable.Rows[0];
                    result = new DepartmentDTO(row.Field<int>("id"),
                        row.Field<string>("title"),
                        row.Field<string>("director_name"),
                        row.Field<string>("phone_number"),
                        row.Field<string>("monthly_budget"),
                        row.Field<string>("yearly_budget"),
                        row.Field<string>("website_url"));
                }

                return new DataOut(new List<DepartmentDTO>() { result }, true);
            }
            else
            {
                return new DataOut(new List<DepartmentDTO>(), false);
            }

        }

        public static DataOut Put(DataIn data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                DepartmentDTO department = data.department;
                int id = data.id;

                string commandText = "UPDATE departments SET ";

                List<string> fieldArr = DepartmentDTO.GetFieldList();
                fieldArr.RemoveAt(0);
                List<string> valueList = department.GetValueList();
                valueList.RemoveAt(0);

                for (int i = 0; i < fieldArr.Count; i++)
                {
                    if (valueList[i] != null)
                    {
                        commandText += fieldArr[i] + "='" + valueList[i] + "',";
                    }
                }

                commandText = UtilT<string>.DeleteLastChar(commandText);

                commandText += " WHERE id=" + id;

                MySqlCommand command = new MySqlCommand(commandText, connection);

                int result = command.ExecuteNonQuery();
                return new DataOut(null, result > 0);
            }
            else
            {
                return new DataOut(new List<DepartmentDTO>(), false);
            }
        }

        public static DataOut Get(DataIn data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                string sql = "SELECT * FROM departments";
                MySqlCommand customerCommand = new MySqlCommand(sql, connection);

                DataTable customerTable = new DataTable();
                MySqlDataAdapter adapter = new MySqlDataAdapter(customerCommand);
                adapter.Fill(customerTable);

                List<DepartmentDTO> result = new List<DepartmentDTO>();
                foreach (DataRow row in customerTable.Rows)
                {
                    result.Add(new DepartmentDTO(row.Field<int>("id"),
                        row.Field<string>("title"),
                        row.Field<string>("director_name"),
                        row.Field<string>("phone_number"),
                        row.Field<string>("monthly_budget"),
                        row.Field<string>("yearly_budget"),
                        row.Field<string>("website_url")));
                }

                return new DataOut(result, true);
            }
            else
            {
                return new DataOut(new List<DepartmentDTO>(), false);
            }
        }

        public static DataOut Delete(DataIn data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                int id = data.id;
                string sql = "DELETE FROM departments WHERE id = " + id;
                MySqlCommand command = new MySqlCommand(sql, connection);

                int result = command.ExecuteNonQuery();

                return new DataOut(null, result > 0);
            }
            else
            {
                return new DataOut(new List<DepartmentDTO>(), false);
            }
        }

        public static DataOut Post(DataIn data, MySqlConnection connection)
        {
            if (data != null & connection != null)
            {
                DepartmentDTO department = data.department;

                string commandText = "INSERT INTO departments(";

                List<string> fieldList = DepartmentDTO.GetFieldList();
                fieldList.RemoveAt(0);

                foreach (string field in fieldList)
                {
                    commandText += field + ", ";
                }

                commandText = UtilT<string>.DeleteLastChar(commandText);
                commandText = UtilT<string>.DeleteLastChar(commandText);

                commandText += ") VALUES(";

                List<string> valueList = department.GetValueList();
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
                department.id = command.LastInsertedId;

                return new DataOut(new List<DepartmentDTO>() { department }, true);
            }
            else
            {
                return new DataOut(new List<DepartmentDTO>(), false);
            }
        }
    }
}

using ServiceStack.Redis;
using ServiceStack.Redis.Generic;
using System.Collections.Generic;
using RestAPI_UserRoles.DTO;
using MySql.Data.MySqlClient;
using System;

namespace RestAPI_UserRoles
{
    public class Redis
    {
        public static List<CustomerDTO> GetCustomers()
        {
            var typedClient = GetConnection();
            List<CustomerDTO> result = new List<CustomerDTO>();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                result.Add(new CustomerDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].name,
                    typedClient.GetAll()[i].email,
                    typedClient.GetAll()[i].role
                    ));
            }

            return result;
        }
        public static CustomerDTO GetIdCustomers(int id)
        {
            var typedClient = GetConnection();
            CustomerDTO result = new CustomerDTO();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                if (typedClient.GetAll()[i].id == id)
                {
                    result = new CustomerDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].name,
                    typedClient.GetAll()[i].email,
                    typedClient.GetAll()[i].role
                    );
            break;
                }
            }
            return result;
        }
        public static void UpdateCustomers()
        {
            DataIn<CustomerDTO> dataIn = new DataIn<CustomerDTO>(null, 0);
            DataOut<CustomerDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<CustomerDTO>, MySqlConnection, DataOut<CustomerDTO>>(CustomersDataManager.Get), dataIn);

            var typedClient = GetConnection();
            typedClient.FlushDb();

            typedClient.StoreAll(dataOut.data);
        }

        public static int GetCount()
        {
            var typedClient = GetConnection();
            return typedClient.GetAll().Count;
        }

        private static IRedisTypedClient<CustomerDTO> GetConnection()
        {
            RedisClient client = new RedisClient("localhost", 6379);
            IRedisTypedClient<CustomerDTO> typedClient = client.As<CustomerDTO>();
            return typedClient;
        }
    }
}

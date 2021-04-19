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
            var typedClient = GetConnection<CustomerDTO>();
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
            var typedClient = GetConnection<CustomerDTO>();
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

            var typedClient = GetConnection<CustomerDTO>();
            typedClient.FlushDb();

            typedClient.StoreAll(dataOut.data);
        }


        public static List<ProductDTO> GetProducts()
        {
            var typedClient = GetConnection<ProductDTO>();
            List<ProductDTO> result = new List<ProductDTO>();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                result.Add(new ProductDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].amount,
                    typedClient.GetAll()[i].productName
                    ));
            }

            return result;
        }
        public static ProductDTO GetIdProducts(int id)
        {
            var typedClient = GetConnection<ProductDTO>();
            ProductDTO result = new ProductDTO();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                if (typedClient.GetAll()[i].id == id)
                {
                    result = new ProductDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].amount,
                    typedClient.GetAll()[i].productName
                    );
                    break;
                }
            }
            return result;
        }
        public static void UpdateProducts()
        {
            DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(null, 0);
            DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.Get), dataIn);

            var typedClient = GetConnection<ProductDTO>();
            typedClient.FlushDb();

            typedClient.StoreAll(dataOut.data);
        }


        public static List<OrderDTO> GetOrders()
        {
            var typedClient = GetConnection<OrderDTO>();
            List<OrderDTO> result = new List<OrderDTO>();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                result.Add(new OrderDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].amount,
                    typedClient.GetAll()[i].user_id,
                    typedClient.GetAll()[i].product_id,
                    typedClient.GetAll()[i].time
                    ));
            }

            return result;
        }
        public static OrderDTO GetIdOrders(int id)
        {
            var typedClient = GetConnection<OrderDTO>();
            OrderDTO result = new OrderDTO();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                if (typedClient.GetAll()[i].id == id)
                {
                    result = new OrderDTO(
                    Convert.ToInt32(typedClient.GetAll()[i].id),
                    typedClient.GetAll()[i].amount,
                    typedClient.GetAll()[i].user_id,
                    typedClient.GetAll()[i].product_id,
                    typedClient.GetAll()[i].time
                    );
                    break;
                }
            }
            return result;
        }
        public static void UpdateOrders()
        {
            DataIn<OrderDTO> dataIn = new DataIn<OrderDTO>(null, 0);
            DataOut<OrderDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<OrderDTO>, MySqlConnection, DataOut<OrderDTO>>(OrdersDataManager.Get), dataIn);

            var typedClient = GetConnection<OrderDTO>();
            typedClient.FlushDb();

            typedClient.StoreAll(dataOut.data);
        }


        private static IRedisTypedClient<T> GetConnection<T>()
        {
            RedisClient client = new RedisClient("localhost", 6379);
            IRedisTypedClient<T> typedClient = client.As<T>();
            return typedClient;
        }
    }
}

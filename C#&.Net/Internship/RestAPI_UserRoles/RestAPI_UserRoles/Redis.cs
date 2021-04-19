using RestAPI_UserRoles.DTO;
using ServiceStack.Redis;
using ServiceStack.Redis.Generic;
using System.Collections.Generic;


namespace RestAPI_UserRoles.Auth.API
{
    public class Redis
    {
        public static void Update()
        {
            var typedClient = GetConnection();
            typedClient.FlushDb();

            typedClient.StoreAll(DataManager.Get());
        }

        public static List<Account> Get()
        {
            var typedClient = GetConnection();
            List<Account> result = new List<Account>();

            for (int i = 0; i < typedClient.GetAll().Count; i++)
            {
                result.Add(new Account(typedClient.GetAll()[i].id,
                    typedClient.GetAll()[i].email,
                    typedClient.GetAll()[i].password,
                    typedClient.GetAll()[i].role
                    ));
            }

            return result;
        }

        private static IRedisTypedClient<Account> GetConnection()
        {
            RedisClient client = new RedisClient("localhost", 6379);
            IRedisTypedClient<Account> typedClient = client.As<Account>();
            return typedClient;
        }
    }
}

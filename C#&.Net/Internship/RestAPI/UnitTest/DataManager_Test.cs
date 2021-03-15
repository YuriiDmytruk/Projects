using System.Collections.Generic;
using Xunit;
using RestAPI;
using MySql.Data.MySqlClient;

namespace UnitTest.RestAPI
{
    public class DataManager_Test
    {
        [Theory]
        [InlineData(null, null)]
        public void GetId_Test(DataIn dataIn, MySqlConnection connect)
        {
            DataOut result = DataManager.GetId(dataIn, connect);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null)]
        public void Put_Test(DataIn dataIn, MySqlConnection connect)
        {
            DataOut result = DataManager.Put(dataIn, connect);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null)]
        public void Post_Test(DataIn dataIn, MySqlConnection connect)
        {
            DataOut result = DataManager.Post(dataIn, connect);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null)]
        public void Delete_Test(DataIn dataIn, MySqlConnection connect)
        {
            DataOut result = DataManager.Delete(dataIn, connect);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null)]
        public void Get_Test(DataIn dataIn, MySqlConnection connect)
        {
            DataOut result = DataManager.Get(dataIn, connect);

            Assert.NotNull(result);
        }
    }
}

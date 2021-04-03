using System.Collections.Generic;
using Xunit;
using RestAPI;

namespace UnitTest.RestAPI
{
    public class UtilT_Test
    {

        [Theory]
        [InlineData(null, null, null)]
        public void Swap_Test(List<DepartmentDTO> list, int x, int y)
        {
            List<DepartmentDTO> result = UtilT<DepartmentDTO>.Swap(list, x, y);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null)]
        [InlineData("qsawd", "awdasdqawd")]
        public void Contains_Test(string conteiner, string toFind)
        {
            bool result = UtilT<string>.Contains(conteiner, toFind);

            Assert.False(result);
        }

        [Theory]
        [InlineData(null)]
        public void DeleteLastChar_Test(string value)
        {
            string result = UtilT<string>.DeleteLastChar(value);

            Assert.NotNull(result);
        }
    }
}

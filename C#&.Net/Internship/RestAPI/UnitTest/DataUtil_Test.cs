using System.Collections.Generic;
using Xunit;
using RestAPI;

namespace UnitTest.RestAPI
{
    public class DataUtil_Test
    {
        [Theory]
        [InlineData(null, null)]
        [InlineData(null, "x")]
        public void Search_Test(List<DepartmentDTO> list, string value)
        {
            List<DepartmentDTO> result = DataUtil.Search(list, value);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, 0, 0)]
        [InlineData(null, -3, 150)]
        [InlineData(null, 0, -5)]
        public void CreatePage_Test(List<DepartmentDTO> departments, int page, int page_size)
        {
            List<DepartmentDTO> result = DataUtil.CreatePage(departments, page, page_size);

            Assert.NotNull(result);
        }

        [Theory]
        [InlineData(null, null, null)]
        [InlineData(null, "asdas", "asdf")]
        [InlineData(null, null, "asd")]
        [InlineData(null, "cascdac", null)]
        public void Sort_Test(List<DepartmentDTO> departments, string sort_by, string sort_type)
        {
            List<DepartmentDTO> result = DataUtil.Sort(departments, sort_by, sort_type);

            Assert.NotNull(result);
        }
    }
}
using Xunit;
using RestAPI;

namespace UnitTest.RestAPI
{
    public class Validator_Test
    {
        [Theory]
        [InlineData(null, null)]
        [InlineData("asdafa", "asdasd")]
        [InlineData(null, "asdasd")]
        public void Validate_Test(string value, string validateInfo)
        {
            Validator valid = new Validator();

            string result = valid.Validate(value, validateInfo);

            Assert.Null(result);
        }
    }
}

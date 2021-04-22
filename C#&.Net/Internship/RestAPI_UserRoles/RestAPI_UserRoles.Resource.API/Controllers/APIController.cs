using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace RestAPI_UserRoles.Controllers
{
    [ApiController]
    [Route("/api")]
    public class APIController : ControllerBase
    {


        [HttpGet]
        public DTO.APIDTO Get()
        {
            DTO.APIDTO result = new DTO.APIDTO();
            Redis.UpdateCustomers();
            result.message.Add("Started");
            result.message.Add("mySQL DB Connected");
            result.message.Add("Customers are cached");

            return result;
        }



        private readonly ILogger<APIController> _logger;
        public APIController(ILogger<APIController> logger)
        {
            _logger = logger;
        }
    }
}

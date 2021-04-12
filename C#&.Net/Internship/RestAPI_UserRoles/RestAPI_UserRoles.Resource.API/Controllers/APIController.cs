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

            result.message.Add("Started; ");

            return result;
        }



        private readonly ILogger<APIController> _logger;
        public APIController(ILogger<APIController> logger)
        {
            _logger = logger;
        }
    }
}

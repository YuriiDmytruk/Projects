using System.Collections.Generic;

namespace RestAPI_UserRoles.DTO
{
    public class APIDTO
    {
        public List<string> message { get; set; }

        public APIDTO()
        {
            message = new List<string>();
        }
    }
}

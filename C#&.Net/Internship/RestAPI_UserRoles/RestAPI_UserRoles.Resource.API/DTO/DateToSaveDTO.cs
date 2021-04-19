using System;

namespace RestAPI_UserRoles.DTO
{
    public class DateToSaveDTO
    {
        public int id { get; set; }
        public string from { get; set; }
        public string to { get; set; }
        public string action { get; set; }
        public string time { get; set; }

        public DateToSaveDTO()
        {

        }

        public DateToSaveDTO(int id, string from, string to, string action)
        {
            this.id = id;
            this.from = from;
            this.to = to;
            this.action = action;
            time = Convert.ToString(DateTime.Now);
        }
    }
}

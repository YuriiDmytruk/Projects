namespace RestAPI_UserRoles.DTO
{
    public class HistoryDTO
    {
        public long id { get; set; }
        public string from { get; set; }
        public string to { get; set; }
        public string action { get; set; }
        public int user_id { get; set; }
        public string role { get; set; }
        public string changed_table { get; set; }

        public HistoryDTO(int id, string from, string to, string action, int user_id, string role, string changed_table)
        {
            this.id = id;
            this.from = from;
            this.to = to;
            this.action = action;
            this.user_id = user_id;
            this.role = role;
            this.changed_table = changed_table;
        }
    }
}

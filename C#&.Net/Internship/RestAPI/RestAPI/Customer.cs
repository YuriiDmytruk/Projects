namespace RestAPI
{
    public class Customer
    {
        public long id { get; set; }
        public string name { get; set; }
        public string email { get; set; }

        public Customer(long id, string name, string email)
        {
            this.id = id;
            this.name = name;
            this.email = email;
        }
    }
}

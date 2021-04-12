namespace RestAPI_UserRoles.DTO
{
    public class Account
    {
        public long id { get; set; }
        public string password { get; set; }
        public string email { get; set; }
        public Role[] role { get; set; }

        public Account(int id, string email, string password, string role)
        {
            this.id = id;
            this.email = email;
            this.password = password;
            if (role == "User")
            {
                this.role = new Role[] { Role.User };
            }
            else
            {
                this.role = new Role[] { Role.Admin };
            }
        }
    }

    public enum Role
    {
        Admin, User
    }
}

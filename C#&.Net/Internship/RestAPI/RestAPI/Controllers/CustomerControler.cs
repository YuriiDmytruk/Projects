using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Collections.Generic;


namespace RestAPI.Controllers
{
    [ApiController]
    [Route("/customer")]
    public class CustomerControler : ControllerBase
    {
        private readonly ILogger<CustomerControler> _logger;

        public CustomerControler(ILogger<CustomerControler> logger)
        {
            _logger = logger;
        }

        [HttpGet]//add ofset limit etc
        public ReturnModel Get()
        {
            List<Customer> customers = DataManager.GetAllCustomers();
            return new ReturnModel(customers, "200", "All Customers");
        }

        [HttpGet("{id}")]//done
        public ReturnModel GetByID(int id)
        {
            Customer customer = DataManager.GetCustomer(id);
            if (customer != null)
            {
                List<Customer> customers = new List<Customer>();
                customers.Add(customer);
                return new ReturnModel(customers, "200", "Customer with id: " + id);
            }

            return new ReturnModel(null, "404", "Customer with id: " + id + " not found");
        }

        [HttpPost]//write method
        public ReturnModel Post(JsonElement jsonData)
        {
            Customer toAdd = new Customer(-1, jsonData.GetProperty("name").GetString(), jsonData.GetProperty("email").GetString());

            List<Customer> customers = new List<Customer>();
            customers.Add(DataManager.InsertCustomer(toAdd));
            return new ReturnModel(customers, "200", "Successfully added");
        }

        [HttpPut("{id}")]//write method
        public ReturnModel Put()
        {
            ReturnModel result = new ReturnModel();
            return result;
        }

        [HttpDelete("{id}")]//done
        public ReturnModel Delete(int id)
        {
            if (DataManager.DeleteCustomer(id))
            {
                return new ReturnModel(null, "200", "Customer with id: " + id + " deleted");
            }

            return new ReturnModel(null, "404", "Customer with id: " + id + " not found");
        }
    }
}

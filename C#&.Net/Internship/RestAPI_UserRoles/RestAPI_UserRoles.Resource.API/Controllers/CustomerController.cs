using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using System;
using RestAPI_UserRoles.DTO;
using System.Linq;
using System.Security.Claims;

namespace RestAPI_UserRoles.Controllers
{
    [ApiController]
    [Route("/api/customers")]
    public class CustomerController : ControllerBase
    {
        private int UserId => Int32.Parse(User.Claims.Single(c => c.Type == ClaimTypes.NameIdentifier).Value);
        private string UserRole => User.Claims.Single(c => c.Type == ClaimTypes.Role).Value;


        // Only Admin
        [HttpGet]
        public ReturnModel<CustomerDTO> Get([FromQuery] string sort_by, [FromQuery] string sort_type, [FromQuery] string find, [FromQuery] int page_size, [FromQuery] int page)
        {
            if (UserRole == "Admin")
            {
                List<CustomerDTO> data = Redis.GetCustomers();

                List<string> errorList = new List<string>();

                data = DataUtil.Sort(data, sort_by, sort_type);

                if (page_size == 0)
                {
                    page_size = data.Count;
                }
                data = DataUtil.CreatePage(data, page, page_size);

                data = DataUtil.Search(data, find);
                if (data.Count == 0)
                {
                    errorList.Add("Nothing was found during the search");
                }

                if (errorList.Count == 0)
                {
                    errorList.Add("None");
                }
                if (data.Count == 0)
                {
                    return new ReturnModel<CustomerDTO>(data, "204", "Nothing found", data.Count, page, errorList);
                }
                else
                {
                    return new ReturnModel<CustomerDTO>(data, "200", "All Customers", data.Count, page, errorList);
                }
            }
            else
            {
                return new ReturnModel<CustomerDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
            }

        }

        // Only Admin or Loged in user
        [HttpGet("{id}")]
        public ReturnModel<CustomerDTO> GetId(int id)
        {
            if (UserId == id || UserRole == "Admin")
            {
                List<CustomerDTO> data = new List<CustomerDTO>();
                data.Add(Redis.GetIdCustomers(id));

                if (data.Count == 0)
                {
                    return new ReturnModel<CustomerDTO>(null, "204", "Customer with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
                }
                else if (data.Count == 1 && data[0] == null)
                {
                    return new ReturnModel<CustomerDTO>(null, "204", "Customer with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
                }
                else
                {
                    return new ReturnModel<CustomerDTO>(data, "200", "Customer with id: " + id, 0, data.Count, new List<string>() { "None" });
                }
            }
            else
            {
                return new ReturnModel<CustomerDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
            }

        }

        //Only Admin can create new Admin
        [HttpPost]
        public ReturnModel<CustomerDTO> Post(JsonElement jsonData)
        {
            if (jsonData.GetProperty("role").GetString() == "Admin" && UserRole != "Admin")
            {
                return new ReturnModel<CustomerDTO>(null, "401", "Forbiden", 0, 0, new List<string>() { "Only Admin can create new admin" });
            }
            else
            {
                Validator validate = new Validator();

                List<string> fieldList = CustomerDTO.GetFieldList();
                fieldList.RemoveAt(0);

                List<string> createList = new List<string>();

                for (int i = 0; i < fieldList.Count; i++)
                {
                    createList.Add(validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]));
                }

                CustomerDTO toAdd = new CustomerDTO(createList);

                if (validate.errorList.Count == 0)
                {
                    DataIn<CustomerDTO> dataIn = new DataIn<CustomerDTO>(toAdd, 0, jsonData.GetProperty("password").GetString());
                    DataOut<CustomerDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<CustomerDTO>, MySqlConnection, DataOut<CustomerDTO>>(CustomersDataManager.Post), dataIn);

                    validate.Add("None");
                    return new ReturnModel<CustomerDTO>(dataOut.data, "200", "Successfully added", 0, dataOut.data.Count, validate.errorList);
                }
                else
                {
                    return new ReturnModel<CustomerDTO>(null, "406", "Not Acceptable", 0, 0, validate.errorList);
                }
            }
        }

        // Only Admin or Loged in user + Only admin can cheange User to Admin
        [HttpPut("{id}")]
        public ReturnModel<CustomerDTO> Put(int id, JsonElement jsonData)
        {
            if (UserId == id || UserRole == "Admin")
            {
                JsonElement copy = jsonData;
                if (copy.TryGetProperty("role", out copy))
                {
                    if (jsonData.GetProperty("role").GetString() == "Admin" && UserRole != "Admin")
                    {
                        return new ReturnModel<CustomerDTO>(null, "401", "Forbiden", 0, 0, new List<string>() { "Only Admin can cheange role User to Admin" });
                    }
                }
                Validator validate = new Validator();

                List<string> fieldList = CustomerDTO.GetFieldList();
                fieldList.RemoveAt(0);

                copy = jsonData;
                for (int i = 0; i < fieldList.Count; i++)
                {
                    copy = jsonData;
                    if (copy.TryGetProperty(fieldList[i], out copy))
                    {
                        fieldList[i] = validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]);
                    }
                    else { fieldList[i] = null; }
                }

                CustomerDTO toAdd = new CustomerDTO(id, fieldList[0], fieldList[1], fieldList[2]);

                if (validate.errorList.Count == 0)
                {
                    copy = jsonData;
                    string password = "";
                    if (copy.TryGetProperty("password", out copy))
                    {
                        password = jsonData.GetProperty("password").GetString();
                    }

                    DataIn<CustomerDTO> dataIn = new DataIn<CustomerDTO>(toAdd, id, password);
                    DataOut<CustomerDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<CustomerDTO>, MySqlConnection, DataOut<CustomerDTO>>(CustomersDataManager.Put), dataIn);

                    validate.Add("None");
                    return new ReturnModel<CustomerDTO>(null, "200", "This fields will be modified in element whith id: " + id, 0, 0, validate.errorList);
                }
                else
                {
                    return new ReturnModel<CustomerDTO>(null, "304", "Not Modified", 0, 0, validate.errorList);
                }
            }
            else
            {
                return new ReturnModel<CustomerDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin can cheange this date" });
            }
        }

        // Only Admin or Loged in user
        [HttpDelete("{id}")]
        public ReturnModel<CustomerDTO> Delete(int id)
        {
            if (UserId == id || UserRole == "Admin")
            {
                DataIn<CustomerDTO> dataIn = new DataIn<CustomerDTO>(null, id);
                DataOut<CustomerDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<CustomerDTO>, MySqlConnection, DataOut<CustomerDTO>>(CustomersDataManager.Delete), dataIn);

                if (dataOut.success)
                {
                    return new ReturnModel<CustomerDTO>(null, "200", "Customer with id: " + id + " deleted", 0, 0, new List<string>() { "None" });
                }
                else
                {
                    if (dataOut.errorMessage == "Admin")
                    {
                        return new ReturnModel<CustomerDTO>(null, "404", "Customer with id: " + id + " not found", 0, 0, new List<string>() { "You can't delete Admin" });
                    }
                    else
                    {
                        return new ReturnModel<CustomerDTO>(null, "404", "Customer with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
                    }
                }
            }
            else
            {
                return new ReturnModel<CustomerDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
            }
        }



        private readonly ILogger<CustomerController> _logger;
        public CustomerController(ILogger<CustomerController> logger)
        {
            _logger = logger;
        }
    }
}

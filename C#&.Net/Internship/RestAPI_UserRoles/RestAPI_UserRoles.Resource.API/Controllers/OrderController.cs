using Microsoft.AspNetCore.Mvc;
using System.Text.Json;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using System;
using RestAPI_UserRoles.DTO;
using System.Linq;
using System.Security.Claims;

namespace RestAPI_UserRoles.Resource.API.Controllers
{
    [ApiController]
    [Route("/api/orders")]
    public class OrderController : Controller
    {

        private int UserId => Int32.Parse(User.Claims.Single(c => c.Type == ClaimTypes.NameIdentifier).Value);
        private string UserRole => User.Claims.Single(c => c.Type == ClaimTypes.Role).Value;

        // Only Loged in User and Admin
        [HttpGet]
        public ReturnModel<OrderDTO> Get([FromQuery] string sort_by, [FromQuery] string sort_type, [FromQuery] string find, [FromQuery] int page_size, [FromQuery] int page)
        {

            DataIn<OrderDTO> dataIn = new DataIn<OrderDTO>(null, 0, "");
            DataOut<OrderDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<OrderDTO>, MySqlConnection, DataOut<OrderDTO>>(OrderDataManager.Get), dataIn);

            if (UserRole != "Admin")
            {
                for (int i = 0; i < dataOut.data.Count; i++)
                {
                    if (dataOut.data[i].user_id != UserId)
                    {
                        dataOut.data.RemoveAt(i);
                    }
                }
            }

            List<string> errorList = new List<string>();

            dataOut.data = DataUtil.Sort(dataOut.data, sort_by, sort_type);

            if (page_size == 0)
            {
                page_size = dataOut.data.Count;
            }
            dataOut.data = DataUtil.CreatePage(dataOut.data, page, page_size);

            dataOut.data = DataUtil.Search(dataOut.data, find);
            if (dataOut.data.Count == 0)
            {
                errorList.Add("Nothing was found during the search");
            }

            if (errorList.Count == 0)
            {
                errorList.Add("None");
            }
            if (dataOut.data.Count == 0)
            {
                return new ReturnModel<OrderDTO>(dataOut.data, "204", "Nothing found", dataOut.data.Count, page, errorList);
            }
            else
            {
                return new ReturnModel<OrderDTO>(dataOut.data, "200", "All Orders", dataOut.data.Count, page, errorList);
            }
        }

        // Only Loged in User and Admin
        [HttpGet("{id}")]
        public ReturnModel<OrderDTO> GetId(int id)
        {

            DataIn<OrderDTO> dataIn = new DataIn<OrderDTO>(null, id);
            DataOut<OrderDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<OrderDTO>, MySqlConnection, DataOut<OrderDTO>>(OrderDataManager.GetId), dataIn);

            if (dataOut.data.Count == 0)
            {
                return new ReturnModel<OrderDTO>(null, "204", "Order with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
            }
            else if (dataOut.data.Count == 1 && dataOut.data[0] == null)
            {
                return new ReturnModel<OrderDTO>(null, "204", "Order with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
            }
            else
            {
                if (UserRole != "Admin")
                {
                    if (dataOut.data[0].user_id != UserId)
                    {
                        return new ReturnModel<OrderDTO>(dataOut.data, "401", "Forbiden", 0, dataOut.data.Count, new List<string>() { "This date is forbiden for you" });
                    }
                    else
                    {
                        return new ReturnModel<OrderDTO>(dataOut.data, "200", "Order with id: " + id, 0, dataOut.data.Count, new List<string>() { "None" });
                    }
                }
                else
                {
                    return new ReturnModel<OrderDTO>(dataOut.data, "200", "Order with id: " + id, 0, dataOut.data.Count, new List<string>() { "None" });
                }
            }
        }

        // Only Loged in User and Admin
        [HttpPost]
        public ReturnModel<OrderDTO> Post(JsonElement jsonData)
        {
            Validator validate = new Validator();

            List<string> fieldList = OrderDTO.GetFieldList();

            fieldList.RemoveAt(0);
            fieldList.RemoveAt(1);
            fieldList.RemoveAt(2);

            List<string> createList = new List<string>();

            for (int i = 0; i < fieldList.Count; i++)
            {
                createList.Add(validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]));
            }

            createList.Add(Convert.ToString(UserId));
            createList.Add(Convert.ToString(DateTime.Now));

            OrderDTO toAdd = new OrderDTO(createList);

            if (validate.errorList.Count == 0)
            {
                DataIn<OrderDTO> dataIn = new DataIn<OrderDTO>(toAdd, 0);
                DataOut<OrderDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<OrderDTO>, MySqlConnection, DataOut<OrderDTO>>(OrderDataManager.Post), dataIn);

                if (dataOut.errorMessage == "AmountError")
                {
                    return new ReturnModel<OrderDTO>(null, "402", "Amount to big", 0, dataOut.data.Count, null);
                }
                else
                {
                    validate.Add("None");
                    return new ReturnModel<OrderDTO>(dataOut.data, "200", "Successfully added", 0, dataOut.data.Count, validate.errorList);
                }
            }
            else
            {
                return new ReturnModel<OrderDTO>(null, "406", "Not Acceptable", 0, 0, validate.errorList);
            }
        }

        // Only Loged in User and Admin
        [HttpDelete("{id}")]
        public ReturnModel<OrderDTO> Delete(int id)
        {
            DataIn<OrderDTO> dataIn = new DataIn<OrderDTO>(new OrderDTO(), id, UserId, UserRole);
            DataOut<OrderDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<OrderDTO>, MySqlConnection, DataOut<OrderDTO>>(OrderDataManager.Delete), dataIn);

            if (dataOut.success)
            {
                return new ReturnModel<OrderDTO>(null, "200", "Product with id: " + id + " deleted", 0, 0, new List<string>() { "None" });
            }
            else
            {
                if (dataOut.errorMessage == "forbiden")
                {
                    return new ReturnModel<OrderDTO>(null, "404", "Product with id: " + id + " not found", 0, 0, new List<string>() { "You can't delete this order" });
                }
                else
                {
                    return new ReturnModel<OrderDTO>(null, "404", "Product with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
                }
            }
        }
    }
}

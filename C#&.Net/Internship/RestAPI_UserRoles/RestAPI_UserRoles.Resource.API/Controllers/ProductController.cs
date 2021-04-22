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
    [Route("/api/products")]
    public class ProductController : Controller
    {
        private string UserRole => User.Claims.Single(c => c.Type == ClaimTypes.Role).Value;


        [HttpGet]
        public ReturnModel<ProductDTO> Get([FromQuery] string sort_by, [FromQuery] string sort_type, [FromQuery] string find, [FromQuery] int page_size, [FromQuery] int page)
        {
            DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(null, 0);
            DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.Get), dataIn);

            List<ProductDTO> data = dataOut.data;

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
                return new ReturnModel<ProductDTO>(data, "204", "Nothing found", data.Count, page, errorList);
            }
            else
            {
                return new ReturnModel<ProductDTO>(data, "200", "All Products", data.Count, page, errorList);
            }
        }

        [HttpGet("{id}")]
        public ReturnModel<ProductDTO> GetId(int id)
        {
            DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(null, 0);
            DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.GetID), dataIn);
            List<ProductDTO> data = dataOut.data;

            if (data.Count == 0)
            {
                return new ReturnModel<ProductDTO>(null, "204", "Product with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
            }
            else if (data.Count == 1 && data[0] == null)
            {
                return new ReturnModel<ProductDTO>(null, "204", "Product with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
            }
            else
            {
                return new ReturnModel<ProductDTO>(data, "200", "Product with id: " + id, 0, data.Count, new List<string>() { "None" });
            }
        }

        //Only Admin 
        [HttpPost]
        public ReturnModel<ProductDTO> Post(JsonElement jsonData)
        {
            if (UserRole == "Admin")
            {
                Validator validate = new Validator();

                List<string> fieldList = ProductDTO.GetFieldList();
                fieldList.RemoveAt(0);

                List<string> createList = new List<string>();

                for (int i = 0; i < fieldList.Count; i++)
                {
                    createList.Add(validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]));
                }

                ProductDTO toAdd = new ProductDTO(createList);

                if (validate.errorList.Count == 0)
                {
                    DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(toAdd, 0);
                    DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.Post), dataIn);

                    validate.Add("None");
                    return new ReturnModel<ProductDTO>(dataOut.data, "200", "Successfully added", 0, dataOut.data.Count, validate.errorList);
                }
                else
                {
                    return new ReturnModel<ProductDTO>(null, "406", "Not Acceptable", 0, 0, validate.errorList);
                }
            }
            else
            {
                return new ReturnModel<ProductDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin can add new products" });
            }
        }

        // Only Admin 
        [HttpPut("{id}")]
        public ReturnModel<ProductDTO> Put(int id, JsonElement jsonData)
        {
            if (UserRole == "Admin")
            {

                Validator validate = new Validator();

                List<string> fieldList = ProductDTO.GetFieldList();
                fieldList.RemoveAt(0);

                JsonElement copy = jsonData;
                for (int i = 0; i < fieldList.Count; i++)
                {
                    copy = jsonData;
                    if (copy.TryGetProperty(fieldList[i], out copy))
                    {
                        fieldList[i] = validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]);
                    }
                    else { fieldList[i] = null; }
                }

                ProductDTO toAdd = new ProductDTO(id, Convert.ToInt32(fieldList[0]), fieldList[1]);

                if (validate.errorList.Count == 0)
                {

                    DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(toAdd, id);
                    DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.Put), dataIn);

                    validate.Add("None");
                    return new ReturnModel<ProductDTO>(null, "200", "This fields will be modified in element whith id: " + id, 0, 0, validate.errorList);
                }
                else
                {
                    return new ReturnModel<ProductDTO>(null, "304", "Not Modified", 0, 0, validate.errorList);
                }
            }
            else
            {
                return new ReturnModel<ProductDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin can cheange this date" });
            }
        }

        // Only Admin 
        [HttpDelete("{id}")]
        public ReturnModel<ProductDTO> Delete(int id)
        {
            if (UserRole == "Admin")
            {
                DataIn<ProductDTO> dataIn = new DataIn<ProductDTO>(null, id);
                DataOut<ProductDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<ProductDTO>, MySqlConnection, DataOut<ProductDTO>>(ProductsDataManager.Delete), dataIn);

                if (dataOut.success)
                {
                    return new ReturnModel<ProductDTO>(null, "200", "Product with id: " + id + " deleted", 0, 0, new List<string>() { "None" });
                }
                else
                {
                    return new ReturnModel<ProductDTO>(null, "404", "Product with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
                }
            }
            else
            {
                return new ReturnModel<ProductDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin can delete products" });
            }
        }
    }
}



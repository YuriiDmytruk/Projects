using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Collections.Generic;
using MySql.Data.MySqlClient;

namespace RestAPI.Controllers
{
    [ApiController]
    [Route("/department")]
    public class DepartmentControl : ControllerBase
    {
        [HttpGet]
        public ReturnModel Get([FromQuery] string sort_by, [FromQuery] string sort_type, [FromQuery] string find, [FromQuery] int page_size, [FromQuery] int page)
        {
            DataIn dataIn = new DataIn(null, 0);
            DataOut dataOut = MySQLConnect.Connect(new System.Func<DataIn, MySqlConnection, DataOut>(DataManager.Get), dataIn);

            List<string> errorList = new List<string>();

            dataOut.departments = DataUtil.Sort(dataOut.departments, sort_by, sort_type);

            if (page_size == 0)
            {
                page_size = dataOut.departments.Count;
            }
            dataOut.departments = DataUtil.CreatePage(dataOut.departments, page, page_size);

            dataOut.departments = DataUtil.Search(dataOut.departments, find);
            if (dataOut.departments.Count == 0)
            {
                errorList.Add("Nothing was found during the search");
            }

            


            if (errorList.Count == 0)
            {
                errorList.Add("None");
            }
            if (dataOut.departments.Count == 0)
            {
                return new ReturnModel(dataOut.departments, "204", "Nothing found", dataOut.departments.Count, page, errorList);
            }
            else
            {
                return new ReturnModel(dataOut.departments, "200", "All Customers", dataOut.departments.Count, page, errorList);
            }

        }

        [HttpGet("{id}")]
        public ReturnModel GetId(int id)
        {
            DataIn dataIn = new DataIn(null, id);
            DataOut dataOut = MySQLConnect.Connect(new System.Func<DataIn, MySqlConnection, DataOut>(DataManager.GetId), dataIn);

            if (dataOut.departments.Count == 0)
            {

                return new ReturnModel(null, "204", "Department with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
            }
            else
            {
                return new ReturnModel(dataOut.departments, "200", "Department with id: " + id, 0, dataOut.departments.Count, new List<string>() { "None" });
            }
        }

        [HttpPost]
        public ReturnModel Post(JsonElement jsonData)
        {
            Validator validate = new Validator();

            List<string> fieldList = DepartmentDTO.GetFieldList();
            fieldList.RemoveAt(0);

            List<string> createList = new List<string>();

            for (int i = 0; i < fieldList.Count; i++)
            {
                createList.Add(validate.Validate(jsonData.GetProperty(fieldList[i]).GetString(), fieldList[i]));
            }


            DepartmentDTO toAdd = new DepartmentDTO(createList);

            if (validate.errorList.Count == 0)
            {
                DataIn dataIn = new DataIn(toAdd, 0);
                DataOut dataOut = MySQLConnect.Connect(new System.Func<DataIn, MySqlConnection, DataOut>(DataManager.Post), dataIn);

                validate.Add("None");
                return new ReturnModel(dataOut.departments, "200", "Successfully added", 0, dataOut.departments.Count, validate.errorList);
            }
            else
            {
                return new ReturnModel(null, "406", "Not Acceptable", 0, 0, validate.errorList);
            }
        }

        [HttpPut("{id}")]
        public ReturnModel Put(int id, JsonElement jsonData)
        {
            ReturnModel result = new ReturnModel();
            Validator validate = new Validator();

            List<string> fieldList = DepartmentDTO.GetFieldList();
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

            DepartmentDTO toAdd = new DepartmentDTO(id, fieldList[0], fieldList[1], fieldList[2], fieldList[3], fieldList[4], fieldList[5]);

            if (validate.errorList.Count == 0)
            {
                DataIn dataIn = new DataIn(toAdd, id);
                DataOut dataOut = MySQLConnect.Connect(new System.Func<DataIn, MySqlConnection, DataOut>(DataManager.Put), dataIn);

                validate.Add("None");
                return new ReturnModel(null, "200", "This fields will be modified in element whith id: " + id, 0, 0, validate.errorList);
            }
            else
            {
                return new ReturnModel(null, "304", "Not Modified", 0, 0, validate.errorList);
            }
        }

        [HttpDelete("{id}")]
        public ReturnModel Delete(int id)
        {
            DataIn dataIn = new DataIn(null, id);
            DataOut dataOut = MySQLConnect.Connect(new System.Func<DataIn, MySqlConnection, DataOut>(DataManager.Delete), dataIn);

            if (dataOut.success)
            {
                return new ReturnModel(null, "200", "Customer with id: " + id + " deleted", 0, 0, new List<string>() { "None" });
            }

            return new ReturnModel(null, "404", "Customer with id: " + id + " not found", 0, 0, new List<string>() { "Not Found" });
        }

        private readonly ILogger<DepartmentControl> _logger;
        public DepartmentControl(ILogger<DepartmentControl> logger)
        {
            _logger = logger;
        }
    }
}

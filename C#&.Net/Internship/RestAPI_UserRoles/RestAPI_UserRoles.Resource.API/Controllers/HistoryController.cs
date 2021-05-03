using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System.Text.Json;
using System.Collections.Generic;
using MySql.Data.MySqlClient;
using System;
using RestAPI_UserRoles.DTO;
using System.Linq;
using System.Security.Claims;

namespace RestAPI_UserRoles.Resource.API.Controllers
{
    public class HistoryController : Controller
    {
        private string UserRole => User.Claims.Single(c => c.Type == ClaimTypes.Role).Value;

        // Only Admin
        [HttpGet]
        public ReturnModel<HistoryDTO> Get()
        {
            if (UserRole == "Admin")
            { 
                DataIn<HistoryDTO> dataIn = new DataIn<HistoryDTO>(null, 0);
                DataOut<HistoryDTO> dataOut = MySQLConnect.Connect(new System.Func<DataIn<HistoryDTO>, MySqlConnection, DataOut<HistoryDTO>>(HistoryDataManager.Get), dataIn);
                if (dataOut.data.Count == 0)
                {
                    return new ReturnModel<HistoryDTO>(dataOut.data, "204", "Nothing found", dataOut.data.Count, 0, new List<string>());
                }
                else
                {
                    return new ReturnModel<HistoryDTO>(dataOut.data, "200", "History", dataOut.data.Count, 0, new List<string>());
                }
            }
            else
            {
                return new ReturnModel<HistoryDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
            }
        }
    }
}

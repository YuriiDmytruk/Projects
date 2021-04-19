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

        //// Only Admin
        //[HttpGet]
        //public ReturnModel<DateToSaveDTO> Get()
        //{
        //    if (UserRole == "Admin")
        //    {
        //        List<DateToSaveDTO> result = Redis.Get();
        //        if (result.Count == 0)
        //        {
        //            return new ReturnModel<DateToSaveDTO>(result, "204", "Nothing found", result.Count, 0, new List<string>());
        //        }
        //        else
        //        {
        //            return new ReturnModel<DateToSaveDTO>(result, "200", "History", result.Count, 0, new List<string>());
        //        }
        //    }
        //    else
        //    {
        //        return new ReturnModel<DateToSaveDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
        //    }
        //}

        //// Only Admin
        //[HttpGet("{id}")]
        //public ReturnModel<DateToSaveDTO> GetId(int id)
        //{
        //    if (UserRole == "Admin")
        //    {

        //        List<DateToSaveDTO> result = new List<DateToSaveDTO>();
        //        result.Add(Redis.GetId(id));
        //        if (result.Count == 0)
        //        {
        //            return new ReturnModel<DateToSaveDTO>(result, "204", "Nothing found", result.Count, 0, new List<string>());
        //        }
        //        else
        //        {
        //            return new ReturnModel<DateToSaveDTO>(result, "200", "History", result.Count, 0, new List<string>());
        //        }
        //    }
        //    else
        //    {
        //        return new ReturnModel<DateToSaveDTO>(null, "401", "Access is forbiden", 0, 0, new List<string>() { "Only Admin has access to this date" });
        //    }

        //}
    }
}

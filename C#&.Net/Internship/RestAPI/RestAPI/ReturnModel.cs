﻿using System.Collections.Generic;

namespace RestAPI
{
    public class ReturnModel
    {
        public List<Customer> customers { get; set; }
        public string status { get; set; }
        public string massage { get; set; }

        public ReturnModel(List<Customer> customers, string status, string massage)
        {
            this.customers = customers;
            this.massage = massage;
            this.status = status;
        }

        public ReturnModel()
        {
            customers = new List<Customer>();
            massage = "";
            status = "";
        }
    }
}

using System.Collections.Generic;

namespace RestAPI
{
    public class ReturnModel
    {
        public List<DepartmentDTO> data { get; set; }
        public string status { get; set; }
        public int page { get; set; }
        public int pageSize { get; set; }
        public string message { get; set; }
        public List<string> errorList { get; set; }

        
        public ReturnModel(List<DepartmentDTO> data, string status, string message, int page, int pageSize, List<string> errorList)
        {
            this.data = data;
            this.message = message;
            this.status = status;
            this.pageSize = page;
            this.page = pageSize;
            this.errorList = errorList;
        }

        public ReturnModel()
        {
            data = new List<DepartmentDTO>();
            message = "";
            status = "";
            page = 1;
            pageSize = 0;
            this.errorList = new List<string>();
        }
    }
}

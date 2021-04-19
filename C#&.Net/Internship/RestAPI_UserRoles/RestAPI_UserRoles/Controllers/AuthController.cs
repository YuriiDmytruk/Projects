using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using RestAPI_UserRoles.DTO;
using Microsoft.Extensions.Options;
using RestAPI_UserRoles.Common;
using Microsoft.IdentityModel.Tokens;
using System.Security.Claims;
using System.IdentityModel.Tokens.Jwt;
using System.Text.Json;
using RestAPI_UserRoles.Auth.API;

namespace RestAPI_UserRoles.Controllers
{

    [ApiController]
    [Route("/api/auth")]
    public class AuthController : Controller
    {
        private readonly IOptions<AuthOptions> authOptions;
        public AuthController(IOptions<AuthOptions> authOptions)
        {
            this.authOptions = authOptions;
        }

        [HttpGet]
        public ReturnModel<string> Get()
        {
            Redis.Update();
            return new ReturnModel<string>(null, "200", "Authorization server started", 0, 0, null);
        }

        [HttpPost]
        public ReturnModel<Account> Post(JsonElement jsonData)
        {
            Account account = AuthenticateUser(jsonData.GetProperty("email").GetString(), jsonData.GetProperty("password").GetString());

            if (account != null)
            {
                var token = GenerateJWT(account);

                return new ReturnModel<Account>(null, "200", "Authorized", 0, 0, new List<string>() { "Your Token :  " + token + "   "});
            }
            else
            {
                return new ReturnModel<Account>(null, "401", "UnAuthorized", 0, 0, new List<string>() { "wrong password or email"});
            }
        }
        private Account AuthenticateUser(string email, string password)
        {
            List<Account> accounts = Redis.Get();

            for (int i = 0; i < accounts.Count; i++)
            {
                if (email == accounts[i].email && password == accounts[i].password)
                {
                    return accounts[i];
                }
            }
            return null;
        }
        private string GenerateJWT(Account account)
        {
            var authParams = authOptions.Value;

            var securityKey = authParams.GetSymmetricSecurityKey();
            var credentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);

            var claims = new List<Claim>()
            {
                new Claim (JwtRegisteredClaimNames.Email, account.email),
                new Claim(JwtRegisteredClaimNames.Sub, account.id.ToString())
            };

            foreach (var role in account.role)
            {
                claims.Add(new Claim("role", role.ToString()));
            }

            var token = new JwtSecurityToken(authParams.Issuer,
                authParams.Audience,
                claims,
                expires: DateTime.Now.AddSeconds(authParams.TokenLifeTime),
                signingCredentials : credentials);

            return new JwtSecurityTokenHandler().WriteToken(token);
        }
    }
}

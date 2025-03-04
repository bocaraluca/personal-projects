using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ScoalaCodeFirst.Models;

namespace ScoalaCodeFirst.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ClaseController : ControllerBase
    {
        private readonly ScoalaDbContext _context;

        public ClaseController(ScoalaDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<List<Clasa>>> GetClase()
        {
            var clase = await _context.Clase.Include(c => c.Elevi).ToListAsync();
            return Ok(clase);
        }
    }
}

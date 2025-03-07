using Firma.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.SqlServer.Query.Internal;

namespace Firma.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AngajatiController : ControllerBase
    {
        private readonly FirmaDbContext _context;

        public AngajatiController(FirmaDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        [Route("/Angajati")]
        public async Task<ActionResult<List<Angajat>>> GetAngajati()
        {
            var angajati = await _context.Angajati.ToListAsync();
            return Ok(angajati);
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Angajat>> GetAngajatById(int id)
        {
            var angajat = await _context.Angajati.FindAsync(id);

            if (angajat == null)
            {
                return NotFound();
            }

            return Ok(angajat);
        }

        [HttpPost]
        public async Task<ActionResult<Angajat>> PostAngajat(Angajat angajat)
        {
            _context.Angajati.Add(angajat);
            await _context.SaveChangesAsync();

            return Ok(angajat);
        }

        [HttpPut]
        public async Task<ActionResult<Angajat>> PutAngajat(int id, Angajat angajat)
        {
            if (id != angajat.IdAngajat) 
            {
                return BadRequest();
            }

            if (!_context.Angajati.Any(e => e.IdAngajat == id))
                return NotFound();

            _context.Entry(angajat).State = EntityState.Modified;
            await _context.SaveChangesAsync();

            return NoContent();
        }

        [HttpDelete]
        public async Task<ActionResult<Angajat>> DeleteAngajat(int id)
        {
            var angajat = _context.Angajati.Find(id);
            if (angajat == null)
                return NotFound("Angajatul nu a fost gasit!");

            _context.Angajati.Remove(angajat);

            await _context.SaveChangesAsync();

            return NoContent();
        }
    }
}

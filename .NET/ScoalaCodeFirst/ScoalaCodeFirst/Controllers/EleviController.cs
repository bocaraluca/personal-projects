using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ScoalaCodeFirst.Models;
using System.Reflection.Metadata.Ecma335;

namespace ScoalaCodeFirst.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EleviController : ControllerBase
    {
        private readonly ScoalaDbContext _context;

        public EleviController(ScoalaDbContext context)
        {
            _context = context;
        }

        // Action Methods
        [HttpGet]
        public async Task<ActionResult<List<Elev>>> GetElevi()
        {
            var elevi = await _context.Elevi.ToListAsync();
            return Ok(elevi);
        }

        // Action Methods
        [HttpGet("filtru")]
   //     [Route("filtru")]
        public async Task<ActionResult<List<Elev>>> GetEleviDupaNume([FromQuery] string text, [FromQuery] string sortBy)
        {
            var elevi = await _context.Elevi.ToListAsync();

            // filtram elevii dupa un criteriu legat de nume
            var stud = elevi.Where(e => e.Nume.Contains(text, StringComparison.OrdinalIgnoreCase ));

            // ordonam lista filtrata dupa un criteriu care soseste prin "query string"

            switch (sortBy)
            {
                case "nume":
                    stud = stud.OrderBy(e => e.Nume);
                    break;

                case "data":  // ordonare dupa data nasterii
                    stud = stud.OrderByDescending(e => e.DataNasterii);
                    break;
                case "clasa":  // ordonare dupa data nasterii
                    stud = stud.OrderBy(e => e.ClasaID);
                    break;

                case "id":  // ordonare dupa data nasterii
                    stud = stud.OrderByDescending(e => e.ElevID);
                    break;

                default: 
                    return BadRequest();
            }
            return Ok(stud);
        }

        // Route:  https://localhost:5500/api/elevi/3
        [HttpGet("{id}")]
        public async Task<ActionResult<Elev>> GetElevById(int id)
        {
            var elev = await _context.Elevi.FindAsync(id);
            if (elev == null)
                return NotFound();

            return elev;
        }

        [HttpPost]
        public async Task<ActionResult<Elev>> PostElev(Elev elev)
        {
            _context.Elevi.Add(elev);
            await _context.SaveChangesAsync();

           // return Ok("Elevul a fost adaugat cu succes");
            return CreatedAtAction("GetElevi", new {ElevId = elev.ElevID}, elev);
        }

        [HttpPut("{id}")]
        public async Task<ActionResult<Elev>> PutElev(int id, Elev elev)
        {
            if (id != elev.ElevID)
                return BadRequest();

            if (!ElevExists(id))
                return NotFound();

            _context.Entry(elev).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            return NoContent();
        }

        private bool ElevExists(int id)
        {
            return _context.Elevi.Any(e => e.ElevID == id);
        }

        [HttpDelete("id")]
        public async Task<ActionResult<Elev>> DeleteElev(int id)
        {
            var elev = await _context.Elevi.FindAsync(id);
            if (elev == null)
                return NotFound();

            _context.Elevi.Remove(elev);
            await _context.SaveChangesAsync();

            return NoContent();
        }


    }
}

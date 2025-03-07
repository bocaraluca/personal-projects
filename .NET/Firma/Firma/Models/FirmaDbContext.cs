using Microsoft.EntityFrameworkCore;

namespace Firma.Models
{
    public class FirmaDbContext : DbContext
    { 
        public FirmaDbContext(DbContextOptions options) : base(options) 
        {
        }

        public DbSet<Angajat> Angajati { get; set;}
    }
}

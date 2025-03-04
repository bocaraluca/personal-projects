using Microsoft.EntityFrameworkCore;

namespace ScoalaCodeFirst.Models
{
    public class ScoalaDbContext : DbContext
    {
        public ScoalaDbContext(DbContextOptions<ScoalaDbContext> options) 
                : base(options)
        {
        }

        public DbSet<Elev> Elevi { get; set; }
        public DbSet<Clasa> Clase { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);
            modelBuilder.Entity<Clasa>()
                .HasMany(c => c.Elevi)
                .WithOne(e => e.Clasa)
                .HasForeignKey(e => e.ClasaID)
                .IsRequired();
        }
    }
}

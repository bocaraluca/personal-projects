using System.ComponentModel.DataAnnotations;

namespace ScoalaCodeFirst.Models
{
    public class Clasa
    {
        [Key]
        public int ClasaID { get; set; }

        [MaxLength(10)]
        public string Denumire { get; set; } = null!;
        public int? NrElevi { get; set; }

        // Collection Navigation Property
        public ICollection<Elev>? Elevi { get; set; }

    }
}

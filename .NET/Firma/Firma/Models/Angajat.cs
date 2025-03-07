using System.ComponentModel.DataAnnotations;

namespace Firma.Models
{
    public class Angajat
    {
        [Key] 
        public int IdAngajat { get; set; }

        [MinLength(3), MaxLength(30)]
        public string Nume { get; set; } = null!;

        public DateTime? DataNasterii { get; set; }

        [MinLength(3), MaxLength(30)]
        public string Pozitia { get; set; } = null!;
    }
}

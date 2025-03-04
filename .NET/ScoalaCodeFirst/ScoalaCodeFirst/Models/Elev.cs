using System.ComponentModel.DataAnnotations;

namespace ScoalaCodeFirst.Models
{
    // Model /Entity
    public class Elev
    {
        [Key]
        public int ElevID { get; set; }

        [MaxLength(20), MinLength(3)]
        public string Nume { get; set; } = null!;

       
        public DateTime? DataNasterii { get; set; }

  
        public int ClasaID { get; set; }


        // reference navigation property
        public Clasa? Clasa { get; set; }
    }
}

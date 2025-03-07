using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Firma.Migrations
{
    /// <inheritdoc />
    public partial class unu : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Angajati",
                columns: table => new
                {
                    IdAngajat = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Nume = table.Column<string>(type: "nvarchar(30)", maxLength: 30, nullable: false),
                    DataNasterii = table.Column<DateTime>(type: "datetime2", nullable: true),
                    Pozitia = table.Column<string>(type: "nvarchar(30)", maxLength: 30, nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Angajati", x => x.IdAngajat);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Angajati");
        }
    }
}

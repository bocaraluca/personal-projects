using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace ScoalaCodeFirst.Migrations
{
    /// <inheritdoc />
    public partial class unu : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Clase",
                columns: table => new
                {
                    ClasaID = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Denumire = table.Column<string>(type: "nvarchar(10)", maxLength: 10, nullable: false),
                    NrElevi = table.Column<int>(type: "int", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Clase", x => x.ClasaID);
                });

            migrationBuilder.CreateTable(
                name: "Elevi",
                columns: table => new
                {
                    ElevID = table.Column<int>(type: "int", nullable: false)
                        .Annotation("SqlServer:Identity", "1, 1"),
                    Nume = table.Column<string>(type: "nvarchar(20)", maxLength: 20, nullable: false),
                    DataNasterii = table.Column<DateTime>(type: "datetime2", nullable: true),
                    ClasaID = table.Column<int>(type: "int", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Elevi", x => x.ElevID);
                    table.ForeignKey(
                        name: "FK_Elevi_Clase_ClasaID",
                        column: x => x.ClasaID,
                        principalTable: "Clase",
                        principalColumn: "ClasaID",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_Elevi_ClasaID",
                table: "Elevi",
                column: "ClasaID");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Elevi");

            migrationBuilder.DropTable(
                name: "Clase");
        }
    }
}

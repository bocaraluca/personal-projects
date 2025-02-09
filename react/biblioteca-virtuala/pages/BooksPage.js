import { Box } from '@mui/material'
import Card from "../components/Card";
import React from 'react'
import adolescentul from "../components/photos/adolescentul.jpg"
import annakarenina from "../components/photos/annakarenina.jpg"
import crimasipedeapsa from "../components/photos/crimasipedeapsa.jpg"
import donquijote from "../components/photos/donquijote.jpg"
import enigmaotiliei from "../components/photos/enigmaotiliei.jpeg"
import fermaanimalelor from "../components/photos/fermaanimalelor.jpg"
import frankenstein from "../components/photos/frankenstein.jpeg"
import fratiikaramazov from "../components/photos/fratiikaramazov.jpeg"
import harrypotter from "../components/photos/harrypotter.jpg"
import ion from "../components/photos/ion.jpg"
import maitreyi from "../components/photos/maitreyi.jpeg"
import mandriesiprejudecata from "../components/photos/mandriesiprejudecata.jpeg"
import marelegatsby from "../components/photos/marelegatsby.jpg"
import marilesperante from "../components/photos/marilesperante.jpg"
import metamorfoza from "../components/photos/metamorfoza.jpg"
import moaracunoroc from "../components/photos/moaracunoroc.jpeg"
import padureaspanzuratilor from "../components/photos/padureaspanzuratilor.jpg"
import patulluiprocust from "../components/photos/patulluiprocust.jpg"
import razboisipace from "../components/photos/razboisipace.jpg"
import stapanulinelelor from "../components/photos/stapanulinelelor.jpg"
import back from '../components/photos/back.jpg';

const BooksPage = () => {
  return (
    <Box sx={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center', 
      backgroundImage: `url(${back})`,
      backgroundRepeat: 'no-repeat',
      backgroundSize: 'cover',
      opacity: 0.95,
      gap: '20px',
      padding: '20px',
      minHeight: '100vh'
    }}>
      {/* Row 1 */}
      <Box sx={{
        width: "80vw",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: '20px'
      }}>
        <Card titlu={"Adolescentul"} src={adolescentul} autor={"F.M. Dostoievski"} link={"/books/adolescentul"} />
        <Card titlu={"Anna Karenina"} src={annakarenina} autor={"Lev Tolstoi"} link={"/books/annakarenina"} />
        <Card titlu={"Crimă și pedeapsă"} src={crimasipedeapsa} autor={"F.M. Dostoievski"} link={"/books/crimasipedeapsa"} />
        <Card titlu={"Don Quijote de la Mancha"} src={donquijote} autor={"Miguel de Cervantes"} link={"/books/donquijote"} />
      </Box>

      {/* Row 2 */}
      <Box sx={{
        width: "80vw",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: '20px'
      }}>
        <Card titlu={"Enigma Otiliei"} src={enigmaotiliei} autor={"G. Călinescu"} link={"/books/enigmaotiliei"} />
        <Card titlu={"Ferma animalelor"} src={fermaanimalelor} autor={"George Orwell"} link={"/books/fermaanimalelor"} />
        <Card titlu={"Frankenstein"} src={frankenstein} autor={"Mary Shelley"} link={"/books/frankenstein"} />
        <Card titlu={"Frații Karamazov"} src={fratiikaramazov} autor={"F.M. Dostoievski"} link={"/books/fratiikaramazov"} />
      </Box>

      {/* Row 3 */}
      <Box sx={{
        width: "80vw",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: '20px'
      }}>
        <Card titlu={"Harry Potter"} src={harrypotter} autor={"J.K. Rowling"} link={"/books/harrypotter"} />
        <Card titlu={"Ion"} src={ion} autor={"Liviu Rebreanu"} link={"/books/ion"} />
        <Card titlu={"Maitreyi"} src={maitreyi} autor={"Mircea Eliade"} link={"/books/maitreyi"} />
        <Card titlu={"Mândrie și prejudecată"} src={mandriesiprejudecata} autor={"Jane Austen"} link={"/books/mandriesiprejudecata"} />
      </Box>

      {/* Row 4 */}
      <Box sx={{
        width: "80vw",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: '20px'
      }}>
        <Card titlu={"Marele Gatsby"} src={marelegatsby} autor={"F. Scott Fitzgerald"} link={"/books/marelegatsby"} />
        <Card titlu={"Marile speranțe"} src={marilesperante} autor={"Charles Dickens"} link={"/books/marilesperante"} />
        <Card titlu={"Metamorfoza"} src={metamorfoza} autor={"Franz Kafka"} link={"/books/metamorfoza"} />
        <Card titlu={"Moara cu noroc"} src={moaracunoroc} autor={"Ioan Slavici"} link={"/books/moaracunoroc"} />
      </Box>

      {/* Row 5 */}
      <Box sx={{
        width: "80vw",
        display: "flex",
        flexDirection: "row",
        flexWrap: "wrap",
        justifyContent: "space-between",
        gap: '20px'
      }}>
        <Card titlu={"Pădurea spânzuraților"} src={padureaspanzuratilor} autor={"Liviu Rebreanu"} link={"/books/padureaspanzuratilor"} />
        <Card titlu={"Patul lui Procust"} src={patulluiprocust} autor={"Camil Petrescu"} link={"/books/patulluiprocust"} />
        <Card titlu={"Război și pace"} src={razboisipace} autor={"Lev Tolstoi"} link={"/books/razboisipace"} />
        <Card titlu={"Stăpânul Inenelor"} src={stapanulinelelor} autor={"J.R.R. Tolkien"} link={"/books/stapanulinelelor"} />
      </Box>
    </Box>
  )
}

export default BooksPage

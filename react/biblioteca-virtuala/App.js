import { Box } from '@mui/material';
import './App.css';
import NavBar from "./components/NavBar";
import { Route, Routes } from 'react-router-dom';
import HomePage from  "./pages/HomePage";
import AboutPage from  "./pages/AboutPage";
import BooksPage from './pages/BooksPage';
import Adolescentul from './pages/Adolescentul'
import AnnaKarenina from './pages/AnnaKarenina'
import CrimaSiPedeapsa from './pages/CrimaSiPedeapsa'
import DonQuijote from './pages/DonQuijote'
import EnigmaOtiliei from './pages/EnigmaOtiliei'
import FermaAnimalelor from './pages/FermaAnimalelor'
import Frankenstein from './pages/Frankenstein'
import FratiiKaramazov from './pages/FratiiKaramazov'
import HarryPotter from './pages/HarryPotter'
import Ion from './pages/Ion'
import Maitreyi from './pages/Maitreyi'
import MandrieSiPrejudecata from './pages/MandrieSiPrejudecata'
import MareleGatsby from './pages/MareleGatsby'
import MarileSperante from './pages/MarileSperante'
import Metamorfoza from './pages/Metamorfoza'
import MoaraCuNoroc from './pages/MoaraCuNoroc'
import PadureaSpanzuratilor from './pages/PadureaSpanzuratilor'
import PatulLuiProcust from './pages/PatulLuiProcust'
import RazboiSiPace from './pages/RazboiSiPace'
import StapanulInelelor from './pages/StapanulInelelor'
import ChestionarPage from './pages/ChestionarPage';

function App() {
  return (
    <Box>
      <NavBar/>
      <Routes>
        <Route path="/" element={<HomePage/>}/>
        <Route path="/about" element={<AboutPage/>}/>
        <Route path="/books" element={<BooksPage/>}/>
        <Route path="/chestionar" element={<ChestionarPage/>}/>
        <Route path="/books/adolescentul" element={<Adolescentul/>}/>
        <Route path="/books/annakarenina" element={<AnnaKarenina/>}/>
        <Route path="/books/crimasipedeapsa" element={<CrimaSiPedeapsa/>}/>
        <Route path="/books/donquijote" element={<DonQuijote/>}/>
        <Route path="/books/enigmaotiliei" element={<EnigmaOtiliei/>}/>
        <Route path="/books/fermaanimalelor" element={<FermaAnimalelor/>}/>
        <Route path="/books/frankenstein" element={<Frankenstein/>}/>
        <Route path="/books/fratiikaramazov" element={<FratiiKaramazov/>}/>
        <Route path="/books/harrypotter" element={<HarryPotter/>}/>
        <Route path="/books/ion" element={<Ion/>}/>
        <Route path="/books/maitreyi" element={<Maitreyi/>}/>
        <Route path="/books/mandriesiprejudecata" element={<MandrieSiPrejudecata/>}/>
        <Route path="/books/marelegatsby" element={<MareleGatsby/>}/>
        <Route path="/books/marilesperante" element={<MarileSperante/>}/>
        <Route path="/books/metamorfoza" element={<Metamorfoza/>}/>
        <Route path="/books/moaracunoroc" element={<MoaraCuNoroc/>}/>
        <Route path="/books/padureaspanzuratilor" element={<PadureaSpanzuratilor/>}/>
        <Route path="/books/patulluiprocust" element={<PatulLuiProcust/>}/>
        <Route path="/books/razboisipace" element={<RazboiSiPace/>}/>
        <Route path="/books/stapanulinelelor" element={<StapanulInelelor/>}/>
      </Routes>
    </Box>
  );
}

export default App;

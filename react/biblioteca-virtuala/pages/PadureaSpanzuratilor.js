import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/padureaspanzuratilor.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const PadureaSpanzuratilor = () => {
  return (
    <Box sx={{
        width: "100vw",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        alignSelf: "center",
        //gap: 1,
        borderRadius: "2px",
        backgroundImage: `url(${back})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        opacity: 0.95
      }}>
        <Typography fontSize={60} paddingTop={'5px'}>Pădurea spânzuraților</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Liviu Rebreanu</Typography>
        <Box sx={{
            width: "90vw",
            height: "90vh",
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            alignSelf: "center",
            }}>
            <Paper
                elevation={7}
                component="form"
                sx={{
                    width: '370px',
                    height: '440px',
                    alignSelf: "center",
                    p: 2,
                    gap: 1,
                    borderRadius: "5px",
                    backgroundImage: `url(${poza})`,
                    margin: '70px',
                    marginRight: '150px',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: '320px'
                }}
            ></Paper>

            <Box sx={{
            width: "1000px",
            maxHeight: "300px",
            display: "flex",
            flexDirection: "column",
            backgroundColor: purple[800],
            padding: '35px',
            borderRadius: '7px'
            }}>
            <Typography fontSize={'18px'} color={'white'}>"Pădurea spânzuraților" este un roman scris de Liviu Rebreanu, 
            care explorează povestea lui Apostol Bologa, un tânăr ofițer român din timpul Primului Război Mondial. 
            În mijlocul unui conflict brutal și a unei societăți divizate de loialități politice și etnice, Bologa se 
            găsește într-un conflict interior între datoria față de țară și iubirea pentru Tincuța, o femeie de etnie 
            maghiară. În timp ce se confruntă cu ororile războiului și cu presiunile sociale, Bologa este prins între 
            două lumi care par să nu poată coexista. Romanul explorează teme precum patriotismul, iubirea interetnică, 
            conștiința morală și tragedia indivizibilă a războiului. "Padurea spanzuratilor" este considerată una dintre 
            cele mai importante opere ale literaturii române, captivând cititorii cu profunditatea sa psihologică și 
            portretizarea vividă a vremii și a societății.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://ferestre.weebly.com/uploads/1/6/9/5/1695755/_padurea_spanzuratilor_-_liviu_rebreanu.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default PadureaSpanzuratilor
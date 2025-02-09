import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/metamorfoza.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const Metamorfoza = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Metamorfoza</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Franz Kafka</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Metamorfoza" este o povestire scrisă de Franz Kafka care 
            urmărește transformarea lui Gregor Samsa, un tânăr comerciant, într-o insectă gigantică. Povestea începe 
            când Gregor se trezește într-o dimineață și descoperă că corpul său s-a transformat complet, iar viața sa 
            și a familiei sale se schimbă dramatic. În timp ce Gregor încearcă să se adapteze la noua sa formă și să își 
            păstreze locul în societate, familia sa reacționează diferit. Ei îl consideră acum un pericol și o povară, 
            iar relațiile lor devin tensionate. Pe măsură ce povestea avansează, Gregor își pierde identitatea umană și 
            se confruntă cu singurătatea și alienarea. "Metamorfoza" explorează teme precum alienarea, singurătatea, 
            responsabilitatea și relațiile interumane, fiind una dintre cele mai cunoscute și influente lucrări ale 
            literaturii moderne. Este adesea interpretată ca o alegorie a condiției umane și a absurdului vieții.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://www.libris.ro/pdf?_pid=10891762&for=Metamorfoza+si+alte+povestiri+-+Franz+Kafka'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default Metamorfoza
import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/fratiikaramazov.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const FratiiKaramazov = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Frații Karamazov</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de F.M. Dostoievski</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Frații Karamazov" este un roman clasic scris de Fyodor 
            Dostoevsky. Povestea se învârte în jurul familiei Karamazov și a conflictelor lor interioare și exterioare. 
            Trei frați - Dmitri, Ivan și Alexei - reprezintă trei personalități distincte și se confruntă cu probleme 
            existențiale și etice. Romanul explorează teme precum credința, moralitatea, paternitatea și moartea, oferind 
            o analiză profundă a condiției umane și a psihologiei umane. "Frații Karamazov" este considerat una dintre 
            cele mai mari opere ale literaturii ruse și unul dintre cele mai influente romane din istoria literaturii 
            universale.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://antropologieteologicabiblioteca.files.wordpress.com/2015/07/fratii-karamazov-de-fiodor-mihailovici-dostoievski.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default FratiiKaramazov
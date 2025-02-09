import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/enigmaotiliei.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const EnigmaOtiliei = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Enigma Otiliei</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de G. Călinescu</Typography>
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
                    backgroundSize: 'cover'
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
            <Typography fontSize={'18px'} color={'white'}>"Enigma Otiliei" este un roman scris de George Călinescu, care 
            explorează lumea burgheziei românești din perioada interbelică. Povestea este centrată în jurul personajului 
            principal, Felix Sima, un tânăr care își petrece timpul la casa unchiului său, Costache Giurgiuveanu. Intriga 
            romanului se concentrează pe moștenirea pe care Otilia, fiica unchiului, ar putea să o primească. Acest lucru 
            atrage atenția mai multor pretendenți și creează tensiuni în familia Giurgiuveanu. În timp ce Felix se 
            îndrăgostește de Otilia, el descoperă secrete și intrigi care îl fac să își pună întrebări despre lumea în 
            care trăiește. "Enigma Otiliei" este o poveste captivantă despre iubire, ambiție și trădare, iar autorul 
            dezvăluie treptat misterele personajelor și ale vieții lor. Romanul este considerat una dintre cele mai 
            importante opere ale literaturii românești moderne și este apreciat pentru portretizarea vividă a societății 
            și a personajelor sale complexe.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://liceulfranciscan.ro/biblioteque/materiale_digitale/George_Calinescu-Enigma_Otiliei.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default EnigmaOtiliei
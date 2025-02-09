import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/fermaanimalelor.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const FermaAnimalelor = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Ferma animalelor</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de George Orwell</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Ferma animalelor" este o alegorie scrisă de George Orwell care 
            prezintă o satiră a regimurilor totalitare, în special a regimului sovietic. Povestea începe cu animalele de 
            la Ferma Părintească care se revoltă împotriva stăpânului lor uman și preiau controlul fermei. În noul lor
            regim, animalele își propun să creeze o societate egalitaristă și justă. Cu toate acestea, treptat, 
            conducătorii lor porci preiau controlul și distorsionează idealurile inițiale, instaurând un regim tot mai 
            autoritar și corupt. Prin personaje antropomorfe și evenimente simbolice, Orwell explorează teme precum 
            abuzul de putere, manipularea maselor și corupția politică. "Ferma animalelor" oferă o critică aspră a 
            tiraniei și a regimurilor totalitare, fiind considerată una dintre cele mai influente lucrări ale secolului XX.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://gawrylyta.files.wordpress.com/2011/11/orwell_20george_20-_20ferma_20animalelor.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default FermaAnimalelor
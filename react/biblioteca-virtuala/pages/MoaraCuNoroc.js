import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/moaracunoroc.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const MoaraCuNoroc = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Moara cu noroc</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Ioan Slavici</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Moara cu noroc" este o nuvelă scrisă de Ioan Slavici, 
            care explorează viața lui Ghita, un om simplu care devine proprietarul unei mori într-un sat din 
            Transilvania. Ghita, inițial un om cinstit, este atras într-o spirală de corupție și crimă după ce moara 
            sa devine un loc de întâlnire pentru oameni dubioși și nelegiuiți. În timp ce prosperitatea aparentă a morii 
            crește, Ghita se confruntă cu consecințele faptelor sale și cu presiunile societății. El se luptă cu 
            conștiința sa și cu dorința de a-și menține averea și puterea, în timp ce evenimentele tragice din jurul 
            morii îl împing spre un final inevitabil. "Moara cu noroc" este considerată una dintre cele mai importante 
            opere ale literaturii române, explorând teme precum corupția, moralitatea și lupta pentru supraviețuire 
            într-o lume nemiloasă.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://www.scoalaluceafarul.ro/carti/moara_cu_noroc.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default MoaraCuNoroc
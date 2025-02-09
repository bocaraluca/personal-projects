import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/donquijote.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const DonQuijote = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Don Quijote de la Mancha</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Miguel de Cervantes</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Don Quijote" este un roman clasic scris de Miguel de Cervantes.
            Povestea urmărește aventurile unui nobil spaniol în vârstă, pe nume Alonso Quijano, care își pierde mințile și 
            devine cunoscut ca Don Quijote de la Mancha după ce citește prea multe romane despre cavaleri și aventuri. El 
            își imaginează că este un cavaler medieval și pornește în căutarea aventurilor alături de vechiul său scutier, 
            Sancho Panza. În timpul călătoriilor lor, Don Quijote se confruntă cu molii pe care le consideră monștri, mori 
            de vânt pe care le crede a fi balauri și alte aventuri fantastice. Romanul este o satiră asupra literaturii 
            cavalerilor și a idealismului excesiv, dar și o explorare profundă a identității, a puterii imaginației și a 
            distincției dintre realitate și ficțiune. Este considerat una dintre cele mai importante opere ale literaturii 
            spaniole și una dintre cele mai influente aromane din istoria literaturii universale.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://humanitas.ro/assets/media/don-quijote.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default DonQuijote
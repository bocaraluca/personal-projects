import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/razboisipace.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const RazboiSiPace = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Război și pace</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Lev Tolstoi</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Război și pace" este un roman monumental scris de Lev Tolstoi, 
            care urmărește destinul a patru familii aristocrate în timpul războaielor napoleoniene și perioada de pace 
            care le urmează. Povestea se desfășoară în Rusia începând din 1805 și se întinde pe parcursul a aproximativ 
            15 ani. Romanul explorează teme precum războiul și pacea, dragostea și relațiile interumane, politica și 
            filozofia, toate reflectate prin prisma vieții și experiențelor personajelor. Personajele principale, precum 
            Pierre Bezukhov, Andrei Bolkonsky și Natalia Rostova, sunt construite cu o profunzime remarcabilă, iar 
            povestea lor este plină de dramatism și învățăminte despre natura umană. "Război și pace" este considerat 
            una dintre cele mai mari opere ale literaturii universale, fiind apreciat pentru profunzimea sa psihologică, 
            analiza socială și abordarea filozofică.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://gawrylyta.files.wordpress.com/2011/11/volumul3.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default RazboiSiPace
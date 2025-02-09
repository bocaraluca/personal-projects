import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/maitreyi.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const Maitreyi = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Maitreyi</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Mircea Eliade</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Maitreyi" este un roman scris de Mircea Eliade, care explorează 
            povestea de dragoste dintre autor și Maitreyi Devi, o studentă indiană. Povestea este plasată în contextul 
            colonial al Indiei britanice și este relatată din perspectiva lui Allan, alter ego-ul lui Eliade. Romanul 
            surprinde fascinația lui Allan pentru cultura indiană și frumusețea Maitreyi, dar și dificultățile întâmpinate 
            în încercarea lor de a trăi o dragoste interzisă din cauza diferențelor de vârstă, cultură și religie. 
            "Maitreyi" explorează teme precum iubirea, maturizarea, conflictul cultural și identitatea, și este considerat 
            una dintre cele mai importante opere ale literaturii românești moderne.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://singerei.educ.md/wp-content/uploads/sites/412/2017/11/Eliade__Mircea_-_Maitreyi.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default Maitreyi
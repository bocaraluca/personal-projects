import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/marelegatsby.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const MareleGatsby = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Marele Gatsby</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de F. Scott Fitzgerald</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Marele Gatsby" este un roman scris de F. Scott Fitzgerald 
            care surprinde viața extravagantă a elitei sociale din anii '20 ai secolului trecut în America. Povestea 
            este povestită din perspectiva lui Nick Carraway, un tânăr scriitor care se mută în Long Island și devine 
            martorul relației dintre Jay Gatsby, un bărbat misterios și bogat, și Daisy Buchanan, o femeie căsătorită cu 
            un alt bărbat bogat, Tom. Gatsby organizează petreceri fabuloase în speranța că își va reîntâlni dragostea de 
            odinioară, Daisy. Romanul explorează teme precum visurile americane, corupția morală, și deziluziile care vin 
            odată cu realizarea acestor vise. Este considerat unul dintre cele mai mari romane ale literaturii americane, 
            datorită stilului său vibrant și imaginii profunde a epocii.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://aman.ro/betawp/wp-content/uploads/ebook/humanitas/F-Scott-Fitzgerald_Marele-Gatsby.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default MareleGatsby
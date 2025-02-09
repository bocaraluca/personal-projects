import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/frankenstein.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const Frankenstein = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Frankenstein</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Mary Shelley</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Frankenstein" este un roman gotic scris de Mary Shelley și 
            publicat în 1818. Povestea urmărește viața lui Victor Frankenstein, un tânăr savant obsedat de dorința de a 
            crea viață din materie moartă. Prin experimentele sale, el reușește să creeze un monstru, dar își dă seama 
            curând că creația sa este de fapt o ființă nefericită și monstruoasă. Monstrul îi cere lui Frankenstein să îi 
            creeze o parteneră, amenințând că, în caz contrar, va aduce nenorocire asupra celor dragi savantului. Însă 
            Victor refuză, iar monstrul își răzbună suferințele provocând moartea celor dragi lui Frankenstein. 
            "Frankenstein" explorează teme profunde precum responsabilitatea creatorului față de creația sa, izolarea 
            socială și consecințele nefaste ale prejudecăților și ale respingerii. Este considerată una dintre primele 
            opere de science fiction, influențând numeroase lucrări ulterioare.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://www.libris.ro/pdf?_pid=10865797&for=Frankenstein+-+Mary+Shelley'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default Frankenstein